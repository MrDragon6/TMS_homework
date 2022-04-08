class NPC:
    health = 30
    mana = 0

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('Hello! I\'m just a friendly NPC.')


class Wizard(NPC):
    health = 50
    mana = 100

    def __init__(self, name):
        NPC.__init__(self, name)

    def greeting(self):
        print('Hello! I\'m a wizard.')


class Warrior(NPC):
    health = 100
    mana = 0

    def __init__(self, name):
        NPC.__init__(self, name)

    def greeting(self):
        print('Hello! I\'m a warrior.')


# Перегрузка __init__

class Round:
    def __init__(self):
        print('Земля круглая!')


class Flat(Round):
    def __init__(self):
        print('Земля плоская!')


if __name__ == '__main__':
    gendalf = Wizard('gendalf')
    gendalf.greeting()
    print(gendalf.mana)
    print(gendalf.health)
    print(gendalf.name)

    Flat()
    Round()



