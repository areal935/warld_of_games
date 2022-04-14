def check_valability(text_to_print, number_of_choicies):
    my_choice = input(text_to_print)
    while my_choice not in [str(i) for i in range(1, number_of_choicies + 1)]:
        print('your choice is not valid please try again')
        my_choice = input(f'please enter INTEGER number between 1 and {number_of_choicies}\n')
    return int(my_choice)
