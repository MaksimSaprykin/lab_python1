# Multi paradigm programming language
# Task 4
# Saprykin Maksym
# zachet_number = 16

from math import *

course_name = '\'Multi paradigm programming language\''
task_number = 'Task 4'
first_name_student = 'Maksym'
last_name = 'Saprykin'
zachet_number = '16'

FORMULA = 'sin(x) * x'
step_x = 0.001

print(course_name + ': ' + task_number)
print(first_name_student + ' ' + last_name + ', ' + zachet_number, '\n')

# ishodna formula
def func(p):
    return eval(f'sin({p})*{p}')

# Description Tasks
print('1. Example:')
print('y = ', FORMULA)

# input data

a = float(input('enter the beginning of the segment  [a, b], a ='))
b = float(input('enter the end of the segment   [a, b], B ='))


def f_range (start, stop, step): # range() на пряму не працює з float, то обходимо наступним чином,
        i = start
        while i < stop:
            yield i             # зробимо генератор
            i += step


min_func = min([func(x) for x in f_range(a, b+step_x, step_x)])

#for i in f_range(a, b+step_x, step_x):
#    x = i
#    if i == a :
#        head_min_func = func()
#    min_func = func()
#    if head_min_func > min_func :
#        head_min_func = min_func

print('На відрізку [', a, ', ', b, ']', 'функція ', FORMULA, 'приймає min значення', min_func)
