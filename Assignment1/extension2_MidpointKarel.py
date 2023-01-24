"""
File: extension2_MidpointKarel.py
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
    # Karel will check if the space is 1x1 or 2x2, if not Karel will scatter the beeper from street 1 avenue 1 to the
    # rightmost point of the street with 1 avenue between each beeper. Then Karel move all the beeper to the leftmost
    # side starting to fill from the left, if no beeper to pick from the rightmost side, Karel will clean up the
    # beepers, then midpoint will be found after no beepers to pick.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east.
    post-condition: Karel is at the midpoint facing west.
    """
    if not front_is_clear():  # 1*1 checker
        put_beeper()
    else:
        move()
        if not front_is_clear():  # 2*2 checker
            put_beeper()
        else:
            turn_around()  # Normal situation
            move()
            turn_around()
            scatter_beeper()
            if not on_beeper():
                move()
            while on_beeper():
                move_beeper()
            midpoint_located()


def scatter_beeper():
    # """
    # Karel will put beepers in a pattern as one avenue between each beeper from street 1 avenue 1.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east.
    post-condition: Karel is at the rightmost point of street 1 facing west.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_around()


def move_beeper():
    # """
    # Karel will detect the beeper from the right side of the street and move the beepers from the right then start
    # filling from the leftmost side of street 1, Karel will stop if Karel didn't move on any beeper for 2 avenue.
    # This function only work in the even length of the street.
    # """
    """
    pre-condition: Karel will be at the rightmost of street 1 facing west.
    post-condition: Karel will be back at the same point as pre-condition facing west.
    """
    move()
    if on_beeper():
        turn_around()
        while front_is_clear():
            move()
    else:
        turn_around()
        move()
        pick_beeper()
        turn_around()

        # Karel will be picked up the beeper from the right then move to leftmost point of street 1 facing east.
        while front_is_clear():
            move()
        turn_around()

        # Karel move to an empty point then put down the beeper it picked up.
        while on_beeper():
            move()
        put_beeper()

        # Karel will go back to the location before executing this command
        while front_is_clear():
            move()
        turn_around()

        # By doing this Karel will be able to do it again in a while loop.
        while not on_beeper():
            move()


def midpoint_located():
    # """
    # Karel will find the midpoint after picking up all the beepers then return to the midpoint.
    # """
    """
    pre-condition: Karel finish moving the beepers and at the rightmost point of street 1 facing west.
    post-condition: Karel is at the midpoint facing west.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    while on_beeper():
        pick_beeper()
        move()
    turn_around()
    move()
    turn_around()
    put_beeper()


def turn_around():
    # """
    # This will make Karel turn left two times.
    # """
    turn_left()
    turn_left()


def go_back():
    # """
    # This will make Karel go back to its previous location.
    # """
    turn_around()
    while front_is_clear():
        move()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
