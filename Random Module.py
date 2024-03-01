import random

x=random.randint(1,6)
print(x)

game=['rock','paper','scissor']
g=random.choice(game)
print(game)

cards=[1,2,3,4,5,6,7,8,9,'A','J','Q','K']
random.shuffle(cards)
print(cards)