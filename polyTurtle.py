# Turtle project 
# by Adrian Carvajal
# 5.27.2025
import turtle
turtle.color("blue")

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

def polygon(num, size):
    for i in range(num):
        turtle.forward(size)
        turtle.left(360 / num)

polygon(4, 100)
back(120)
polygon(3, 50)
