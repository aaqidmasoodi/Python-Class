# https://docs.python.org/3/library/turtle.html#turtle.reset
import turtle
import time

# class ScrolledCanvas(TK.Frame):
# GAME VARS
DELTA_TIME = 1/240
score_a = 0
score_b = 0


# this.
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



# score write 
scorer = turtle.Turtle()
scorer.color('white')
scorer.penup()
scorer.goto(0,250)
# write (str, align, font)
scorer.write(f'{score_a} | {score_b}', font=('OpenSans', 24, 'bold'))
scorer.hideturtle()

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
	if ball.xcor() > 450 or ball.xcor() < -450:
		dx = -dx
		ball.goto(0,0)



	# ball and paddle collison
	# left
	if ball.xcor() < paddle_a.xcor() + 20 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
		ball.setx(paddle_a.xcor() + 20)
		dx = -dx
		score_a += 1
		scorer.clear() # clear whatever this particular turtle has written
		scorer.write(f'{score_a} | {score_b}', font=('OpenSans', 24, 'bold')) # rewrite the score

	# right
	elif ball.xcor() > paddle_b.xcor() - 20 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
		ball.setx(paddle_b.xcor() - 20)
		dx = -dx
		score_b += 1
		scorer.clear()
		scorer.write(f'{score_a} | {score_b}', font=('OpenSans', 24, 'bold')) # rewrite the score




	screen.update() # update the screen
	time.sleep(DELTA_TIME) # sleep for half second
