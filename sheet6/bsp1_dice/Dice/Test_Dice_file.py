import Dice


def _test_parse_input():
    assert Dice.parse_input("1") == 1
    assert Dice.parse_input("6") == 6


def _test_roll_dice():
    assert len(Dice.roll_dice(4)) == 4
    result = Dice.roll_dice(4)
    print(result)
    assert all([1 <= el <= 6 for el in result])  # check type and range of output values


def _test_generate_dice_faces_diagram():
    assert (
        Dice.generate_dice_faces_diagram([5, 3])
        == r"""~~~~~~~ RESULTS ~~~~~~~
┌─────────┐ ┌─────────┐
│  ●   ●  │ │  ●      │
│    ●    │ │    ●    │
│  ●   ●  │ │      ●  │
└─────────┘ └─────────┘"""
    )


_test_parse_input()
_test_roll_dice()
_test_generate_dice_faces_diagram()
print("All tests were a success!")
