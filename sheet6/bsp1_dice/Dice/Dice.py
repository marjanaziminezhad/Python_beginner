#!/usr/bin/env python
# dice.py

# DICE_FACES = ?
import random
from Dice_diagramm import *  # tut so als ob der Code im aktuellen File stehen würde
import Simulation


def parse_input(user_input: str) -> int:
    """Validate user input and convert to integer between 1 and 6.
    Return integer between 1 and 6.
    Examples:
    >>> parse_input("5")
    5
    >>> parse_input("7")
    Traceback (most recent call last):
        ...
    SystemExit: 1
    """

    if user_input.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(user_input)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)


def roll_dice(number_dice: int, with_advantage=False) -> list[int]:
    """Simulate rolling the dice, corresponding to number_dice.
    Return list of integers representing results of dice rolling.
    Example:
    >>> len(roll_dice(2))
    2
    """

    roll_results = []
    for _ in range(number_dice):
        if with_advantage:
            roll = random.randint(5, 6)
        else:
            roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces


def generate_dice_faces_diagram(dice_values: list[int]) -> str:
    """Create graphical representation of the dice values.
    Return resulting string.
    Example:
    >>> print(generate_dice_faces_diagram([6, 3]))
    ~~~~~~~ RESULTS ~~~~~~~
    ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │  ●      │
    │  ●   ●  │ │    ●    │
    │  ●   ●  │ │      ●  │
    └─────────┘ └─────────┘

    """
    dice_faces = _get_dice_faces(dice_values)
    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    assert len(dice_faces_rows) == DIE_HEIGHT
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


if __name__ == "__main__":
    # Main section
    # 1. Get and validate user's input
    user_input_string = input("Enter a number between 1 and 6: ")
    number_dice_int = parse_input(user_input_string)
    Simulation.roll_the_dice()
    # 2. Roll the dice
    roll_results_list = roll_dice(number_dice_int)
    # 3. Generate the die faces diagram
    dice_faces_diagram_string = generate_dice_faces_diagram(roll_results_list)
    print(dice_faces_diagram_string)
    import doctest

    doctest.testmod()
