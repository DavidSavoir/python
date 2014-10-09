#ex15.py
#imports the argv module from sys library
from sys import argv

#assigns variables script and filename to argv
script, filename = argv

#assigns the opening of filename to the variable text

txt = open(filename)

#prints filename

print "Here's your file %r:" % filename
#prints the contents of the file txt.
print txt.read()

"""print "Type the filename again"
#assigns the user input to the variable file_again after print '>'
file_again = raw_input("> ")

#assigns the openening of filename stored in file_again to variable txt_again
txt_again = open(file_again)
#reads out content of file 
print txt_again.read()
"""
