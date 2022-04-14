from random import randint
from help_fun import check_valability


def generate_number(my_difficulty):
    return randint(1, my_difficulty)


def get_guess_from_user(my_difficulty):
    return check_valability(f'please chose a number between 1 a and {my_difficulty}', my_difficulty)


def compare_results(my_difficulty):
    return generate_number(my_difficulty) == get_guess_from_user(my_difficulty)


def play(max_difficulty, my_name):
    chosen_difficulty = check_valability(f' hi {my_name} please chose the difficulty of the game '
                                         f'between 1 and {max_difficulty}', max_difficulty)
    return compare_results(chosen_difficulty)



