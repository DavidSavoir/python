"""
Write a program that uses a while loop to accept input from the user (if the user presses Enter, exit the program).
Save the input to a file, then print it.
Upon starting, the program will display any previous content of the file."""

f = open('source.txt', 'w')
print(f.read())

f.seek(0)

while True:
	userinput=input('Enter text:')
	if userinput =='':
		break
	else:
		#f = open('source.txt', 'a')
		f.write(userinput)
		f = open('source.txt', 'r')
		outp = f.readlines()
		print (outp)
		#f.readlines()
f.close()		

"""Enter text: Python is fun.
Python is fun.
Enter text: O'Reilly makes good classes.
Python is fun.O'Reilly makes good classes.
Enter text:
Below is an example of possible output from a second run of the program.

Python is fun.O'Reilly makes good classes.
Enter text: The file is saving correctly
Python is fun.O'Reilly makes good classes.The file is saving correctly
Enter text:"""


"""result = open('source.txt','a')
result.write(userinput)
while userinput!='':
	userinput = input('Enter text:')
	result = open('source.txt','a')
	result.write(userinput)
	#f.close()
	f = open('source.txt', 'r')
	print(f.readlines())"""