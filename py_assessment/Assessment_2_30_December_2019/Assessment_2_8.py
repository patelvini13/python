n = int(input("Enter a number : "))

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i>j):
                print(j,end = " ")
        print(i)

pattern(n)