def recursiveFun(n):
	if i == n :
		return "*"
	else:
		recursiveFun(n-1)


n = int(input("Enter a number : "))
i = n

print(recursiveFun(n))
