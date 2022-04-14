import os
from time import sleep
SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 404
MAX_DIFF = 10


clean_screen = lambda: print('\n' * 150)
# def clean_screen():
#     str1 = 'cls' if os.name in ('nt', 'dos') else 'clear'
#     os.system('cls')


print('bla bla')
sleep(2)
# clean_screen()
os.system('cls')
print("\033[H\033[3J", end="")
