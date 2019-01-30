import turtle
import time
import random
import math
from ball import Ball
#turtle.bgpic("agarBG.gif")
turtle.colormode(1)
turtle.tracer(0)
turtle.hideturtle()
running=True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
global score
score = 0
#part 1#
color =(random.random(), random.random(), random.random())
my_ball= Ball(0,0,60,10,50, color)
print(my_ball.color)
number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5

your_name = turtle.textinput("Enter your name", "What is your name?") 

##part 2:
BALLS = []
for i in range (number_of_balls):
	x = random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)
	y = random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx , maximum_ball_dx)
	dy = random.randint(minimum_ball_dy , maximum_ball_dy)
	r = random.randint(minimum_ball_radius , maximum_ball_radius)
	color =(random.random(), random.random(), random.random())
	ball_add = Ball(x,y,dx,dy,r,color)
	BALLS.append(ball_add)
def move_all_balls():
	for ball in BALLS:
		ball.move(screen_width, screen_height)
		#part3
def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	distance= math.sqrt((ball_a.xcor()-ball_b.xcor())**2+(ball_a.ycor()-ball_b.ycor())**2)
	if distance<= ball_a.r+ball_b.r:
		return True
	else:
		return False
#part4- check collisions for all balls.
def check_all_balls_collision():
	global running
	all_balls=[]
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
	for ball_a in all_balls:
		for ball_b in all_balls:
			if collide(ball_a,ball_b):
				global score
				r1=ball_a.r
				r2=ball_b.r
				x = random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)
				y = random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)
				dx =  random.randint(minimum_ball_dx , maximum_ball_dx)
				dy = random.randint(minimum_ball_dy , maximum_ball_dy)
				r = random.randint(minimum_ball_radius , maximum_ball_radius)
				color = (random.random(), random.random(), random.random())
				if(r1>r2):
					ball_b.new_Ball(x,y,dx,dy,r,color)
					ball_a.r=ball_a.r+4
					ball_a.shapesize(ball_a.r/10)

					scoreT.clear()
					scoreT.write("SCORE:" + str(score), font=("Arial", 60, "normal"))

					if(my_ball==ball_b):
						running=False
					if (my_ball==ball_a):
						score = score + 10
						print(score,"SCORE")
				else:
					ball_a.new_Ball(x,y,dx,dy,r,color)
					ball_b.r=ball_b.r+4
					ball_b.shapesize(ball_b.r/10)
					scoreT.clear()
					scoreT.write("SCORE:" + str(score), font=("Arial", 60, "normal"))

					if(my_ball==ball_a):
						running=False
					if (my_ball==ball_b):
						score = score + 10
						print(score,"SCORE")

#PART5-Movearound(AHAHAHAHAHAHHA)
def movearound():
	cursor_x = turtle.getcanvas().winfo_pointerx() - screen_width*2
	cursor_y = screen_height*1.4 - turtle.getcanvas().winfo_pointery()
	my_ball.goto(cursor_x,cursor_y)
	# final_x = cursor_x
	# final_y = cursor_y
	# if cursor_x >= my_ball.x:
	#     if my_ball.dx <cursor_x - my_ball.x:
	#         final_x = my_ball.x + my_ball.dx
	#     else:
	#         final_x = cursor_x
	# else:
	#     if my_ball.x-cursor_x>my_ball.dx:
	#         final_x = my_ball.x - my_ball.dx
	#     else:
	#         final_x = cursor_x
	# if cursor_y >= my_ball.y:
	#     if my_ball.dy < cursor_y - my_ball.y:
	#         final_y = my_ball.y + my_ball.dy
	#     else:
	#         final_y = cursor_y
	# else:
	#     if my_ball.y-cursor_y>my_ball.dy:
	#         final_y = my_ball.y - my_ball.dy
	#     else:
	#         final_y = cursor_y
	#         print
	# print("(C" + str(cursor_x) + "," + str(cursor_y) + ")")
	# print("("+ str(final_x) + "," + str(final_y) + ")")
	# my_ball.goto(final_x, final_y)




	#FEATURES:
#my_ball name feature:













def gameOver():
	turtle.pu()
	turtle.goto(0,150)
	turtle.write("GAME OVER!", True, align="center", font=("David", 85, "normal"))






#createBotton
botton = turtle.clone()
turtle.register_shape("replay.gif")
botton.shape("replay.gif")

def replay(x,y):
	global score
	score = 0
	scoreT.pu()
	scoreT.goto(-170,-250)
	scoreT.write("SCORE:" + str(score), font=("Arial", 30, "normal") , align="center")
	turtle.clear()
	scoreT.goto(-170,-250)
	botton.hideturtle()
	global running
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2
	print("replay")
	#my_ball.new_Ball(0,0,10,10,20, "red")
	running = True
	while(running):
		move_all_balls()
		movearound()
		check_all_balls_collision()
		turtle.update()
		screen_width = turtle.getcanvas().winfo_width()/2
		screen_height = turtle.getcanvas().winfo_height()/2
		my_ball.clear()
		my_ball.pencolor("black")
		my_ball.write(your_name, align = "center",font=("Arial", 15, "normal"))
		screen_width = turtle.getcanvas().winfo_width()/2
		screen_height = turtle.getcanvas().winfo_height()/2
		time.sleep(.1)
	print("GAMEOVER")
	botton.showturtle()
	turtle.update()
	botton.goto(0,0)
	gameOver()
	print("game over")


scoreT = turtle.clone()
scoreT.pu()
scoreT.goto(-170,-250)
scoreT.write("SCORE:" + str(score), font=("Arial", 30, "normal") , align="center")
botton.onclick(replay)

#for ball in BALLS:
#    x = random.randint(-screen_width + maximum_ball_radius, screen_height)
#    y = rendom.randint(-screen_height + maximum_ball_radius)





while(running):
	move_all_balls()
	movearound()
	check_all_balls_collision()
	turtle.update()
	my_ball.clear()
	my_ball.pencolor("black")
	my_ball.write(your_name, align = "center",font=("Arial", 15, "normal"))
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2
	time.sleep(.1)
	my_ball.clear()

botton.showturtle()
turtle.update()
botton.goto(0,0)
gameOver()
print("game over")

turtle.mainloop()