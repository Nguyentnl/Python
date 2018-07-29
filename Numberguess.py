"""Rolling a pair of dice. Let's guess the sum"""

from random import randint
from time import sleep


def get_user_guess():
    guess = int(raw_input("Guess a number: "))
    return guess

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print "The maximum possible value is: %d" % max_val
    guess = get_user_guess()
    if guess > max_val:
        print "This is invalid number. No guess higher than the maximum possible value"
    else:
        print "Rolling..."
        sleep(2)
        print "The first roll is: %d" % first_roll
        sleep(1)
        total_roll = first_roll + second_roll
        print "The total roll is: %d" % total_roll
        print "Result..."
        sleep(1)
        if guess == total_roll:
            print "Congratulations! You win the game"
        else:
            print "Sorry. Good luck the next time"


roll_dice(6)
