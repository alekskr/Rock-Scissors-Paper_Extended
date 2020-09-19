"""Rock-Scissors-Paper"""

import random
import sys

print("\nTo play a move, enter 'rock', 'paper', or 'scissors' (without quotes).\n"
      "To view your score, enter !rating.\n"
      "To quit the game, enter !exit.\n\n")


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
        option = random.choice(options)
        user_choice = input()
        if user_choice not in options and user_choice not in ('!exit', '!rating'):
            print('Invalid input')
        elif user_choice == '!rating':
            print('Your rating:', rating(points))
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
                # if user_choice == options[-1] and option == options[0]:
                #     points = points + 100
                #     print('Well done. The computer chose {} and failed'.format(option))
                #     break
                # elif user_options != '' and user_choice not in (options[0], options[-1]) and \
                #         option not in range(index, index - 8):
                if len(user_options) != 1 and ai not in range(index, index - 8):
                    points = points + 100
                    print('Well done. The computer chose {} and failed'.format(ai))
                    break
                else:
                    print('Sorry, but the computer chose {}'.format(ai))
                    break


options_default = ('rock', 'scissors', 'paper')
options_extended = ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
                    'dragon', 'devil', 'lightning', 'gun')

user_name = input('Enter your name: ')
print('Hello, {}'.format(user_name))
user_options = input('Enter your options or leave the line empty for default options: ').split(',')
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
    options = options_extended
    extended()

# если индекс юзера последний, а индекс компа первый, то юзер победил. Если индекс юзера первый, а компа последний,
# то юзер проиграл. Если индекс юзера n не первый и не последний, а индекс компа не лежит в диапазоне от n до n-7,
# то юзер выиграл
