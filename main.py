""" The Monthy Hall problem

"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2021 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

import random


def shuffle():
    mylist = ["apple", "banana", "cherry"]
    random.shuffle(mylist)
    return mylist


def mh_title():
    print('Monthy Hall paradox')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mh_title()
    print(shuffle())
