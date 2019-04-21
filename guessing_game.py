# --------------------------------
# Number Guessing Game
# --------------------------------

import random

high_score = []


def main_menu():
    print("""
------------------------------------
Welcome to the Number Guessing Game!
------------------------------------
Enter 'Start' to start game.
Enter 'Quit' to quit game. 
""")

while True:
    main_menu()
    if high_score:
        print("** Last games highest score was {} **".format(min(high_score)))
    user_command = input(">").lower()
    if user_command == "start":
        random_number = random.randint(1, 10)
        attempt_count = 1
        while True:
            try:
                user_guess = input("Pick a number between 1 and 10: ")
                user_guess = int(user_guess)
                if user_guess > 10:
                    print("Uh-Oh! Looks like that number is not between 1 and 10. Try again.")
                    attempt_count += 1
                    continue
                elif user_guess == random_number:
                    print("You got it! It took you {} tries!".format(attempt_count))
                    high_score.append(attempt_count)
                    print("\nThe high score is {}".format(min(high_score)))
                    play_again = input("\nWould you like to play again? [Y]es or [N]o: ").lower()
                    if play_again == "y":
                        random_number = random.randint(1, 10)
                        attempt_count = 1
                        continue
                    elif play_again == "n":
                        print("\nReturning to the main menu, see you next time!")
                        break
                    else:
                        print("\nI don't understand that :(. Returning to the main menu.")
                        break
                elif user_guess > random_number:
                    print("It's lower!")
                    attempt_count += 1
                    continue
                elif user_guess < random_number:
                    print("It's higher!")
                    attempt_count += 1
                    continue
            except ValueError:
                # Handle exception if user does not enter a valid number the program
                print("Woah! I didn't expect that! Guesses must be between 1 and 10. Let's start again...")

    elif user_command == "quit":
        print("Thank you for playing!")
        break
    elif user_command != "start" or "quit":
        print("\nOops! I don't understand that. Please enter 'start' to begin or 'quit' to end the game")
        continue
