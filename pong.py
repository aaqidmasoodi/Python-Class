# https://docs.python.org/3/library/turtle.html#turtle.reset
import turtle
import time

# GAME VARS
DELTA_TIME = 1/240


# window
screen = turtle.Screen()
screen.title('PONG GAME')
screen.bgcolor('#1f1f1f')
screen.setup(width=800, height=600)
screen.tracer(0)


# ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)



# paddle A
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.goto(-350, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.goto(350, 0)

dx = 2
dy = 2


# paddle movement functions
def paddle_a_up():
	paddle_a.sety(paddle_a.ycor() + 40)


def paddle_a_down():
	paddle_a.sety(paddle_a.ycor() - 40)

def paddle_b_up():
	paddle_b.sety(paddle_b.ycor() + 40)


def paddle_b_down():
	paddle_b.sety(paddle_b.ycor() - 40)



# Add event lister to the screen
screen.listen() # 
# do not call this function, pass the name of the function which you
# want onkeypress to call

# CALLBACKS
screen.onkeypress(paddle_a_up, 'w')
screen.onkeypress(paddle_a_down, 's')
screen.onkeypress(paddle_b_up, 'Up')
screen.onkeypress(paddle_b_down, 'Down')


# infinite loop
while True:

	# Move the ball
	ball.setx(ball.xcor() + dx)
	ball.sety(ball.ycor() + dy)


	# top and bottom collision
	if ball.ycor() > 290 or ball.ycor() < -290:
		dy = -dy

	# right and left collision
	if ball.xcor() > 390 or ball.xcor() < -390:
		dx = -dx


	# paddle and ball collision

	if ball.xcor() < paddle_a.xcor() + 20 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
		ball.setx(paddle_a.xcor() + 20)
		dx *= -1

	elif ball.xcor() > paddle_b.xcor() - 20 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
		ball.setx(paddle_b.xcor() - 20)
		dx *= -1


	screen.update() # update the screen
	time.sleep(DELTA_TIME) # sleep for half second
