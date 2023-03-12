# Multi paradigm programming language
# Task 2
# Saprykin Maksym
# zachet_number = 16

course_name = '\'Multi paradigm programming language\''
task_number = 'Task 2'
first_name_student = 'Maksym'
last_name = 'Saprykin'
zachet_number = '16'
formula = 'x - (x + y/z)/(78 + y)'

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
print('input x: and press Enter', '\n'
      'input y: and press Enter', '\n'
      'input z: and press Enter', '\n')
x = float(input())
y = float(input())
z = float(input())

print(formula, '=', func())