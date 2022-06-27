import turtle
import time
import os

# GAME VARS

ACCELERATION = 0.4
DELTA_TIME = 1/240
floor_kick = 10


scr = turtle.Screen()
scr.setup(width=800, height=600)
scr.tracer(0)

# Images

# ball
ball = turtle.Turtle()
ball.shape('circle')
ball.penup()
ball.dy = 0


# speed gauge
speed_gauge = turtle.Turtle()
speed_gauge.penup()
speed_gauge.goto(250,250)
speed_gauge.hideturtle()
speed_gauge.write(f'dy: {ball.dy: .2f}', align='center', font=('OpenSans', 24, 'normal'))


# events
def bounce():
	global floor_kick

	floor_kick = 10
# forward
# goto
# stupid but fast very fast
# change the x or y coordinate


scr.listen()
scr.onkeypress(bounce, 'space')

# OOP

while True:

	# write ball speed to the scren
	speed_gauge.clear()
	speed_gauge.write(f'dy: {ball.dy: .2f}', align='center', font=('OpenSans', 24, 'normal'))

	ball.sety(ball.ycor() + ball.dy) # contant
	# IT IS BECAUSE OF THIS STATEMENT

	ball.dy -= ACCELERATION # 0.1 # here we are changing ball.dy

	if ball.ycor() < -280:
		ball.dy = floor_kick
		if floor_kick > 0:
			floor_kick -= 2
		else:
			floor_kick = 0

	scr.update()
	time.sleep(DELTA_TIME)