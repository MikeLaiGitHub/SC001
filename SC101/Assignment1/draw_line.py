"""
File: draw_line.py
Name: Mike
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 10
n = 1
x = 0
y = 0
window = GWindow()


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_hole)


def create_hole(haha):
    global n, x, y
    if n == 1:
        hole = GOval(SIZE, SIZE, x=haha.x-SIZE/2, y=haha.y-SIZE/2)
        window.add(hole)
        x = haha.x
        y = haha.y
        n -= 1
    else:
        obj = window.get_object_at(x, y)
        window.remove(obj)
        line = GLine(x, y, haha.x, haha.y)
        window.add(line, x, y)
        x = 0
        y = 0
        n += 1




# def remove(circle):
#     obj = window.get_object_at(circle.x, circle.y)
#     if obj is not None:
#         window.remove(obj)


if __name__ == "__main__":
    main()
