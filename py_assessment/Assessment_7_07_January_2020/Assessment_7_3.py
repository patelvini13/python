# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user.
#  Filter should filter out all such numbers which greater than or equal to 70 
#  and less than or equal to 90. Map function will increase each number by 10. 
#  Reduce will return product of all that numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000
from functools import reduce

class Assessment_7_3:

	def composite_func(self,list1):
		fil = list(filter(lambda x: x >= 70 and x <= 90,list1))
		m1 = list(map(lambda x : x + 10,fil))
		res = reduce(lambda x,y:x+y,m1)

		return fil,m1,res



if __name__ == '__main__':

	n = int(input("Enter total no of elements : "))

	list1 = []

	for i in range(0,n):
		list1.append(int(input("Enter an element : ")))

	o1 = Assessment_7_3()

	for i in o1.composite_func(list1):
		print(i)


