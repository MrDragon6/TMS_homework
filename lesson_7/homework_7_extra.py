class Engine:
    """
    Имитирует работу двигателя.
    Принимает в себя 3 аргумента: тип двигателя, к-во лошадиных сил и наличие турбины.

    Тип двигателя (engine_type) может быть v6, v8 или v10
    (коэффициенты ускорения соответственно 0.2, 0.4 и 0.6)

    К-во лошадиных сил (horsepower) - любое положительное целочисленное значение.

    Наличие турбины (turbine) - значение типа bool: True или False
    """

    def __init__(self, engine_type: str, horsepower: int, turbine: bool):
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.turbine = turbine
        self.power = 0

        if engine_type == 'v6':
            self.acceleration_factor = 0.2
        elif engine_type == 'v8':
            self.acceleration_factor = 0.4
        elif engine_type == 'v10':
            self.acceleration_factor = 0.6
        else:
            print('Ошибка! Проверьте введённый тип двигателя!')
            exit()

        # Здесь и далее использую такую конструкцию вместо raise Exception,
        # чтобы текст ошибки был короче и приятнее без всех этих красных ругательств.

        if turbine:
            self.turbine_factor = 0.8
        else:
            self.turbine_factor = 1.0

        if horsepower < 0:
            print('Ошибка! Количество лошадиных сил должно быть положительным значением!')
            exit()

    def generate_power(self):
        self.power = self.horsepower * self.acceleration_factor / self.turbine_factor
        return self.power


class Wheel:
    """
    Имитирует колесо для машины.

    Принимает 2 аргумента:
    1) Диаметр колеса (diameter) - значение типа float от 16 до 21 дюймов
    2) Вес колеса (wheel_weight) в кг, тип float
    """

    def __init__(self, diameter: float, wheel_weight: float):
        self.diameter = diameter  # Зачем нам диаметр колеса, если он ни на что не влияет?
        self.wheel_weight = wheel_weight

        if self.diameter < 16 or self.diameter > 21:
            print('Ошибка! Диаметр колеса должен быть от 16 до 21 дюйма!')
            exit()


class Car(Engine, Wheel):
    """
    Имитирует машину.

    Принимает в себя классы Engine и Wheel со всеми аргументами,
    а также аргументы car_type, отвечающий за тип машины (легковая, грузовая, джип),
    и wheel_number, отвечающий за количество колёс (не меньше 4).

    """

    def __init__(self, car_type: str, wheel_number: int, engine_type: str, horsepower: int,
                 turbine: bool, diameter: float, wheel_weight: float):
        Engine.__init__(self, engine_type, horsepower, turbine)
        Wheel.__init__(self, diameter, wheel_weight)
        self.car_type = car_type
        self.wheel_number = wheel_number
        self.engine_started = False
        self.distance = None
        self.time = None

        wheels = []  # Действительно ли нам нужен массив для колёс?

        if wheel_number < 4:
            print('Ошибка! Вы уверены в количестве колёс машины?')
            exit()

        for wheel in range(1, wheel_number + 1):
            wheels.append(wheel)

        if car_type == 'passenger car':
            self.car_weight = 1200
        elif car_type == 'truck':
            self.car_weight = 1800
        elif car_type == 'jeep':
            self.car_weight = 1500
        else:
            print('Ошибка! Укажите корректный тип машины!')
            exit()

    def start_engine(self):
        """Заводит мотор машины."""

        self.engine_started = True

    def move(self, distance: int):
        """
        Рассчитывает время в секундах, за которое машина проедет расстояние,
        заданное пользователем в метрах в аргументе distance.
        Рекомендуется указывать значение distance в районе 5-10 м.
        """
        # Правда, к реальности это никакого отношения не имеет...
        # Например, джип 300 л.с. с турбиной проезжает 1 км за 100 минут.

        self.distance = distance  # Лучше вводить небольшое значение на уровне 5-10 м.

        if self.engine_started:
            self.generate_power()
            self.time = (self.car_weight + self.wheel_weight * self.wheel_number) / self.power * distance
            return self.time
        else:
            print('Ошибка! Двигатель машины не заведён!')
            exit()


# Начало гоночной игры
def racing_game():
    """Запускает консольную гоночную игру."""

    car_list = []  # Пустой список для рандомных машин

    def create_random_cars():
        """Создаёт список рандомных машин."""

        import random

        # Для интереса решил давать игрокам готовые наборы машин с рандомными характеристиками.
        # Если давать выбирать каждый атрибут, будет слишком скучно.
        # Например, количество лошадиных сил ничем не ограничено + игроки будут брать лучший двигатель.
        # А так интерес в том, чтобы прикинуть в уме, какая машина из предложенных будет быстрее.

        car_list.clear()  # Очищаем лист для заездов-реваншей.

        for car in range(0, 5):  # Заполняем список car_list рандомными машинами
            Car.car_type = random.choice(['passenger car', 'jeep', 'truck'])
            Car.wheel_number = random.randrange(4, 9, 2)
            Car.engine_type = random.choice(['v6', 'v8', 'v10'])
            Car.horsepower = random.randrange(400, 801)
            Car.turbine = bool(random.randrange(0, 2))
            Car.diameter = random.randrange(16, 22)
            Car.wheel_weight = random.randrange(8, 21)

            car_list.append(Car(Car.car_type, Car.wheel_number, Car.engine_type, Car.horsepower,
                                Car.turbine, Car.diameter, Car.wheel_weight))

    def create_players():
        """Приминает имена игроков и создаёт из них список."""

        num_of_players = int(input('\nНачнём игру! \nУкажите количество игроков (2-5): '))

        if num_of_players not in range(2, 6):
            print('Ошибка! Игроков может быть только от 2 до 5!')
            exit()

        player_list = []  # Список с именами игроков

        for player in range(num_of_players):
            while True:
                name = input(f'Введите имя игрока №{player+1}: ')

                if name in player_list:
                    print('\nИмя уже занято!')
                else:
                    player_list.append(name)
                    break

        create_track(player_list)

    def create_track(player_list):
        """Создаёт трассу для гонок длиной, заданной пользователем"""

        track_length = int(input('Какой длины трасса (рекомендуется в районе 5-10)? '))

        if track_length < 0:
            print('Ошибка! Трасса не может быть отрицательной длины.')
            exit()

        choose_car(player_list, track_length)

    def choose_car(player_list, track_length):
        """Выводит для игроков рандомный список машин и даёт выбрать одну из списка,
        после чего запоминает их выбор."""

        create_random_cars()
        print('\nДля этого заезда представлены следующие машины:')

        num = 1

        for car in car_list:  # Выводим список из созданных машин для выбора игроками
            turbine_check = 'with turbine' if car.turbine else 'without turbine'

            print(f'{num}) {car.car_type}, {car.wheel_number} wheels, {car.engine_type} engine, '
                  f'{car.horsepower} horsepower, {turbine_check}, {car.diameter} inch wheel, '
                  f'{car.wheel_weight} kg each.')
            num += 1

        print('')

        available_car_numbers = list(range(1, 6))  # Список свободных номеров машин
        chosen_cars_list = []  # Список с выбранными игроками машинами

        for player_name in player_list:  # Игроки выбирают себе машины
            while True:
                car_number = int(input(f'{player_name}, выберите свободную машину по номеру (от 1 до 5): '))

                if car_number in available_car_numbers:
                    chosen_cars_list.append(car_list[car_number - 1])
                    break
                elif car_number < 1 or car_number > 5:
                    print('Машины с таким номером в списке нет.')
                else:
                    print('Выбранная машина уже занята!')

        calculate_time(chosen_cars_list, player_list, track_length)

    def calculate_time(chosen_cars_list, player_list, track_length):
        """Рассчитывает время каждого игрока, необходимое на преодоление трассы."""

        time_list = []  # Список со временем преодоления трассы всеми игроками

        for car in chosen_cars_list:
            Car.start_engine(car)
            time = Car.move(car, track_length)
            time_list.append(time)

        animate_racing(player_list, time_list, track_length)

    def animate_racing(player_list, time_list, track_length):
        """Создаёт анимацию в консоли с полоской-баром и % преодоления трассы каждым из игроков."""

        from time import sleep
        import os  # в IDE типа PyCharm не работает, но работает в консоли ОС

        def cls():  # функция для чистки текста в консоли (для принт-анимации)
            os.system('cls' if os.name == 'nt' else 'clear')

        for percent in range(int(min(time_list) + 1)):
            for name in player_list:
                width = 30
                personal_percent = int(100 * percent / time_list[player_list.index(name)])
                hashes = width * personal_percent // 100
                blanks = width - hashes

                # Блок для красивого выравнивания текста при анимации по самому длинному имени
                max_len = max(list(map(lambda name: len(name), player_list)))
                blank_spaces_after_name = ' ' * (max_len - len(name) + 1)

                print(f'\r{name}', f'{blank_spaces_after_name}[', hashes * '#', blanks * ' ', ']',
                      f' {personal_percent:.0f}%', sep='', flush=True, end='')
                print('\n', end='')
            sleep(0.5)
            cls()

        announce_results(time_list, player_list, track_length)

    def announce_results(time_list, player_list, track_length):
        """Объявляет результаты гоночной игры, предлагает реванш."""

        print(f'Время игроков по очереди: {time_list}')  # Проверка результата

        print(f'Победил {player_list[time_list.index(min(time_list))]}!')

        while True:
            rematch_old_cars = input('\nУстроить реванш на тех же машинах (ничего не изменится, увы)?'
                                     '\nВведите \"Да\" или \"Нет\": ')

            if rematch_old_cars.lower() == 'да':
                print(f'И снова победил {player_list[time_list.index(min(time_list))]}!')
            else:
                rematch_new_cars = input('\nТогда устроим реванш на новых машинах на той же трассе?'
                                         '\nВведите \"Да\" или \"Нет\": ')

                if rematch_new_cars.lower() == 'да':
                    choose_car(player_list, track_length)

                else:
                    print('\nГонка завершена!')
                    exit()

    create_players()


if __name__ == '__main__':
    # player1 = Car('jeep', 4, 'v10', 300, True, 16, 10)
    # player1.start_engine()
    # print(player1.move(1000))

    racing_game()
