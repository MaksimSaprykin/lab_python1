""" Multi paradigm programming language
    Task 2
    Saprykin Maksym
    zachet_number = 16
"""

COURSE_NAME = '\'Multi paradigm programming language\''
TASK_NUMBER = 'Task 2'
STUDENT = {'first_name': 'Maksym', 'last_name': 'Saprykin', 'zachet_number': '№16'}
STUDENT = {'Maksym', 'Saprykin', 'zachet_number - 16'}


def print_info():
    print(f'{COURSE_NAME}:{TASK_NUMBER}')
    print(STUDENT, '\n')


def func(formula):
    f_rezult = eval(formula)
    return f_rezult


# Description Tasks
def description_task(formula):
    print('1. Solve an example:')
    print(formula, '= ?')


def print_rezult(formula):
    print(formula, '=', func(formula))


if __name__ == '__main__':
    F = 'x - (x + y/z)/(78 + y)'
    x = float(input('input x:'))
    y = float(input('input x:'))
    z = float(input('input x:'))
    description_task(F)
