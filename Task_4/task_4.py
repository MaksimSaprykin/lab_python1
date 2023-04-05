# Multi paradigm programming language
# Task 4
# Saprykin Maksym
# zachet_number = 16

import math as m
import utils as ut
import numpy as np

TASK_NUMBER = 'Task 4'
FORMULA = 'sin(x) * x'
STEP_X = 0.001
TEMPLATE_A = 'enter the beginning of the segment  [a, b], a ='
TEMPLATE_B = 'enter the end of the segment   [a, b], B ='


def f_range(start, stop, step):  # range() на пряму не працює з float, то обходимо наступним чином,
    i = start
    while i < stop:
        yield i  # зробимо генератор
        i += step


def min_func_expression(a, b):
    temp_b = a
    if a > b:
        b = a
        a = temp_b
    return min([m.sin(x) * x for x in np.arange(a, b + STEP_X, STEP_X)])


if __name__ == '__main__':
    ut.print_info(TASK_NUMBER)
    ut.description_task(FORMULA)

    a = ut.inp_variable('a', TEMPLATE_A)
    b = ut.inp_variable('b', TEMPLATE_B)

    print(f'On the segment [{a}:{b}], function {FORMULA} takes the min value = {min_func_expression(a, b)}')