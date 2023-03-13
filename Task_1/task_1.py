# Multi paradigm programming language
# Task 1
# Saprykin Maksym
# zachet_number = 16
# ==============================================================#

# from math import *

course_name = '\'Introduction to programming\''
task_number = 'Task 1'
first_name_student = 'Maksym'
last_name = 'Saprykin'
zachet_number = '16'
first_name_teacher = 'Vladislav'
export_formula = '7.8-(1+2.1/3)/(78+21.3)'

print(course_name + ': ' + task_number)
print(first_name_student + ' ' + last_name + ', ' + zachet_number)

i = 1
while i < 45:
    i += 1
    str_teacher = (first_name_teacher + ', ') * (i - 1)
else:
    print(str_teacher + first_name_teacher)

val1 = eval(export_formula)
print(export_formula, '= ' , val1)