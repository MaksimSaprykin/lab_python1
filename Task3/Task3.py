# Multi paradigm programming language
# Task 3
# Saprykin Maksym
# zachet_number = 16

from math import *

course_name = '\'Multi paradigm programming language\''
task_number = 'Task 3'
first_name_student = 'Maksym'
last_name = 'Saprykin'
zachet_number = '16'
formula = '(x + 2 * x + 3) / (z - 2) + atan(z)'

print(course_name + ': ' + task_number)
print(first_name_student + ' ' + last_name + ', ' + zachet_number, '\n')

# ishodna formula
def func ():
    f = eval(formula)
    return f

# Description Tasks
print('1. Solve an example:')
print(formula, '= ?')

# input data

while True:
    z = float(input('input z:'))
    if z == 2:
        print('Not input z = 2, divide by 0 cannot be')
    else:
        break
x = float(input('input x:'))

print('y = ', formula, '=', func())