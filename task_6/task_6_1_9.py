import re
from pathlib import Path
import requests

import utils as ut

TEMPLATE = 'Enter an integer {} = '


def task_6_1():
    file_name1 = 'numbers.txt'
    file_name2 = 'sum_numbers.txt'
    address_create = r'c:\test_txt\\' + file_name1
    address_read = address_create
    address_save = r'c:\test_txt\\' + file_name2
    path_read = Path(address_read)
    path_save = Path(address_save)

    if not path_read.is_file():
        ut.create_txt_and_path(address_create)
        print(f'The file {file_name1} has been created.')

    sum_numbers: int = 0

    with path_read.open(mode='r', encoding='utf-8') as file_read:
        for char in file_read:
            number = int(char.strip())
            sum_numbers += number

    print('Sum numbers:', sum_numbers)

    with path_save.open(mode='w', encoding='utf-8') as file_save:
        file_save.write(str(sum_numbers))

    print('Sum write to file : sum_numbers.txt.')


def task_6_2():
    file_name3 = 'task_6_2_parity_info.txt'
    number = ut.inp_variable('n', TEMPLATE)
    number = validate_inp('n', number, 0)  # proverka na integer or float
    result = check_parity(number)

    with open(file_name3, 'w', encoding='utf-8') as file:
        file.write(result)

    print(f'Inform add to file  {file_name3}')


def check_parity(number):
    if number % 2 == 0:
        return 'Number of guys'
    return 'The number of nonpartners'


def validate_inp(variable_name, variable_val, incorect_value):
    while variable_val % 1 != incorect_value:
        print(f'Input incorrect, {variable_name} = {variable_val} is NOT integer')
        variable_val = ut.inp_variable(variable_name, TEMPLATE)
    return variable_val


def task_6_3(file_name4):
    list_lines = []
    with open(file_name4, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
            list_lines.append(line.strip())
    print(list_lines)


def task_6_4(file_name4):
    with open(file_name4, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            print(line.replace('Python', 'C'))


def task_6_5(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        while True:
            name = input('Enter "Name" or Enter "Exit" for Output: ')
            if name == 'Exit':
                break
            text = f'Hello {name}\n'
            print(text)
            file.write(text)


def task_6_6(file_name):
    sum_count: int = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            count = line.lower().count('the')
            sum_count += count
    print(f'Count "the" in the book {file_name} = {sum_count}')


def task_6_7(url_book_t, formatted_book, formatted_old_book_t):
    text_book = requests.get(url_book_t, timeout=10).text
    with open(formatted_old_book_t, 'w', encoding='utf-8') as file:
        file.write(text_book)
    format_text = text_book.replace('\n', ' ')
    with open(formatted_book, 'w', encoding='utf-8') as file:
        file.write(format_text)


def task_6_8(url_book_t, new_file):
    text_book = requests.get(url_book_t, timeout=10).text
    chapter_find = r'CHAPTER [IVXLCDM]+\b.*'
    chapters = re.findall(chapter_find, text_book)
    with open(new_file, 'w', encoding='utf-8') as file:
        for match in chapters:
            file.write(f'{match}')
            print(match)


def task_6_9(url_book_t):
    text_book = requests.get(url_book_t, timeout=10).text
    big_char_count: int = 0
    small_char_count: int = 0
    for char in text_book:
        if char.isalpha():
            if char.isupper():
                big_char_count += 1
            elif char.islower():
                small_char_count += 1
    big_char_percent = 100 * big_char_count / len(text_book)
    smal_char_percent = 100 * small_char_count / len(text_book)
    print(f'The big char to text   : {big_char_percent:^6.2f}%')
    print(f'The small char to text : {smal_char_percent:^6.2f}%')


if __name__ == '__main__':
    # task_6_1()
    # task_6_2()
    # task_6_3('learning_python.txt')
    # task_6_4('learning_python.txt')
    # task_6_5('guest_book.txt')
    FILE_NAME_BOOK1 = 'Doctor_Hathern.txt'
    FILE_NAME_BOOK2 = 'How_we_elected_Lincoln.txt'
    # task_6_6(FILE_NAME_BOOK1)
    # task_6_6(FILE_NAME_BOOK2)
    URL_BOOK = 'https://www.gutenberg.org/cache/epub/70881/pg70881.txt'
    FORMATTED_OLD_BOOK = 'not_formatted_text.txt'
    FORMATTED_NEW_BOOK = 'formatted_text.txt'
    # task_6_7(URL_BOOK, FORMATTED_NEW_BOOK, FORMATTED_OLD_BOOK)
    URL_BOOK1 = 'https://www.gutenberg.org/files/521/521-0.txt'
    FILE_NAME_CHAPTERS = 'chapters.txt'
    # task_6_8(URL_BOOK1, FILE_NAME_CHAPTERS)
    URL_BOOK2 = 'https://www.gutenberg.org/files/1184/1184-0.txt'
    # task_6_9(URL_BOOK2)
