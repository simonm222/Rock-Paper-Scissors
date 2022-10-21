import random

is_true = True
players_name = str(input("Please type your player name here: \n"))
bot_name = "BOT"

# While loop so the game can be replayed until the user types no
while is_true:

    def rock_paper_scissors(choice, name):
        """Function that takes the choice and name of the player/bot and prints what they chose"""
        if choice == 1:
            print(f"{name} chose rock")
            return 1
        elif choice == 2:
            print(f"{name} chose paper")
            return 2
        elif choice == 3:
            print(f"{name} chose scissors")
            return 3


    def compare(first_player, other_player, first_name, other_name):
        """
        Compares the first players choice and bots choice
        Takes players name and bots name to output name specific string
        """
        if first_player == other_player:
            print("It's a tie")
        elif first_player == 3 and other_player == 1:
            print(f"{first_name} loses {other_name} wins")
        elif first_player == 1 and other_player == 3:
            print(f"{first_name} wins {other_name} loses")
        elif first_player > other_player:
            print(f"{first_name} wins {other_name} loses")
        elif first_player < other_player:
            print(f"{first_name} loses {other_name} wins")


    # Ask for the users choice and saves it into a variable for later use

    users_choice = int(input("Type 1 for rock 2 for paper or 3 for scissors: "))
    bot_choice = random_choice = random.randint(1, 3)

    # Call the RPS function to output what the player and bot chose
    single_player_choice = rock_paper_scissors(users_choice, players_name)
    bot = rock_paper_scissors(bot_choice, bot_name)

    # Call the compare function to compare then print who won and lost
    compare(first_player=users_choice, first_name=players_name, other_player=bot, other_name=bot_name)

    # input that asks whether the player wants to play again or not
    play_again = str(input("Would you like to play again? Type yes or no: ")).lower()

    # Closes the while loop if the player chooses no - otherwise continues
    if play_again == "no":
        print("Thanks for playing goodbye!")
        is_true = False
    elif play_again == "yes":
        continue
    else:
        check_if_true = True
        while check_if_true:
            new_input = str(input("Sorry i didn't get that... Please type either yes or no: ")).lower()
            if new_input == "yes":
                check_if_true = False
            elif new_input == "no":
                print("Thanks for playing goodbye!")
                check_if_true = False
                is_true = False



