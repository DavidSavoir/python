#caser.py
import sys

def capitalized(stringcap):
    stringcap = str(stringcap)
    capitalize_string = stringcap.capitalize()
    print (capitalize_string)


def titled(stringtitle):
    titled_string = stringtitle.title()
    print (titled_string)


def uppered(stringupper):
    upper_string = stringupper.upper()
    print (upper_string)


def lowered(stringlower):
    lower_string = stringlower.lower()
    print (lower_string)


def exit(exiting):
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

while True:
    inp = input(prompt_action)
    inpstr = input(prompt_string)
    option = diction.get(inp, None)
    if option:
        option(inpstr)
    else:
        print ("Please select a valid option")



"""
if option == exit:
        exit()
    elif option in diction:
        option = diction.get(inp, None)
    else:
        print('Please select a valid option!')
"""