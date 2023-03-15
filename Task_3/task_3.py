# Multi paradigm programming language
# Task 3
# Saprykin Maksym
# zachet_number = 16

from math import *

COURSE_NAME = '\'Multi paradigm programming language\''
TASK_NUMBER = 'Task 3'
STUDENT = {'Maksym', 'Saprykin', 'zachet_number - 16'}

FORMULA = '(x + 2 * x + 3) / (z - 2) + atan(z)'

print(f'{COURSE_NAME}:{TASK_NUMBER}')
print(STUDENT, '\n')


# ishodna formula
def calculation_expression(x, z):
    return eval(f'({x}+2*{x}+3)/({z}-2)+atan({z})')

# Description Tasks
print('1. Example:')
print('y = ', FORMULA)

# input data

while True:
    z = float(input('input z:'))
    if z != 2:
        break
    print('Not input z = 2, divide by 0 cannot be')

x = float(input('input x:'))

print('y = ', FORMULA, '=', calculation_expression(x, z))
