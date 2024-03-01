#And , Or , Not operators
temp=int(input('What is the temperature outside ='))
if temp >=0 and temp <=30:
    print('The temperature is good outside')
    print('You can go outside')
elif temp <0 or temp > 30:
    print('The temperature is very bad.')
    print("Don't go outside")
#the not operation will turn true into false and false into true