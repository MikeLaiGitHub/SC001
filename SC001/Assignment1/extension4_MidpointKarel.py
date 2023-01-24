"""
File: extension4_MidpointKarel.py
Name: Mike
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    # """
    # Karel will check if the space is 1x1 or 2x2, then find the midpoint by going to the diagonal point of street 1
    # avenue 1 and go to midpoint by going down twice and move left once from the spot near the diagonal point, making
    # Karel move half way back from the starting point.
    # """
    """
    pre-condition: Karel is at the street 1 avenue 1 facing east.
    post-condition: Karel will be at the midpoint at street 1 facing south.
    """
    one_one_two_two_checker()
    move_to_diagonal_point()
    setup_for_midpoint_finder()
    midpoint_finder()


def setup_for_midpoint_finder():
    # """
    # To make this method work, Karel will need to be at the point near the diagonal point of street 1 avenue 1.
    # """
    """
    pre-condition: Karel is at the diagonal point of street 1 avenue 1 facing east.
    post-condition: Karel is at the point near the diagonal point of street 1 avenue 1 facing south.
    """
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def move_to_diagonal_point():
    # """
    # Karel will go to the diagonal point of street 1 avenue 1.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east.
    post-condition: Karel is at the diagonal point of street 1 avenue 1 facing east.
    """
    while front_is_clear():
        turn_left()
        move()
        turn_right()
        move()


def midpoint_finder():
    # """
    # Karel will find and go to the midpoint by going down twice and going left once.
    # """
    """
    pre-condition: Karel is at the point near the diagonal point of street 1 avenue 1 facing south.
    post-condition: Karel is at the midpoint in street 1 facing south.
    """
    while front_is_clear():
        move()
        if front_is_clear():
            move()
        if front_is_clear():
            turn_right()
            move()
            turn_left()


def turn_right():
    # """
    # This will make Karel turn left three times.
    # """
    for i in range(3):
        turn_left()


def one_one_checker():
    # """
    # This function will check if the given space is 1x1 or not.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east.
    post-condition: Karel finish checking facing east at street 1 avenue 1.
    """
    for i in range(2):
        if not front_is_clear():
            turn_around()
    put_beeper()


def two_two_checker():
    # """
    # This function will check if the given space is 2x2 or not.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east.
    post-condition: Karel finish checking facing east at street 1 avenue 1.
    """
    move()
    if front_is_clear():
        go_back()
        turn_around()
    put_beeper()


def one_one_two_two_checker():
    # """
    # This function will combine 1x1 and 2x2 checker in 1.
    # """
    if not front_is_clear():
        one_one_checker()
    else:
        two_two_checker()


def go_back():
    # """
    # This will make Karel go back to its previous location.
    # """
    turn_around()
    move()


def turn_around():
    # """
    # This will make Karel turn left 2 times.
    # """
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
