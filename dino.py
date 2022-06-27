import turtle
import time


# GAME VARS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# window 
scr = turtle.Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.tracer(0)



# cube
dino = turtle.Turtle()
dino.penup()
dino.shape('square')
dino.shapesize(stretch_len=2, stretch_wid=2)
dino.goto(-350, -50)
dino.x_change = 0
dino.velocity = 4
dino.dy = 0

def move_dino_right() -> None:
	dino.x_change = dino.velocity


def move_dino_left() -> None:
	dino.x_change = -dino.velocity


def stop_dino() -> None:
	dino.x_change = 0


def jump():
	dino.dy = 10



scr.listen()
scr.onkeypress(move_dino_right, 'd')
scr.onkeypress(move_dino_left, 'a')
scr.onkeyrelease(stop_dino, 'd')
scr.onkeyrelease(stop_dino, 'a')

scr.onkeypress(jump, 'space')


while True:


	# make dino fall
	dino.sety(dino.ycor() + dino.dy)

	dino.dy -= 0.4


	if dino.ycor() < -270:
		dino.sety(-270)
		dino.dy = 0





	# move the dino along x
	dino.setx(dino.xcor() + dino.x_change)


	scr.update()
	time.sleep(1/120)