n = int(input("Enter a number : "))

def Factorial_fun(n):
    if n == 1:
        return 1
    else:
        return n * Factorial_fun(n-1)

print("Factorial is : ", Factorial_fun(n))