""" Multi paradigm programming language
    Task 3
    Saprykin Maksym
    zachet_number = 16
"""
from string import Template
import math as m
import utils as ut

TASK_NUMBER = 'Task 3'
TEMPLATE = 'input {} = '


# ishodna formula
def calculation_expression(var_x, var_z):
    return (var_x + 2 * var_x + 3) / (var_z - 2) + m.atan(var_z)


# input data
def inp_validate(values):
    while True:
        try:
            return float(input(TEMPLATE.format(values)))
        except ValueError:
            print('Enter not number')


# input data
def inp_data():
    x_i = inp_validate('x')
    z_i = inp_validate('z')
    while z_i == 2:
        print('Input incorrect, divide by 0 cannot be')
        z_i = inp_validate('z')
    return ut.print_rezult(F, calculation_expression(x_i, z_i))

#    while True:
#        try:
#            return print_rezult(calculation_expression(x_i, z_i))
#        except ZeroDivisionError:
#            print('Input incorrect, divide by 0 cannot be')
#            z_i = inp_validate('z')


#def print_rezult(rezultat):
#    print(F, '=', rezultat)


if __name__ == '__main__':
    F = '(x + 2 * x + 3) / (z - 2) + ctag(z)'
    ut.print_info(TASK_NUMBER)
    ut.description_task(F)
    inp_data()
