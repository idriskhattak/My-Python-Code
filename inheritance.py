class Animal:       #parent class

    def eating(self):
        print('This animal is eating')

    def sleep(self):
        print('This animal is sleeping')

class Rabbit(Animal):     #child class
    def running(self):
        print('The rabbit is running')

class Fish(Animal):        #child class
    def swim(self):
        print("The fish is swimming")

class Hawk(Animal):        #child class
    def fly(self):
        print("The hawk is flying")

rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

rabbit.sleep()
rabbit.eating()
rabbit.running()
print('\n')

fish.sleep()
fish.eating()
fish.swim()
print('\n')

hawk.eating()
hawk.sleep()
hawk.fly()
