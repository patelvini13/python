s = input("Enter a string : ")

def fun_1(s):
    n = len(s)
    for i in range(0,n):
        for j in range(1,n):
            for k in range(2,n):
                print(s[i],"",s[j],"",s[k])


fun_1(s)