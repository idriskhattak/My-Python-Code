
students=[('idris','B',26),      #for sorting a list
          ('zakir','A',28),
          ('ali','D',24),
          ('eisa','C',25),
          ('aizaz','A',23)]

grades= lambda grades:grades[1]
students.sort(key=grades)
for i in students:
    print(i)

students2=(('idris','B',26),   #for sorting a tuple
          ('zakir','A',28),
          ('ali','D',24),
          ('eisa','C',25),
          ('aizaz','A',23))

grades= lambda grades:grades[1]

sorted_students=sorted(students2,key=grades)
for i in sorted_students:
    print(i)