# Scope = the region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.

name='Idrees' #this is a global variable that call inside a function or outside

def display_name():
    name='Khan'
    print(name)    #this is a variable inside a function and it cannot be used outside the function

print(name)
display_name()




