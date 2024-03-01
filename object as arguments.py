
class Car:
    color= None

class Motorcycle:
    color=None

def change_color(vechile,color):
    vechile.color=color

car_1=Car()
car_2=Car()
car_3=Car()

bike=Motorcycle()

change_color(car_1,'Red')
change_color(bike,'black')
print(car_1.color)
print(bike.color)