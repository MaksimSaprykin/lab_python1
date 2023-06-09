""" Multi paradigm programming language
    Task 5 : 5.2
    Saprykin Maksym
    zachet_number = 16
"""
import math as m

import utils as ut


# check for invalid known numbers = 0, rezult = 1
def sum_stash_number(my_number):
    if my_number == 0:
        return 1
    return int(m.log(abs(my_number), 10) + 1)


if __name__ == '__main__':
    TASK_NUMBER = 'Task 5.2'
    TEMPLATE = 'Input {} '
    ut.print_info(TASK_NUMBER)
    x = ut.inp_variable('nomber', 'Enter nomber :')
    print(sum_stash_number(x))
