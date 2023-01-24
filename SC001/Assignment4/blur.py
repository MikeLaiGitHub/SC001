"""
File: blur.py
Name: Mike
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = new_img.get_pixel(x, y)
            # Todo: get pixel of new_img at x,y
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:          # Get pixel at the top-left corner of the image.
                img_pixel2 = img.get_pixel(x+1, y)
                img_pixel6 = img.get_pixel(x, y+1)
                img_pixel7 = img.get_pixel(x+1, y+1)
                times = 4
                img_pixel.red = (img_pixel.red + img_pixel2.red + img_pixel6.red + img_pixel7.red)/times
                img_pixel.blue = (img_pixel.blue + img_pixel2.blue + img_pixel6.blue + img_pixel7.blue)/times
                img_pixel.green = (img_pixel.green + img_pixel2.green + img_pixel6.green + img_pixel7.green)/times
            elif x == img.width-1 and y == 0:        # Get pixel at the top-right corner of the image.
                img_pixel4 = img.get_pixel(x-1, y)
                img_pixel9 = img.get_pixel(x-1, y+1)
                img_pixel10 = img.get_pixel(x, y+1)
                times = 4
                img_pixel.red = (img_pixel.red + img_pixel4.red + img_pixel9.red + img_pixel10.red)/times
                img_pixel.blue = (img_pixel.blue + img_pixel4.blue + img_pixel9.blue + img_pixel10.blue)/times
                img_pixel.green = (img_pixel.green + img_pixel4.green + img_pixel9.green + img_pixel10.green)/times
            elif x == 0 and y == img.height-1:        # Get pixel at the bottom-left corner of the image
                img_pixel11 = img.get_pixel(x, y-1)
                img_pixel12 = img.get_pixel(x+1, y-1)
                img_pixel17 = img.get_pixel(x+1, y)
                times = 4
                img_pixel.red = (img_pixel.red + img_pixel11.red + img_pixel12.red + img_pixel17.red)/times
                img_pixel.blue = (img_pixel.blue + img_pixel11.blue + img_pixel12.blue + img_pixel17.blue)/times
                img_pixel.green = (img_pixel.green + img_pixel11.green + img_pixel12.green + img_pixel17.green)/times
            elif x == img.width-1 and y == img.height-1:        # Get pixel at the bottom-right corner of the image
                img_pixel14 = img.get_pixel(x, y-1)
                img_pixel15 = img.get_pixel(x-1, y-1)
                img_pixel19 = img.get_pixel(x-1, y)
                times = 4
                img_pixel.red = (img_pixel.red + img_pixel14.red + img_pixel15.red + img_pixel19.red)/times
                img_pixel.blue = (img_pixel.blue + img_pixel14.blue + img_pixel15.blue + img_pixel19.blue)/times
                img_pixel.green = (img_pixel.green + img_pixel14.green + img_pixel15.green + img_pixel19.green)/times
            elif img.width-1 > x > 0 and y == 0:     # Get top edge's pixels (without two corners)
                img_pixel_t1 = img.get_pixel(x-1, y)
                img_pixel_t2 = img.get_pixel(x+1, y)
                img_pixel_t3 = img.get_pixel(x-1, y+1)
                img_pixel_t4 = img.get_pixel(x, y+1)
                img_pixel_t5 = img.get_pixel(x+1, y+1)
                times = 6
                img_pixel.red = (img_pixel.red + img_pixel_t1.red + img_pixel_t2.red + img_pixel_t3.red +
                                 img_pixel_t4.red + img_pixel_t5.red)/times
                img_pixel.blue = (img_pixel.blue + img_pixel_t1.blue + img_pixel_t2.blue + img_pixel_t3.blue +
                                  img_pixel_t4.blue + img_pixel_t5.blue)/times
                img_pixel.green = (img_pixel.green + img_pixel_t1.green + img_pixel_t2.green + img_pixel_t3.green +
                                   img_pixel_t4.green + img_pixel_t5.green)/times
            elif img.width-1 > x > 0 and y == img.height:     # Get bottom edge's pixels (without two corners)
                img_pixel_b1 = img.get_pixel(x-1, y)
                img_pixel_b2 = img.get_pixel(x+1, y)
                img_pixel_b3 = img.get_pixel(x-1, y-1)
                img_pixel_b4 = img.get_pixel(x, y-1)
                img_pixel_b5 = img.get_pixel(x+1, y-1)
                times = 6
                img_pixel.red = (img_pixel.red + img_pixel_b1.red + img_pixel_b2.red + img_pixel_b3.red +
                                 img_pixel_b4.red + img_pixel_b5.red)/times
                img_pixel.blue = (img_pixel.blue + img_pixel_b1.blue + img_pixel_b2.blue + img_pixel_b3.blue +
                                  img_pixel_b4.blue + img_pixel_b5.blue)/times
                img_pixel.green = (img_pixel.green + img_pixel_b1.green + img_pixel_b2.green + img_pixel_b3.green +
                                   img_pixel_b4.green + img_pixel_b5.green)/times
            elif x == 0 and 0 < y < img.height-1:     # Get left edge's pixels (without two corners)
                img_pixel_l1 = img.get_pixel(x, y-1)
                img_pixel_l2 = img.get_pixel(x+1, y-1)
                img_pixel_l3 = img.get_pixel(x+1, y)
                img_pixel_l4 = img.get_pixel(x+1, y+1)
                img_pixel_l5 = img.get_pixel(x, y+1)
                times = 6
                img_pixel.red = (img_pixel.red + img_pixel_l1.red + img_pixel_l2.red + img_pixel_l3.red +
                                 img_pixel_l4.red + img_pixel_l5.red)/times
                img_pixel.blue = (img_pixel.blue + img_pixel_l1.blue + img_pixel_l2.blue + img_pixel_l3.blue +
                                  img_pixel_l4.blue + img_pixel_l5.blue)/times
                img_pixel.green = (img_pixel.green + img_pixel_l1.green + img_pixel_l2.green + img_pixel_l3.green +
                                   img_pixel_l4.green + img_pixel_l5.green)/times
            elif x == img.width-1 and 0 < y < img.height-1:     # Get right edge's pixels (without two corners)
                img_pixel_r1 = img.get_pixel(x, y-1)
                img_pixel_r2 = img.get_pixel(x-1, y-1)
                img_pixel_r3 = img.get_pixel(x-1, y)
                img_pixel_r4 = img.get_pixel(x-1, y+1)
                img_pixel_r5 = img.get_pixel(x, y+1)
                times = 6
                img_pixel.red = (img_pixel.red+img_pixel_r1.red+img_pixel_r2.red+img_pixel_r3.red + img_pixel_r4.red +
                                 img_pixel_r5.red)/times
                img_pixel.blue = (img_pixel.blue + img_pixel_r1.blue + img_pixel_r2.blue+img_pixel_r3.blue +
                                  img_pixel_r4.blue + img_pixel_r5.blue)/times
                img_pixel.green = (img_pixel.green + img_pixel_r1.green + img_pixel_r2.green + img_pixel_r3.green +
                                   img_pixel_r4.green + img_pixel_r5.green)/times
            else:       # Inner pixels.
                if 0 < x < img.width-1 and 0 < y < img.height-1:
                    img_pixel_m1 = img.get_pixel(x-1, y)
                    img_pixel_m2 = img.get_pixel(x+1, y)
                    img_pixel_m3 = img.get_pixel(x-1, y-1)
                    img_pixel_m4 = img.get_pixel(x, y-1)
                    img_pixel_m5 = img.get_pixel(x+1, y-1)
                    img_pixel_m6 = img.get_pixel(x-1, y+1)
                    img_pixel_m7 = img.get_pixel(x, y+1)
                    img_pixel_m8 = img.get_pixel(x+1, y+1)
                    times = 9
                    img_pixel.red = (img_pixel.red+img_pixel_m1.red+img_pixel_m2.red+img_pixel_m3.red+img_pixel_m4.red
                                     + img_pixel_m5.red + img_pixel_m6.red + img_pixel_m7.red + img_pixel_m8.red)/times
                    img_pixel.blue = (img_pixel.blue+img_pixel_m1.blue+img_pixel_m2.blue+img_pixel_m3.blue +
                                      img_pixel_m4.blue+img_pixel_m5.blue+img_pixel_m6.blue+img_pixel_m7.blue +
                                      img_pixel_m8.blue)/times
                    img_pixel.green = (img_pixel.green+img_pixel_m1.green+img_pixel_m2.green+img_pixel_m3.green +
                                       img_pixel_m4.green+img_pixel_m5.green+img_pixel_m6.green+img_pixel_m7.green +
                                       img_pixel_m8.green)/times
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(20):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
