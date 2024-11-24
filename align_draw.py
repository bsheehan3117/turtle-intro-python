'''
    CS5001
    Spring 2023
    HW2

    Brendan Sheehan

    This program uses python turtle to draw a series of different
    sized squares.
'''

import turtle

brendan = turtle.Turtle()

def draw_square(x, y, length_of_side):

    '''
    Function: draw_square
    Lifts the turtle pen, moves to coordinates, puts the pen down,
    and draws a square of chosen size based on side length.
    Parameters:
    x coordinate, y coordinate, length of side of square.
    '''
    
    brendan.penup()
    brendan.goto(x, y)
    brendan.pendown()
    brendan.forward(length_of_side)
    brendan.left(90)
    brendan.forward(length_of_side)
    brendan.left(90)
    brendan.forward(length_of_side)
    brendan.left(90)
    brendan.forward(length_of_side)
    brendan.left(90)

def main():
    
# set up turtle, screen dimensions, and image
    
    window = turtle.Screen()
    window_size = turtle.screensize(970, 635)
    window.bgpic("shape_window.png")
    window.title("Turtle")

    t.color(red, green)

# draw squares at various coordinates of various sizes

    draw_square(0, 0, 100)
    draw_square(25, 25, 50)
    draw_square(-100, -100, 100)
    draw_square(-75, -75, 50)
    draw_square(-50, 0, 50)
    draw_square(0, -25, 25)
    draw_square(-25, 0, 25)
    draw_square(0, -50, 50)

    turtle.done()

if __name__ == "__main__":
    main()
