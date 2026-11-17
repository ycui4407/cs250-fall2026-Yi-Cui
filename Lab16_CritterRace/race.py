"""
race.py  -  the Race class

One Race object = one race between a group of Racer objects.
"""

# TODO 2b: import ONLY the  sleep  function from the  time  library.
#          ( sleep(0.4)  pauses the program for 0.4 seconds. It makes the race animation work.)

from time import sleep
class Race:
    """A race: every round, each racer moves. First to the finish line wins."""

    def __init__(self, racers, finish_line=40):
        self.racers = racers            # a list of Racer objects
        self.finish_line = finish_line  # distance needed to win
        self.round = 0                  # how many rounds have been played
        self.winner = None              # the winning Racer (None until someone wins)

    def reset(self):
        """Get ready for a new race."""
        for racer in self.racers:
            racer.reset()
        self.round = 0
        self.winner = None

    def play_round(self):
        """Every racer moves once. Check if anyone crossed the finish line."""
        self.round += 1
        for racer in self.racers:
            racer.move()

        finished = [racer for racer in self.racers if racer.position >= self.finish_line]
        if finished:
            # If two racers cross in the same round, the one that ran farther wins.
            self.winner = max(finished, key=lambda racer: racer.position)

    def draw_track(self):
        """Print the race track so you can watch the race."""
        print(f"\n  Round {self.round}")
        for racer in self.racers:
            spot = min(racer.position, self.finish_line)
            track = "." * spot + racer.symbol + " " * (self.finish_line - spot)
            print(f"  {racer.name:<8}|{track}|")

    def run(self, watch=False):
        """Run a whole race and return the winner.

        watch=True prints the track after every round (a little animation).
        """
        self.reset()
        while self.winner is None:
            self.play_round()
            nobody_moved = all(racer.position == 0 for racer in self.racers)
            if (self.round >= 3 and nobody_moved) or self.round > 100:     # safety net
                raise RuntimeError("Nobody is moving! Finish Racer.move() in racer.py (Step 3) first.")
            if watch:
                self.draw_track()
                sleep(0.4)
        return self.winner
