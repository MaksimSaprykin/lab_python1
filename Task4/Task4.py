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
formula = 'sin(x) * x'
step_x = 0.001

print(course_name + ': ' + task_number)
print(first_name_student + ' ' + last_name + ', ' + zachet_number, '\n')

# ishodna formula
def func ():
    f = eval(formula)
    return f

# Description Tasks
print('1. Example:')
print('y = ', formula)

# input data

a = float(input('enter the beginning of the segment  [a, b], a ='))
b = float(input('enter the end of the segment   [a, b], B ='))

#segment = range((b-a)/step_x, step_x)
#for _ in segment:

    x = a

#    if z == 2:
#        print('Not input z = 2, divide by 0 cannot be')
#    else:
#        break


print('y = ', formula, '=', func())