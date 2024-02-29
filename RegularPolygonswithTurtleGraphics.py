# Author: Weijia Fang
# Title: Regular Polygons with Turtle Graphics
# Completion Date: Apr 2019

from turtle import *
import random

#A function to determine length
def length_polygon(sides):
    length = 600/sides
    return length

#A function to determine the pen width
def width_pen(sides):
    border_width = sides%20 + 1
    return border_width

#A function to determine the color of line
def border_color():
    colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
              'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']
    index = random.randrange(0,12)
    bordercolor = colors[index]
    return bordercolor

#A function to determine the color of fill
def fill_color():
    colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
              'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']
    index = random.randrange(0,12)
    fillcolor = colors[index]
    return fillcolor

#A function to make polygon
def make_polygon(sides, length, bordercolor, widthPen, filledcolor):
	color(bordercolor, filledcolor)
	clear()
	pensize(widthPen)
	angle = 360/sides
	begin_fill()

	for i in range(sides):
		forward(length)
		left(angle)
	
	end_fill()
    
#Main function
print("This program will draw a polygon with 3 or more sides.")
sides = int(input("Enter the number of sides, less than 3 to exit: "))
            
#A While loop that allow the user to draw as many polygons as desired
while sides >= 3:
	length = length_polygon(sides)
	bordercolor = border_color()
	filledcolor = fill_color()
	width = width_pen(sides)
	make_polygon(sides, length, bordercolor, width, filledcolor)
	sides = int(input("Enter the numer of sides, less than 3 to exit: "))
