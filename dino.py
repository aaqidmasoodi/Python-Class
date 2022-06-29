import turtle
import time

# GAME VARS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ACCELARATION = 0.4


# window 
scr = turtle.Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.bgpic('dino_bg.gif')
scr.tracer(0)



# cube
dino = turtle.Turtle()
dino.penup()
dino.shape('square')
dino.color('white')
dino.shapesize(stretch_len=2, stretch_wid=2)
dino.goto(-300, -50)
dino.dy = 0




# list of objects
obstacles = []
heights = [3,4,5]
x_spawns = [400, 600, 800]


for i in range(3):
	obstacles.append(turtle.Turtle())

index = 0
for obstacle in obstacles:
	obstacle.shape('square')
	obstacle.color('white')
	obstacle.penup()
	obstacle.shapesize(stretch_wid=heights[index], stretch_len=1)
	obstacle.goto(x_spawns[index], -250)
	index += 1







def jump():

	if dino.ycor() == -270: # if dino is on the ground
		dino.dy = 10


scr.listen()
scr.onkeypress(jump, 'space')


while True:


	# make dino fall
	dino.sety(dino.ycor() + dino.dy)

	dino.dy -= ACCELARATION


	if dino.ycor() < -270:
		dino.sety(-270)
		dino.dy = 0



	for obstacle in obstacles:
		obstacle.setx(obstacle.xcor() - 3)


	scr.update()
	time.sleep(1/120)