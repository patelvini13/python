# Write a program which accepts file name from user and check whether 
# that file exists in current directory or not.
# Input: Demo.txt
# Check whether Demo.txt exists or not.


file_name = input("Enter the name of file : ")

def func_check(f_name):
	try:
		f = open(f_name,"r")
		print("File exists in current directory")
	except:
		print("FileNotFoundException !!!")

func_check(file_name)
