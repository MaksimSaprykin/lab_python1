""" Multi paradigm programming language
    Task 3
    Saprykin Maksym
    zachet_number = 16
"""
from string import Template
import math as m

COURSE_NAME = '\'Multi paradigm programming language\''
TASK_NUMBER = 'Task 3'
STUDENT = {'Maksym', 'Saprykin', 'zachet_number - 16'}
t_input = Template('input ')


def print_info():
    print(f'{COURSE_NAME}:{TASK_NUMBER}')
    print(STUDENT, '\n')


# Description Tasks
def description_task(formula):
    print('1. Solve an example:')
    print(formula, '= ?')


# ishodna formula
def calculation_expression(var_x, var_z):
    return (var_x + 2 * var_x + 3) / (var_z - 2) + m.atan(var_z)


# input data
def inp_data():
    while True:
        try:
            x_i = float(input(f'{t_input.template}: x = '))
            z_i = float(input(f'{t_input.template}: z = '))
        except ValueError:
            print('Enter not number')
            continue
        else:
            try:
                print_rezult(calculation_expression(x_i, z_i))
            except ZeroDivisionError:
                print('Input incorrect, divide by 0 cannot be')
                continue
            break


def print_rezult(rezultat):
    print(F, '=', rezultat)


if __name__ == '__main__':
    F = '(x + 2 * x + 3) / (z - 2) + ctag(z)'
    print_info()
    description_task(F)
    inp_data()
