from random import randint
from help_fun import check_valability
from time import sleep


def generate_sequence(my_difficulty):
    seq_list = []
    for i in range(my_difficulty):
        seq_list.append(randint(1, 101))
    return seq_list


def get_list_from_user(my_difficulty):
    help_dic = {1: 'first', 2: 'second', 3: 'third', 4: 'forth', 5: 'fifth'}
    user_guess = [0 for _ in range(my_difficulty)]
    for i in range(my_difficulty):
        text = f'please enter the {help_dic[i + 1]} number out of {my_difficulty}'
        user_guess[i] = check_valability(text, 101)
    return user_guess


def is_list_equal(my_list, comp_list):
    return my_list == comp_list


def play(my_difficulty, my_name):
    showing_time = 0.7
    print(f'hi {my_name} welcome to memory game here a randomly generated list by the computer')
    print(f'of in integer numbers between 1 and 101 with the length of {my_difficulty} will be flashed on the screen')
    print(f'for {showing_time}sec and then you need to guess it')
    input('are you reddy? press enter to continue')
    random_list = generate_sequence(my_difficulty)
    print(random_list, end='')
    sleep(showing_time)
    print('\b'*100, end='')
    return is_list_equal(get_list_from_user(my_difficulty), random_list)




