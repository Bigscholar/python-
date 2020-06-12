import turtle
turtle.setup(650,350,400,200)
turtle.pensize(5)
turtle.right(90)
for i in range(4):
	turtle.fd(150)
	turtle.right(90)
	turtle.circle(-150,45)
	turtle.right(90)
	turtle.fd(150)
	turtle.right(45)
turtle.done()