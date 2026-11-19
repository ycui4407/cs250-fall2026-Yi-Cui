"""
detective.py  -  catch the cake thief

STEP 4  sets                        senders_between(), who_mentioned(), find_culprit()
STEP 5  arguments + scope           search(), count_words(), add_drama()
"""


# -------------------------------------------------------------------
# STEP 4: sets
# -------------------------------------------------------------------
def senders_between(messages, start, end):
    """Return a SET of critters who sent a message between start and end (both included).

    start and end are (hour, minute) tuples, e.g. (15, 0) and (15, 30).
    """
    # TODO 4a: ONE line with a SET comprehension  { ... for ... if ... }
    #   Keep the sender of every message whose time is between start and end.
    #   Tuples compare like clock times:  (15, 0) <= (15, 18) <= (15, 30)  is True
    #   so you can write:   start <= time <= end
    return {sender for time, sender, text in messages if start <= time <= end }


def who_mentioned(messages, phrase):
    """Return a SET of critters whose message contains phrase (ignore upper/lower case)."""
    # TODO 4b: ONE line with a set comprehension.
    #   Keep the sender if  phrase  appears in the text.
    #   Ignore upper/lower case: compare  phrase.lower()  with  text.lower()
    #   (Pixel shouts "CREAM CHEESE", and that must count too!)
    return {sender for time, sender, text in messages if phrase.lower() in text.lower() }


def find_culprit(online, knew_secret, alibis):
    """Return the set of critters who were online AND knew the secret, minus anyone with an alibi."""
    # TODO 4c: ONE line with set operators:
    #   &  keeps names that are in BOTH sets      -  removes names that are in the second set
    return (online & knew_secret) - alibis

# ---------------------------------------hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 check_my_work.py 0
# ==========================================================
#    Lab 17 (The Great Carrot Cake Heist) - Check My Work
# ==========================================================
#
# STEP 0 - Setup
#   [PASS] Python 3.8 or newer (you have 3.15.2)
#   [FAIL] matplotlib is installed
#          Hint: install it like in Lab 16 (PyCharm: Python Packages window)
#   [PASS] chat.txt is in the lab folder
#
# ----------------------------------------------------------
#   2 / 3 checks passed
#   Read the hints above, fix one thing, and run me again.
# ----------------------------------------------------------
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist %   [FAIL] matplotlib is installed
#
# zsh: no matches found: [FAIL]
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist %
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist %
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % pip install matplotlib
# zsh: command not found: pip
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 -m pip install matplotlib
# Collecting matplotlib
#   Using cached matplotlib-3.11.2-cp315-cp315-macosx_11_0_arm64.whl.metadata (80 kB)
# Collecting contourpy>=1.0.1 (from matplotlib)
#   Using cached contourpy-1.4.0-cp315-cp315-macosx_11_0_arm64.whl.metadata (3.8 kB)
# Collecting cycler>=0.10 (from matplotlib)
#   Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
# Collecting fonttools>=4.28.2 (from matplotlib)
#   Using cached fonttools-4.68.0-cp315-cp315-macosx_10_15_universal2.whl.metadata (139 kB)
# Collecting kiwisolver>=1.3.1 (from matplotlib)
#   Using cached kiwisolver-1.5.1-cp315-cp315-macosx_11_0_arm64.whl.metadata (5.2 kB)
# Collecting numpy>=1.25 (from matplotlib)
#   Using cached numpy-2.5.5-cp315-cp315-macosx_14_0_arm64.whl.metadata (6.6 kB)
# Collecting packaging>=20.0 (from matplotlib)
#   Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
# Collecting pillow>=9 (from matplotlib)
#   Using cached pillow-13.0.0-cp315-cp315-macosx_11_0_arm64.whl.metadata (9.1 kB)
# Collecting pyparsing>=3 (from matplotlib)
#   Using cached pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
# Collecting python-dateutil>=2.7 (from matplotlib)
#   Using cached python_dateutil-4.0.0-py3-none-any.whl.metadata (7.3 kB)
# Collecting tzdata (from python-dateutil>=2.7->matplotlib)
#   Using cached tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
# Using cached matplotlib-3.11.2-cp315-cp315-macosx_11_0_arm64.whl (9.3 MB)
# Using cached contourpy-1.4.0-cp315-cp315-macosx_11_0_arm64.whl (283 kB)
# Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
# Using cached fonttools-4.68.0-cp315-cp315-macosx_10_15_universal2.whl (3.1 MB)
# Using cached kiwisolver-1.5.1-cp315-cp315-macosx_11_0_arm64.whl (64 kB)
# Using cached numpy-2.5.5-cp315-cp315-macosx_14_0_arm64.whl (5.5 MB)
# Using cached packaging-26.3-py3-none-any.whl (129 kB)
# Using cached pillow-13.0.0-cp315-cp315-macosx_11_0_arm64.whl (4.9 MB)
# Using cached pyparsing-3.3.3-py3-none-any.whl (126 kB)
# Using cached python_dateutil-4.0.0-py3-none-any.whl (92 kB)
# Using cached tzdata-2026.6-py2.py3-none-any.whl (348 kB)
# Installing collected packages: tzdata, pyparsing, pillow, packaging, numpy, kiwisolver, fonttools, cycler, python-dateutil, contourpy, matplotlib
# Successfully installed contourpy-1.4.0 cycler-0.12.1 fonttools-4.68.0 kiwisolver-1.5.1 matplotlib-3.11.2 numpy-2.5.5 packaging-26.3 pillow-13.0.0 pyparsing-3.3.3 python-dateutil-4.0.0 tzdata-2026.6
#
# [notice] A new release of pip is available: 26.2.2 -> 26.3
# [notice] To update, run: pip3 install --upgrade pip
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 check_my_work.py 0
# ==========================================================
#    Lab 17 (The Great Carrot Cake Heist) - Check My Work
# ==========================================================
#
# STEP 0 - Setup
#   [PASS] Python 3.8 or newer (you have 3.15.2)
#   [PASS] matplotlib is installed
#   [PASS] chat.txt is in the lab folder
#
# ----------------------------------------------------------
#   3 / 3 checks passed
#   CASE CLOSED! Great detective work!
# ----------------------------------------------------------
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 check_my_work.py 1
# ==========================================================
#    Lab 17 (The Great Carrot Cake Heist) - Check My Work
# ==========================================================
#
# STEP 1 - Strings + tuples
#   [PASS] TODO 1: parse_line() returns ((15, 18), 'Tina', 'zzz... still asleep in my shell')
#   [PASS] TODO 1: the result is a tuple, and the time inside it is a tuple too
#   [PASS] TODO 1: the whole chat loads (32 messages, extra spaces removed)
#
# ----------------------------------------------------------
#   3 / 3 checks passed
#   CASE CLOSED! Great detective work!
# ----------------------------------------------------------
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 main.py
#
#    THE GREAT CARROT CAKE HEIST
#    Someone ate the bake-sale cake. The only evidence: the group chat.
#
#    Loaded 32 messages. The first one is a tuple:
#    ((14, 2), 'Biscuit', "I baked a carrot cake for tomorrow's bake sale!!! It's cooling in the kitchen.")
#
# ============================================================
#   CLUE 1  (Step 2: lists)  What was Tina doing?
# ============================================================
#    [locked] Finish Step 2 to unlock this clue.
#
# ============================================================
#   CLUE 2  (Step 3: dictionaries)  Who talked the most?
# ============================================================
#    [locked] Finish Step 3 to unlock this clue.
#
# ============================================================
#   CLUE 3  (Step 4: sets)  Who could have done it?
# ============================================================
#    [locked] Finish Step 4 to unlock this clue.
#
# ============================================================
#   CLUE 4  (Step 5: arguments + scope)  The evidence
# ============================================================
#    [locked] Finish Step 5 to unlock this clue.
#
#    Not enough clues yet to name the thief. Keep going!
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 check_my_work.py 2
# ==========================================================
#    Lab 17 (The Great Carrot Cake Heist) - Check My Work
# ==========================================================
#
# STEP 2 - Lists + list comprehensions
#   [PASS] TODO 2a: messages_from() returns a list of one critter's texts
#   [PASS] TODO 2b: shouts() keeps only the ALL CAPS messages
#
# ----------------------------------------------------------
#   2 / 2 checks passed
#   CASE CLOSED! Great detective work!
# ----------------------------------------------------------
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 main.py
#
#    THE GREAT CARROT CAKE HEIST
#    Someone ate the bake-sale cake. The only evidence: the group chat.
#
#    Loaded 32 messages. The first one is a tuple:
#    ((14, 2), 'Biscuit', "I baked a carrot cake for tomorrow's bake sale!!! It's cooling in the kitchen.")
#
# ============================================================
#   CLUE 1  (Step 2: lists)  What was Tina doing?
# ============================================================
#    Tina: slow and steady... time for a nap in my shell. goodnight everyone
#    Tina: zzz... still asleep in my shell... definitely not in the kitchen
#    Tina: mmm what a nice dream. a very sweet dream
#    Tina: wow. who would eat a whole cake with cream cheese frosting. so sad.
#    Tina: ...
#
#    7 messages were written in ALL CAPS. The loudest:
#    PERFECT FOR CARROTS! PERFECT FOR CARROTS!
#
# ============================================================
#   CLUE 2  (Step 3: dictionaries)  Who talked the most?
# ============================================================
#    [locked] Finish Step 3 to unlock this clue.
#
# ============================================================
#   CLUE 3  (Step 4: sets)  Who could have done it?
# ============================================================
#    [locked] Finish Step 4 to unlock this clue.
#
# ============================================================
#   CLUE 4  (Step 5: arguments + scope)  The evidence
# ============================================================
#    [locked] Finish Step 5 to unlock this clue.
#
#    Not enough clues yet to name the thief. Keep going!
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python check_my_work.py 3
# zsh: command not found: python
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 check_my_work.py 3
# ==========================================================
#    Lab 17 (The Great Carrot Cake Heist) - Check My Work
# ==========================================================
#
# STEP 3 - Dictionaries
#   [PASS] TODO 3: count_messages() counts messages per sender
#   [PASS] TODO 3: works on the real chat (Biscuit sent 8 messages)
#
# ----------------------------------------------------------
#   2 / 2 checks passed
#   CASE CLOSED! Great detective work!
# ----------------------------------------------------------
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 main.py
#
#    THE GREAT CARROT CAKE HEIST
#    Someone ate the bake-sale cake. The only evidence: the group chat.
#
#    Loaded 32 messages. The first one is a tuple:
#    ((14, 2), 'Biscuit', "I baked a carrot cake for tomorrow's bake sale!!! It's cooling in the kitchen.")
#
# ============================================================
#   CLUE 1  (Step 2: lists)  What was Tina doing?
# ============================================================
#    Tina: slow and steady... time for a nap in my shell. goodnight everyone
#    Tina: zzz... still asleep in my shell... definitely not in the kitchen
#    Tina: mmm what a nice dream. a very sweet dream
#    Tina: wow. who would eat a whole cake with cream cheese frosting. so sad.
#    Tina: ...
#
#    7 messages were written in ALL CAPS. The loudest:
#    PERFECT FOR CARROTS! PERFECT FOR CARROTS!
#
# ============================================================
#   CLUE 2  (Step 3: dictionaries)  Who talked the most?
# ============================================================
#    Biscuit  ########  8
#    Rocket   #####  5
#    Tina     #####  5
#    Mochi    ####  4
#    Nibbles  ####  4
#    Chaos    ###  3
#    Pixel    ###  3
#
#    Top talker: Biscuit with 8 messages
#    Most exclamation marks: Biscuit
#
# ============================================================
#   CLUE 3  (Step 4: sets)  Who could have done it?
# ============================================================
#    [locked] Finish Step 4 to unlock this clue.
#
# ============================================================
#   CLUE 4  (Step 5: arguments + scope)  The evidence
# ============================================================
#    [locked] Finish Step 5 to unlock this clue.
#
#    Not enough clues yet to name the thief. Keep going!
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 check_my_work.py 4
# ==========================================================
#    Lab 17 (The Great Carrot Cake Heist) - Check My Work
# ==========================================================
#
# STEP 4 - Sets
#   [PASS] TODO 4a: senders_between() returns a SET of names in the time window
#   [PASS] TODO 4b: who_mentioned() ignores upper/lower case
#   [PASS] TODO 4c: find_culprit() = (online & knew_secret) - alibis
#
# ----------------------------------------------------------
#   3 / 3 checks passed
#   CASE CLOSED! Great detective work!
# ----------------------------------------------------------
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % python3 main.py
#
#    THE GREAT CARROT CAKE HEIST
#    Someone ate the bake-sale cake. The only evidence: the group chat.
#
#    Loaded 32 messages. The first one is a tuple:
#    ((14, 2), 'Biscuit', "I baked a carrot cake for tomorrow's bake sale!!! It's cooling in the kitchen.")
#
# ============================================================
#   CLUE 1  (Step 2: lists)  What was Tina doing?
# ============================================================
#    Tina: slow and steady... time for a nap in my shell. goodnight everyone
#    Tina: zzz... still asleep in my shell... definitely not in the kitchen
#    Tina: mmm what a nice dream. a very sweet dream
#    Tina: wow. who would eat a whole cake with cream cheese frosting. so sad.
#    Tina: ...
#
#    7 messages were written in ALL CAPS. The loudest:
#    PERFECT FOR CARROTS! PERFECT FOR CARROTS!
#
# ============================================================
#   CLUE 2  (Step 3: dictionaries)  Who talked the most?
# ============================================================
#    Biscuit  ########  8
#    Rocket   #####  5
#    Tina     #####  5
#    Mochi    ####  4
#    Nibbles  ####  4
#    Chaos    ###  3
#    Pixel    ###  3
#
#    Top talker: Biscuit with 8 messages
#    Most exclamation marks: Biscuit
#
# ============================================================
#   CLUE 3  (Step 4: sets)  Who could have done it?
# ============================================================
#    Online during the heist:  ['Biscuit', 'Chaos', 'Mochi', 'Pixel', 'Rocket', 'Tina']
#    Knew the secret frosting: ['Biscuit', 'Pixel', 'Tina']
#    Have an alibi:            ['Biscuit', 'Pixel', 'Rocket']
#
# ============================================================
#   CLUE 4  (Step 5: arguments + scope)  The evidence
# ============================================================
#    [locked] Finish Step 5 to unlock this clue.
#
# ============================================================
#   THE REVEAL
# ============================================================
#    After careful analysis, the cake thief is...  TINA!!!
#
#    Tina: ...it was slow. and steady. and DELICIOUS.
#
#    Opening the case file chart... (close the chart window to finish)
#
#    [locked] Finish Step 6 (charts.py) to see the case file.
# hongyili@Hongyis-MacBook-Air Lab17_CakeHeist % ----------------------------
# STEP 5: arguments
# -------------------------------------------------------------------
def search(messages, word, sender=None, ignore_case=True):    # TODO 5a (part 1): add 2 parameters with default values
    """Return a list of message tuples whose text contains word.

    sender       (default None)  -> if given, only that critter's messages
    ignore_case  (default True)  -> if True, "CAKE" also matches "cake"
    """
    # TODO 5a (part 2):
    #   1. add the parameters  sender=None  and  ignore_case=True  to the def line above
    #   2. loop over the messages and keep the WHOLE tuple (time, who, text) when:
    #        - sender is None, OR who == sender
    #        - AND word is in text  (if ignore_case is True, compare both in lower case)
    #   3. return the list of matching tuples
    results = []

    for time, who, text in messages:
        if sender is not None and who != sender:
            continue

        if ignore_case:
            found = word.lower() in text.lower()
        else:
            found = word in text

        if found:
            results.append((time, who, text))

    return results

def count_words(messages, *words):    # TODO 5b (part 1): make this take ANY number of words
    """Return a dictionary: for each word, how many messages contain it (ignore case).

    count_words(messages, "cake", "nap")  ->  {"cake": 6, "nap": 2}
    """
    # TODO 5b (part 2):
    #   1. change  words  to  *words  in the def line, so you can call
    #      count_words(messages, "cake", "nap", "dream")  with as many words as you like
    #      (inside the function, words is then a TUPLE of all those words)
    #   2. build a dictionary  {word: number of messages that contain it}
    #      Reuse your search() function:   len(search(messages, word))
    counts = {}

    for word in words:
        counts[word] = len(search(messages, word))

    return counts

# -------------------------------------------------------------------
# STEP 5: scope
# -------------------------------------------------------------------
total_drama = 0          # a GLOBAL variable: it lives outside every function


def add_drama(text):
    """Add drama points for one message to the global total_drama. Return the points."""
    # TODO 5c: this function has a SCOPE BUG. Run main.py (or check_my_work.py 5) to see it:
    #   UnboundLocalError: cannot access local variable 'total_drama'...
    #   Fix it by adding ONE line at the top of this function that tells Python
    #   total_drama is the GLOBAL variable, not a new local one.
    global total_drama
    points = text.count("!")
    if text.isupper():
        points += 5
    total_drama = total_drama + points
    return points
