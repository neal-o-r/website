from turtle import right, left, forward, speed, exitonclick, hideturtle

 
def dragon(level=4, size=200, direction=45):
# A script that draws the dragon fractal, using python's turtle graphics module.

    if level:

        right(direction) 

        dragon(level-1, size/1.41421356237, 45)

        left(direction * 2)

        dragon(level-1, size/1.41421356237, -45)

        right(direction)

    else:

        forward(size)
 
speed(0)
hideturtle()

dragon(10)
exitonclick() # click to exit
