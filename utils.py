from pathlib import Path
import random

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


def create_txt_and_path(address_t):
    # Створюємо об'єкт шляху за вказаною адресою
    path_new = Path(address_t)

    # Переконуємося, що батьківський каталог існує
    path_new.parent.mkdir(parents=True, exist_ok=True)

    # Відкриваємо файл для запису
    numbers = [random.randint(-50, 50) for _ in range(10)]
    path_new = Path(address_t)
    path_new.parent.mkdir(parents=True, exist_ok=True)
    with path_new.open(mode='w', encoding='utf-8') as file_task:
        for n_var in numbers:
            file_task.write(str(n_var) + "\n")

    print('The file was successfully created at:', address_t)
