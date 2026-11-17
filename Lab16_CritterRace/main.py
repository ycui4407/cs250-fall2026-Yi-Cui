"""
main.py  -  the Critter Grand Prix game

Run THIS file to play.
"""

# TODO 2f: write FOUR import lines here:
#   1. import the  Racer  class from our file  racer.py
#   2. import the  Race   class from our file  race.py
#   3. import our module  stats.py  and give it the alias  st
#   4. import our module  charts.py  (no alias)
from racer import Racer
from race import Race
import stats as st
import charts
BANNER = r"""
  ==================================================
        C R I T T E R    G R A N D    P R I X
  ==================================================
     T = turtle   R = rabbit   C = cat   H = hamster
"""

MENU = """
  1. Meet the racers
  2. Run ONE race (watch it live!)
  3. Run a SEASON of 100 races
  0. Quit
"""


def make_racers():
    """Create the four racers for the Grand Prix."""
    return [
        Racer("Tina", "turtle", "T", 4, 5),           # slow and steady, never naps
        Racer("Rocket", "rabbit", "R", 6, 10, 0.5),   # super fast, but naps half the time
        Racer("Chaos", "cat", "C", 0, 9),             # completely unpredictable
        Racer("Nibbles", "hamster", "H", 3, 7, 0.1),  # quick, sometimes stops for a snack
    ]


def show_racers(racers):
    """Print every racer with a number."""
    for number, racer in enumerate(racers, start=1):
        print(f"  {number}. {racer}")


def ask_prediction(racers):
    """Ask the player who they think will win. Return that Racer."""
    show_racers(racers)
    while True:
        answer = input("\n  Who will win? Type a number: ")
        try:
            number = int(answer)
        except ValueError:
            print("  Please type a NUMBER.")
            continue
        if 1 <= number <= len(racers):
            return racers[number - 1]
        print(f"  Please pick 1 to {len(racers)}.")


def play_one_race(racers):
    """Run one race the player can watch, then draw a line chart."""
    guess = ask_prediction(racers)
    race = Race(racers)
    winner = race.run(watch=True)

    print(f"\n  *** {winner.name} the {winner.species} wins in {race.round} rounds! ***")
    if winner is guess:
        print("  You called it! Great prediction!")
    else:
        print(f"  You picked {guess.name}. Better luck next time!")

    print("  Opening the race chart... (close the chart window to continue)")
    charts.plot_race(race)


def play_season(racers):
    """Run 100 races, print the results, then draw a bar chart."""
    print("  Running 100 races...")
    wins, lengths = st.run_season(racers, 100)
    percents = st.win_percent(wins)

    for name, count in wins.items():
        print(f"  {name:<8} {count:>3} wins  ({percents[name]}%)")
    print(f"\n  Champion of the season: {st.top_racer(wins)}")
    print(f"  Average race length: {st.average_length(lengths)} rounds")

    print("  Opening the season chart... (close the chart window to continue)")
    charts.plot_season(wins)


def main():
    print(BANNER)
    print("  Welcome to the Critter Grand Prix!")
    racers = make_racers()

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        print()
        if choice == "1":
            show_racers(racers)
        elif choice == "2":
            play_one_race(racers)
        elif choice == "3":
            play_season(racers)
        elif choice == "0":
            print("  Thanks for racing! See you at the next Grand Prix.")
            break
        else:
            print("  That is not an option. Try again.")


if __name__ == "__main__":
    main()
