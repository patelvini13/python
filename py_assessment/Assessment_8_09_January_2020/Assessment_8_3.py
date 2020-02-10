# Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Value1, Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(),
# Subtraction(), Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1, Value2 and return
# result.
# Subtraction() method will perform subtraction of Value1, Value2 and
# return result.
# Multiplication() method will perform multiplication of Value1, Value2 and
# return result.
# Division() method will perform division of Value1, Value2 and return
# result.
# After designing the above class call all instance methods by creating
# multiple objects.

class Arithmetic:

	def __init__(self,Value1,Value2,result):
		self.Value1 = Value1
		self.Value2 = Value2
		self.result = result

	def Accept(self,Value1,Value2):

		
	def Addition(self):
		self.result = self.Value1 + self.Value2

	def Subtraction(self):
		self.result = self.Value1 - self.Value2
		

	def Multiplication(self):
		self.result = self.Value1 * self.Value2

	def Division(self):
		self.result = self.Value1 / self.Value2

if __name__ == '__main__':

	obj1 = Arithmetic(0.0,0.0,0.0)
	obj22 = Arithmetic(0.0,0.0,0.0)
	
	print("For obj1 : \n")
	print("Addition = ",)
	

	print("\n For obj2 : \n")
	