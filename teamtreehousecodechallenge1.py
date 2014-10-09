__author__ = 'david.savoir'

the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

the_list.insert(0, the_list.pop(3))
count=0
for element in the_list:
    if element == "a":
        the_list.remove(element)
    elif element == False:
        the_list.remove(element)
for sublist in the_list:
    if sublist == [1,2,3]:
        the_list.remove(sublist)
        print ("found sublist")

while True:
    if count < 21:
        count = 4
        the_list.extend([count])
        count= count+1
        print (count)
    else:
        break

print (the_list)
