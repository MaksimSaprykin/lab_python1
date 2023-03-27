""" Multi paradigm programming language
    Task 2
    Saprykin Maksym
    zachet_number = 16
"""
import utils as ut

TASK_NUMBER = 'Task 2'
TEMPLATE = 'Input {}'


# Description Tasks
def description_task(formula):
    print('1. Solve an example:')
    print(formula, '= ?')


def inp_validate(values):
    while True:
        try:
            return float(input(TEMPLATE.format(values)))
        except ValueError:
            print('Enter not number')


# input data
def inp_data():
    x_i = inp_validate('x')
    y_i = inp_validate('y')
    z_i = inp_validate('z')
    while True:
        try:
            return print_rezult(calculation_expression(x_i, y_i, z_i))
        except ZeroDivisionError:
            print('Input incorrect, divide by 0 cannot be')
            z_i = inp_validate('z')


def calculation_expression(var_x, var_y, var_z):
    return var_x - (var_x + var_y / var_z) / (78 + var_y)


def print_rezult(rezultat):
    print(F, '=', rezultat)


if __name__ == '__main__':
    F = 'x - (x + y/z)/(78 + y)'
    ut.print_info(TASK_NUMBER)
    description_task(F)
    inp_data()
