from turtle import right, left, forward, speed, exitonclick, hideturtle
from functools import partial

replacements = 8
angle = 90
size = 5

string = 'f'## string initialisation

for i in range(replacements):
    string = string.replace('f','f+f-f-f+f')
    #   string = string.replace('x','x+yf+')
    #   string = string.replace('y','-fx-y')

#f = string.replace('x','')
#fractal = f.replace('y','')

draw = {'f': partial(forward, size),
        '+': partial(left, angle),
        '-': partial(right, angle),
}
for c in string: draw[c]()

