# Exception = Events detected during execution that interrupt the flow of program
#             can be handle by exception.
try:
   numinator=int(input("Enter any number ="))
   denominator=int(input("Enter another number ="))
   division=numinator/denominator
   print(division)
except ZeroDivisionError:
    print("You can't devide something by 0")

except ValueError:
    print("You cant devide something with an alphabet")

finally:
    print('What ever happens this will print')