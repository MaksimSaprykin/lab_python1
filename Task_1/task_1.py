# Multi paradigm programming language
# Task 1
# Saprykin Maksym
# zachet_number = 16
# ==============================================================#

# from math import *

COURSE_NAME = '\'Multi paradigm programming language\''
TASK_NUMBER = 'Task 4'
STUDENT = {'Maksym', 'Saprykin', 'zachet_number - 16'}
FIRST_NAME_TEACHER = 'Vladislav'
FORMULA = '7.8-(1+2.1/3)/(78+21.3)'


def print_info():
    print(f'{COURSE_NAME}:{TASK_NUMBER}')
    print(', '.join(STUDENT), '\n')


def try_python_essentials():
    str45 = [FIRST_NAME_TEACHER for _ in range(45)]
    print(','.join(str45))


def f_expression():
    print(f'{FORMULA}={7.8 - (1 + 2.1 / 3) / (78 + 21.3)}')


if __name__ == '__main__':
    print_info()
    try_python_essentials()
    f_expression()
