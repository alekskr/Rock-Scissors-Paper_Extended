"""test"""
import random

# options_extended = ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
#                     'dragon', 'devil', 'lightning', 'gun')
# print(len(options_extended))
# print(options_extended[-1])
# user_options = input('Enter your options or leave the line empty for default options: ').split(',')
# print(len(user_options))


options = ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
           'dragon', 'devil', 'lightning', 'gun')


win = {'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
       'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']}
       # 'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
       # 'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
       # 'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
       # 'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
       # 'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
       # 'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
       # 'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
       # 'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
       # 'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
       # 'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
       # 'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
       # 'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
       # 'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']}
while True:
    # ai = random.choice(options)
    ai = 'wolf'
    user_choice = input()
    for k, v in win.items():
        print(k, v)
        if user_choice == k and ai in v:
            print('Well done. The computer chose {} and failed'.format(ai))
        else:
            print('Sorry, but the computer chose {}'.format(ai))
        #     break
        # break
