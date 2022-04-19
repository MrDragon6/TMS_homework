from app import ammos, guns, tank


if __name__ == '__main__':
    tank = tank.Tank('тигр', 1000)
    dice = guns.Dice()

    tank._load_ammos()
    print(tank.current_armor)
    tank.select_armor('керамическая')
    print(tank.current_armor.type)
    print('')

    print(tank.current_ammo)
    print(len(tank.hecartridge_list))
    print(tank._is_gun_loaded)
    tank.load_gun('фугасный')
    print(len(tank.hecartridge_list))
    print(tank._is_gun_loaded)
    print('')

    tank.shoot()
    gun1 = guns.Gun(300, 30)
    ammo1 = ammos.HEATCartridge(gun1)
    tank.handle_hit(ammo1)
    print(tank.health)
