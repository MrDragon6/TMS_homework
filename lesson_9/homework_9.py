import random


class Dice:
    """Создаёт кубик для игры."""

    def __init__(self):
        self.result = None

    def throw(self):
        """Возвращает случайное int число от 1 до 6."""

        self.result = random.randrange(1, 7)
        return self.result


class Gun:
    """
    Создаёт пушку для танка.
    Принимает 2 аргумента: калибр и длина пушки.
    Имеет 1 метод is_on_target (фиксирует попадание в чужой танк).
    """

    def __init__(self, caliber: int, length: int):
        """
        Устанавливает необходимые атрибуты для объекта gun.
        ______________________
        Принимаемые атрибуты:
        caliber (калибр): int
        gun_length (длина пушки): int
        """

        if caliber < 0 or length < 0:
            raise Exception('gun caliber and length can\'t be less than 0!')

        self.caliber = caliber
        self.length = length

    def is_on_target(self, dice: Dice):
        """
        Вычисляет по формуле, было ли попадание в чужой танк.
        Возвращает значение True или False.
        ______________________
        Принимаемые атрибуты:
        dice (бросок кубика): int
        """

        is_target_hit = True if self.length * dice.throw() > 100 else False
        return is_target_hit


class Ammo:
    """Создаёт снаряды для пушки танка.
    Принимает 2 аргумента: объект класса Gun и тип снаряда.
    Имеет 2 метода: get_damage (расчёт урона от попадания)
    и get_penetration (возвращает силу пробития брони).
    """

    def __init__(self, gun: Gun, type: str):
        """
        Устанавливает необходимые атрибуты для объекта ammo.
        ______________________
        Принимаемые атрибуты:
        gun (объект пушки): Gun
        type (тип снаряда): str
        """

        self.gun = gun
        self.type = type
        self.penetration_power = 0

    def get_damage(self, gun: Gun):
        """
        Рассчитывает урон, наносимый вражескому танку.
        ______________________
        Принимаемые атрибуты:
        caliber (калибр): int
        """

        damage = gun.caliber * 3
        return damage

    def get_penetration(self, gun: Gun):
        """Возвращает силу пробития брони, равную
        калибру пушки танка."""

        self.penetration_power = gun.caliber
        return self.penetration_power


class HECartridge(Ammo):
    """Создаёт фугасный снаряд."""

    def __init__(self, gun: Gun):
        super().__init__(gun, type='фугасный')


class HEATCartridge(Ammo):
    """Создаёт кумулятивный снаряд."""

    def __init__(self, gun: Gun):
        super().__init__(gun, type='кумулятивный')

    def get_damage(self, gun: Gun):
        """Переопределяет метод родительского класса Ammo,
        умножая урон на коэффициент 0.6."""

        damage = super().get_damage(gun) * 0.6
        return damage


class APCartridge(Ammo):
    """Создаёт подкалиберный снаряд."""

    def __init__(self, gun):
        super().__init__(gun, type='подкалиберный')

    def get_damage(self, gun: Gun):
        """Переопределяет метод родительского класса Ammo,
        умножая урон на коэффициент 0.3."""

        damage = super().get_damage(gun) * 0.3
        return damage


class Armor:
    """Создаёт броню для танка.
     Принимает 2 аргумента: толщину брони и её тип.
     Имеет 1 метод is_penetrated (возвращает bool значение (пробита ли броня)
     по условию: {пробивная способность снаряда} > {толщина брони}.)
     """

    def __init__(self, thickness: int, type: str):
        """
        Устанавливает необходимые атрибуты для объекта armor.
        ______________________
        Принимаемые атрибуты:
        thickness (толщина брони): int
        type (тип брони): str
        """

        if thickness < 0:
            raise Exception('armor thickness can\'t be less than 0!')

        self.thickness = thickness
        self.type = type

    def is_penetrated(self, ammo: Ammo):
        """Возвращает bool значение (пробита ли броня) по условию:
        {пробивная способность снаряда} > {толщина брони}."""

        is_penetrated = True if ammo.gun.caliber > self.thickness else False
        return is_penetrated


class HArmor(Armor):
    """Создаёт гомогенную броню."""

    def __init__(self, thickness):
        super().__init__(thickness, type='гомогенная')

    def is_penetrated(self, ammo: Ammo):
        """Возвращает bool значение (пробита ли броня) по условию:
        {пробивная способность снаряда} > {толщина брони}."""

        factors = {'фугасный': 1.2,
                   'кумулятивный': 1.0,
                   'подкалиберный': 0.7}

        is_penetrated = True if \
            ammo.gun.caliber > self.thickness * factors.get(ammo.type) \
            else False

        return is_penetrated


# проверка
# gun1 = Gun(20, 30)
# gun2 = Gun(20, 30)
# gun3 = Gun(20, 30)
# dice1 = Dice()
# print(gun1.caliber)
# print(gun1.length)
# print(dice1.result)
# print(gun1.is_on_target(dice1))
#
# print('------------------')
# ammo1 = HECartridge(gun1)
# ammo2 = HEATCartridge(gun2)
# ammo3 = APCartridge(gun3)
#
# print(ammo1.get_damage(gun1))
# print(ammo1.type)
# print(ammo2.get_damage(gun2))
# print(ammo2.type)
# print(ammo3.get_damage(gun2))
# print(ammo3.type)
#
# print('------------------')
# armor1 = HArmor(30)
# print(armor1.type)
# print(armor1.thickness)
# print(armor1.is_penetrated(ammo3))
