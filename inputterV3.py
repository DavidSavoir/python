"""f = open('source.txt', 'r')
print (f.readlines)
print ("Content of file here")
f.seek(0)
f.close()"""

#f.seek(0)

with open("source.txt", "r") as f:
	for line in f.readlines():
		print (line)
#f.seek(0)

while True:
	with open('source.txt', 'a') as f:
		#print ("Passed true")
		#userinput=input('Enter text:')
		userinput = input('Enter text:')
		if userinput =='':
			#print("Entering if no content")
			break
		else:
			#print("Entering else")
			f.write(userinput)
	with open("source.txt", "r") as f:
		print (f.read())

"""
Getting there.

Per comments last time:

"Anyway, back to my main point:  it's not safe to start out in read mode, "

So:

with open("source.txt", "r") as f:

as a first line is not safe.  You don't know if source.txt exists.  I would prefer
if you avoided using "with" syntax since we have not introduced it yet in the
Lesson. But I won't make not using it a requirement -- just make sure you
aren't reliant on it and know to do it the way we've shown.

The Lesson showed how to open and close in append mode to insure
a non-crash beginning.  Example:

#!/usr/local/bin/python3
"""File-based to-do list maintainer."""

otasks = open('open_tasks.txt','a')
otasks.close()
dtasks = open('done_tasks.txt','a')
dtasks.close()

When you test your code, make sure you try it for a file that
does not exist yet.

Good work so far.


-Kirby
"""
				
				
