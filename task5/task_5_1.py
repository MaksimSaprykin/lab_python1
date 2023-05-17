""" Multi paradigm programming language
    Task 5 : 5.1
    Saprykin Maksym
    zachet_number = 16
"""
import math as m

import utils as ut


def series_sum(n_iter, eps):
    a_n_pred = m.exp(n_iter) * (100 ** (-n_iter ** 2))
    sum_a = 0
    while True:
        n_iter += 1
        a_n = m.exp(n_iter) * (100 ** (-n_iter ** 2))
        sum_a += a_n
        if abs(a_n_pred - a_n) <= eps:
            return sum_a, n_iter
        a_n_pred = a_n


if __name__ == '__main__':
    TASK_NUMBER = 'Task 5.1'
    FORMULA = '(e^n) * (100^(-n^2))'
    EPS = 10 ** (-4)
    N = 0
    ut.print_info(TASK_NUMBER)
    ut.description_task(FORMULA)
    x, i = series_sum(N, EPS)
    print(f'Sum sequence {FORMULA}={x}, count iter = {i + 1}')
