"""
charts.py  -  draw charts with matplotlib

Every chart is shown in a window AND saved as a picture in the my_charts folder.
"""

# TODO 2e: import  matplotlib.pyplot  and give it the alias  plt
#          (plt is the nickname almost every Python programmer uses for it.)
import matplotlib.pyplot as plt
from pathlib import Path

CHART_FOLDER = Path(__file__).parent / "my_charts"
RACE_CHART = CHART_FOLDER / "race_chart.png"
SEASON_CHART = CHART_FOLDER / "season_chart.png"


# -------------------------------------------------------------------
# STEP 4: a LINE chart of one race
# -------------------------------------------------------------------
def plot_race(race, filename=RACE_CHART):
    """Line chart: how far each racer had run after every round."""
    CHART_FOLDER.mkdir(exist_ok=True)
    plt.figure(figsize=(9, 5))

    # TODO 4a: Draw ONE line for EACH racer.
    #   Loop over  race.racers.  For each racer, call  plt.plot(...)  with:
    #     - the list  racer.history  (its position after every round)
    #     - marker="o"          (a dot on every round)
    #     - label=racer.name    (the name shown in the legend)
    for racer in race.racers:
        plt.plot(racer.history, marker="o", label=racer.name)

    # The dashed finish line (already done)
    plt.axhline(race.finish_line, color="gray", linestyle="--", label="Finish line")

    # TODO 4b: Add
    #   - a title  (fun idea: include the winner's name, race.winner.name)
    #   - the x-axis label  "Round"
    #   - the y-axis label  "Distance"
    #   - a legend
    #   Stuck? plot_season() below does the same things for a bar chart.

    # Save the chart as a picture, then show it in a window (already done)
    plt.title(f"Race Winner: {race.winner.name}")
    plt.xlabel("Round")
    plt.ylabel("Distance")
    plt.legend()

    plt.savefig(filename)
    plt.show()


# -------------------------------------------------------------------
# Already done for you: a BAR chart of a whole season (use it as a model!)
# -------------------------------------------------------------------
def plot_season(wins, filename=SEASON_CHART):
    """Bar chart: how many races each racer won in a season."""
    CHART_FOLDER.mkdir(exist_ok=True)
    plt.figure(figsize=(8, 5))

    names = list(wins.keys())
    counts = list(wins.values())
    plt.bar(names, counts, color="#4C9A8B")

    plt.title(f"Season results ({sum(counts)} races)")
    plt.xlabel("Racer")
    plt.ylabel("Number of wins")

    plt.savefig(filename)
    plt.show()
