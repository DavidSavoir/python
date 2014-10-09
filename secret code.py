#secret code.py
new_letter=[]

userinput = input("Message:")

for letter in userinput:
    new_letter.append(chr(ord(letter)+1))


new_letter.reverse()


secretstring=''.join(new_letter)

print(secretstring)

"""
Testing:

Message:This is it
Uijt!jt!ju

That's not the output we need:  not reversed:

uj!tj!tjiU
"""
