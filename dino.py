import turtle
import time
import random



# score
score = 0

# GAME VARS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ACCELARATION = 0.4


# window 
scr = turtle.Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.bgcolor('#1f1f1f')
scr.title('DINO - CodeWithAaqid')
scr.tracer(0)



# cube
dino = turtle.Turtle()
dino.penup()
dino.shape('square')
dino.color('#efefef')
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
	obstacle.color('#efefef')
	obstacle.penup()
	rand_index = random.choice([0,1,2])
	obstacle.curr_height = heights[rand_index] * 20
	obstacle.shapesize(stretch_wid=heights[rand_index], stretch_len=1)
	obstacle.goto(x_spawns[index], -(300 - (obstacle.curr_height//2)))
	index += 1

# GAME MENU
menu = turtle.Turtle()
menu.color('#efefef')
menu.hideturtle()
menu.penup()


# score
score_writer = turtle.Turtle()
score_writer.color('#efefef')
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0,220)
score_writer.write(f'Score: {score}', align='center', font=('OpenSans', 24, 'bold'))


def jump():

	if dino.ycor() == -270: # if dino is on the ground
		dino.dy = 12

def start_game(sadf, asdfsdf):
	global state
	global score
	state = 'running'
	score = 0

scr.listen()
scr.onkeypress(jump, 'space')
scr.onscreenclick(start_game) # callback

state = 'paused'
while True:


	# make dino fall
	if state == 'running':


		# score based on distance
		score += 1
		score_writer.clear()
		score_writer.write(f'Score: {score}', align='center', font=('OpenSans', 24, 'bold'))

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


			# good
			if dino.xcor() + 20  > obstacle.xcor() - 10 and dino.ycor() - 20 < obstacle.ycor() + (obstacle.curr_height//2) and dino.xcor() - 20 < obstacle.xcor() + 10:
				state = 'game_over'


			# check for collision

		


	elif state == 'paused':
		score_writer.clear()
		dino.hideturtle()
		menu.clear()
		menu.write("Click to Play", align="center", font=('OpenSans', 48, 'bold'))


	elif state == 'game_over':
		dino.hideturtle()
		menu.clear()
		menu.write("Game Over", align="center", font=('OpenSans', 48, 'bold'))
		index = 0
		for obstacle in obstacles:
			obstacle.goto(x_spawns[index], -(300 - (obstacle.curr_height//2)))
			index += 1



	scr.update()
	time.sleep(1/240)