import turtle
def drawline(draw):
    if draw == 1:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawdot():
    turtle.penup()
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(40)
    turtle.pendown()
    turtle.circle(1,360)
    turtle.penup()
    turtle.left(90)
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(40)
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
def drawnum(num):
    for i in num:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            drawdigit(eval(i))
            turtle.penup()
            turtle.fd(10)
        elif i == '.':
            drawdot()
def main():
    turtle.penup()
    turtle.color("brown")
    turtle.pensize(5)
    turtle.fd(-300)
    drawnum('2020.06.16')
    turtle.hideturtle()
    turtle.done
main()













