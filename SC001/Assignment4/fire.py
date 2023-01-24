"""
File: fire.py
Name: Mike
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def main():
    """
    TODO:
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


def highlight_fires(filepath):
    red_highlight = SimpleImage(filepath)
    for pixel in red_highlight:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return red_highlight


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
