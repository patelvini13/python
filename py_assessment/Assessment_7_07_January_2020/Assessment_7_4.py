# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even. 
# Map function will calculate its square. Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

class Assessment_7_4:

	def composite_func(self,list1):
		fil = list(filter(lambda x: x%2 == 0,list1))
		m1 = list(map(lambda x : x ** 2,fil))
		res = reduce(lambda x,y:x+y,m1)

		return fil,m1,res



if __name__ == '__main__':

	n = int(input("Enter total no of elements : "))

	list1 = []

	for i in range(0,n):
		list1.append(int(input("Enter an element : ")))

	o1 = Assessment_7_4()

	for i in o1.composite_func(list1):
		print(i)