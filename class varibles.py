#class variables are declared outside  the constructor
class Car:

    wheels=4 #this is the class variable called outside the constructor

    def __init__(self,make,model,year,owner):    #the innit is used to construct objects
        self.make=make         #these all are the varibales called inside a contructor these variables
        self.model=model       # are called instance varibles
        self.year=year
        self.owner=owner

    def drive(self):
        print('this car is driving')

    def stop(self):
        print('this car has stopped')

car1=Car('Corolla','Gerande',2022,'Idris')
print(car1.make)
print(car1.model)
print(car1.year)
print('Owner of this car is '+car1.owner)


print(car1.wheels)

