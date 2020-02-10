# Accept file name and one string from user and return the frequency 
# of that string from file.
# Input: Demo.txt Marvellous
# Search “Marvellous” in Demo.txt

import sys

f1 = sys.argv[1]
s = sys.argv[2]

dict1={}

def fun_check(f1,s):
	f = open(f1,"r")
	str1 = f.read().split()

	for i in str1:
		if not i in dict1.keys():
			if i == s:
				dict1[s]+=1
fun_check(f1,s)




