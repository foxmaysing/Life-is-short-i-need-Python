# 这是一个猜骰子大小的游戏，骰子个数为3
# 初始资金为1000，默认赔率为1

import random
def roll_dice(numbers = 3, points = None):
    print('<<<<<< ROLL THE DICE >>>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isbig = 11 <= total <= 18
    issmall = 3 <= total <= 10
    if isbig:
        return 'big'
    elif issmall:
        return 'small'

def start_game():
    your_money = 1000
    while your_money > 0:
        print('<<<<<< GAME STARTS ! >>>>>>')
        choices = ['big', 'small']
        your_choice = input('Big or small:')
        if your_choice in choices:
            your_bet = int(input('How much you wanna bet?  ~~~ '))
            points = roll_dice()
            total = sum(points)
            youwin = your_choice == roll_result(total)
            if youwin:
                print('The points are', points, 'You Win!')
                print('You gained {}, you have {} now.'.format(your_bet, your_money + your_bet))
                your_money = your_money + your_bet
            else:
                print('The points are', points, 'You Lose!')
                print('You lost {}, you have {} now.'.format(your_bet, your_money - your_bet))
                your_money = your_money - your_bet
        else:
            print('Invalid Words')
            start_game()
    else:
        print("Game over!")
start_game()
