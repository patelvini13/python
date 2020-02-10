n = int(input("Enter a number : "))

def pattern(n):
    for i in range(n):
        for j in range(n):
                print("*",end = " ")
        print("\n")

pattern(n)
