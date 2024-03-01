
buddies=[('idrees',21),
         ('aizaz',24),
         ('hamid',12),
         ('zakir',17),
         ('awais',26),
         ('eisa',18),]

age= lambda data:data[1] >=18

drinking_buddies=list(filter(age,buddies))

for i in drinking_buddies:
    print(i)
