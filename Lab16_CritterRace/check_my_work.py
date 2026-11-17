"""
check_my_work.py  -  Run this file after each step to test your code.

You do NOT need to change anything in this file.
Just press Run in your IDE and type the step number,
or press Enter to check everything.
"""

import contextlib
import importlib
import io
import random
import statistics
import sys
import tempfile
import time
import traceback
import warnings
from pathlib import Path
from types import SimpleNamespace

LAB_FOLDER = Path(__file__).resolve().parent
sys.path.insert(0, str(LAB_FOLDER))
warnings.filterwarnings("ignore")

results = []          # True / False for every check


def check(passed, message, hint=""):
    """Record and print the result of one check."""
    results.append(passed)
    if passed:
        print(f"  [PASS] {message}")
    else:
        print(f"  [FAIL] {message}")
        if hint:
            print(f"         Hint: {hint}")


def safe(test_function, message, hint=""):
    """Run one check. If the student's code crashes, show why instead of stopping."""
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            passed = bool(test_function())
    except Exception as error:
        where = ""
        tb = traceback.extract_tb(error.__traceback__)
        student = [f for f in tb if Path(f.filename).resolve().parent == LAB_FOLDER
                   and Path(f.filename).name != "check_my_work.py"]
        if student:
            where = f" (in {Path(student[-1].filename).name}, line {student[-1].lineno})"
        check(False, message, f"your code crashed with {type(error).__name__}: {error}{where}")
        return
    check(passed, message, hint)


def load(module_name):
    """Import one of the lab files, or explain why it could not be imported."""
    try:
        if module_name in sys.modules:
            return importlib.reload(sys.modules[module_name])
        return importlib.import_module(module_name)
    except SyntaxError as error:
        print(f"  [FAIL] {module_name}.py has a SYNTAX error on line {error.lineno}: {error.msg}")
    except ModuleNotFoundError as error:
        print(f"  [FAIL] {module_name}.py could not import '{error.name}'.")
        if error.name and error.name.startswith("matplotlib"):
            print("         matplotlib is not installed yet. See Step 0 in the guide.")
        else:
            print("         Check the spelling of your import line (file names have no .py).")
    except Exception as error:
        print(f"  [FAIL] Could not import {module_name}.py: {type(error).__name__}: {error}")
    results.append(False)
    return None


def matplotlib_ready():
    try:
        import matplotlib
        matplotlib.use("Agg")           # draw charts without opening windows while checking
        return True
    except ModuleNotFoundError:
        return False


# ===================================================================
def step0():
    print("\nSTEP 0 - Setup")
    check(sys.version_info >= (3, 8), f"Python 3.8 or newer (you have {sys.version.split()[0]})",
          "install a newer Python from python.org")
    check(matplotlib_ready(), "matplotlib is installed",
          "install it: see Step 0 in the guide (PyCharm: Python Packages window, search matplotlib)")


def step1():
    print("\nSTEP 1 - Big-picture worksheet")
    print("  (This step is on paper - nothing for the computer to check.)")


def step2():
    print("\nSTEP 2 - Imports")
    racer = load("racer")
    if racer:
        check(getattr(racer, "random", None) is random,
              "TODO 2a: racer.py imports the random library",
              "write  import random  at the top of racer.py")
    race = load("race")
    if race:
        check(getattr(race, "sleep", None) is time.sleep,
              "TODO 2b: race.py imports sleep from the time library",
              "write  from time import sleep")
    stats = load("stats")
    if stats and race:
        check(getattr(stats, "Race", None) is race.Race,
              "TODO 2c: stats.py imports the Race class from race.py",
              "write  from race import Race")
        check(getattr(stats, "average", None) is statistics.mean,
              "TODO 2d: stats.py imports mean from statistics with the alias average",
              "write  from statistics import mean as average")
    if not matplotlib_ready():
        check(False, "TODO 2e: charts.py imports matplotlib.pyplot as plt",
              "matplotlib is not installed yet - do Step 0 first")
        return
    import matplotlib.pyplot
    charts = load("charts")
    if charts:
        check(getattr(charts, "plt", None) is matplotlib.pyplot,
              "TODO 2e: charts.py imports matplotlib.pyplot with the alias plt",
              "write  import matplotlib.pyplot as plt")
    main = load("main")
    if main and racer and race and stats and charts:
        ok = (getattr(main, "Racer", None) is racer.Racer and getattr(main, "Race", None) is race.Race
              and getattr(main, "st", None) is stats and getattr(main, "charts", None) is charts)
        missing = [n for n, want in [("Racer", racer.Racer), ("Race", race.Race), ("st", stats),
                                     ("charts", charts)] if getattr(main, n, None) is not want]
        check(ok, "TODO 2f: main.py imports Racer, Race, stats as st, and charts",
              "still missing in main.py: " + ", ".join(missing) if missing else "")


def step3():
    print("\nSTEP 3 - Racer.move()")
    racer = load("racer")
    if not racer:
        return
    Racer = racer.Racer

    def steps_in_range():
        r = Racer("Test", "turtle", "T", 2, 5)
        steps = [r.move() for _ in range(60)]
        return (all(isinstance(s, int) and 2 <= s <= 5 for s in steps)
                and r.position == sum(steps) and len(set(steps)) > 1)
    safe(steps_in_range, "TODO 3: move() returns a random step from min_step to max_step and adds it to position",
         "use random.randint(self.min_step, self.max_step), then  self.position += step  and  return step")

    def history_grows():
        r = Racer("Test", "turtle", "T", 3, 3)
        for _ in range(4):
            r.move()
        return r.history == [0, 3, 6, 9, 12]
    safe(history_grows, "TODO 3: move() adds the new position to the end of history",
         "after moving:  self.history.append(self.position)")

    def naps():
        sleepy = Racer("Sleepy", "rabbit", "R", 5, 9, 1.0)       # always naps
        awake = Racer("Awake", "rabbit", "R", 5, 9, 0.0)         # never naps
        sleepy_steps = [sleepy.move() for _ in range(20)]
        awake_steps = [awake.move() for _ in range(20)]
        return all(s == 0 for s in sleepy_steps) and all(s >= 5 for s in awake_steps)
    safe(naps, "TODO 3: a racer naps (step 0) when random.random() < nap_chance",
         "if random.random() < self.nap_chance:  step = 0   else:  step = random.randint(...)")


def step4():
    print("\nSTEP 4 - The race chart (matplotlib)")
    names_4 = ["TODO 4a: one line for each racer (using racer.history)",
               'TODO 4b: a title, x-label "Round" and y-label "Distance"',
               "TODO 4b: a legend that shows the racers' names"]
    if not matplotlib_ready():
        for name in names_4:
            check(False, name, "matplotlib is not installed yet - do Step 0 first")
        return
    import matplotlib.pyplot as plt
    charts = load("charts")
    if not charts or getattr(charts, "plt", None) is None:
        for name in names_4:
            check(False, name, "finish TODO 2e (import matplotlib.pyplot as plt) first")
        return

    a = SimpleNamespace(name="Tina", history=[0, 4, 9, 13])
    b = SimpleNamespace(name="Rocket", history=[0, 0, 8, 16])
    c = SimpleNamespace(name="Chaos", history=[0, 7, 9, 12])
    fake_race = SimpleNamespace(racers=[a, b, c], finish_line=15, winner=b, round=3)

    drawn = {}
    original_show = plt.show
    plt.show = lambda *args, **kwargs: drawn.setdefault("figure", plt.gcf())
    try:
        out_file = Path(tempfile.mkdtemp()) / "test_chart.png"
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                charts.plot_race(fake_race, out_file)
        except Exception as error:
            for name in names_4:
                check(False, name, f"plot_race() crashed with {type(error).__name__}: {error}")
            return
    finally:
        plt.show = original_show

    ax = drawn.get("figure", plt.gcf()).axes[0]
    lines = [ln for ln in ax.get_lines() if list(ln.get_ydata()) in (a.history, b.history, c.history)]
    check(len(lines) == 3, "TODO 4a: one line for each racer (using racer.history)",
          f"found {len(lines)} racer lines - loop over race.racers and plt.plot(racer.history, ...)")
    check(bool(ax.get_title()) and ax.get_xlabel() == "Round" and ax.get_ylabel() == "Distance",
          'TODO 4b: a title, x-label "Round" and y-label "Distance"',
          "use plt.title(...), plt.xlabel(\"Round\"), plt.ylabel(\"Distance\")")
    names = [t.get_text() for t in ax.get_legend().get_texts()] if ax.get_legend() else []
    check("Tina" in names and "Rocket" in names,
          "TODO 4b: a legend that shows the racers' names",
          "call plt.legend(), and give each line  label=racer.name")
    plt.close("all")


def step5():
    print("\nSTEP 5 - Play the Grand Prix!")
    folder = LAB_FOLDER / "my_charts"
    check((folder / "race_chart.png").exists(),
          "You ran ONE race in main.py (my_charts/race_chart.png exists)",
          "run main.py and choose option 2")
    check((folder / "season_chart.png").exists(),
          "You ran a SEASON in main.py (my_charts/season_chart.png exists)",
          "run main.py and choose option 3")


# ===================================================================
STEPS = {"0": step0, "1": step1, "2": step2, "3": step3, "4": step4, "5": step5}

if __name__ == "__main__":
    print("=" * 58)
    print("   Lab 16 (Critter Grand Prix) - Check My Work")
    print("   T....R....C....H  ->  |FINISH|")
    print("=" * 58)
    choice = input("Which step do you want to check? (0-5, or Enter for ALL): ").strip()

    if choice in STEPS:
        STEPS[choice]()
    else:
        for run_step in STEPS.values():
            run_step()

    passed = results.count(True)
    total = len(results)
    print("\n" + "-" * 58)
    print(f"  {passed} / {total} checks passed")
    if total and passed == total:
        print("  ALL CLEAR!  Great work - move on to the next step!")
    else:
        print("  Read the hints above, fix one thing, and run me again.")
    print("-" * 58)
