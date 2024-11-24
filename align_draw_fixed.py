'''
    CS5001
    Spring 2023
    HW2

    Brendan Sheehan

    This program uses python turtle to draw a series of different
    sized squares.
'''

import turtle

# naming turtle

brendan = turtle.Turtle()

def draw_fifty_sq(size):

    '''
    Function: draw_fifty_sq
        Draws a 50x50 pixel square in turtle
    Parameters:
        size of square
    '''

    brendan.forward(50)
    brendan.left(90)
    brendan.forward(50)
    brendan.left(90)
    brendan.forward(50)
    brendan.left(90)
    brendan.forward(50)
    brendan.left(90)
    size = 50


def draw_hundred_sq(size):

    '''
    Function: draw_hundred_sq
        Draws a 100x100 pixel square in turtle
    Parameters:
        size of square
    '''
    brendan.forward(100)
    brendan.left(90)
    brendan.forward(100)
    brendan.left(90)
    brendan.forward(100)
    brendan.left(90)
    brendan.forward(100)
    brendan.left(90)
    size = 100



def draw_twenty_five_sq(size):

    '''
    Function: draw_twenty_five_sq
        Draws a 25x25 pixel square in turtle
    Parameters:
        size of square
    '''

    brendan.forward(25)
    brendan.left(90)
    brendan.forward(25)
    brendan.left(90)
    brendan.forward(25)
    brendan.left(90)
    brendan.forward(25)
    brendan.left(90)
    size = 12

def main():
# set up turtle, screen dimensions, and image
    
    window = turtle.Screen()
    window_size = turtle.screensize(970, 635)
    window.bgpic("shape_window.png")
    window.title("Turtle")

# draw top right border square

    draw_hundred_sq(100)

# move pen & draw top right inner square

    brendan.penup()
    brendan.goto(25,25)
    brendan.pendown()

    draw_fifty_sq(50)

# move pen & draw bottom left border square

    brendan.penup()
    brendan.goto(-100,-100)
    brendan.pendown()

    draw_hundred_sq(100)

# move pen & draw bottom left inner square

    brendan.penup()
    brendan.goto(-75,-75)
    brendan.pendown()

    draw_fifty_sq(50)

# move pen & draw outer left border of middle sq

    brendan.penup()
    brendan.goto(-50,0)
    brendan.pendown()

    draw_fifty_sq(50)

#move pen & draw inner left border of middle sq

    brendan.penup()
    brendan.goto(-25,0)
    brendan.pendown()

    draw_twenty_five_sq(25)

#move pen & draw inner right border of middle sq

    brendan.penup()
    brendan.goto(0,-25)
    brendan.pendown()

    draw_twenty_five_sq(25)

# move pen & draw outer right border of middle sq

    brendan.penup()
    brendan.goto(0,-50)
    brendan.pendown()

    draw_fifty_sq(50)

# return pen to 0,0

    brendan.penup()
    brendan.goto(0,0)
    brendan.pendown()
    brendan.left(90)

    turtle.done()

if __name__ == "__main__":
    main()
