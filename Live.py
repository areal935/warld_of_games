from help_fun import check_valability
import CurrencyRouletteGame
import GuessGame
import memory_game
from utils import MAX_DIFF


def welcome(my_name):
    print(f'Hello {my_name} and welcome to the World of Games (WoG)\
Here you can find many cool games to play.\n')


def load_game():
    game_text = 'Please choose a game to play:\n\
    \t\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n\
    \t\t2. Guess Game - guess a number and see if you chose like the computer\n\
    \t\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'
    diff_text = 'Please choose game difficulty from 1 to 5:\n'
    help_dic = {1: memory_game, 2: GuessGame, 3: CurrencyRouletteGame}
    game = check_valability(game_text, 3)
    diff = check_valability(diff_text, MAX_DIFF)
    return help_dic[game].play(diff, 'ariel')


load_game()
