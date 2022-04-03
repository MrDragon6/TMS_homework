# Задание 1-1: ингредиенты бургера

# В этом задании предполагается отдельный декоратор для каждого ингредиента?
# Я понял так.

def print_burger_ingredient_tomato(func):

    def wrapper():
        print('помидоры')
        func()

    return wrapper


def print_burger_ingredient_bun(func):

    def wrapper():
        print('булка')
        func()

    return wrapper


def print_burger_ingredient_salad(func):

    def wrapper():
        print('салат')
        func()

    return wrapper


@print_burger_ingredient_tomato
@print_burger_ingredient_bun
@print_burger_ingredient_salad
def print_burger_main_ingredient():
    print('котлета')


# Задание 1-2: декоратор для вывода названия декорируемой функции + её аргументов

import inspect


def function_info(func):

    def wrapper(*args):
        func(*args)
        print(func)
        print(inspect.signature(func))

    return wrapper


@function_info
def sum_numbers(a, b):
    return int(a) + int(b)


# Задание 1-3: декоратор с обратным отсчётом

import time


def countdown(sec: int):

    def inner(func):

        def wrapper():
            nonlocal sec

            while sec:
                mins, secs = divmod(sec, 60)
                time_format = '{:02}:{:02}'.format(mins, secs)
                print(time_format)
                time.sleep(1)
                sec -= 1

            func()

        return wrapper
    return inner


@countdown(5)
def simple_function():
    print('Я просто функция')


# Задание 2-1: округление дробных чисел в списке
# Мне не оч нравится, как round округляет, но для этого задания сойдёт

values = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]


def rounding():
    round_values = list(map(lambda x: round(x), values))
    print(round_values)


# Задание 2-2: отфильтровать числа больше 80

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]


def filter_scores_above_80():
    scores_above_80 = list(filter(lambda x: x > 80, scores))
    print(scores_above_80)


# Задание 2-3: поиск палиндромов в списке

values_2 = ["demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP"]


def find_palindrome():
    palindrome_list = list(filter(lambda x: x == x[::-1], values_2))
    print(palindrome_list)


# Задание 2-4: произведение чисел списка

from functools import reduce

values_3 = [1, 2, 3, 4]


def multiply_num_in_list():
    result = int(reduce(lambda x, y: x * y, values_3))
    print(result)


# Задание 2-5: найти наибольшее число в списке

values_4 = [3, 5, 2, 4, 7, 1]


def find_biggest_number_in_list():
    biggest_number = int(reduce(lambda x, y: x if x > y else y, values_4))
    print(biggest_number)


# Задание 2-6: посчитать количество слов "капитан"

sentences = ['капитан джек воробей', 'капитан дальнего плавания', 'ваша лодка готова, капитан']


def captain_count_in_list():
    captain_count = int(reduce(lambda x, y: x+1 if 'капитан' in y else x, sentences, 0))
    print(captain_count)


if __name__ == '__main__':
    captain_count_in_list()


