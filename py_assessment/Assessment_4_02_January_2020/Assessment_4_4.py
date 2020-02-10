s = input("Enter a string : ")
n = int(input("Enter position to remove one character : "))


def fun_remove(s, n):
    s1 = ""
    for i in (0,len(s)):
        if i == n:
            s1 = s.replace(s,s[i],"")
    print(s1)
            

fun_remove(s, n)