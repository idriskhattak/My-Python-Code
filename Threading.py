
import threading
import time

def eat_breakfast():
    time.sleep(3)
    print('I eat my breakfast')

def tea():
    time.sleep(3)
    print('I drank my tea')

def ready():
    time.sleep(4)
    print('It took me 4 minutes to get ready')

#eat_breakfast()
#tea()
#ready()
         #this program is gonna take us about 10 sec to complete because it is executing sequentialy one by one
         #but with the help of threading we can complete these tasks in just 4 seconds now lets create multi threads
         # for every task
x = threading.Thread(target=eat_breakfast,args=())
x.start()

y = threading.Thread(target=tea,args=())
y.start()

z = threading.Thread(target=ready,args=())
z.start()

print(threading.activeCount())
#print(threading.enumerate())