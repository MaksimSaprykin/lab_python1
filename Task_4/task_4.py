# Multi paradigm programming language
# Task 4
# Saprykin Maksym
# zachet_number = 16

import math as m
import utils as ut

TASK_NUMBER = 'Task 4'
FORMULA = 'sin(x) * x'
STEP_X = 0.001
TEMPLATE_A = 'enter the beginning of the segment  [a, b], a ='
TEMPLATE_B = 'enter the end of the segment   [a, b], B ='


# ishodna formula
def calculation_expression(x):
    return m.sin(x) * x


# input data
def inp_data():
    a = ut.inp_variable('a', TEMPLATE_A)
    b = ut.inp_variable('b', TEMPLATE_B)
    return a, b


def f_range(start, stop, step):  # range() на пряму не працює з float, то обходимо наступним чином,
    i = start
    while i < stop:
        yield i  # зробимо генератор
        i += step


def min_func_expression(a, b):
    return min([calculation_expression(x) for x in f_range(a, b + STEP_X, STEP_X)])


if __name__ == '__main__':
    ut.print_info(TASK_NUMBER)
    ut.description_task(FORMULA)
    a_b = inp_data()
    print(f'On the segment {a_b}, function {FORMULA} takes the min value = {min_func_expression(a_b[0], a_b[1])}')
