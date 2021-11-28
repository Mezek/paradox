""" The Monthy Hall problem

"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2021 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

import random
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
from iteration_utilities import duplicates


def mh_title():
    print('Monthy Hall paradox')


def shuffled_cards():
    mylist = ["goat", "car", "goat"]
    random.shuffle(mylist)
    return mylist


def winning_tip():
    cards = shuffled_cards()
    choice_index = random.randrange(0, len(cards))
    print(f'cards: {cards}')
    player_choice = cards.pop(choice_index)
    print(f'first choice: {player_choice}')
    print(f'cards: {cards}')
    win = 1
    if len(list(duplicates(cards))) > 0:
        win = 0
        print('Stay win!')
    else:
        print('Switch win!')
    return win


def plot_outcome(num):
    round = [0]
    w_stay = [0]
    w_switch = [0]
    for i in range(num):
        round.append(i+1)
        if winning_tip() == 0:
            w_stay.append(w_stay[-1] + 1)
            w_switch.append((w_switch[-1]))
        else:
            w_stay.append(w_stay[-1])
            w_switch.append((w_switch[-1] + 1))
    fig = plt.figure(figsize=(10, 4))
    ax1 = plt.subplot(111)
    ax1.set_xlabel(f'Round')
    ax1.set_ylabel(f'Wins')
    # ax1.set_xlim(0, num+1)
    # ax1.xaxis.set_ticks(np.arange(0, len(round)+1, 10))
    # plt.xticks(np.arange(len(round)), np.arange(1, len(round) + 1))
    # w_stay[:] = [x / num for x in w_stay]
    ax1.plot(round, w_stay, linestyle='', marker='o', markersize='5', color='red')
    ax1.plot(round, w_switch, linestyle='', marker='o', markersize='5', color='blue')
    ax1.plot(0, 0, linestyle='', marker='o', markersize='5', color='white')

    print(f'\nProbability to win:')
    print(f'- with switching: {w_switch[-1] / num * 100:.2f} %')
    print(f'- with staying  : {w_stay[-1] / num * 100:.2f} %')

    return 0


if __name__ == '__main__':
    mh_title()
    plot_outcome(30)
    plt.show()
