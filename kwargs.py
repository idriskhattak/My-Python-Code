# **kwargs= parameter that will pack all arguments into a dictionary
#           usefull so that a function can accept a varying amount of keyword arguments.

def name(fisrt_name,last_name):
    print("My full name is "+fisrt_name+" "+last_name)

print(name(fisrt_name='Idrees',last_name="khan"))

def name2(**names):    #(names) is our dictionary name
    print('hello ',end='')
    for key,value in names.items():
        print(value,end=' ')

print(name2(middle='Mr',first='Idrees',last='khan'))