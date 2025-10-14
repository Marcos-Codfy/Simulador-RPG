from Person import Person

class Enemy(Person):
    def __init__(self):
        super().__init__()
        self.name = "Generic Enemy"
        self.hp = 50
        self.power_atk = 20
        self.defense = 10
        self.level = 1

class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Goblin"
        self.hp = 80
        self.power_atk = 30
        self.defense = 15
        self.type_waepon = "Club"

class Orc(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Orc"
        self.hp = 180
        self.power_atk = 50
        self.defense = 30
        self.type_waepon = "Axe"

class Dragon(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Dragon"
        self.hp = 300
        self.power_atk = 80
        self.defense = 45
        self.type_waepon = "Fire"