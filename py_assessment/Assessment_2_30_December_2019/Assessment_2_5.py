n = int(input("Enter a number : "))

def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return 1
        else:
            return 0
x=prime(n)
if(x==1):
    print("It is Not Prime Number")
else:
    print("It is Prime Number")

