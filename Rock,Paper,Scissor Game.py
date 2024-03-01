import random
while True:
       choices=['rock', 'paper' , 'scissor']
       computer=random.choice(choices)
       player=None
       player=input('rock , paper or scissor =').lower()

       while player not in choices:
           print('Please select only between (rock , paper or scissor).')
           player = input('rock , paper or scissor =').lower()

       if  computer==player:
           print('Computer choice='+computer)
           print('Player choice ='+player)
           print('TIE')


       elif  player=='rock':
            if computer=='paper':
                print('Computer choice='+computer)
                print('Player choice ='+player)
                print('You Lose')
            if computer == 'scissor':
                print('Computer choice=' + computer)
                print('Player choice =' + player)
                print('You Win')

       elif  player=='scissor':
            if computer=='paper':
                print('Computer choice='+computer)
                print('Player choice ='+player)
                print('You Win')
            if computer == 'rock':
                print('Computer choice=' + computer)
                print('Player choice =' + player)
                print('You Lose')

       elif  player=='paper':
            if computer=='scissor':
               print('Computer choice='+computer)
               print('Player choice ='+player)
               print('You Lose')
            if computer == 'rock':
               print('Computer choice=' + computer)
               print('Player choice =' + player)
               print('You Win')

       play_again=input('Do you want to play again (yes/no)').lower()
       if play_again=='no':
           break
print('bye')
