# Multi paradigm programming language
# Task 4
# Saprykin Maksym
# zachet_number = 16

from math import *  # Знайти рішення як амінити на 'import math as m'

# но тоді доведеться перед мат.функ. дописувати m.sin

COURSE_NAME = '\'Multi paradigm programming language\''
TASK_NUMBER = 'Task 4'
STUDENT = {'first_name':'Maksym', 'last_name': 'Saprykin', 'zachet_number':'№16'}
STUDENT = {'Maksym', 'Saprykin', 'zachet_number - 16'}
FORMULA = 'sin(x) * x'
step_x = 0.001

print(f'{COURSE_NAME}:{TASK_NUMBER}')
print(STUDENT,'\n')


# ishodna formula
def calculation_expression(x):
    return eval(f'sin({x})*{x}')


# Description Tasks
print('1. Example:')
print('y = ', FORMULA)

# input data

a = float(input('enter the beginning of the segment  [a, b], a ='))
b = float(input('enter the end of the segment   [a, b], B ='))


def f_range(start, stop, step):  # range() на пряму не працює з float, то обходимо наступним чином,
    i = start
    while i < stop:
        yield i  # зробимо генератор
        i += step


min_func = min([calculation_expression(x) for x in f_range(a, b + step_x, step_x)])

print('На відрізку [', a, ', ', b, ']', 'функція ', FORMULA, 'приймає min значення', min_func)
