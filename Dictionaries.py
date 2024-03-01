# Dictionary = A changeable, unordered collection of unique key:value
# pairs fast because they use hashing, allow us to access value quickly.

capital={'pakistan':'islamabad',
         'china':'beijing',
         'japan':'tokyo',
         'russia':'moscow'}
print(capital)
print(capital.keys())
print(capital.values())
print(capital['pakistan'])
capital.update({'india':'new delhi'})
print(capital)

for key,value in capital.items():
    print(key,value)