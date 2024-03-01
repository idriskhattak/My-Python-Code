# list= list is used to store multiple items to 1 variable

list = ['Chicken','Handi','Biryani','Kabab']
print(list)
list.remove('Handi')
print(list)

print(list[2])
list.append('Pulao')
list.insert(0,'Chicken karahi')
for i in list:
    print(i,end=' ')