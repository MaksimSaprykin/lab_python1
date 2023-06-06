import sqlite3
import csv


def create_database():
    try:
        # Підключення до бази даних
        conn = sqlite3.connect('imdb.db')
        curs = conn.cursor()

        # Створення таблиці ratings
        curs.execute('''CREATE TABLE IF NOT EXISTS ratings
                     (id INTEGER PRIMARY KEY,
                      title VARCHAR(100) COLLATE NOCASE UNIQUE,
                      year INT,
                      rating FLOAT)''')

        conn.commit()
        print('База даних створена')

    except sqlite3.Error as error:
        print('Помилка при створенні бази даних:', error)
    finally:
        if conn:
            conn.close()
            print('З\'єднання з базою даних закрите')


def import_data(sql_data):
    try:
        # Підключення до бази даних
        conn = sqlite3.connect('imdb.db')
        curs = conn.cursor()

        # Імпорт даних з файлу imdb.csv
        with open('imdb.csv', 'r', encoding='utf-8') as file:
            csv_data = csv.reader(file)
            next(csv_data)  # Пропустити заголовок
            for row in csv_data:
                title = row[0]
                year = int(row[1])
                rating = float(row[2])
                curs.execute(sql_data, (title, year, rating))

            conn.commit()
            print('Дані успішно імпортовано')

    except sqlite3.Error as error:
        print('Помилка при імпорті даних до бази даних:', error)
    finally:
        if conn:
            conn.close()
            print('З\'єднання з базою даних закрите')


def query_sql(sql_data):
    try:
        # Підключення до бази даних
        conn = sqlite3.connect('imdb.db')
        curs = conn.cursor()

        # Зчитування та виведення на екран результатів SQL-запиту
        curs.execute(sql_data)
        rows = curs.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as error:
        print('Помилка при виконанні SQL-запиту:', error)
    finally:
        if conn:
            conn.close()
            print('З\'єднання з базою даних закрите')


if __name__ == '__main__':
    # створені запити SQL
    # pylint: disable=invalid-name
    sql_sort_az = '''SELECT * FROM ratings ORDER BY title'''
    sql_sort_8_7 = '''SELECT * FROM ratings WHERE rating >= 8.70'''
    sql_import = '''INSERT OR IGNORE INTO ratings (title, year, rating) VALUES (?, ?, ?)'''

    # Виклик функцій для створення бази даних, імпорту даних та виведення результатів
    create_database()
    import_data(sql_import)

    print('Усі значення таблиці ratings у алфавітному порядку за полем title:')
    query_sql(sql_sort_az)

    print('Записи таблиці ratings з рейтингом більшим за 8.70:')
    query_sql(sql_sort_8_7)
