n = int(input("Enter a number : "))

def funRecursion(n):
	if n == 1:
		return n
	else:
		return n + funRecursion(n-1)

print(funRecursion(n))