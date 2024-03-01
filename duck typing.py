class Duck:
    def go(self):
        print('the duck is waking')

    def talk(self):
        print('this duck is qwaking')

class Chicken:
    def go(self):
        print("this chicken is walking")

    def talk(self):
        print('this chicking is clucking')

class Person:
    def catch(self,duck):
        duck.go()
        duck.talk()
        print("You catch the critter")

chicken=Chicken()
duck=Duck()
person=Person()

person.catch(chicken)
