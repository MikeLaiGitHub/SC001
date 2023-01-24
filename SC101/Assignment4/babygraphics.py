"""
File: babygraphics.py
Name: Mike
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    new_width = width-GRAPH_MARGIN_SIZE*2
    x_coordinate = int(new_width/len(YEARS))*int(year_index)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    canvas.create_text(GRAPH_MARGIN_SIZE+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[0], anchor=tkinter.NW)
    remain_width = CANVAS_WIDTH-GRAPH_MARGIN_SIZE*2
    count = 1
    n = 1
    while count <= len(YEARS)-1:
        canvas.create_line(GRAPH_MARGIN_SIZE+remain_width/len(YEARS)*count, 0,
                           GRAPH_MARGIN_SIZE+remain_width/len(YEARS)*count, CANVAS_HEIGHT)
        canvas.create_text(GRAPH_MARGIN_SIZE+remain_width/len(YEARS)*count+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[n], anchor=tkinter.NW)
        n += 1
        count += 1


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    next_color = 0  # Determine the color for the name to use.
    for name in lookup_names:
        is_first = 0      # Determine the first data for the graphic.
        color = COLORS[next_color % len(COLORS)]
        if name in name_data:
            for i in range(len(YEARS)):
                # If the first data has a rank, calculate the y coordinate.
                if str(YEARS[i]) in name_data[name]:
                    canvas.create_text(GRAPH_MARGIN_SIZE+get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX,
                                       get_y_coordinate(CANVAS_HEIGHT, int(name_data[name][str(YEARS[i])])),
                                       text=name+name_data[name][str(YEARS[i])], anchor=tkinter.SW,
                                       font='times 10', fill=color)
                    is_first += 1

                # If the first data doesn't have a rank, its y will be the same as CANVAS_HEIGHT-GRAPH_MARGIN_SIZE.
                elif str(YEARS[i]) not in name_data[name]:
                    store_rank = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    canvas.create_text(GRAPH_MARGIN_SIZE+TEXT_DX+get_x_coordinate(CANVAS_WIDTH, i), store_rank,
                                       text=name + '*', anchor=tkinter.SW, font='times 10', fill=color)
                    is_first += 1

                # Create the line by constantly updating the two points to connect each other.
                if str(YEARS[i]) not in name_data[name] and i+1 <= len(YEARS)-1:
                    if str(YEARS[i+1]) in name_data[name]:
                        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i),
                                           CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i + 1),
                                           get_y_coordinate(CANVAS_HEIGHT, name_data[name][str(YEARS[i+1])]),
                                           fill=color)
                    if str(YEARS[i+1]) not in name_data[name]:
                        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i + 1),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, fill=color)
                elif str(YEARS[i]) in name_data[name] and i+1 <= len(YEARS)-1:
                    if str(YEARS[i + 1]) in name_data[name]:
                        canvas.create_line(GRAPH_MARGIN_SIZE+get_x_coordinate(CANVAS_WIDTH, i),
                                           get_y_coordinate(CANVAS_HEIGHT, name_data[name][str(YEARS[i])]),
                                           GRAPH_MARGIN_SIZE+get_x_coordinate(CANVAS_WIDTH, i+1),
                                           get_y_coordinate(CANVAS_HEIGHT, name_data[name][str(YEARS[i+1])]),
                                           fill=color)
                    if str(YEARS[i + 1]) not in name_data[name]:
                        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i),
                                           name_data[name][str(YEARS[i])],
                                           GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i + 1),
                                           CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, fill=color)
        next_color += 1


def get_y_coordinate(height, rank):
    new_height = height-GRAPH_MARGIN_SIZE*2
    y_coordinate = GRAPH_MARGIN_SIZE+new_height*int(rank)//1000
    return y_coordinate


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)
    # new_width = CANVAS_WIDTH - GRAPH_MARGIN_SIZE * 2
    # count = 0
    # while count <= len(YEARS):
    #     canvas.create_text(GRAPH_MARGIN_SIZE + new_width / 12 * count, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                        text='YEARS[count]', anchor=tkinter.NW, font='times 5')
    #     count += 1

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
