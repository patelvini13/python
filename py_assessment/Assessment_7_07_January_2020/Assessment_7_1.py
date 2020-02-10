# Write a program which contains one lambda function which accepts one 
# parameter and return power of two.
# Input: 4 Output: 16
# Input: 6 Output: 36

class Lambda_class:

	def power(self,n):
		return (lambda x : x ** 2)(n)

if __name__ == '__main__':

	n = int(input("Enter a number : "))
	
	o1 = Lambda_class()

	print(o1.power(n))
