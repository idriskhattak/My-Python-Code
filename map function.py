
store=[('shirts',20),
       ('cap',29),
       ('shoes',12),
       ('bags',11)]

to_euros= lambda data:(data[0],data[1]*0.82)

store_euros= list(map(to_euros,store))

for i in store_euros:
    print(i)