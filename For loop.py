# forloop= a forloop is statement that will execute its block of code a limited amount of times.
# forloop= limited
# whileloop= unlimited
import time
for i in range(10):
    print(i)
for i in range(50,100):
    print(i)
for i in range(50,100,2):
    print(i)
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print('Happy new year')