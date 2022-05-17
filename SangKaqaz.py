import random
# sang kaqaz 
options = ['rock','paper', 'scissor']
scores = {'user':0 , 'computer':0 , 'draw': 0}
for i in range(10):
    computer_choice = random.choice(options)

    user_choice = input('play the game: ')

    if user_choice == 'rock' and computer_choice == 'paper' or user_choice == 'paper' and computer_choice == 'scissor' or user_choice == 'scissor' and computer_choice == 'rock':
        print('computer wins')
        scores['computer'] += 1 

    elif user_choice == 'rock' and computer_choice == 'rock' or user_choice == 'paper' and computer_choice == 'paper' or user_choice == 'scissor' and computer_choice == 'scissor':
        print('draw')
        scores['draw'] += 1

    elif computer_choice == 'rock' and user_choice == 'paper' or computer_choice == 'paper' and user_choice == 'scissor' or computer_choice == 'scissor' and user_choice == 'rock':
        print('you win')
        scores['user'] += 1 

print(scores)