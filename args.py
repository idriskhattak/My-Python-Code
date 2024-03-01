#args = parameter that will pack all arguments into a tuple
#       useful so that a function can accept a varying amount of arguments

def add(num1,num2):
    sum=num1+num2
    return sum

print(add(6,4))

def add2(*idrees):  #while using arg(*) we can use as many parameters as we want
    sum2=0
    for i in idrees:
        sum2 +=i
    return sum2

print(add2(2,3,4,5,6,7,8,9))