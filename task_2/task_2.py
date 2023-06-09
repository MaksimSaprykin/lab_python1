""" Multi paradigm programming language
    Task 2
    Saprykin Maksym
    zachet_number = 16
"""
import utils as ut

TASK_NUMBER = 'Task 2'
TEMPLATE = 'Input {} = '


# check for invalid known numbers
def validate_inp(variable_name, incorect_value):
    while True:
        variable_val = ut.inp_variable(variable_name, TEMPLATE)
        if variable_val != incorect_value:
            return variable_val
        print(f'Input incorrect, {variable_name} != {incorect_value}')


# input data
def inp_data():
    x_i = ut.inp_variable('x', TEMPLATE)
    y_i = validate_inp('y', -78)
    z_i = validate_inp('z', 0)
    return ut.print_rezult(F, calculation_expression(x_i, y_i, z_i))


def calculation_expression(var_x, var_y, var_z):
    return var_x - (var_x + var_y / var_z) / (78 + var_y)


if __name__ == '__main__':
    F = 'x - (x + y/z)/(78 + y)'
    ut.print_info(TASK_NUMBER)
    ut.description_task(F)
    inp_data()
