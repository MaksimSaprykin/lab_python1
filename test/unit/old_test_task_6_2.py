import pytest

from task_6.task_6_1_9 import check_parity, validate_inp


# task6_2

# тест умови
@pytest.mark.parametrize('number, expected_result', [
    (2, 'Number of guys'),
    (10, 'Number of guys'),
    (3, 'The number of nonpartners'),
    (101, 'The number of nonpartners')
])
def test_check_parity(number, expected_result):
    assert check_parity(number) == expected_result


# тест еррор
def test_check_parity_invalid_input():
    with pytest.raises(TypeError):
        check_parity('abc')


# тест на 0
def test_check_parity_zero():
    assert check_parity(0) == 'Number of guys'


@pytest.mark.parametrize('variable_val, incorrect_value, expected_result', [
    (10, 0, 10),  # Коректне значення
    # (10.5, 0, None),  # Некоректне значення
    # (7.2, 0, None),  # Некоректне значення
    (15, 0, 15),  # Коректне значення
    # (8.5, 0, None),  # Некоректне значення
    (16, 0, 16),  # Коректне значення
    # (9.2, 0, None),  # Некоректне значення
    (18, 0, 18),  # Коректне значення
    # (9.2, 0, None)  # Некоректне значення
    (-17, 0, -17)  # Коректне значення
])
def test_validate_inp(variable_val, incorrect_value, expected_result):
    assert validate_inp('var', variable_val, incorrect_value) == expected_result
