from sys import stdout
import random
import time

target = 0


def add_text(text, speed=0.5):
    stdout.write(text)
    stdout.flush()
    time.sleep(speed)


def first_guess():
    add_text("I'm thinking of a number between -100 and 100. Can you guess it?")
    return input("\n")


def victory():
    add_text("You got it! \n")
    if play_again():
        play()


def play_again():
    add_text("Would you like to play again? (Y/N)")
    return yes_no()


def yes_no():
    response = input("\n")
    if response.lower() == "y":
        return True
    if response.lower() == "yes":
        return True
    return False


def too_big():
    add_text("Incorrect guess - your guess is larger than the target number. \n")
    guess_again()


def too_small():
    add_text("Incorrect guess - your guess is smaller than the target number. \n")
    guess_again()


def guess_again():
    add_text("Please guess again.")
    guessing(input("\n"))


def guessing(guess):
    guess = int(guess)
    if guess == target:
        victory()

    if guess > target:
        too_big()

    if guess < target:
        too_small()


def goodbye():
    add_text("goodbye")


def play():
    global target
    target = random.randint(-100, 100)
    guessing(first_guess())
    goodbye()


play()
