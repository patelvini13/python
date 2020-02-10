#  Write a program which contains one lambda function which 
# accepts two parameters 
#  and return its multiplication.
# Input: 4 3 Output: 12
# Input: 6 3 Output: 18

class Lambda_class:

	def power(self,a,b):
		return (lambda a,b : a * b)(a,b)


if __name__ == '__main__':

	n1 = int(input("Enter 1st number number : "))
	n2 = int(input("Enter 2nd number number : "))
	
	o1 = Lambda_class()

	print(o1.power(n1,n2))
