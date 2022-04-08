# Задание: создать простой калькулятор с использованием try/except

# Собственное исключение
class WrongOperationException(Exception):
    pass


def add(x, y):
    """Суммирует два числа x и y."""
    return x + y


def subtract(x, y):
    """Вычитает число y из числа x."""
    return x - y


def multiply(x, y):
    """Умножает число x на число y."""
    return x * y


def divide(x, y):
    """Делит число x на число y."""
    try:
        return x / y
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'


def raise_to_a_power(x, y):
    """Возводит число x в степень y."""
    return x ** y


while True:
    try:
        num1 = float(input('\nВведите первое число: '))
        num2 = float(input('Введите второе число: '))

        print('\nДоступные операции:'
              '\n1) Сложение'
              '\n2) Вычитание'
              '\n3) Умножение'
              '\n4) Деление'
              '\n5) Возведение в степень')

        operation_number = int(input('\nКакую операцию выполнить? Укажите номер: '))

        if operation_number < 1 or operation_number > 5:
            raise WrongOperationException
        # Я бы сделал это через else + print без exception-а, но для задания нужно так

        elif operation_number == 1:
            print(f'{num1} + {num2} = {add(num1, num2)}')
        elif operation_number == 2:
            print(f'{num1} - {num2} = {subtract(num1, num2)}')
        elif operation_number == 3:
            print(f'{num1} * {num2} = {multiply(num1, num2)}')
        elif operation_number == 4:
            print(f'{num1} / {num2} = {divide(num1, num2)}')
        else:
            print(f'{num1} ** {num2} = {raise_to_a_power(num1, num2)}')

        next_operation = input('\nЖелаете ещё раз воспользоваться калькулятором? (да/нет): ')
        if next_operation.lower() == 'нет':
            break

    except WrongOperationException:
        print('Проверьте набранный номер. Он должен быть от 1 до 5.')

    except ValueError:
        print('Некорректный ввод данных.')
