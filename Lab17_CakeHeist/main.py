"""
main.py  -  run the investigation!

Run this file after each step: every finished step unlocks a new clue.
(You do not need to change anything in this file.)
"""

from time import sleep

import chat_tools as ct          # our module, with an alias
import detective                 # our module
from charts import plot_case_file

HEIST_WINDOW = ((15, 0), (15, 30))           # a tuple of two (hour, minute) tuples
SECRET = "cream cheese"                      # only the baker knew the frosting was cream cheese...
ALIBIS = {"Biscuit", "Rocket", "Pixel"}      # a SET: at the park, at the vet, locked in his cage


def header(title):
    print("\n" + "=" * 60)
    print("  " + title)
    print("=" * 60)


def clue_1(messages):
    header("CLUE 1  (Step 2: lists)  What was Tina doing?")
    for text in ct.messages_from(messages, "Tina"):
        print("   Tina:", text)
    loud = ct.shouts(messages)
    print(f"\n   {len(loud)} messages were written in ALL CAPS. The loudest:")
    print("  ", max(loud, key=len))


def clue_2(messages):
    header("CLUE 2  (Step 3: dictionaries)  Who talked the most?")
    counts = ct.count_messages(messages)
    for name, number in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):
        print(f"   {name:<8} {'#' * number}  {number}")
    name, number = ct.top_talker(counts)                    # tuple unpacking
    print(f"\n   Top talker: {name} with {number} messages")
    drama = ct.drama_scores(messages)
    print(f"   Most exclamation marks: {max(drama, key=drama.get)}")


def clue_3(messages):
    header("CLUE 3  (Step 4: sets)  Who could have done it?")
    online = detective.senders_between(messages, *HEIST_WINDOW)   # *  unpacks the tuple
    knew = detective.who_mentioned(messages, SECRET)
    print("   Online during the heist: ", sorted(online))
    print("   Knew the secret frosting:", sorted(knew))
    print("   Have an alibi:           ", sorted(ALIBIS))
    return detective.find_culprit(online, knew, ALIBIS)


def clue_4(messages):
    header("CLUE 4  (Step 5: arguments + scope)  The evidence")
    for time, sender, text in detective.search(messages, "crumbs"):
        print(f"   {time[0]}:{time[1]:02d}  {sender}: {text}")
    words = detective.count_words(messages, "cake", "nap", "carrot", "dream")
    print("   Word counter:", words)
    detective.total_drama = 0
    for time, sender, text in messages:
        detective.add_drama(text)
    print(f"   Total drama in this chat: {detective.total_drama} points")


def reveal(messages, culprit):
    header("THE REVEAL")
    print("   After careful analysis, the cake thief is", end="", flush=True)
    for _ in range(3):
        sleep(0.6)
        print(".", end="", flush=True)
    sleep(0.6)
    name = ", ".join(sorted(culprit)).upper()
    print(f"  {name}!!!")
    if culprit == {"Tina"}:
        print("\n   Tina: ...it was slow. and steady. and DELICIOUS.")
    print("\n   Opening the case file chart... (close the chart window to finish)")
    plot_case_file(messages, ct.count_messages(messages), culprit, HEIST_WINDOW)
    print("   Saved: case_file.png")


def main():
    print("\n   THE GREAT CARROT CAKE HEIST")
    print("   Someone ate the bake-sale cake. The only evidence: the group chat.")
    try:
        messages = ct.load_chat()
    except NotImplementedError:
        print("\n   [locked] Finish Step 1 (parse_line) to read the chat.")
        return
    print(f"\n   Loaded {len(messages)} messages. The first one is a tuple:")
    print("  ", messages[0])

    culprit = None
    for step, clue in [(2, clue_1), (3, clue_2), (4, clue_3), (5, clue_4)]:
        try:
            result = clue(messages)
            if step == 4:
                culprit = result
        except NotImplementedError:
            print(f"   [locked] Finish Step {step} to unlock this clue.")
        except UnboundLocalError as error:
            print(f"   [bug!] {error}")
            print("   That is the scope bug in add_drama(). Fix it in TODO 5c.")

    if culprit:
        try:
            reveal(messages, culprit)
        except NotImplementedError:
            print("\n   [locked] Finish Step 6 (charts.py) to see the case file.")
    else:
        print("\n   Not enough clues yet to name the thief. Keep going!")


if __name__ == "__main__":
    main()
