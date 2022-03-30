class Ship:
    def __init__(self, damage):
        self.damage = damage

    def deal_damage(self):
        print(f"{self.__class__.__name__} caused {self.damage} points of damage")


class BattleShip(Ship):
    def __init__(self, special_damage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.special_damage = special_damage

    def deal_special_damage(self):
        print(f"{self.__class__.__name__} inflicted {self.special_damage} to the enemy")

class BigBattleShip(BattleShip):
    def __init__(self, bomb_damage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bomb_damage = bomb_damage

    def deal_special_damage_twice(self):
        return super().deal_special_damage()
        return super().deal_special_damage()

    def use_bomb(self):
        print(f"{self.__class__.__name__} dealt {self.use_bomb()} damage!")

class CargoShip(Ship):
    def __init__(self, capacity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.capacity = capacity

    def transport(self):
        return self.capacity

ship = Ship(5)
battleship = BattleShip(special_damage=10, damage=5)
bigbattleship = BigBattleShip(bomb_damage=40, special_damage=10, damage=9)

print(ship.damage)
battleship.deal_damage()
battleship.deal_special_damage()
