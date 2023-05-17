""" Multi paradigm programming language
    Task 5 : 5.2
    Saprykin Maksym
    zachet_number = 16
"""
import math as m

import utils as ut

# check for invalid known numbers
def validate_inp(variable_name, incorect_value):
    while True:
        variable_val = ut.inp_variable(variable_name, TEMPLATE)
        if variable_val != incorect_value:
            return variable_val
        print(f'Input incorrect, {variable_name} != {incorect_value}')

def sum_stash_number(my_number):
    return int(m.log(abs(my_number), 10) + 1)


if __name__ == '__main__':
    TASK_NUMBER = 'Task 5.2'
    TEMPLATE = 'Input {} '
    ut.print_info(TASK_NUMBER)
    x = validate_inp('Enter nomber', 0)
    print(sum_stash_number(x))
