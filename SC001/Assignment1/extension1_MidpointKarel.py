"""
File: extension1_MidpointKarel.py
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
    # Karel will check if the space is 1x1 or 2x2, if not then Karel will find the midpoint by put beeper at rightmost
    # and leftmost then move both in by one avenue until both on the same spot.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east.
    post-condition: Karel at the midpoint facing east or west depending on the length of the street is odd or even.
    """
    one_one_two_two_checker()
    put_both_side()
    mid_point_finder()


def turn_around():
    # """
    # This will make Karel turn left 2 times.
    # """
    turn_left()
    turn_left()


def mid_point_finder():
    # """
    # Karel will find the midpoint by moving both beepers at the leftmost then rightmost by 1 avenue in until both
    # beeper are at the same spot.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 of the street facing west.
    post-condition: Karel at the midpoint facing east or west depending on the length of the street is odd or even.
    """
    if on_beeper():
        pick_beeper()
        move()
        put_beeper()
    while front_is_clear():
        move()
        if on_beeper():
            turn_around()
            pick_beeper()
            move()
            if on_beeper():
                pass
            else:
                put_beeper()
    turn_around()
    while not on_beeper():
        move()


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


def put_both_side():
    # """
    # Karel will put beepers at the leftmost and rightmost of the street.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east.
    post-condition: Karel put down the beepers at the rightmost of the street facing west.
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
