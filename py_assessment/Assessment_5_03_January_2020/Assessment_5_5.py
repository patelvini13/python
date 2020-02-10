def funFactorial(n):
	if n == 1:
		return 1
	else:
		return n*funFactorial(n-1)

n = int(input("Enter a number : "))

result = funFactorial(n)
print(result)