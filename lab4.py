#problem1+2
class Rectangle(object):
	def __init__(self,width,height):
		self.width = width
		self.height = height
	def Area(self):
		return self.width * self.height
	def Perimeter(self):
		return (self.width + self.height) * 2 
	def Print_Properties(self):
		print(self.width, self.height)

rec1 = Rectangle(10,12)
rec1.Area()
print(rec1.Area())
rec1.Perimeter()
print(rec1.Perimeter())
rec1.Print_Properties()

#problem3
class Person(object):
	def __init__(self,age,city,gender,food,sport,weight):
		self.age = age
		self.city = city
		self.gender = gender
		self.food = food
		self.sport = sport
		self.weight = weight
	def Eat(self):
		self.weight += 2
		print("I ate " + self.food)
	def Sport(self):
		print("I am playing " + self.sport)
Noy = Person("15","KFASH","female","Pizza","sleeping", 77)
Noy.Eat()
Noy.Sport()

