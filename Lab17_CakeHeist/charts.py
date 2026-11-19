"""
charts.py  -  the case file picture

STEP 6  draw two charts side by side and save them as case_file.png
"""

import matplotlib.pyplot as plt
from pathlib import Path

CASE_FILE = Path(__file__).parent / "case_file.png"


def minutes_after_two(time):
    """(15, 18) -> 78   (minutes after 14:00). Tuple unpacking!"""
    hour, minute = time
    return (hour - 14) * 60 + minute


def plot_case_file(messages, counts, culprit_names, window, filename=CASE_FILE):
    """Left: messages per critter (bar chart). Right: chat timeline with the heist window."""
    fig, (left, right) = plt.subplots(1, 2, figsize=(13, 5))

    # ---------------- LEFT: who talks the most? ----------------
    # TODO 6: draw a bar chart of the counts dictionary on the LEFT panel.
    #   1. names   = a LIST of the dictionary's keys       (hint: list(counts.keys()))
    #   2. numbers = a LIST of the dictionary's values
    #   3. left.bar(names, numbers, color="#E2702A")       (pick any color you like!)
    #   4. left.set_title("Who talks the most?")   and   left.set_ylabel("Messages")
    #   Then delete the raise line below.
    names = list(counts.keys())
    numbers = list(counts.values())

    left.bar(names, numbers, color="#E2702A")
    left.set_title("Who talks the most?")
    left.set_ylabel("Messages")
    # ---------------- RIGHT: the timeline (already done) -------
    critters = sorted(counts)                                   # a sorted LIST of names
    row = {name: i for i, name in enumerate(critters)}          # dict comprehension: name -> row
    start, end = window
    right.axvspan(minutes_after_two(start), minutes_after_two(end), color="#F4C7C3")
    right.text((minutes_after_two(start) + minutes_after_two(end)) / 2, -0.75, "HEIST WINDOW",
               ha="center", va="center", fontsize=10, color="#C62828", fontweight="bold")
    right.set_ylim(-1.2, len(critters) - 0.5)
    for time, sender, text in messages:
        guilty = sender in culprit_names
        right.scatter(minutes_after_two(time), row[sender],
                      color="#C62828" if guilty else "#0F7B7B", s=90 if guilty else 45)
    right.set_yticks(range(len(critters)))
    right.set_yticklabels(critters)
    right.set_xlabel("Minutes after 2:00 pm")
    right.set_title("Who was chatting during the heist?")

    fig.suptitle("The Great Carrot Cake Heist: case file", fontsize=15)
    fig.tight_layout()
    fig.savefig(filename)
    plt.show()
