""" Multi paradigm programming language
    Task 3
    Saprykin Maksym
    zachet_number = 16
"""
import math as m
import utils as ut

TASK_NUMBER = 'Task 3'
TEMPLATE = 'input {} = '


# ishodna formula
def calculation_expression(var_x, var_z):
    return (var_x + 2 * var_x + 3) / (var_z - 2) + m.atan(var_z)


# check for invalid known numbers
def validate_inp(variable_name, variable_val, incorect_value):
    while variable_val == incorect_value:
        print(f'Input incorrect, {variable_name} != {incorect_value}')
        variable_val = ut.inp_variable(variable_name, TEMPLATE)
    return variable_val


# input data
def inp_data():
    x_i = ut.inp_variable('x', TEMPLATE)
    z_i = ut.inp_variable('z', TEMPLATE)
    z_i = validate_inp('z', z_i, 2)
    return ut.print_rezult(F, calculation_expression(x_i, z_i))


if __name__ == '__main__':
    F = '(x + 2 * x + 3) / (z - 2) + ctag(z)'
    ut.print_info(TASK_NUMBER)
    ut.description_task(F)
    inp_data()
