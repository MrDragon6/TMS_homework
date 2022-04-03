names_list = ['Sergey', 'Alexandr', 'Anton']


def check_upper(func):
    """Проверяет работу функции upper_names:
    Проходит по всем буквам имён в списке и смотрит, являются ли они заглавными.
    """

    def wrapper():
        print('До работы функции все буквы списка заглавные: {}'.format(str(names_list).isupper()))
        func()
        print('После работы функции все буквы списка заглавные: {}'.format(str(names_list).isupper()))

    return wrapper


@check_upper
def upper_names():
    """"Заменяет все буквы в именах из списка на заглавные."""

    global names_list
    names_list = list(map(lambda name: name.upper(), names_list))
    print(names_list)


if __name__ == '__main__':
    upper_names()
