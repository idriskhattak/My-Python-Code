# Sets = a sets is a collection of unoredered unindexed,no duplicates data
# for Sets we use curly braces {}. , lists [] , Tuple()

grocery={'tomatoes','onion','carrot','vegetables','knife'}
dishes={'plates','forks','spoon','knife'}

#grocery.update(dishes)
#print(grocery)

grocery.add('nothing')
print(grocery)

grocery.remove('nothing')
print(grocery)

print('these are same elements presented in grocery and dishes'+ str(grocery.intersection(dishes)))
print('These are the different elements in grocery from dishes'+str(grocery.difference(dishes)))
for i in grocery:
    print(i)
