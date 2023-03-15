# Multi paradigm programming language
# Task 1
# Saprykin Maksym
# zachet_number = 16
# ==============================================================#

# from math import *

COURSE_NAME = '\'Multi paradigm programming language\''
TASK_NUMBER = 'Task 4'
STUDENT = {'Maksym', 'Saprykin', 'zachet_number - 16'}
first_name_teacher = 'Vladislav'
export_formula = '7.8-(1+2.1/3)/(78+21.3)'

print(f'{COURSE_NAME}:{TASK_NUMBER}')
print(STUDENT, '\n')

str = [first_name_teacher for i in range(45)]

print(','.join(str))

val1 = eval(export_formula)
print(export_formula, '= ' , val1)
