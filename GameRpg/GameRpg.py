class Person:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mana = 0
        self.power_atk = 0
        self.mana = 0
        self.defense = 0
        self.level = 0
        self.type_weapon = ""

    def Atack(self):
        return self.power_atk

    def Defend(self):
        return self.defense

 
class Warrior(Person):
    def __init__(self):
        super().__init__()
        self.name = "Warrior"
        self.hp = 150
        self.mana = 50
        self.power_atk = 60
        self.defense = 60
        self.level = 1
        self.type_waepon = "Sword"

class Mage(Person):
    def __init__(self):
        super().__init__()
        self.name = "Mage"
        self.hp = 100
        self.mana = 150
        self.power_atk = 70
        self.defense = 30
        self.level = 1
        self.type_waepon = "Staff"

class Archer(Person):
    def __init__(self):
        super().__init__()
        self.name = "Archer"
        self.hp = 120
        self.mana = 80
        self.power_atk = 60
        self.defense = 40
        self.level = 1
        self.type_waepon = "Bow"
           




player = Archer()

print("HP:", player.hp)
print("Mana:", player.mana)
print("Attack Power:", player.Atack())
print("Defense:", player.Defend())
print("Level:", player.level)
print("Type of Weapon:", player.type_waepon)










