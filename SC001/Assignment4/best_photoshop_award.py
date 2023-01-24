"""
File: best_photoshop_award.py
Name: Mike
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""

from simpleimage import SimpleImage
THRESHOLD = 1.15
BLACK_PIXEL = 120


def main():
    """
    創作理念：看見彗星墜落, 時間不足無法補足撞擊點的效果
    """
    fg = SimpleImage('image_contest/WhatsApp Image 2022-11-17 at 11.17.12 AM.jpeg')
    bg = SimpleImage('image_contest/National-Meteor-Watch-Day.jpeg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


def combine(bg, me):
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
