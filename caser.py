#caser.py 
import sys

def capitalized(stringcap):
    stringcap = str(stringcap)
    capitalize_string = stringcap.capitalize()
    return capitalize_string


def titled(stringtitle):
    titled_string = stringtitle.title()
    return titled_string


def uppered(stringupper):
    upper_string = stringupper.upper()
    print ("test")
    return upper_string


def lowered(stringlower):
    lower_string = stringlower.lower()
    return lower_string


def exit():
    sys.exit()


if __name__ == "__main__":
    diction = {
        'capitalized': capitalized,
        'title': titled,
        'upper': uppered,
        'lower': lowered,
        'exit': exit
    }

options = diction.keys()
prompt_action = 'Pick a function name ({0}):'.format(','.join(options))
prompt_string = 'Enter a string: '
"""
while True:
    inp = input(prompt_action)
    inpstr = input(prompt_string)
    option = diction.get(inp, None)
    option(inpstr)
    if option == exit:
        exit()
"""

"""
    elif option == capitalized:
        capitalized(inpstr))
    elif option == titled:
        print(titled(inpstr))
    elif option == uppered:
        print(uppered(inpstr))
    elif option == lowered:
        print(lowered(inpstr))

    else:
        print('Please select a valid option')
"""
"""
if option has "exiting": 
		exit()
	elif option == capitalized:
		capitalized()
	elif option == titled:
		titled()
	elif option == uppered:
		uppered()
	elif option == lowered:
		lowered(inpstr)
	else: 
		print ('Please select a valid option')
"""


while True:
    inp = input(prompt_action)
    inpstr = input(prompt_string)
    option = diction.get(inp, None)
    option(inpstr)
    # Call the function on inputstring
    print(option(inpstr))
    #diction[prompt_action](inputstr)
    if option:
        #option(inpstr) #option is not callable ??? > This returns memory location
        print('-' * 40)
    else:
        print('Please select a valid option !')

"""
Here you already have your function object:

    option = diction.get(inp, None)

so the next thing to do is call it:  option(inpstr)

If you allow your exit function to take a string (even if you don't
use it) then a call to exit can be treated just like any other.
"""

"""
see comments. Also I am not entering the functions (e.g. uppered)
"""