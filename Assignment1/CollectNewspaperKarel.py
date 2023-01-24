"""
File: CollectNewspaperKarel.py
Name: Mike
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    # """
    # Karel will go out of his home and take the newspaper then go back to his home.
    # """
    """
    pre-condition: Karel is at home facing East at street 4 avenue 3.
    post-condition: Karel took the newspaper got back to the same position as pre-condition in home facing East.
    """
    go_take_newspaper()
    go_home()


def turn_around():
    # """
    # this function turn Karel to the left two times.
    # """
    turn_left()
    turn_left()


def turn_right():
    # """
    # This function will make Karel turn left 3 times.
    # """
    for i in range(3):
        turn_left()


def go_take_newspaper():
    # """
    # Karel will go out of home and take newspaper.
    # """
    """
    pre-condition: Karel is at home at street 4 avenue 3.
    post-condition: Karel go out of its home and got the newspaper. Facing East at street 3 avenue 6.
    """
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_right()
        move()
        turn_left()
        move()
    if on_beeper():
        pick_beeper()


def go_home():
    # """
    # Karel got the newspaper and will go back to home.
    # """
    """
    pre-condition: Karel have the newspaper facing East at street 4 avenue 6.
    post-condition: Karel go back to home with the newspaper facing East at street 4 avenue 3.
    """
    turn_around()
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_right()
        move()
        turn_right()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
