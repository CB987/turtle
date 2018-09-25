from turtle import *
import random
import math

# # def square(size):
# #     forward(size) #call fxn inside fxn
# #     right(90)
# #     forward(size)
# #     right(90)
# #     forward(size)
# #     right(90)
# #     forward(size)

# # square(50)
# # input() #keeps editor open     

# #write functions for different shapes and draw away
# #use random fxn (import) for shapes of difference sizes
# # generative-- see last fxn in demo

# # def rainbow():
# #     pencolor('red')
# #     width(30)

# # p_width, c_width, p_color, f_color

# def draw_circle():
#   begin_fill()
#   fillcolor("red")
#   #pencolor(p_color)
#   #width(p_width)
#   circle(100)
#   # end_fill()
# draw_circle()
# input()

# color('blue', 'purple')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
bgcolor("light blue")

def clouds():
    whereX = random.randint(-100, 200)
    whereY = random.randint(-100, 200)
    up()
    goto(whereX, whereY)
    setheading(90)
    down()    
    pencolor("white")
    begin_fill()
    fillcolor("white")
    def arcOfChoice():
        for x in range(3):
            circle(25, 160)
            right(150)
    arcOfChoice()
    circle(25, 270)
    right(120)
    arcOfChoice()
    circle(25, 270)
    end_fill()
    up()


          


def rainbow():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
    x = 150
    arc = 150
    for pretty in colors:
        home()
        up()

# pick the turtle up
        forward(x)
        x -= 10
# move it right half the radius of the desired arc 
        right(-105)
# have it start drawing at a slight angle to the right

        down()
        pencolor(pretty)
        width(10)
        circle(arc, 151)
        arc -= 10
        up()
# forward(65)
# right(-105)
# down()
# pencolor("orange")
# width(10)
# circle(140, 145)
for x in range(3):
    clouds()    

rainbow()    
input()

# Parameters:	
# radius – a number
# extent – a number (or None)
# steps – an integer (or None)
# Draw a circle with given radius. The center is radius units left
# turtle.circle(120, 180)  # draw a semicircle of the turtle; extent – an angle – determines which part of the circle is drawn. I