n = int(input("Enter a number : "))

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
                print(j, end = ' ')
        print("\n")

pattern(n)