#abstractmethod is that you must have to use a method in child class which is declared in parent class..

from abc import ABC, abstractmethod
class Vechle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vechle):
    def go(self):
        print('This car is driving')

    def stop(self):
        print('This car has stopped')
class Motorcycle(Vechle):

    def go(self):
        print('This motorcycle is driving')

    def stop(self):
        print('This motorcycle has stopped')

car = Car()
motorcycle=Motorcycle()

car.go()
car.stop()
motorcycle.go()
motorcycle.stop()


