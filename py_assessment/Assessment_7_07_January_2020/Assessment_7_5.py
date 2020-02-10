# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user.
#  Filter should filter out all prime numbers. 
#  Map function will multiply each number by 2. 
#  Reduce will return Maximum number from that numbers. 
#  (You can also use normal functions instead of lambda functions).
# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

class Assessment_7_5:

	def prime_func(self,n):
		flag = 0
		if n == 1:
			flag = 1
		elif n <= 0:
			flag = 1
		else:
			for i in range(2,n):
				if n % i == 0 :
					flag = 1
		return flag

	def composite_func(self,list1):

		fil = list(filter(lambda x : o1.prime_func(x) == 0,list1))
		m1 = list(map(lambda x : x * 2,fil))
		res = reduce(lambda x,y:x if x>y else y,m1)

		return fil,m1,res



if __name__ == '__main__':

	n = int(input("Enter total no of elements : "))

	list1 = []

	for i in range(0,n):
		list1.append(int(input("Enter an element : ")))

	o1 = Assessment_7_5()

	for i in o1.composite_func(list1):
		print(i)
