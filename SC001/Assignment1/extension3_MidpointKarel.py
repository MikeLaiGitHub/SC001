"""
File: extension3_MidpointKarel.py
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
    # Karel will check if the space is 1x1 or 2x2, if not Karel will put beepers like a stair to the diagonal point, and
    # do the same from the bottom rightmost of the street, midpoint will be located after Karel reach the beeper in the
    # same avenue.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east.
    post-condition: Karel at the midpoint facing west.
    """
    one_one_two_two_checker()
    stair_put_beeper()
    find_midpoint()
    stair_clean_beeper()
    return_midpoint()


def stair_put_beeper():
    # """
    # Karel will put the beepers in a stair shape to the diagonal point.
    # """
    """
    pre-condition: Karel is at street one avenue one facing east.
    post-condition: Karel put down the beepers and its at the diagonal point of street 1 avenue 1 facing east.
    """
    while front_is_clear():
        turn_left()
        put_beeper()
        move()
        put_beeper()
        turn_right()
        move()
    put_beeper()


def stair_clean_beeper():
    # """
    # Karel will clean up the beepers besides the beeper at the midpoint at street 1
    # """
    """
    pre-condition: Karel is at the midpoint in street 1 facing south.
    post-condition: Karel is at the diagonal point of street 1 avenue 1 facing east.
    """
    turn_right()
    while front_is_clear():
        move()
    turn_around()
    while front_is_clear():
        turn_left()
        pick_beeper()
        move()
        pick_beeper()
        turn_right()
        move()
    pick_beeper()


def find_midpoint():
    # """
    # Karel will use the same way that it used to put the beepers but not putting down beepers, Karel will be at the
    # midpoint's avenue when it's on a beeper then go down to street one for the midpoint.
    # """
    """
    pre-condition: Karel is at the diagonal point of street one avenue one facing east.
    post-condition: Karel is at the midpoint facing south.
    """
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    while not on_beeper():
        turn_right()
        move()
        if not on_beeper():
            turn_left()
            move()
    if facing_west():
        turn_left()
        while front_is_clear():
            move()
        put_beeper()
    if facing_north():
        turn_around()
        while front_is_clear():
            move()
        put_beeper()


def return_midpoint():
    # """
    # This function is to make Karel go back to the midpoint in street one after cleaning up all the beepers.
    # """
    """
    pre-condition: Karel is at the diagonal point of street 1 avenue 1 facing East.
    post-condition: Karel is back to the midpoint in street 1 facing west.
    """
    turn_right()
    while front_is_clear():
        move()
    turn_right()
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
    # Karel will go back to its previous location.
    # """
    turn_around()
    while front_is_clear():
        move()


def turn_right():
    # """
    # This will make Karel turn left three times.
    # """
    for i in range(3):
        turn_left()


def turn_around():
    # """
    # This will make Karel turn left two times.
    # """
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
