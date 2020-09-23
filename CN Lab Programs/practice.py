import turtle

ball=turtle.Turtle()
ball.speed(10)
 

ball.speed(3)
for i in range(180):
	ball.forward(100)
	ball.right(30)
	ball.forward(20)
	ball.left(60)
	ball.forward(50)
	ball.right(30)
	ball.penup()
	ball.setposition(0,0)
	ball.pendown()
	ball.right(2)
