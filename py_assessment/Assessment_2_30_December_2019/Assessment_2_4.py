n= int(input("Enter a number : "))

def factor_add(n):
    l1=[]
    for i in range(1,n+1):
        if(n%i == 0):
            l1.append(i)
    return (sum(l1))

print("Factor addition is : ",factor_add(n))
