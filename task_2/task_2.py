""" Multi paradigm programming language
    Task 2
    Saprykin Maksym
    zachet_number = 16
"""
import utils as ut

TASK_NUMBER = 'Task 2'
TEMPLATE = 'Input {}'


# Description Tasks
# def description_task(formula):
#    print('1. Solve an example:')
#    print(formula, '= ?')


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
    while y_i == -78 or z_i == 0:
        if y_i == -78:
            print('Input incorrect, y_i NOT = -78')
            y_i = inp_validate('y')
        if z_i == 0:
            print('Input incorrect, z != 0')
            z_i = inp_validate('z')
    return ut.print_rezult(F, calculation_expression(x_i, y_i, z_i))


#    while True:
#        try:
#            return print_rezult(calculation_expression(x_i, y_i, z_i))
#        except ZeroDivisionError:
#            print('Input incorrect, divide by 0 cannot be')
#            z_i = inp_validate('z')


def calculation_expression(var_x, var_y, var_z):
    return var_x - (var_x + var_y / var_z) / (78 + var_y)


# def print_rezult(rezultat):
#    print(F, '=', rezultat)


if __name__ == '__main__':
    F = 'x - (x + y/z)/(78 + y)'
    ut.print_info(TASK_NUMBER)
    ut.description_task(F)
    inp_data()
