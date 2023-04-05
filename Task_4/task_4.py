# Multi paradigm programming language ...
# Task 4
# Saprykin Maksym
# zachet_number = 16

import math as m

import numpy as np

import utils as ut

TASK_NUMBER = 'Task 4'
FORMULA = 'sin(x) * x'
STEP_X = 0.001
TEMPLATE_A = 'enter the beginning of the segment  [A, B], A ='
TEMPLATE_B = 'enter the end of the segment   [A, B], B ='


def f_range(start, stop, step):  # range() на пряму не працює з float, то обходимо наступним чином,
    i = start
    while i < stop:
        yield i  # зробимо генератор
        i += step


def min_func_expression(a_begin, b_end):
    temp_b = a_begin
    if a_begin > b_end:
        b_end = a_begin
        a_begin = temp_b
    return min([m.sin(x) * x for x in np.arange(a_begin, b_end + STEP_X, STEP_X)])
    #return min(m.sin(x) * x for x in f_range(a_begin, b_end + STEP_X, STEP_X))


if __name__ == '__main__':
    ut.print_info(TASK_NUMBER)
    ut.description_task(FORMULA)

    a = ut.inp_variable('a_begin', TEMPLATE_A)
    b = ut.inp_variable('b_end', TEMPLATE_B)

    print(f'On the segment [{a}:{b}], function {FORMULA} '
          f'takes the min value = {min_func_expression(a, b)}')
