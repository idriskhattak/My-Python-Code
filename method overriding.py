class Animal:
    def eat(self):
        print("this animal is eating")

class Rabbit(Animal):
    def eat(self):
        print('This rabbit is eating')

rabbit=Rabbit()
rabbit.eat()