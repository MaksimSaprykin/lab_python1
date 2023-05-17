""" Multi paradigm programming language
    Task 5 : 5.3
    Saprykin Maksym
    zachet_number = 16
"""
import utils as ut


def validate_number(variable_name):
    while True:
        try:
            number_0 = ut.inp_variable(variable_name, 'Enter a positive number: ')
            if number_0 >= 0:
                return number_0
            print('The number must be positive.')
        except ValueError:
            print("Incorrect input. The number should be >= 0")


def heron_square_root(n_var):
    guess = n_var / 2  # Початкове наближення
    epsilon = 1e-4  # Точність
    while abs(guess * guess - n_var) > epsilon:
        guess = (guess + n_var / guess) / 2  # Обчислення наступного наближення
    return guess


# Приклад використання:
if __name__ == '__main__':
    TASK_NUMBER = 'Task 5.3'
    TEMPLATE = 'Input {} '
    ut.print_info(TASK_NUMBER)

    number = validate_number('a')
    result = heron_square_root(number)
    print("Квадратний корінь:", result)
