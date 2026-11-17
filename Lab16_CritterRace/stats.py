"""
stats.py  -  helper functions for a whole SEASON of races

This module has no classes, only functions.
"""

# TODO 2c: import the  Race  class from our own file  race.py
from race import Race
# TODO 2d: import the  mean  function from the  statistics  library
#          and give it the new name (alias)  average
from statistics import mean as average

def run_season(racers, num_races=100):
    """Run many races. Return (wins, lengths).

    wins    -> a dictionary like {"Tina": 21, "Rocket": 30, ...}
    lengths -> a list with the number of rounds each race lasted
    """
    wins = {racer.name: 0 for racer in racers}
    lengths = []
    race = Race(racers)
    for _ in range(num_races):
        winner = race.run()
        wins[winner.name] += 1
        lengths.append(race.round)
    return wins, lengths


def win_percent(wins):
    """Turn win counts into percentages, e.g. {"Tina": 21.0, ...}."""
    total = sum(wins.values())
    return {name: round(100 * count / total, 1) for name, count in wins.items()}


def top_racer(wins):
    """Return the name of the racer with the most wins."""
    return max(wins, key=wins.get)


def average_length(lengths):
    """Return the average number of rounds per race, rounded to 1 decimal."""
    return round(average(lengths), 1)
