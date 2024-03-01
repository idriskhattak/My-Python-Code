#----------------------------
def new_game():
    guesses=[]
    correct_guesses=0
    qustions_num = 1
    for key in qustions:
        print('----------------------------')
        print(key)
        for i in options[qustions_num-1]:
            print(i)
        guess=input('Enter (A,B,C or D) to chose the correct option')
        guess=guess.upper()
        guesses.append(guess)

        correct_guesses+=check_answer(qustions.get(key),guess)
        qustions_num += 1
    display_score(correct_guesses,guesses)
#----------------------------

def check_answer(answer,guess):
    if answer==guess:
        print('Correct')
        return 1
    else:
        print('Wrong')
        return 0
#----------------------------

def display_score(correct_guesses,guesses):
    print('----------------------')
    print('Results')
    print('----------------------')
    print('Answers',end=' ')
    for i in qustions:
        print(qustions.get(i),end='')
    print()

    print('Guesses', end=' ')
    for i in guesses:
        print(i, end='')
    print()
    score=int((correct_guesses/len(qustions))*100)
    print('Your score is:'+str(score)+'%')


#----------------------------

def play_again():
    response=input('Do you want to play again? (YES or NO) :').upper()
    if response=='YES':
        return True
    else:
        return False

qustions={'Who created python?':'A',
          "What year python was created?":'B',
          'Python is tributed to which company group?':'C',
          'Is Earth round?':'A'}
options=[['A. Guido van Rossum','B. Elon Musk','C. Bill Gates','D. Mark Zuckerburg'],
         ['A.1989','B.1991','C.2000','D.2002'],
         ['A. Lonely Island','B. Smosh','C. Monty Python', 'D. SNL'],
         ['A.True','B.False','C.Sometime','D.All of the above']]

new_game()

while play_again():
    new_game()

print("BYE BYE")