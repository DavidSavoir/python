#
# check_string.py
#

check = input ("Please enter an upper-case string ending with a period: ")

if check != check.upper() or check[-1]!=".":
	print ("Input is not all upper case or, \nthe input does not end with a period.")
else:
	print ("Input meets both requirements")

