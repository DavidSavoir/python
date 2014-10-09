__author__ = 'david.savoir'

def first_4(x):
    return x[:4]

def first_and_last_4(z):
    first_items = z[:4]
    last_items = z[-4:]
    newest_list = first_items.append(last_items)
    print (newest_list)
    return newest_list


lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

first_and_last_4(lst)



