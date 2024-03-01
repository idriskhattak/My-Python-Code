import os
import shutil
path='test.txt'
fol='folder'
fol2='folder2'
try:
   # os.remove(path) #this will delete a file
   # os.rmdir(fol)    #this will delete an empty directory
   shutil.rmtree(fol2)  #this will delete all directory including files within

except FileNotFoundError:
    print('File was not found')
