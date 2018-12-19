from turtle import *
import random
import turtle
import math
class Ball(Turtle):
	def __init__(self,radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

	
ball1 = Ball(10,"red",3)
ball2 = Ball(30, "pink", 5)

def check_collision(ball1,ball2):
	x1, y1 = ball1.pos()
	x2 ,y2 = ball2.pos()
	d = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1,2))
	if d <= ball1.radius +ball2.radius:
		print("mission accomplished")
		ball2.goto(100,0)
check_collision(ball1, ball2)
turtle.mainloop()





