"""Rock-Scissors-Paper"""

import random
import sys

print("\nTo play a move, enter 'rock', 'paper', or 'scissors' (without quotes).\n"
      "To view your score, enter !rating.\n"
      "To quit the game, enter !exit.\n\n")


def rating():
    """your rating"""
    try:
        return points + name_score[user_name]
    except KeyError:
        return points


options = ('rock', 'scissors', 'paper')
user_name = input('Enter your name: ')
print('Hello, {}'.format(user_name))
name_score = {}
f = open('1.txt')
for line in f:
    table = line.split()
    name_score[table[0]] = int(table[1])
points = 0
while True:
    option = random.choice(options)
    user_choice = input()
    if user_choice not in options and user_choice not in ('!exit', '!rating'):
        print('Invalid input')
    elif user_choice == '!rating':
        print('Your rating:', rating())
    elif user_choice == '!exit':
        print('Bye!')
        f.close()
        sys.exit()
    elif user_choice == option:
        points = points + 50
        print('There is a draw ({})'.format(option))
    elif user_choice == options[0] and option == options[2] or \
            user_choice == options[1] and option == options[0] or \
            user_choice == options[2] and option == options[1]:
        print('Sorry, but the computer chose {}'.format(option))
    else:
        points = points + 100
        print('Well done. The computer chose {} and failed'.format(option))
