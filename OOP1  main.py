#think of self is the object that we are taking as car
from car import Car

car1=Car('Honda','Civic','2022','Black')
car2=Car('Corolla','Gerande',2022,'RED')

print(car2.make)
print(car2.model)
print(car2.year)
print(car2.color,'\n')

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color,'\n')

car1.drive()
car1.stop()

