import turtle
import time
import random


# GAME VARS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ACCELARATION = 0.4


# window 
scr = turtle.Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.bgpic('dino_bg.gif')
scr.title('DINO - CodeWithAaqid')
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
x_spawns = [400, 800, 1200]



for i in range(3):
	obstacles.append(turtle.Turtle())



index = 0
for obstacle in obstacles:
	obstacle.shape('square')
	obstacle.color('white')
	obstacle.penup()
	rand_index = random.choice([0,1,2])
	obstacle.curr_height = heights[rand_index] * 20
	obstacle.shapesize(stretch_wid=heights[rand_index], stretch_len=1)
	obstacle.goto(x_spawns[index], -(300 - (obstacle.curr_height//2)))
	index += 1

# GAME MENU
menu = turtle.Turtle()
menu.color('white')
menu.hideturtle()
menu.penup()



def jump():

	if dino.ycor() == -270: # if dino is on the ground
		dino.dy = 10

def start_game(x, y):
	global is_running
	is_running = True


scr.listen()
scr.onkeypress(jump, 'space')
scr.onscreenclick(start_game)

is_running = False
while True:


	# make dino fall
	if is_running:
		# get ready
		dino.showturtle()
		menu.clear()

		# main loop
		dino.sety(dino.ycor() + dino.dy)

		dino.dy -= ACCELARATION


		if dino.ycor() < -270:
			dino.sety(-270)
			dino.dy = 0


		index = 0
		for obstacle in obstacles:

			obstacle.setx(obstacle.xcor() - 3)

			# respawn
			# just remake the same thing but write it yourself
			if obstacle.xcor() < -400:
					rand_index = random.choice([0,1,2])
					obstacle.curr_height = heights[rand_index] * 20
					obstacle.shapesize(stretch_wid=heights[rand_index], stretch_len=1)
					obstacle.goto(800, -(300 - (obstacle.curr_height//2)))

			index += 1

			# check for collision
			


	else:
		dino.hideturtle()
		menu.clear()
		menu.write("Click to Play", align="center", font=('OpenSans', 48, 'bold'))



	scr.update()
	time.sleep(1/120)