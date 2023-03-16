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
print(', '.join(STUDENT), '\n')

str = [first_name_teacher for _ in range(45)]

print(','.join(str))
print(export_formula, '= ', eval(export_formula))
