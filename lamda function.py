
def mul(x):
    return x*2

print(mul(5))

multiplication=lambda x:x*2
print('this is multiplication by using lambda function '+str(multiplication(5)))

double= lambda x,y:x*y
print('This is double variables multiplication by lambda function '+str(double(2,3)))

age= lambda age:True if age >=18 else False

print(age(12))

