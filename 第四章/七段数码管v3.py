import turtle
import time
def drawgap():
    turtle.penup()
    turtle.fd(5)
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
    drawline(1) if digit in [2,3,4,5,6,8,9] else drawline(0)
    drawline(1) if digit in [1,3,4,5,6,7,8,9,0] else drawline(0)
    drawline(1) if digit in [2,3,5,6,8,9,0] else drawline(0)
    drawline(1) if digit in [2,6,8,0] else drawline(0)
    turtle.left(90)
    drawline(1) if digit in [4,5,6,8,9,0] else drawline(0)
    drawline(1) if digit in [2,3,5,6,7,8,9,0] else drawline(0)
    drawline(1) if digit in [1,2,3,4,7,8,9,0] else drawline(0)
    turtle.left(180)
def drawDate(date):
    for i in date:
        if i == '+':
            turtle.write('年', font = ("Arial", 18, "normal"))
            turtle.penup()
            turtle.fd(50)
        elif i == '-':
            turtle.write('月', font = ('Arial', 18, 'normal'))
            turtle.penup()
            turtle.fd(50)
        elif i == '=':
            turtle.write('日', font = ('Arial', 18, 'normal'))
            turtle.penup()
            turtle.fd(50)
        else:
            drawdigit(eval(i))
            turtle.penup()
            turtle.fd(15)
            
def main():
    turtle.penup()
    turtle.color("brown")
    turtle.pensize(5)
    turtle.fd(-300)
    turtle.speed(9)
    
    drawDate('2020+06-16=')
    turtle.hideturtle()
    turtle.done()
main()













