"""
File: CheckerboardKarel.py
Name: Mike
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    # """
    # This whole function will be fit for any odd or even length square space with an extra code for 8x1 square.
    # Karel will put beepers in the given space with one street or avenue between each other beeper.
    # """
    """
    pre-condition: Karel is at street 1 avenue 1 facing east ready to fill the checkerboard.
    post-condition: Karel filled the checkerboard and stop at either upper right facing East or upper left facing West.
                    depending on the checkerboard that its filling.
    """
    eight_one_checker()
    while front_is_clear():
        odd_street_filling_v1()
        if on_beeper() and left_is_clear():
            odd_turn()
        else:
            even_street_filling_odd()
        odd_street_filling_v2()
        if right_is_clear() and left_is_clear():
            even_turn()
        else:
            pass


def odd_street_filling_v1():
    # """
    # This function is to fill an odd street in any even length space with one avenue between each beeper.
    # """
    """
    Pre-condition: Karel ready to go from left side of the street and fill in the first street with beepers,
                   1 avenue is between each beeper.
    Post-condition: Karel finished filling and will stop at the next street on the right ready to fill.
    """
    while front_is_clear():
        if front_is_clear():
            move()
            put_beeper()
            if front_is_clear():
                move()


def odd_street_filling_v2():
    # """
    # After Karel fill in the first street it will fill in the next street in the even street in even length space.
    # """
    """
    Pre-condition: Karel is at the right side of the even street facing West ready to fill.
    Post-Condition: Karel finished filling and move to the next street on the left facing East ready to fill.
    """
    while front_is_clear():
        if front_is_clear():
            move()
            put_beeper()
            if front_is_clear():
                move()


def turn_right():
    # """
    # This will make Karel turn right.
    # """
    for i in range(3):
        turn_left()


def odd_turn():
    # """
    # This will make Karel take a turn from the odd street to the even street facing the other side.
    # """
    turn_left()
    move()
    turn_left()


def even_turn():
    # """
    # This will make Karel take a turn from the even street to the odd street facing the other side.
    # """
    turn_right()
    move()
    turn_right()


def even_street_filling_odd():
    # """
    # This function will make Karel fill the even street in any odd length space with 1 avenue between each beeper.
    # """
    """
    pre-condition: Karel will be at the right side of the street facing west ready to fill.
    post-condition: Karel finished filling and move to the next street on the left facing East ready to fill.
    """
    if left_is_clear():
        odd_turn()
        put_beeper()
        while front_is_clear():
            move()
            move()
            put_beeper()


def eight_one_checker():
    # """
    # This function will check if the space is Even x1(ex: 8x1) which if the front is not clear Karel will turn left
    # then fill the avenue its at.
    # """
    if not front_is_clear():
        turn_left()
        odd_street_filling_v1()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
