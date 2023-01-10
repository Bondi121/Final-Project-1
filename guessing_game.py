import random
from statistics import mean
from statistics import mode
from statistics import median


attempts_list = []
print(attempts_list)

#Display intro message to the player
print("Hello, welcome to the game")
#Store a random number as the answer


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
    print("The mean was: ", mean(attempts_list), " attempts")
    print("The median was: ", median(attempts_list)," attempts")
    print("The mode was: ", mode(attempts_list), " attempts")
    repeat_game = str(input("Would you like to play again: Y / N: ")).lower()
    while repeat_game not in ["n", "y"]:
        repeat_game = wrong_answer()
    return repeat_game

def start_game():
    attempt = 0
    random_number = random.randint(0, 101)
    print(random_number)
    while True:
        #Prompt the player for a guess
        guess_number = try_again()
        #if the guess great than the solution, display "it's lower"
        if guess_number < random_number:
            print("the number is higher...guess again!")
            attempt += 1
            print(attempt)
            continue
        if guess_number > random_number:
            print("the number is lower...guess again!")
            attempt += 1
            print(attempt)
            continue
            #if the guess is less than the solution, display "it's higher"
        if guess_number == random_number:
            print("you guessed the correct number")
            attempt = attempt + 1
            print("You had this many attempts:", attempt)
            attempts_list.append(attempt)
            repeat_game = play_again()
            if repeat_game.lower().strip() == "n":
                break
            elif repeat_game.lower().strip() == "y":
                start_game()

            #Save their attempt to a list

start_game()

#At the end of the game, show the plazer # number of atempts # mean, median, and mode of the saved attempts list
#ask player if they want to play again

#once the guess is corret, stoop looping, inform the player they got it and show number of attepts


