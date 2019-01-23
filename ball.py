from turtle import*
class Ball(Turtle):
	"""docstring for Ball"""
	def __init__(self, x,y,dx,dy,r,color):
		Turtle.__init__(self)
		
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)
		self.penup()
		self.goto(x,y)
	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		current_y=self.ycor()
		new_x=current_x+self.dx
		new_y=current_y+self.dy
		print("moving")
		print(new_x,new_y,self.dy)
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_ball=new_y-self.r
		self.goto(new_x,new_y)
		if(right_side_ball>=screen_width):
			self.dx= -self.dx
		if(left_side_ball<= -screen_width):
			self.dx= -self.dx
		if(up_side_ball>=screen_height):
			self.dy= -self.dy
		if(down_side_ball<=-screen_height):
			self.dy= -self.dy
	def new_Ball(self,x,y,dx,dy,r,color):
			self.x = x
			self.y = y
			self.dx = dx
			self.dy = dy
			self.r = r
			self.shape("circle")
			self.shapesize(r/10)
			self.color(color)
			self.penup()
			self.goto(x,y)