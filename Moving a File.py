import os
source='copy.txt'
destintion='C:\\Users\\Idris Khan\\Desktop\\moved.file.txt'

try:
    if os.path.exists(destintion):
        print('There is already a file available with this name')
    else:
        os.replace(source,destintion)
        print("Your file was moved to the destination")
except FileNotFoundError:
    print("Yuor file was not found")


