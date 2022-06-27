import turtle
import time

# GAME VARS
GRAVITY = 0.1
DELTA_TIME = 1/240
LIFT = 5

# WINDOW
scr = turtle.Screen()
scr.setup(width=1280, height=720)
scr.addshape('flappy_bird.gif')
scr.tracer(0)

# BIRD
bird = turtle.Turtle()
bird.shape('flappy_bird.gif')
bird.penup()
bird.goto(-350,0)
bird.dy = 0

# LIFT
def lift_bird(x, y):
	bird.dy = LIFT



# EVENT BINDING
scr.listen()
scr.onclick(lift_bird)




while True:

	# move the bird
	bird.sety(bird.ycor() + bird.dy)

	# apply gravity
	bird.dy -= GRAVITY




	scr.update()
	time.sleep(DELTA_TIME)