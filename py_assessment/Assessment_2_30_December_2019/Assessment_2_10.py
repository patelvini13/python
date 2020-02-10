n = int(input("Enter a number : "))
n1 = str(n)

def check(n):
    ans = 0
    for i in n:
        ans = ans + int(i)
    return  ans

print(check(n1))