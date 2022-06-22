import turtle
import time
import os

# GAME VARS

ACCELERATION = 0.4
DELTA_TIME = 1/240

scr = turtle.Screen()
scr.setup(width=800, height=600)
scr.tracer(0)


# ball
ball = turtle.Turtle()
ball.shape('circle')
ball.penup()
ball.dy = 0


# speed gauge
speed_gauge = turtle.Turtle()
speed_gauge.penup()
speed_gauge.goto(300,250)
speed_gauge.hideturtle()
speed_gauge.write(f'Speed: {ball.speed}', align='center', font=('OpenSans', 24, 'normal'))



# forward
# goto
# stupid but fast very fast
# change the x or y coordinate

while True:

	# write ball speed to the scren
	speed_gauge.clear()
	speed_gauge.write(f'Speed: {ball.dy}', align='center', font=('OpenSans', 24, 'normal'))

	ball.sety(ball.ycor() + ball.dy) # contant
	# IT IS BECAUSE OF THIS STATEMENT

	ball.dy -= ACCELERATION # 0.1 # here we are changing ball.dy

	if ball.ycor() < -280:
		ball.dy = 10
		os.system('aplay bounce.wav &')

	scr.update()
	time.sleep(DELTA_TIME)