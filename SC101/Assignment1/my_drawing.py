"""
File: my_drawing.py
Name: Mike
----------------------
"""
from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
"""
Title: Minecraft Steve
Base on a default skin of a character in a game called Minecraft, consist of 72 rectangles. It's easy on making it
but hard on calculating the coordinate of every rectangle for the right place.
"""


def main():
    window = GWindow(width=600, height=840, title='Minecraft Steve')
    head = GRect(180, 180, x=210, y=5)
    head.filled = True
    head.fill_color = 'peachpuff'
    head.color = 'peachpuff'
    window.add(head)

    hair1 = GRect(180, 45, x=210, y=5)
    hair1.filled = True
    hair1.fill_color = 'black'

    window.add(hair1)

    hair2 = GRect(22.5, 22.5, x=210, y=50)
    hair2.filled = True
    hair2.fill_color = 'black'
    window.add(hair2)

    hair3 = GRect(22.5, 22.5, x=367.5, y=50)
    hair3.filled = True
    hair3.fill_color = 'black'
    window.add(hair3)

    eye1 = GRect(22.5, 22.5, x=232.5, y=95)
    eye1.filled = True
    eye1.fill_color = 'white'
    eye1.color = 'white'
    window.add(eye1)

    eye2 = GRect(22.5, 22.5, x=345, y=95)
    eye2.filled = True
    eye2.fill_color = 'white'
    eye2.color = 'white'
    window.add(eye2)

    eye3 = GRect(22.5, 22.5, x=255, y=95)
    eye3.filled = True
    eye3.fill_color = 'mediumblue'
    eye3.color = 'mediumblue'
    window.add(eye3)

    eye4 = GRect(22.5, 22.5, x=322.5, y=95)
    eye4.filled = True
    eye4.fill_color = 'mediumblue'
    eye4.color = 'mediumblue'
    window.add(eye4)

    nose = GRect(45, 22.5, x=277.5, y=117.5)
    nose.filled = True
    nose.fill_color = 'maroon'
    nose.color = 'maroon'
    window.add(nose)

    mouth1 = GRect(90, 45, x=255, y=140)
    mouth1.filled = True
    mouth1.fill_color = 'saddlebrown'
    mouth1.color = 'saddlebrown'
    window.add(mouth1)

    mouth2 = GRect(45, 22.5, x=277.5, y=140.5)
    mouth2.filled = True
    mouth2.fill_color = 'sienna'
    mouth2.color = 'sienna'
    window.add(mouth2)

    clothe = GRect(180, 225, x=210, y=185)
    clothe.filled = True
    clothe.fill_color = 'turquoise'
    clothe.color = 'turquoise'
    window.add(clothe)

    neck_detail1 = GRect(22.5, 22.5, x=255, y=185)
    neck_detail1.filled = True
    neck_detail1.fill_color = 'peru'
    neck_detail1.color = 'peru'
    window.add(neck_detail1)

    neck_detail2 = GRect(45, 22.5, x=300, y=185)
    neck_detail2.filled = True
    neck_detail2.fill_color = 'peru'
    neck_detail2.color = 'peru'
    window.add(neck_detail2)

    neck_detail3 = GRect(45, 22.5, x=277.5, y=207.5)
    neck_detail3.filled = True
    neck_detail3.fill_color = 'peru'
    neck_detail3.color = 'peru'
    window.add(neck_detail3)

    neck_detail4 = GRect(22.5, 22.5, x=277.5, y=185)
    neck_detail4.filled = True
    neck_detail4.fill_color = 'burlywood'
    neck_detail4.color = 'burlywood'
    window.add(neck_detail4)

    arm1 = GRect(90, 270, x=120, y=185)
    arm1.filled = True
    arm1.fill_color = 'turquoise'
    arm1.color = 'turquoise'
    window.add(arm1)

    arm1_skin = GRect(90, 180, x=120, y=275)
    arm1_skin.filled = True
    arm1_skin.fill_color = 'burlywood'
    arm1_skin.color = 'burlywood'
    window.add(arm1_skin)

    arm1_detail1 = GRect(22.5, 45, x=142.5, y=297.5)
    arm1_detail1.filled = True
    arm1_detail1.fill_color = 'tan'
    arm1_detail1.color = 'tan'
    window.add(arm1_detail1)

    arm1_detail2 = GRect(22.5, 22.5, x=121, y=431.5)
    arm1_detail2.filled = True
    arm1_detail2.fill_color = 'tan'
    arm1_detail2.color = 'tan'
    window.add(arm1_detail2)

    arm1_detail3 = GRect(22.5, 67.5, x=186.5, y=320)
    arm1_detail3.filled = True
    arm1_detail3.fill_color = 'tan'
    arm1_detail3.color = 'tan'
    window.add(arm1_detail3)

    arm1_detail4 = GRect(22.5, 45, x=164, y=409)
    arm1_detail4.filled = True
    arm1_detail4.fill_color = 'tan'
    arm1_detail4.color = 'tan'
    window.add(arm1_detail4)

    arm1_detail5 = GRect(22.5, 22.5, x=186.5, y=431.5)
    arm1_detail5.filled = True
    arm1_detail5.fill_color = 'tan'
    arm1_detail5.color = 'tan'
    window.add(arm1_detail5)

    arm2 = GRect(90, 270, x=390, y=185)
    arm2.filled = True
    arm2.fill_color = 'turquoise'
    arm2.color = 'turquoise'
    window.add(arm2)

    arm2_skin = GRect(90, 180, x=390, y=275)
    arm2_skin.filled = True
    arm2_skin.fill_color = 'burlywood'
    arm2_skin.color = 'burlywood'
    window.add(arm2_skin)

    arm2_detail1 = GRect(22.5, 22.5, x=391, y=431.5)
    arm2_detail1.filled = True
    arm2_detail1.fill_color = 'tan'
    arm2_detail1.color = 'tan'
    window.add(arm2_detail1)

    arm2_detail2 = GRect(22.5, 45, x=412.5, y=409)
    arm2_detail2.filled = True
    arm2_detail2.fill_color = 'tan'
    arm2_detail2.color = 'tan'
    window.add(arm2_detail2)

    arm2_detail3 = GRect(22.5, 22.5, x=456.5, y=431.5)
    arm2_detail3.filled = True
    arm2_detail3.fill_color = 'tan'
    arm2_detail3.color = 'tan'
    window.add(arm2_detail3)

    arm2_detail4 = GRect(22.5, 67.5, x=391, y=320)
    arm2_detail4.filled = True
    arm2_detail4.fill_color = 'tan'
    arm2_detail4.color = 'tan'
    window.add(arm2_detail4)

    arm2_detail5 = GRect(22.5, 45, x=435, y=297.5)
    arm2_detail5.filled = True
    arm2_detail5.fill_color = 'tan'
    arm2_detail5.color = 'tan'
    window.add(arm2_detail5)

    clothe_detail8 = GRect(22.5, 22.5, x=390.5, y=251.5)
    clothe_detail8.filled = True
    clothe_detail8.fill_color = 'lightseagreen'
    clothe_detail8.color = 'lightseagreen'
    window.add(clothe_detail8)

    clothe_detail9 = GRect(22.5, 22.5, x=456.5, y=251.5)
    clothe_detail9.filled = True
    clothe_detail9.fill_color = 'lightseagreen'
    clothe_detail9.color = 'lightseagreen'
    window.add(clothe_detail9)

    clothe_detail10 = GRect(22.5, 22.5, x=456.5, y=185.5)
    clothe_detail10.filled = True
    clothe_detail10.fill_color = 'lightseagreen'
    clothe_detail10.color = 'lightseagreen'
    window.add(clothe_detail10)

    clothe_detail11 = GRect(22.5, 22.5, x=390.5, y=208)
    clothe_detail11.filled = True
    clothe_detail11.fill_color = 'lightseagreen'
    clothe_detail11.color = 'lightseagreen'
    window.add(clothe_detail11)

    clothe_detail12 = GRect(22.5, 22.5, x=120, y=185)
    clothe_detail12.filled = True
    clothe_detail12.fill_color = 'lightseagreen'
    clothe_detail12.color = 'lightseagreen'
    window.add(clothe_detail12)

    clothe_detail13 = GRect(22.5, 22.5, x=120, y=252.5)
    clothe_detail13.filled = True
    clothe_detail13.fill_color = 'lightseagreen'
    clothe_detail13.color = 'lightseagreen'
    window.add(clothe_detail13)

    clothe_detail14 = GRect(22.5, 22.5, x=187.5, y=252.5)
    clothe_detail14.filled = True
    clothe_detail14.fill_color = 'lightseagreen'
    clothe_detail14.color = 'lightseagreen'
    window.add(clothe_detail14)

    clothe_detail15 = GRect(22.5, 22.5, x=187.5, y=207.5)
    clothe_detail15.filled = True
    clothe_detail15.fill_color = 'lightseagreen'
    clothe_detail15.color = 'lightseagreen'
    window.add(clothe_detail15)

    clothe_detail16 = GRect(22.5, 22.5, x=120, y=230)
    clothe_detail16.filled = True
    clothe_detail16.fill_color = 'mediumturquoise'
    clothe_detail16.color = 'mediumturquoise'
    window.add(clothe_detail16)

    clothe_detail17 = GRect(22.5, 45, x=142.5, y=185)
    clothe_detail17.filled = True
    clothe_detail17.fill_color = 'mediumturquoise'
    clothe_detail17.color = 'mediumturquoise'
    window.add(clothe_detail17)

    clothe_detail18 = GRect(22.5, 22.5, x=187.5, y=185)
    clothe_detail18.filled = True
    clothe_detail18.fill_color = 'mediumturquoise'
    clothe_detail18.color = 'mediumturquoise'
    window.add(clothe_detail18)

    clothe_detail19 = GRect(22.5, 22.5, x=390, y=185)
    clothe_detail19.filled = True
    clothe_detail19.fill_color = 'mediumturquoise'
    clothe_detail19.color = 'mediumturquoise'
    window.add(clothe_detail19)

    clothe_detail20 = GRect(22.5, 45, x=435.5, y=185)
    clothe_detail20.filled = True
    clothe_detail20.fill_color = 'mediumturquoise'
    clothe_detail20.color = 'mediumturquoise'
    window.add(clothe_detail20)

    clothe_detail21 = GRect(22.5, 22.5, x=457.5, y=230)
    clothe_detail21.filled = True
    clothe_detail21.fill_color = 'mediumturquoise'
    clothe_detail21.color = 'mediumturquoise'
    window.add(clothe_detail21)

    clothe_detail22 = GRect(22.5, 22.5, x=277.5, y=387.5)
    clothe_detail22.filled = True
    clothe_detail22.fill_color = 'mediumturquoise'
    clothe_detail22.color = 'mediumturquoise'
    window.add(clothe_detail22)

    clothe_detail23 = GRect(22.5, 67.5, x=300, y=320)
    clothe_detail23.filled = True
    clothe_detail23.fill_color = 'mediumturquoise'
    clothe_detail23.color = 'mediumturquoise'
    window.add(clothe_detail23)

    clothe_detail24 = GRect(22.5, 22.5, x=322.5, y=387.5)
    clothe_detail24.filled = True
    clothe_detail24.fill_color = 'mediumturquoise'
    clothe_detail24.color = 'mediumturquoise'
    window.add(clothe_detail24)

    clothe_detail25 = GRect(22.5, 22.5, x=277.5, y=297.5)
    clothe_detail25.filled = True
    clothe_detail25.fill_color = 'mediumturquoise'
    clothe_detail25.color = 'mediumturquoise'
    window.add(clothe_detail25)

    clothe_detail26 = GRect(22.5, 22.5, x=210, y=185)
    clothe_detail26.filled = True
    clothe_detail26.fill_color = 'lightseagreen'
    clothe_detail26.color = 'lightseagreen'
    window.add(clothe_detail26)

    clothe_detail27 = GRect(22.5, 22.5, x=210, y=207.5)
    clothe_detail27.filled = True
    clothe_detail27.fill_color = 'mediumturquoise'
    clothe_detail27.color = 'mediumturquoise'
    window.add(clothe_detail27)

    clothe_detail28 = GRect(22.5, 45, x=232.5, y=185)
    clothe_detail28.filled = True
    clothe_detail28.fill_color = 'mediumturquoise'
    clothe_detail28.color = 'mediumturquoise'
    window.add(clothe_detail28)

    clothe_detail29 = GRect(45, 22.5, x=345, y=185)
    clothe_detail29.filled = True
    clothe_detail29.fill_color = 'lightseagreen'
    clothe_detail29.color = 'lightseagreen'
    window.add(clothe_detail29)

    clothe_detail30 = GRect(22.5, 22.5, x=255, y=207.5)
    clothe_detail30.filled = True
    clothe_detail30.fill_color = 'lightseagreen'
    clothe_detail30.color = 'lightseagreen'
    window.add(clothe_detail30)

    clothe_detail31 = GRect(22.5, 22.5, x=255, y=230)
    clothe_detail31.filled = True
    clothe_detail31.fill_color = 'mediumturquoise'
    clothe_detail31.color = 'mediumturquoise'
    window.add(clothe_detail31)

    clothe_detail32 = GRect(22.5, 45, x=277.5, y=230)
    clothe_detail32.filled = True
    clothe_detail32.fill_color = 'mediumturquoise'
    clothe_detail32.color = 'mediumturquoise'
    window.add(clothe_detail32)

    clothe_detail33 = GRect(22.5, 22.5, x=322.5, y=207.5)
    clothe_detail33.filled = True
    clothe_detail33.fill_color = 'lightseagreen'
    clothe_detail33.color = 'lightseagreen'
    window.add(clothe_detail33)

    clothe_detail34 = GRect(22.5, 22.5, x=322.5, y=230)
    clothe_detail34.filled = True
    clothe_detail34.fill_color = 'mediumturquoise'
    clothe_detail34.color = 'mediumturquoise'
    window.add(clothe_detail34)

    pants = GRect(180, 360, x=210, y=410)
    pants.filled = True
    pants.fill_color = 'darkblue'
    pants.color = 'darkblue'
    window.add(pants)

    clothe_detail1 = GRect(22.5, 180, x=367.5, y=275)
    clothe_detail1.filled = True
    clothe_detail1.fill_color = 'lightseagreen'
    clothe_detail1.color = 'lightseagreen'
    window.add(clothe_detail1)

    clothe_detail2 = GRect(22.5, 22.5, x=345, y=275)
    clothe_detail2.filled = True
    clothe_detail2.fill_color = 'lightseagreen'
    clothe_detail2.color = 'lightseagreen'
    window.add(clothe_detail2)

    clothe_detail3 = GRect(67.5, 22.5, x=210.5, y=386.5)
    clothe_detail3.filled = True
    clothe_detail3.fill_color = 'lightseagreen'
    clothe_detail3.color = 'lightseagreen'
    window.add(clothe_detail3)

    clothe_detail4 = GRect(22.5, 67.5, x=277.5, y=319)
    clothe_detail4.filled = True
    clothe_detail4.fill_color = 'lightseagreen'
    clothe_detail4.color = 'lightseagreen'
    window.add(clothe_detail4)

    clothe_detail6 = GRect(22.5, 90, x=210.5, y=275)
    clothe_detail6.filled = True
    clothe_detail6.fill_color = 'lightseagreen'
    clothe_detail6.color = 'lightseagreen'
    window.add(clothe_detail6)

    clothe_detail7 = GRect(22.5, 89.5, x=300, y=230.5)
    clothe_detail7.filled = True
    clothe_detail7.fill_color = 'lightseagreen'
    clothe_detail7.color = 'lightseagreen'
    window.add(clothe_detail7)

    clothe_detail8 = GRect(22.5, 45, x=234, y=275)
    clothe_detail8.filled = True
    clothe_detail8.fill_color = 'lightseagreen'
    clothe_detail8.color = 'lightseagreen'
    window.add(clothe_detail8)

    pants_detail1 = GRect(45, 22.5, x=232.5, y=635)
    pants_detail1.filled = True
    pants_detail1.fill_color = 'midnightblue'
    pants_detail1.color = 'midnightblue'
    window.add(pants_detail1)

    pants_detail2 = GRect(45, 22.5, x=322.5, y=635)
    pants_detail2.filled = True
    pants_detail2.fill_color = 'midnightblue'
    pants_detail2.color = 'midnightblue'
    window.add(pants_detail2)

    pants_detail3 = GRect(22.5, 22.5, x=322, y=411)
    pants_detail3.filled = True
    pants_detail3.fill_color = 'midnightblue'
    pants_detail3.color = 'midnightblue'
    window.add(pants_detail3)

    pants_detail4 = GRect(22.5, 22.5, x=344.5, y=432.5)
    pants_detail4.filled = True
    pants_detail4.fill_color = 'midnightblue'
    pants_detail4.color = 'midnightblue'
    window.add(pants_detail4)

    clothe_detail5 = GRect(22.5, 22.5, x=345.5, y=410)
    clothe_detail5.filled = True
    clothe_detail5.fill_color = 'lightseagreen'
    clothe_detail5.color = 'lightseagreen'
    window.add(clothe_detail5)

    feet = GRect(180, 45, x=210, y=770)
    feet.filled = True
    feet.fill_color = 'gray'
    feet.color = 'gray'
    window.add(feet)


if __name__ == '__main__':
    main()
