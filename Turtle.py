# Author: Weijia Fang
# Title: Turtle
# Completion Date: Apr 2019

# Import turtle as the letter t to make it easier to use.
import turtle as t
import random
# Create Screen named wn and Turtle named Leo.
wn = t.Screen()
leo = t.Turtle()
# Close the animation of canvas in order to make polygon faster.
wn.tracer(0)


# This function is used to output a random color for the line(pen of turtle).
def line_color():
    colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
              'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']
    index = random.randrange(0, 12)
    random_line_color = colors[index]
    return random_line_color


# This function is used to output a random color to fill the polygon.
def inside_color():
    colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
              'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']
    index = random.randrange(0, 12)
    random_inside_color = colors[index]
    return random_inside_color


# The length function which is 600 pixel in total.
def length_function(sides):
    long = 600/sides
    return long


# The width of the pen is limited in [1,20].
def width_function(sides):
    wide = (sides % 20) + 1
    return wide


# This part is to make the polygon with all the requirement.
def make_polygon(t, sides, length, border_color, width, fill_color):
    t.clear()
    t.setheading(0)
    angle = 360/sides
    t.pensize(width)
    t.color(border_color, fill_color)
    t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.right(angle)
    t.end_fill()


print('This program will draw a polygon with 3 or more sides.')
# Make the user input the sides number of polygon.
input_sides = int(input('Enter the number of sides, less than 3 to exit:'))
# The loop with process while the sides number is >=3 which is the lowest requirement to form a polygon.
while input_sides >= 3:
    line_color()
    inside_color()
    length_function(input_sides)
    make_polygon(t, input_sides, length_function(input_sides), line_color(), width_function(input_sides),
                 inside_color())
    # Make sure canvas show the latest turtle
    wn.update()
    input_sides = int(input('Enter the number of sides, less than 3 to exit:'))
# Close turtle, other wise the computer will regard the turtle a not responding progress.
t.done()
