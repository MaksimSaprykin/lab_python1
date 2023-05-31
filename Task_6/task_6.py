import csv
import requests
import re
import sqlite3

from pathlib import Path

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

    with path_read.open(mode="r") as file_read:
        for _ in file_read:
            number = int(_.strip())
            sum_numbers += number

    print('Sum numbers:', sum_numbers)

    with path_save.open(mode="w") as file_save:
        file_save.write(str(sum_numbers))

    print("Sum write to file : sum_numbers.txt.")


def task_6_2():
    file_name3 = 'task_6_2_parity_info.txt'
    number = ut.inp_variable('n', TEMPLATE)
    number = validate_inp('n', number, 0)  # proverka na integer or float
    result = check_parity(number)

    with open(file_name3, 'w') as file:
        file.write(result)

    print(f'Inform add to file  {file_name3}')


def check_parity(number):
    if number % 2 == 0:
        return 'Number of guys'
    else:
        return 'The number of nonpartners'


def validate_inp(variable_name, variable_val, incorect_value):
    while variable_val % 1 != incorect_value:
        print(f'Input incorrect, {variable_name} = {variable_val} is NOT integer')
        variable_val = ut.inp_variable(variable_name, TEMPLATE)
    return variable_val


def task_6_3(file_name4):
    list_lines = []
    with open(file_name4, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
            list_lines.append(line.strip())
    print(list_lines)


def task_6_4(file_name4):
    with open(file_name4, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.replace('Python', 'C'))


def task_6_5(file_name):
    with open(file_name, 'w') as file:
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


def task_6_7(url_book, formatted_book, formatted_old_book):
    text_book = requests.get(url_book).text
    with open(formatted_old_book, 'w', encoding="utf-8") as file:
        file.write(text_book)
    format_text = text_book.replace('\n', ' ')
    with open(formatted_book, 'w', encoding="utf-8") as file:
        file.write(format_text)


def task_6_8(url_book, new_file):
    text_book = requests.get(url_book).text
    chapter_find = r'CHAPTER [IVXLCDM]+\b.*'
    chapters = re.findall(chapter_find, text_book)
    with open(new_file, 'w', encoding="utf-8") as file:
        for match in chapters:
            file.write(f'{match}')
            print(match)


def task_6_9(url_book):
    text_book = requests.get(url_book).text
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


def task_6_10(db_name, data_file): #
    def created_bd(db_name):
        conn = sqlite3.connect(db_name)
        curs = conn.cursor()
        curs.execute('''CREATE TABLE ratings
                                    (id INTEGER PRIMARY KEY, title VARCHAR(20), year INT, rating FLOAT)''')
        conn.commit()
        curs.close()
        conn.close()

    def import_data(data_file):
        conn = sqlite3.connect(db_name)
        curs = conn.cursor()
        data_path = Path(data_file)

        if data_path.is_file():
            print(f'The file {data_file} already exists.')
            with open(data_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Пропускаємо перший рядок (заголовки стовпців)
                for row in reader:
                    curs.execute('INSERT INTO ratings (title, year, rating) VALUES (?, ?, ?)', row)
        else:
            print(f'The data file {data_file} does not exist.')

        conn.commit()
        curs.close()
        conn.close()

    db_path = Path(db_name)

    if db_path.is_file():
        print(f'The file {db_name} already exists.')
    else:
        print(f'The file {db_name} has been created.')
        created_bd(db_name)

    import_data(data_file)


if __name__ == '__main__':
    # task_6_1()
    # task_6_2()
    # task_6_3('learning_python.txt')
    # task_6_4('learning_python.txt')
    # task_6_5('guest_book.txt')
    file_name_book1 = 'Doctor_Hathern.txt'
    file_name_book2 = 'How_we_elected_Lincoln.txt'
    # task_6_6(file_name_book1)
    # task_6_6(file_name_book2)
    url_book = 'https://www.gutenberg.org/cache/epub/70881/pg70881.txt'
    formatted_old_book = 'not_formatted_text.txt'
    formatted_new_book = 'formatted_text.txt'
    # task_6_7(url_book, formatted_new_book, formatted_old_book)
    url_book1 = 'https://www.gutenberg.org/files/521/521-0.txt'
    file_name_headlines = 'chapters.txt'
    # task_6_8(url_book1, file_name_headlines)
    url_book2 = 'https://www.gutenberg.org/files/1184/1184-0.txt'
    # task_6_9(url_book2)
    db_name = 'imdb.db'
    data_file = 'imdb.csv'
    #task_6_10(db_name, data_file)

