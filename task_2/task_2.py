
""" Multi paradigm programming language
    Task 2
    Saprykin Maksym
    zachet_number = 16
"""
from ast import literal_eval

COURSE_NAME = '\'Multi paradigm programming language\''
TASK_NUMBER = 'Task 2'
STUDENT = {'Maksym', 'Saprykin', 'zachet_number - 16'}


def print_info():
    print(f'{COURSE_NAME}:{TASK_NUMBER}')
    print(STUDENT, '\n')


def func(formula):
    #f_rezult = literal_eval(formula, {'x': x, 'y': y, 'z': z})

    return literal_eval(formula)


# Description Tasks
def description_task(formula):
    print('1. Solve an example:')
    print(formula, '= ?')


def print_rezult(formula):
    print(F, '=', func(formula))


if __name__ == '__main__':
    F = 'x - (x + y/z)/(78 + y)'
    description_task(F)
    x = float(input('input x:'))
    y = float(input('input x:'))
    z = float(input('input x:'))
    #print_rezult(F)
    c = literal_eval('3+5+67+89')
    print(c)
