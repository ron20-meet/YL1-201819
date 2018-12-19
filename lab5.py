from turtle import *
import turtle
import random
turtle.colormode(255)
#ex1
class Square(Turtle):
	def __init__(self,size):
  		Turtle.__init__(self)
 		self.shape("square")
		self.size = size
 		self.shapesize(size*size)

 	def random_color(self):
 		r = random.randint(0,256)
 		g = random.randint(0,256)
 		b = random.randint(0,256)
 		self.color(r,g,b)


square=Square(2)
square.random_color()
turtle.mainloop()
#ex2+3
class Hexagon(Turtle):
	def __init__(self,size, color, speed):
		Turtle.__init__(self)
		self.size = size
		self.color(color)
		self.speed = speed
 		self.shapesize(size*size)
 		self.begin_poly()
 		for i in range (6):
 			self.fd(100)
 			self.right(60)
 		self.end_poly()
 		p = self.get_poly()
 		turtle.register_shape("hexagon", p)
 		self.shape("hexagon")
h = Hexagon(1,"blue", 30)
turtle.mainloop()