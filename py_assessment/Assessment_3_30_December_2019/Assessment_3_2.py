n = int(input("Enter no. of elements for a list : "))
l1=[]

def func_1(n):
    for i in range(0,n):
        l1.append(int(input("Enter element of list : ")))
    print(l1)
    return max(l1)

print("Maximum number is : ",func_1(n))