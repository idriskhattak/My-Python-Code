# str.format()= optiional method that gives users more control when displaying output

animal= 'cow'
item= 'moon'

print('The '+animal+' jumped over '+item)

print('The {} jumped over {}'.format(animal,item))

print('The {} jumped over {}'.format(item,animal))

print('The {} jumped over {}'.format('idrees','moon'))

print('The {1} jumped over {0}'.format(animal,item))

print('The {animal} jumped over {item}'.format(animal='dog',item='building')) #using keyword

number=3.1423

print('The number pi is {:.2f}'.format(number))

numbers=1000

print('the number is {:,}'.format(numbers))
print('the number is {:b}'.format(numbers)) #binary format
print('the number is {:o}'.format(numbers)) #octal
print('the number is {:X}'.format(numbers)) #hexa
print('the number is {:E}'.format(numbers)) #SCINTIFIC