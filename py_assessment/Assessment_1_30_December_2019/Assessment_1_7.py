num = int(input("Enter a number : "))

def fun_check(n1):
    if(n1%5==0):
        return "true"
    else:
        return  "false"

print(fun_check(num))