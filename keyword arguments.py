# Keyword Arguments = Arguments proceded by an identifies when we pass them to function
#                     the order of the arguments dosent matter, unlike positional arguments
#                     python know the names of the arguments that our function recives

def hello(first_name,middle_name,last_name):
    print("your full name is "+first_name+" "+middle_name+' '+last_name)

hello('Idrees','Khan','Khattak')

def hello1(first_name,middle_name,last_name):
    print("your full name is "+first_name+" "+middle_name+' '+last_name)

hello1('khan','idrees','Khattat')

def hello3(first_name,middle_name,last_name):
    print("your full name is "+first_name+" "+middle_name+' '+last_name)

hello3(middle_name='Khan',first_name='Idrees',last_name='Khattak')
