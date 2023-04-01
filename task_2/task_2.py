""" Multi paradigm programming language
    Task 2
    Saprykin Maksym
    zachet_number = 16
"""
import utils as ut

TASK_NUMBER = 'Task 2'
TEMPLATE = 'Input {}'


# number check
def inp_variable(values):
    while True:
        try:
            return float(input(TEMPLATE.format(values)))
        except ValueError:
            print('Enter not number')


# check for invalid known numbers
def validate_inp(variable_name, variable_val, incorect_value):
    while variable_val == incorect_value:
        print(f'Input incorrect, {variable_name} != {incorect_value}')
        variable_val = inp_variable(variable_name)
    return variable_val


# input data
def inp_data():
    x_i = inp_variable('x')
    y_i = inp_variable('y')
    y_i = validate_inp('y', y_i, -78)
    z_i = inp_variable('z')
    z_i = validate_inp('z', z_i, 0)
    return ut.print_rezult(F, calculation_expression(x_i, y_i, z_i))


def calculation_expression(var_x, var_y, var_z):
    return var_x - (var_x + var_y / var_z) / (78 + var_y)


if __name__ == '__main__':
    F = 'x - (x + y/z)/(78 + y)'
    ut.print_info(TASK_NUMBER)
    ut.description_task(F)
    inp_data()
