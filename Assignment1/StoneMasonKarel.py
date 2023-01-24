"""
File: StoneMasonKarel.py
Name: Mike
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    # """
    # Karel will fix all the pillars.
    # """
    """
    pre-condition: Karel is at the street 1 avenue 1 facing right.
    post-condition: Karel fixed all the pillars at the bottom rightmost of the last pillar facing East.
    """
    while front_is_clear():
        fix()
        next_pillar()
    if not front_is_clear():
        fix()


def fix():
    # """
    # Karel will fix the pillar at his position then go back to the previous spot.
    # """
    """
    pre-condition: Karel is at the bottom of the pillar facing East.
    post-condition: Karel fixed the pillar and go back to the bottom of it facing East.
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        else:
            move()
    if not front_is_clear():
        if not on_beeper():
            put_beeper()
    go_back()


def go_back():
    # """
    # Karel will go back to its previous location.
    # """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def turn_around():
    # """
    # Karel will turn left 2 times.
    # """
    turn_left()
    turn_left()


def turn_right():
    # """
    # Karel will turn left three times.
    # """
    for i in range(3):
        turn_left()


def next_pillar():
    # """
    # Karel will go from the current pillar to the next pillar.
    # """
    for i in range(4):
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
