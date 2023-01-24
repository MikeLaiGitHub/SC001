"""
File: mirror_lake.py
Name: Mike
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filepath):
    mirror = SimpleImage(filepath)
    l_img = SimpleImage.blank(mirror.width, mirror.height*2)
    for x in range(mirror.width):
        for y in range(mirror.height):
            img_pixel = mirror.get_pixel(x, y)
            l_img.pixel1 = l_img.get_pixel(x, y)
            l_img.pixel1.red = img_pixel.red
            l_img.pixel1.green = img_pixel.green
            l_img.pixel1.blue = img_pixel.blue
            l_img.pixel2 = l_img.get_pixel(x, l_img.height-1-y)
            l_img.pixel2.red = img_pixel.red
            l_img.pixel2.green = img_pixel.green
            l_img.pixel2.blue = img_pixel.blue
    return l_img


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
