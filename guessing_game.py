import random
from statistics import mean
from statistics import mode
from statistics import median


attempts_list = []
print("Hello, welcome to the game.")


def try_again():
    number = input("Please guess a number between 0 and 100: ")
    try:
        number = int(number)
        return number
    except ValueError:
        print("Oh no, we ran into an error. Please try again")
    return try_again()

def wrong_answer():
    print("The answer you provided is not correct!")
    decision = str(input("Would you like to play again: Y / N: ")).lower()
    return decision

def play_again():
    print(f"The average of all your rounds is: {mean(attempts_list)} attempt(s)")
    print(f"The median of all your rounds is: {median(attempts_list)} attempt(s)")
    print(f"The highest attempt of all your rounds is: {mode(attempts_list)} attempt(s)")
    print(f"Your current highscore is: {min(attempts_list)} attempt(s)")
    repeat_game = str(input("Would you like to play again: Y / N: ")).lower()
    while repeat_game not in ["n", "y"]:
        repeat_game = wrong_answer()
    return repeat_game

def start_game():
    attempt = 0
    random_number = random.randint(0, 101)
    print(random_number)
    while True:
        guess_number = try_again()
        if guess_number > 100 or guess_number < 0:
            print("the number has to be between 0 and 100, please try again")
            continue
        if guess_number < random_number:
            print("the number is higher...guess again!")
            attempt += 1
            continue
        if guess_number > random_number:
            print("the number is lower...guess again!")
            attempt += 1
            continue
        if guess_number == random_number:
            print("you guessed the correct number")
            attempt = attempt + 1
            print("You had this many attempt(s) in this round:", attempt)
            attempts_list.append(attempt)
            repeat_game = play_again()
            if repeat_game.lower().strip() == "n":
                print("Thanks for playing the game!")
                print(f"Your highscore was: {min(attempts_list)} attempt(s)")
                quit()
            elif repeat_game.lower().strip() == "y":
                start_game()


start_game()



