import io


# Задание 1


def reverse_iter(user_list):
    while True:
        yield from user_list[::-1]


# Задание 2
class MyEnumerate(enumerate):
    def __init__(self, iterable):
        super().__init__()


# Задание 3
result = []


def find_words_ending_with_a(text):
    it_3 = iter(text)

    while True:
        try:
            word = next(it_3)
            if word[-1] == 'а':
                result.append(word)
        except StopIteration:
            break


# Задание 4
def peep(iterator: iter):
    result_list = list(iterator)
    first_el = result_list[0]
    return first_el, iter(result_list)


# Задание 5
def grep(input_word):
    word_to_search = str(input_word)

    while True:
        text = yield
        if word_to_search in text:
            print(text)


# Задание 6
def test_ex(user_text):
    while True:
        add_text = yield

        if add_text is None:
            break

        user_text += str(add_text)
        print(user_text)


# Задание 7
def test_ex_2():
    while True:
        new_text = yield

        if new_text is None:
            break

        with io.open('task_7.txt', 'a', encoding='utf-8') as f:
            f.write(' ')
            f.write(new_text)


# Задание 8
def switchboard():
    while True:
        choice = yield 'Send 1 for concat strings, 2 for writing str in file, 3 for exit'
        if choice == 1:
            yield from test_ex('')
        elif choice == 2:
            yield from test_ex_2()
        elif choice == 3:
            print('Thank you for using our service!')
            return
        else:
            print('Wrong choice! Please try again.')


if __name__ == '__main__':
    # Задание 1
    it = reverse_iter([1, 2, 3, 4])
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

    # Задание 2
    # for index, letter in MyEnumerate('abc'):
    #     print(f'{index}: {letter}')

    # Задание 3
    # with io.open('parse.txt', encoding='utf-8') as f:
    #     list_of_words = f.read().split()
    #     find_words_ending_with_a(list_of_words)
    #     print(result)

    # Задание 4
    # it = iter(range(5))
    # x, it1 = peep(it)
    # print(x, list(it1))

    # Задание 5
    # search = grep('coroutine')
    # next(search)
    # search.send('I love you')
    # search.send('Don\'t you love me?')
    # search.send('I love coroutines instead!')

    # Задание 6
    # g = test_ex('Hleb')
    # next(g)
    # value_1 = g.send(' Xleb')
    # value_2 = g.send(' TMS')

    # Задание 7
    # g = test_ex_2()
    # next(g)
    # g.send('Hleb')
    # g.send('Xleb')
    # g.send('TMS')

    # Задание 8
    # s = switchboard()
    # next(s)
    # s.send(1)
    # s.send('Hleb')
    # s.send(' Xleb')
    # s.send(None)
    # s.send(2)
    # s.send('Xleb')
    # s.send(None)
    # s.send(3)
