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


def extended():
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
            f.close()
            sys.exit()
        elif user_choice == ai:
            points = points + 50
            print('There is a draw ({})'.format(ai))
        else:
            for index, item in enumerate(options):
                for jindex, jitem in enumerate(options):
                    if ai[index] == item[index] and user_choice[jindex] in jitem[jindex] and jindex >= index:
                        points = points + 100
                        print('Well done. The computer chose {} and failed'.format(ai))
                        break
                    break
                else:
                    print('Sorry, but the computer chose {}'.format(ai))
                    break


options_default = ('rock', 'scissors', 'paper')
options_extended = ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
                    'dragon', 'devil', 'lightning', 'gun')

user_name = input('Enter your name: ')
print('Hello, {}'.format(user_name))
user_options = 'rock,gun,lightning,devil,dragon,water,air,sponge,wolf,tree,human,snake,scissors,fire'.split(',')
# user_options = input('Enter your options or leave the line empty for default options: ').split(',')
print(user_options)
print("To play a move, enter item from yous list:\n"
      "-{}\n"
      "To view your score, enter !rating.\n"
      "To quit the game, enter !exit.\n\n".format('\n-'.join(user_options)))
game_options = []
# user options are set in accordance with the list of advanced options
for i in options_extended:
    if i in user_options:
        game_options.append(i)
print(game_options)
print("Okay, let's start")
name_score = {}
f = open('1.txt')
for line in f:
    table = line.split()
    name_score[table[0]] = int(table[1])
if user_options == ['']:
    options = options_default
    default()
else:
    options = game_options
    extended()

# если индекс юзера последний, а индекс компа первый, то юзер победил. Если индекс юзера первый, а компа последний,
# то юзер проиграл. Если индекс юзера n не первый и не последний, а индекс компа не лежит в диапазоне от n до n-7,
# то юзер выиграл
