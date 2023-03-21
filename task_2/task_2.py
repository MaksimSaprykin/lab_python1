""" Multi paradigm programming language
    Task 2
    Saprykin Maksym
    zachet_number = 16
"""
from string import Template

COURSE_NAME = '\'Multi paradigm programming language\''
TASK_NUMBER = 'Task 2'
STUDENT = {'Maksym', 'Saprykin', 'zachet_number - 16'}
t_input = Template('input ')


def print_info():
    print(f'{COURSE_NAME}:{TASK_NUMBER}')
    print(STUDENT, '\n')


# Description Tasks
def description_task(formula):
    print('1. Solve an example:')
    print(formula, '= ?')


# input data
def inp_data():
    while True:
        try:
            x_i = float(input(f'{t_input.template}: x = '))
            y_i = float(input(f'{t_input.template}: y = '))
            z_i = float(input(f'{t_input.template}: z = '))
        except ValueError:
            print('Enter not number')
            continue
        else:
            try:
                print_rezult(calculation_expression(x_i, y_i, z_i))
            except ZeroDivisionError:
                print('Input incorrect, divide by 0 cannot be')
                continue
            break


def calculation_expression(var_x, var_y, var_z):
    return var_x - (var_x + var_y / var_z) / (78 + var_y)


def print_rezult(rezultat):
    print(F, '=', rezultat)


if __name__ == '__main__':
    F = 'x - (x + y/z)/(78 + y)'
    description_task(F)
    inp_data()
