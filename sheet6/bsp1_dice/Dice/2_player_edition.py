import Dice


def players(num_of_players):
    """Takes a number of players and iterates the loop over the number of players and carrys out the dice.py file to simulate the dice."""
    player_with_advantage = 0  # wähle einen Spieler der den Vorteil erhalten soll. 0 für Spieler 1 und 1 für Spieler 2
    user_input_string = input("Enter a number between 1 and 6: ")
    number_dice_int = Dice.parse_input(user_input_string)
    for player in range(num_of_players):
        # 2. Roll the dice
        has_advantage = (
            player == player_with_advantage
        )  # gibt true zurück für den jeweiligen Spieler, der den Vorteil besitzt. Das ganze wird dann im if-Statement der Dice-Funktion berücksichtigt.
        roll_results_list = Dice.roll_dice(number_dice_int, has_advantage)
        # 3. Generate the die faces diagram
        dice_faces_diagram_string = Dice.generate_dice_faces_diagram(roll_results_list)
        print("Player", player + 1)
        print(dice_faces_diagram_string)


players(2)
# Main section
