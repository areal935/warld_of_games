from help_fun import check_valability
import random as rd
import requests
import numpy as np


def get_money_interval(my_dificalty):
    response = requests.get('https://v6.exchangerate-api.com/v6/f41286ee1165d94e93203895/latest/USD')
    rate = response.json()['conversion_rates']['ILS']
    comp_choice = rd.uniform(1, 100)
    #nonlocal value
    value = int(rate * comp_choice)
    step = 5 - my_dificalty
    interval = range(value - step, value + step)
    # interval = np.arange(rate * comp_choice - step, rate * comp_choice + step, 0.01)
    # print(interval)
    # print(round(rate * comp_choice, 2) in round(interval, 2))
    return interval


def get_guess_from_user():
    return check_valability(f'please your guess in nis for a number of 1$-100$', 400)


def play(my_dificalty, my_name):
    print(f'hi {my_name} welcome to currency roulette game hire you need to guess the shakell equivalent of random  '
          f'number  in $ between 1 and 100')
    interval = get_money_interval(my_dificalty)
    return get_guess_from_user() in interval




