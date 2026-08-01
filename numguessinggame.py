# Python Number Guessing Game

# importing random module
import random

# this is where you play the game
def game(lowest_num, highest_num, guesses):
    # a list of guessed numbers is created to save all the numbers you have guessed
    guessed_numbers = []
    # the number you have to guess is generated here
    answer = random.randint(lowest_num, highest_num)

    # you guess the number until all the guesses are used or... well you guessed it
    while guesses > 0:
        guess = input(f"Enter your guess between {lowest_num} and {highest_num}: ")

        if guess.isdigit():
            guess = int(guess)

            if guess < lowest_num or guess > highest_num:
                print(f"You should pick a number between {lowest_num} and {highest_num}")
            elif guess < answer:
                print("Too low! Try again!")
                guessed_numbers.append(guess)
            elif guess > answer:
                print("Too high! Try again!")
                guessed_numbers.append(guess)
            elif guess == answer:
                print(f"CORRECT! The answer was {answer}")
                break
        else:
            print("Invalid guess. Try again!")

        guesses -= 1

    # if you didn't guess the number after all the guesses are used, the answer shows here
    if guesses == 0 and answer not in guessed_numbers:
        print("Better luck next time.")
        print(f"The answer was {answer}")


# this is where the program starts
print("Python Number Guessing Game")
is_running = True

while is_running:
    # you choose the difficulty here
    while True:
        difficulty = input("Choose the difficulty (E for Easy, M for Medium, MH for Medium-Hard, H for Hard, X for Extremely Hard, C for Custom, Q to Quit): ").lower()

        if difficulty == "e": # easy difficulty
            game(1,100,10)
            break
        elif difficulty == "m": # medium difficulty
            game(1, 100, 5)
            break
        elif difficulty == "mh": # medium-hard difficulty
            game(1, 1000, 5)
            break
        elif difficulty == "h": # hard difficulty
            game(1, 1000, 3)
            break
        elif difficulty == "x": # extreme difficulty
            game(1, 1000, 1)
            break
        elif difficulty == "c":
            num_is_valid = False

            # this is where you customize your difficulty. you need to obey 4 rules (shown below)
            while not num_is_valid:
                custom_lowest_num = float(input("Choose the lowest number: "))
                custom_highest_num = float(input("Choose the highest number: "))
                custom_guess = float(input("How many guesses?: "))

                # 1. numbers should be integers. you cannot use numbers with decimal point
                if custom_lowest_num - int(custom_lowest_num) != 0 or custom_highest_num - int(custom_highest_num) != 0 or custom_guess - int(custom_guess) != 0:
                    print("Numbers should be integers. Try again!")
                # 2. numbers should be positive. you cannot put negative numbers
                elif custom_lowest_num < 0 or custom_highest_num < 0 or custom_guess < 0:
                    print("Numbers should be positive. Try again!")
                # 3. lowest number should be less than the highest number
                elif custom_lowest_num > custom_highest_num:
                    print("The lowest number cannot be greater than the highest number ")
                # 4. both the lowest number and the highest number cannot be equal
                elif custom_lowest_num == custom_highest_num:
                    print("The lowest number and the highest number cannot be equal")
                # if you obey these rules, you can play in your difficulty
                else:
                    custom_lowest_num = int(custom_lowest_num)
                    custom_highest_num = int(custom_highest_num)
                    custom_guess = int(custom_guess)
                    num_is_valid = True

            game(custom_lowest_num, custom_highest_num, custom_guess)
            break
        elif difficulty == "q":
            is_running = False
            break
        else:
            print("Invalid choice!")


    # wanna play again? you should answer with y or n
    while is_running:
        play_again = input("Want to play again? (Y/N): ").lower()

        if play_again == "n":
            is_running = False
        elif play_again == "y":
            break
        elif play_again not in ("y", "n"):
            print("Invalid choice!")

# the end
print("Thank you for playing!")
print("See you next time! 👍")