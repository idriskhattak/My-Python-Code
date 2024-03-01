class Prey:
    def flees(self):
        print('The animal flees')

class Predator:
    def hunt(self):
        print('The animal hunts')

class Rabbit(Prey):
    pass

class Fish(Prey,Predator):
    pass

rabbit=Rabbit()
fish=Fish()

rabbit.flees()
print('\n')

fish.flees()
fish.hunt()