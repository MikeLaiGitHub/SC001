"""
File: bouncing_ball.py
Name: Mike
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
end = 0
m = 0

window = GWindow(800, 500, title='bouncing_ball.py')
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncy)


def bouncy(_):
    global GRAVITY, end, m
    if m == 0:
        n = 1
        t = 1
        k = 0
        oval = GOval(SIZE, SIZE, x=START_X, y=START_Y)
        window.add(oval)
        while k != 3 and end == 0:
            while oval.y + oval.height <= window.height:
                pause(DELAY)
                oval.move(VX, GRAVITY*n)
                n += 1
            bounce_up = -GRAVITY*n
            while bounce_up < -1:
                pause(DELAY)
                oval.move(VX, bounce_up)
                n -= 1
                bounce_up = bounce_up*(REDUCE**t)
            t += 0.15
            n = 1
            if oval.x > window.width:
                k += 1
                if k == 3:
                    end += 1
        oval = GOval(SIZE, SIZE, x=START_X, y=START_Y)
        window.add(oval)
        m += 1


if __name__ == "__main__":
    main()
