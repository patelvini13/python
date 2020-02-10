# Write a program which accept file name from user and open that file 
# and display the contents of that file on screen.
# Input: Demo.txt
# Display contents of Demo.txt on console.

f_name = input("Enter File name : ")

def fun_read(f_name):
	try:
		f = open(f_name,"r")
		print(f.read())
	except:
		print("FileNotFoundException !!")

fun_read(f_name)