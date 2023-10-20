# dice.py

import random


def parse_input(input_string: str) -> int:
    """Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    what went wrong and abort program.

    >>> print(parse_input("2"))
    2

    >>> print(parse_input("7"))
    Traceback (most recent call last):
    ...
    AssertionError: Input must be 1-6, but is 7

    >>> parse_input(3)
    Traceback (most recent call last):
    ...
    AttributeError: 'int' object has no attribute 'strip'

    """
    assert input_string.strip() in {
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
    }, f"Input must be 1-6, but is {input_string}"
    return int(input_string)


def roll_dice(num_dice: int) -> list[int]:
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.

    >>> random.seed(10)
    >>> roll_dice(3)
    [5, 1, 4]

    >>> len(roll_dice(2))
    2

    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


#   assert all(
#       [1 <= el <= 6 for el in roll_result]
#   )  # where does it go? pylint shades assertion grey which meanst that it is unreachable


DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])  # number of vertical components
DIE_WIDTH = len(DICE_ART[1][0])  # number of horizontal components
DIE_FACE_SEPARATOR = " "


def generate_dice_faces_diagram(dice_values: list[int]) -> str:
    """Return an ASCII diagram of dice faces from `dice_values`.

    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:

    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘


    >>> print(generate_dice_faces_diagram([4, 1, 3, 2]))
    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘

    >>> random.seed(10)
    >>> len(DICE_ART[1])
    5

    """
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)
    diagram_header = _headers(dice_faces_rows)
    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    assert len(DICE_ART[1]) == DIE_HEIGHT  # is this position correct?

    return dice_faces_diagram


def _headers(dice_faces_rows: list[str]) -> str:
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")
    return diagram_header


def _get_dice_faces(dice_values: list[int]) -> list[str]:
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces


def _generate_dice_faces_rows(dice_faces: list[str]) -> list[str]:
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows


# ~~~ App's main code block ~~~
# 1. Get and validate user's input
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)
# 2. Roll the dice
roll_results = roll_dice(num_dice)
# print(roll_results)  # for testing purposes, remove later
# 3. Generate the ASCII diagram of dice faces
dice_face_diagram = generate_dice_faces_diagram(roll_results)
# 4. Display the diagram
print(f"\n{dice_face_diagram}")


def _test():
    # for parse_input
    assert parse_input("1") == 1
    assert parse_input("6") == 6

    # for roll dice
    random.seed(
        10
    )  # we dont need to import it, as import random is the second line we run in the python script
    roll_dice(3)  # shebang is the first

    assert len(roll_dice(3)) == 3  # simple length check

    result = roll_dice(4)
    print(result)
    assert all([1 <= el <= 6 for el in result])

    # for generate_dice_faces diagram
    print(generate_dice_faces_diagram([4, 1, 3, 2]))
    assert len(DICE_ART[1]) == DIE_HEIGHT


# _test()  # comment this line out to prevent calling the test function
