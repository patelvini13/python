num = int(input("Enter a number : "))

def check_num(n1):
    if(n1==0):
        print("Zero")
    elif(n1>0):
        print("Positive Number")
    else:
        print("Negative Number")

check_num(num)
