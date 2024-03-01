class Organism:          #parent class
    alive=True

class Animal(Organism):    #child class
    def eat(self):
        print("This animal is eating")

class Dog(Animal):          #another child class that is derived from the child class
    def bark(self):
        print("This dog is barking")

dog=Dog()

print(dog.alive)
dog.eat()
dog.bark()