# Multi paradigm programming language
# Task 4
# Saprykin Maksym
# zachet_number = 16

import math as m
import utils as ut

TASK_NUMBER = 'Task 4'
FORMULA = 'sin(x) * x'
STEP_X = 0.001


# ishodna formula
def calculation_expression(x):
    return m.sin(x) * x

# input data

a = float(input('enter the beginning of the segment  [a, b], a ='))
b = float(input('enter the end of the segment   [a, b], B ='))


def f_range(start, stop, step):  # range() на пряму не працює з float, то обходимо наступним чином,
    i = start
    while i < stop:
        yield i  # зробимо генератор
        i += step


min_func = min([calculation_expression(x) for x in f_range(a, b + STEP_X, STEP_X)])

print('На відрізку [', a, ', ', b, ']', 'функція ', FORMULA, 'приймає min значення', min_func)

if __name__ == '__main__':
    ut.print_info()
    ut.description_task()

