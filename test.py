"""test"""
# import random

# options_extended = ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
#                     'dragon', 'devil', 'lightning', 'gun')
# print(len(options_extended))
# print(options_extended[-1])
# user_options = input('Enter your options or leave the line empty for default options: ').split(',')
# print(len(user_options))


# options = ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
#            'dragon', 'devil', 'lightning', 'gun')
#
#
# win = {'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
#        'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
#        'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
#        'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
#        'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
#        'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
#        'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
#        'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
#        'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
#        'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
#        'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
#        'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
#        'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
#        'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
#        'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']}
# while True:
#     ai = random.choice(options)
#     user_choice = input()
#     if ai in win[user_choice]:
#         print('Well done. The computer chose {} and failed'.format(ai))
#     else:
#         print('Sorry, but the computer chose {}'.format(ai))


"""Rock-Scissors-Paper"""

import random
import sys


def rating(all_points):
    """your rating"""
    try:
        return all_points + name_score[user_name]
    except KeyError:
        return all_points


def default():
    """game with default options"""
    points = 0
    while True:
        ai = random.choice(options)
        user_choice = input()
        if user_choice not in options and user_choice not in ('!exit', '!rating'):
            print('Invalid input')
        elif user_choice == '!rating':
            print('Your rating:', rating(points))
        elif user_choice == '!exit':
            print('Bye!')
            f.close()
            sys.exit()
        elif user_choice == ai:
            points = points + 50
            print('There is a draw ({})'.format(ai))
        elif user_choice == options[0] and ai == options[2] or \
                user_choice == options[1] and ai == options[0] or \
                user_choice == options[2] and ai == options[1]:
            print('Sorry, but the computer chose {}'.format(ai))
        else:
            points = points + 100
            print('Well done. The computer chose {} and failed'.format(ai))


def game():
    """game with extended options"""
    points = 0
    while True:
        ai = random.choice(options)
        user_choice = input()
        if user_choice not in options and user_choice not in ('!exit', '!rating'):
            print('Invalid input')
        elif user_choice == '!rating':
            print('Your rating:', rating(points))
        elif user_choice == '!exit':
            print('Bye!')
            if user_name in name_score:
                name_score[user_name] = name_score[user_name] + points
            else:
                name_score[user_name] = points
            f.seek(0)
            for k, v in name_score.items():
                f.write('{} {}\n'.format(k, v))

            f.close()
            sys.exit()
        elif user_choice == ai:
            points = points + 50
            print('There is a draw ({})'.format(ai))
        else:
            if ai in win[user_choice]:
                points = points + 100
                print('Well done. The computer chose {} and failed'.format(ai))
            else:
                print('Sorry, but the computer chose {}'.format(ai))


options_default = ('rock', 'scissors', 'paper')
options_extended = ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
                    'dragon', 'devil', 'lightning', 'gun')
win = {'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
       'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
       'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
       'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
       'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
       'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
       'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
       'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
       'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
       'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
       'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
       'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
       'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
       'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
       'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']}

user_name = input('Enter your name: ').capitalize()
print('Hello, {}!'.format(user_name))
# user_options = 'rock,gun,lightning,devil,dragon,water,air,sponge,wolf,tree,human,snake,scissors,fire'.split(',')
print('Extended options:', ', '.join(options_extended), '\n')
user_options = input("Enter your options from 'Extended options' separated by a space or "
                     "leave the line empty for default options: ").split(' ')
print("To play a move, enter item from yours list:\n"
      "-{}\n"
      "To view your score, enter !rating.\n"
      "To quit the game, enter !exit.\n\n".format('\n-'.join(user_options)))

print("Okay, let's start")
name_score = {}
f = open('rating.txt', 'a+', encoding='utf-8')
f.seek(0)
for line in f:
    table = line.split()
    name_score[table[0]] = int(table[1])
print(name_score)
if user_options == ['']:
    options = options_default
else:
    options = user_options
game()
