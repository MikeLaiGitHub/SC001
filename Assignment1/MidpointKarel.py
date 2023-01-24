"""
File: MidpointKarel.py
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
    # This function will check the the space is 1x1 or 2x2, if not both then Karel will fill the street and take beeper
    # from left then right until midpoint is located.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east.
    post-condition: Karel at the midpoint facing either west or east.
    """
    one_one_two_two_checker()
    fill_the_street()
    clean_both_side()
    clean_inside()
    midpoint_located()


def fill_the_street():
    # """
    # Karel will fill the street with beepers.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east.
    post condition: Karel filled the street with beepers facing west.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_around()


def turn_around():
    # """
    # Karel will turn left two times.
    # """
    turn_left()
    turn_left()


def clean_both_side():
    # """
    # Karel will clean up the beepers at the leftmost and rightmost point.
    # """
    """
    pre-condition: Karel is at the rightmost point of the street facing west.
    post-condition: Karel finished clean up the beepers at the leftmost and rightmost point facing west.
    """
    for i in range(2):
        while front_is_clear():
            move()
        if on_beeper():
            pick_beeper()
            turn_around()


def clean_inside():
    # """
    # Karel will cleanup the beepers inside left and right until no beeper left and 1 avenue away from midpoint.
    # """
    """
    pre-condition: Karel is at the rightmost of the street facing west.
    post-condition: Karel finish cleaning up the beepers and 1 avenue away from the midpoint facing west or east depend
                    on the length of the street is odd or even.
    """
    move()
    while on_beeper():
        move()
    turn_around()
    move()
    pick_beeper()
    move()
    if on_beeper():
        clean_inside()


def go_back():
    # """
    # Karel will go back to its previous location.
    # """
    turn_around()
    move()


def midpoint_located():
    # """
    # Karel will go back to the midpoint.
    # """
    """
    pre-condition: Karel finish cleaning up the beepers and 1 avenue away from the midpoint facing west or east
                   depending on the length of the street is even or odd.
    post-condition: Karel go back to the midpoint facing either right oe west depending on the length of the street is
                    even or odd.
    """
    if not on_beeper():
        go_back()
        put_beeper()


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
    # This function will combine two checker in 1.
    # """
    if not front_is_clear():
        one_one_checker()
    else:
        two_two_checker()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
