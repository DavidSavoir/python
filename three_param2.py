#three_param.py
def my_func(a, b='\nb was not entered', c='\nc was not entered'):
    print (a,"\n",b,"\n",c, sep = "")
my_func("test")
my_func("test","test")
my_func("test","test","test")

print(my_func) # This is NOT printing the location of the function in memory.

# How to remove the spaces that are appearing after each second or third line that is  print

