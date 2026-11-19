"""
check_my_work.py  -  test your code after each step.

Two ways to run it:
  1. In your IDE: press Run, then type a step number (or press Enter for ALL).
  2. In the TERMINAL (recommended!):
         python3 check_my_work.py 2        (Mac)
         python check_my_work.py 2         (Windows)
     Leave out the number to check every step.

You do NOT need to change anything in this file.
"""

import contextlib
import importlib
import io
import sys
import tempfile
import traceback
import warnings
from pathlib import Path

LAB_FOLDER = Path(__file__).resolve().parent
sys.path.insert(0, str(LAB_FOLDER))
warnings.filterwarnings("ignore")
results = []

LINE = "15:18 | Tina | zzz... still asleep in my shell"
MINI = [((14, 5), "Mochi", "noted. will not touch."),
        ((15, 2), "Rocket", "at the vet. CAKE later!"),
        ((15, 18), "Tina", "zzz... dreaming of Cake"),
        ((15, 31), "Biscuit", "WHERE IS THE CAKE???"),
        ((15, 41), "Tina", "cream cheese frosting. so sad."),
        ((15, 43), "Pixel", "CREAM CHEESE!")]


def check(passed, message, hint=""):
    results.append(passed)
    print(f"  [{'PASS' if passed else 'FAIL'}] {message}")
    if not passed and hint:
        print(f"         Hint: {hint}")


def safe(test, message, hint=""):
    """Run one check; explain crashes instead of stopping."""
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            passed = bool(test())
    except NotImplementedError:
        check(False, message, "not started yet (the TODO still raises NotImplementedError)")
        return
    except Exception as error:
        tb = traceback.extract_tb(error.__traceback__)
        mine = [f for f in tb if Path(f.filename).resolve().parent == LAB_FOLDER
                and Path(f.filename).name != "check_my_work.py"]
        where = f" (in {Path(mine[-1].filename).name}, line {mine[-1].lineno})" if mine else ""
        check(False, message, f"your code crashed with {type(error).__name__}: {error}{where}")
        return
    check(passed, message, hint)


def load(name):
    try:
        if name in sys.modules:
            return importlib.reload(sys.modules[name])
        return importlib.import_module(name)
    except SyntaxError as error:
        print(f"  [FAIL] {name}.py has a SYNTAX error on line {error.lineno}: {error.msg}")
    except Exception as error:
        print(f"  [FAIL] Could not import {name}.py: {type(error).__name__}: {error}")
    results.append(False)
    return None


def matplotlib_ready():
    try:
        import matplotlib
        matplotlib.use("Agg")
        return True
    except ModuleNotFoundError:
        return False


# ===================================================================
def step0():
    print("\nSTEP 0 - Setup")
    check(sys.version_info >= (3, 8), f"Python 3.8 or newer (you have {sys.version.split()[0]})")
    check(matplotlib_ready(), "matplotlib is installed",
          "install it like in Lab 16 (PyCharm: Python Packages window)")
    check((LAB_FOLDER / "chat.txt").exists(), "chat.txt is in the lab folder",
          "keep chat.txt next to the .py files")


def step1():
    print("\nSTEP 1 - Strings + tuples")
    ct = load("chat_tools")
    if not ct:
        return
    safe(lambda: ct.parse_line(LINE) == ((15, 18), "Tina", "zzz... still asleep in my shell"),
         "TODO 1: parse_line() returns ((15, 18), 'Tina', 'zzz... still asleep in my shell')",
         "split at '|', then split the time at ':', convert with int(), and .strip() every part")
    safe(lambda: isinstance(ct.parse_line(LINE), tuple) and isinstance(ct.parse_line(LINE)[0], tuple),
         "TODO 1: the result is a tuple, and the time inside it is a tuple too",
         "return ((int(hour), int(minute)), sender, text)  - note the two sets of ( )")
    safe(lambda: len(ct.load_chat()) == 32 and ct.load_chat()[14][2] == "zzzzz",
         "TODO 1: the whole chat loads (32 messages, extra spaces removed)",
         "Mochi's '   zzzzz' at 15:05 must become 'zzzzz': strip the text too")


def step2():
    print("\nSTEP 2 - Lists + list comprehensions")
    ct = load("chat_tools")
    if not ct:
        return
    safe(lambda: ct.messages_from(MINI, "Tina") == ["zzz... dreaming of Cake", "cream cheese frosting. so sad."]
         and ct.messages_from(MINI, "Nobody") == [],
         "TODO 2a: messages_from() returns a list of one critter's texts",
         "[text for time, who, text in messages if who == sender]")
    safe(lambda: ct.shouts(MINI) == ["WHERE IS THE CAKE???", "CREAM CHEESE!"],
         "TODO 2b: shouts() keeps only the ALL CAPS messages",
         "add  if text.isupper()  at the end of the list comprehension")


def step3():
    print("\nSTEP 3 - Dictionaries")
    ct = load("chat_tools")
    if not ct:
        return
    safe(lambda: ct.count_messages(MINI) == {"Mochi": 1, "Rocket": 1, "Tina": 2, "Biscuit": 1, "Pixel": 1},
         "TODO 3: count_messages() counts messages per sender",
         "counts[sender] = counts.get(sender, 0) + 1")
    safe(lambda: ct.count_messages(ct.load_chat())["Biscuit"] == 8,
         "TODO 3: works on the real chat (Biscuit sent 8 messages)",
         "finish Step 1 first, then check your loop")


def step4():
    print("\nSTEP 4 - Sets")
    d = load("detective")
    if not d:
        return
    safe(lambda: d.senders_between(MINI, (15, 0), (15, 30)) == {"Rocket", "Tina"}
         and d.senders_between(MINI, (14, 0), (14, 59)) == {"Mochi"},
         "TODO 4a: senders_between() returns a SET of names in the time window",
         "{sender for time, sender, text in messages if start <= time <= end}")
    safe(lambda: d.who_mentioned(MINI, "cream cheese") == {"Tina", "Pixel"}
         and d.who_mentioned(MINI, "CAKE") == {"Rocket", "Tina", "Biscuit"},
         "TODO 4b: who_mentioned() ignores upper/lower case",
         "compare phrase.lower() with text.lower()")
    safe(lambda: d.find_culprit({"A", "B", "C"}, {"B", "C", "D"}, {"C"}) == {"B"},
         "TODO 4c: find_culprit() = (online & knew_secret) - alibis",
         "use the set operators & and -")


def step5():
    print("\nSTEP 5 - Arguments + scope")
    d = load("detective")
    if not d:
        return
    safe(lambda: [m[1] for m in d.search(MINI, "cake")] == ["Rocket", "Tina", "Biscuit"],
         "TODO 5a: search(messages, 'cake') finds 'CAKE' and 'Cake' too (ignore_case defaults to True)",
         "add  sender=None, ignore_case=True  to the def line")
    safe(lambda: [m[1] for m in d.search(MINI, "cake", sender="Tina")] == ["Tina"]
         and [m[1] for m in d.search(MINI, "CAKE", ignore_case=False)] == ["Rocket", "Biscuit"],
         "TODO 5a: the keyword arguments sender= and ignore_case= work",
         "skip messages from other senders; when ignore_case is False, compare the text as it is")
    safe(lambda: d.count_words(MINI, "cake", "cheese", "vet") == {"cake": 3, "cheese": 2, "vet": 1}
         and d.count_words(MINI) == {},
         "TODO 5b: count_words(messages, *words) takes any number of words",
         "change  words  to  *words,  then  counts[word] = len(search(messages, word))")

    def scope():
        d.total_drama = 0
        first = d.add_drama("WHERE IS THE CAKE!!!")       # 3 marks + 5 for ALL CAPS
        d.add_drama("hi!")
        return first == 8 and d.total_drama == 9
    safe(scope, "TODO 5c: add_drama() updates the GLOBAL total_drama (scope bug fixed)",
         "add the line  global total_drama  as the first line inside add_drama()")


def step6():
    print("\nSTEP 6 - The case file chart")
    if not matplotlib_ready():
        check(False, "TODO 6: bar chart of messages per critter", "matplotlib is not installed")
        return
    import matplotlib.pyplot as plt
    charts = load("charts")
    if not charts:
        return

    def bars():
        out = Path(tempfile.mkdtemp()) / "test.png"
        original = plt.show
        plt.show = lambda *a, **k: None
        try:
            charts.plot_case_file(MINI, {"Mochi": 1, "Rocket": 1, "Tina": 2, "Biscuit": 1, "Pixel": 1},
                                  {"Tina"}, ((15, 0), (15, 30)), out)
        finally:
            plt.show = original
        left = plt.gcf().axes[0]
        heights = sorted(p.get_height() for p in left.patches)
        ok = heights == [1, 1, 1, 1, 2] and left.get_title() != ""
        plt.close("all")
        return ok and out.exists()
    safe(bars, "TODO 6: the left panel is a bar chart of the counts, with a title",
         "names = list(counts.keys()), numbers = list(counts.values()), then left.bar(...) and left.set_title(...)")
    check((LAB_FOLDER / "case_file.png").exists(),
          "You ran main.py and solved the case (case_file.png exists)",
          "run main.py after all steps are done")


# ===================================================================
STEPS = {"0": step0, "1": step1, "2": step2, "3": step3, "4": step4, "5": step5, "6": step6}

if __name__ == "__main__":
    print("=" * 58)
    print("   Lab 17 (The Great Carrot Cake Heist) - Check My Work")
    print("=" * 58)
    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        try:
            choice = input("Which step do you want to check? (0-6, or Enter for ALL): ").strip()
        except EOFError:
            choice = ""

    if choice in STEPS:
        STEPS[choice]()
    else:
        for run_step in STEPS.values():
            run_step()

    passed, total = results.count(True), len(results)
    print("\n" + "-" * 58)
    print(f"  {passed} / {total} checks passed")
    print("  CASE CLOSED! Great detective work!" if total and passed == total
          else "  Read the hints above, fix one thing, and run me again.")
    print("-" * 58)
