from turtle import *
import random
import math

bgcolor("black")

colors = [
    '#ff6666',
    '#ff8c66',	
    '#ffb366',	
    '#ffd966',	
    '#ffff66',	
    '#d9ff66',	
    '#b3ff66',	
    '#8cff66',	
    '#66ff66',	
    '#66ff8c',	
    '#66ffb3',	
    '#66ffd9',	
    '#66ffff',	
    '#66d9ff',	
    '#66b3ff',	
    '#6699ff',	
    '#668cff',	
    '#6666ff',	
    '#8c66ff',	
    '#b366ff',	
    '#d966ff',	
    '#ff66ff',	
    '#ff66d9',	
    '#ff66b3',	
    '#ff668c',
]

speed(0)

def f(length, depth): #the fractal function, stolen from http://www.algorithm.co.il/blogs/computer-science/fractals-in-10-minutes-no-6-turtle-snowflake/
        width(3)
        if depth == 0:
            forward(length)
        else:
            f(length/3, depth-1)
            right(60)
            f(length/3, depth-1)
            left(120)
            f(length/3, depth-1)
            right(60)
            f(length/3, depth-1)

def more(): #making it repeat the fractal line, rotated by 15 deg and in the next color in the list
    right(15)
    pencolor(x) 
    f(300, 4)
    up()
    goto(0,0)
    down()     

for x in colors:
    more()

input()