# dice.py

#DICE_FACES = ?
import random
def parse_input(input_string):
    """Validate user input and convert to integer between 1 and 6.
    Return integer between 1 and 6."""
    assert input_string.strip() in {"1", "2", "3", "4", "5", "6"}, f"Input must be 1-6, but is {input_string}"
    return int(input_string)
    pass


def roll_dice(num_dice):
    """Simulate rolling the dice, corresponding to number_dice.
    Return list of integers representing results of dice rolling."""
    assert len(roll_dice(3)) == 3  # simple length check


    result = roll_dice(4)
    print(result) # check type and range of output values
    assert all([1 <= el <= 6 for el in result])
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_result
    
    pass


def generate_dice_faces_diagram(dice_values):
    """Create graphical representation of the dice values.
    Return resulting string."""
    pass


# Main section
#user_input = None  # get user input here; use "None" for testing
numb_dice = parse_input("3")
#roll_results = roll_dice(number_dice)
#dice_faces_diagram = generate_dice_faces_diagram(roll_results)
#print(dice_faces_diagram)

