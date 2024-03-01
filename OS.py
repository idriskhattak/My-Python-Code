import os

path='C:\\Users\\Idris Khan\\Desktop\\test.txt'
if os.path.exists(path):
    print('Yes the path file exists')
    if os.path.isfile(path):
        print("Yes it is a file")
    else:
        print("no its not a file")

else:
    print("Sorry the path dosent exist")

