COURSE_NAME = '\'Multi paradigm programming language\''
STUDENT = {'Maksym', 'Saprykin', 'zachet_number - 16'}


def print_info(tusk_number):
    print(f'{COURSE_NAME}:{tusk_number}')
    print(STUDENT, '\n')


def print_rezult(formula_str, rezultat):
    print(formula_str, '=', rezultat)


# Description Tasks
def description_task(formula):
    print('1. Solve an example:')
    print(formula, '= ?')


# number check
def inp_variable(values, templete_t):
    while True:
        try:
            return float(input(templete_t.format(values)))
        except ValueError:
            print('Enter not number')


