import math
from task5.task_5_1 import series_sum
from task5.task_5_2 import sum_stash_number
from task5.task_5_3 import validate_number, heron_square_root

import pytest
import utils as ut


# task5_1
# @pytest.mark.parametrize('input_param_n_iter, expected_eps, expected_n_iter', [(0, 10 ** -4, 2),
#                                                                                (1, 10 ** -4, 2),
#                                                                                (2, 10 ** -4, 2),
#                                                                                (11, 10 ** -4, 2)])
# def test_series_sum_good(input_param_n_iter, expected_eps, expected_n_iter):
#     # Отримані значення
#     actual_sum, actual_n_iter = series_sum(input_param_n_iter, expected_eps)
#
#     # Очікувані значення
#     expected_sum = series_sum(input_param_n_iter, expected_eps)[0]
#
#     # Перевірка
#     assert math.isclose(actual_sum, expected_sum, rel_tol=expected_eps)
#     assert actual_n_iter == expected_n_iter

# task5_2
# @pytest.mark.parametrize('input_number, expected_count_number', [(0, 1), (1, 1), (20, 2), (111, 3), (-111.3, 3)])
# def test_sum_stash_number_good(input_number, expected_count_number):
#     # Отримані значення
#     actual_count_number = sum_stash_number(input_number)
#
#     # Перевірка
#     assert actual_count_number == expected_count_number
#
# @pytest.mark.parametrize('input_number, expected_count_number', [('123', TypeError)])
# def test_sum_stash_number_error(input_number, expected_count_number):
#     with pytest.raises(expected_count_number):
#         sum_stash_number(input_number)


# task5_3
# тест для коректних значень
# @pytest.mark.parametrize('input_number, expected_rezult', [(9, 3), (25, 5)])
# def test_heron_square_root_good(input_number, expected_rezult):
#     # Отримані значення
#     actual_rezult = heron_square_root(input_number)
#     # Перевірка
#     assert pytest.approx(actual_rezult, 10 ** -3) == expected_rezult


# тест для негативних значень, на відьємних значеннях підвисає тест
#@pytest.mark.parametrize('input_number', [-9, -25])
#def test_heron_square_root_negative(input_number):
#     with pytest.raises(ValueError):
#         heron_square_root(input_number)

# тест для помилок невалідатних значень ,
# @pytest.mark.parametrize('input_number, expected_rezult', [('123', TypeError), (None, TypeError)])
# def test_heron_square_root_error(input_number, expected_rezult):
#     with pytest.raises(expected_rezult):
#         heron_square_root(input_number)

@pytest.mark.parametrize("number", [0, 1, 10, 100, 0.5])
def test_validate_number_pozitive(number):
    variable_name = "test_variable"

    # Замінюємо ut.inp_variable на функцію-заглушку, що завжди повертає number
    def inp_variable_mock(variable_name, message):
        return number
    ut.inp_variable = inp_variable_mock

    # Викликаємо функцію validate_number
    result = validate_number(variable_name)

    # Перевіряємо, чи результат співпадає з очікуваним значенням
    assert result == number, f"Expected: {number}, Actual: {result}"


@pytest.mark.parametrize("number", [-1, -10, -100, -0.5, -1.5, -10.2, -100.9])
def test_validate_number_invalid(number):
    variable_name = "test_variable"

    # Замінюємо ut.inp_variable на функцію-заглушку, що завжди повертає number
    def inp_variable_mock(variable_name, message):
        return number
    ut.inp_variable = inp_variable_mock

    # Викликаємо функцію validate_number
    result = validate_number(variable_name)

    # Перевіряємо, чи функція повертає None для недопустимих чисел
    assert result is None, f"Expected: None, Actual: {result}"



