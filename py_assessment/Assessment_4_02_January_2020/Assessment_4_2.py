s = input("Enter a string : ")

def no_of_words(s):
    l = s.split()
    return len(l)

print("No. of words in given string are ",no_of_words(s))