
class Calculater():

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def add(self):
		return(self.x + self.y)

	def sub(self):
		return(self.x - self.y)

	def multi(self):
		return(self.x * self.y)

	def div(self):
		return(self.x/self.y)


a = Calculater(15,5)
print(a.add())
print(a.sub())
print(a.multi())
print(a.div())