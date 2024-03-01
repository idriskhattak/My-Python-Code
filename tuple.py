# tuple  = collection which is ordered and unchangable used to
# group together related data
#for lists we [] square brackets but for tupple we will use circle brackets()

student=('idrees',14,'jan')
print(student)
print(student.count('idrees'))

for x in student:
    print(x)

if 'idrees' in student:
    print('yes idrees is available here')
