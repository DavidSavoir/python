diction = {}
wordset = set()
while True:
    words = input("Enter text: ").split()
    if not words:
        break
    for word in words:
        lenset = len(wordset)
        wordset.add(word)
        if len(wordset) > lenset:
            diction[word] = len(wordset)
        for k, v in diction.items():
            print(k, v)

"""

Enter text: how now brown cow
how 1
now 2
cow 4
brown 3
Enter text: the cow jumped over the moon
brown 3
cow 4
jumped 6
over 7
moon 8
how 1
the 5
now 2
Enter text:
Finished"""

"""
This is 99% right but I'm getting:

    lenset=len(wordset)
         ^
IndentationError: expected an indented block

And indeed I'm seeing a non-indented suite giving a for loop with no body:

    else: 
        for word in words:     #  <--- head with no body
        lenset=len(wordset)
        wordset.add(word)

What I would suggest is dropping the whole idea of an else suite
after if... break.  When the if ends in break, you don't need an else.
That would let you outdent the for loop.  But you still need to 
determine that for loop's scope versus the output for loop.  All 
the user's words should be added to the dict, or not, before a next
listing occurs.

-Kirby
"""