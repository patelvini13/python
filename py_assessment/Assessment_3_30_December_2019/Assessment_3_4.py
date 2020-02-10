def func_1(n):
    for i in range(0,n):
        l1.append(int(input("Enter element of list : ")))
    print(l1)

def fun_serach(s,l1):
    count = 0
    for i in l1:
        if i == s :
            count = count +1
    return count

l1 = []
n = int(input("Enter no. of elements for a list : "))
print(func_1(n))

s = int(input("Enter no. for search : "))
print(fun_serach(s,l1))

