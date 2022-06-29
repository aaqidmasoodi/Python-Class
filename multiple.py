import turtle
import time
import random

scr = turtle.Screen()
scr.setup(width=800, height=600)
scr.tracer(0)


balls = []
for i in range(100):
	ball = turtle.Turtle()
	ball.shape('circle')
	ball.penup()
	ball.dx = random.random() * random.choice([10,-10])
	ball.dy = random.random() * random.choice([10,-10])
	balls.append(ball)

while True:

	for ball in balls:
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)


		# top and bottom collision
		if ball.ycor() > 290 or ball.ycor() < -290:
			ball.dy = -ball.dy

		# right and left collision
		if ball.xcor() > 390 or ball.xcor() < -390:
			ball.dx = -ball.dx



	scr.update()
	time.sleep(1/240)


