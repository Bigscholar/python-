import turtle
import time
def drawgap():
    turtle.penup()
    turtle.fd(5)
    turtle.pendown()
def drawline(draw):
    drawgap()
    if draw == 1:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)
def drawdigit(digit):
    turtle.color("green")
    turtle.speed(6)
    drawline(1) if digit in [2,3,4,5,6,8,9] else drawline(0)
    drawline(1) if digit in [1,3,4,5,6,7,8,9,0] else drawline(0)
    drawline(1) if digit in [2,3,5,6,8,9,0] else drawline(0)
    drawline(1) if digit in [2,6,8,0] else drawline(0)
    turtle.left(90)
    drawline(1) if digit in [4,5,6,8,9,0] else drawline(0)
    drawline(1) if digit in [2,3,5,6,7,8,9,0] else drawline(0)
    drawline(1) if digit in [1,2,3,4,7,8,9,0] else drawline(0)
    turtle.left(180)
def drawWhite():
    turtle.color("white")
    turtle.speed(10)
    turtle.pendown()
    for i in range(3):
        turtle.left(90)
        turtle.fd(50)
    for i in range(4):
        turtle.fd(50)
        turtle.left(90)
    turtle.left(90)
def main():
    turtle.pensize(5)
    turtle.hideturtle()
    for i in range(5, 0, -1):
        drawdigit(i)
        time.sleep(1)
        drawWhite()
    turtle.done()
main()













