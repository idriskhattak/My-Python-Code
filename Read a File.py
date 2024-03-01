try:
    with open('C:\\Users\\Idris Khan\\Desktop\\test.txt') as idris:
        print(idris.read())
except FileNotFoundError:
    print('The file was not found')
