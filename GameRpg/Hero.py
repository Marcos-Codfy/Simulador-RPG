from Person import Person # Importa a classe Pai

"""
CONCEITO DE HERANÇA (Inheritance):
A classe 'Hero' herda de 'Person'.
Isso significa que 'Hero' automaticamente tem todos os atributos e métodos
de 'Person' (como .hp, .defense, .Atack(), .Defend(), etc.).

Esta é uma classe "intermediária" para agrupar lógica que
é comum a TODOS os heróis, mas não aos inimigos.
"""
class Hero(Person):
    def __init__(self, name, hp, mana, power_atk, defense, level):
        """
        CONCEITO DE 'super()' (Ligação):
        'super()' é uma "ligação" (binding) para a classe Pai (Person).
        Estamos chamando o construtor __init__ da classe Person
        para que ela inicialize os atributos comuns que passamos para ela.
        """
        super().__init__(name, hp, mana, power_atk, defense, level)



"""
CONCEITO DE HERANÇA (nível 2):
Warrior, Mage, e Archer herdam de 'Hero'.
Isso significa que eles são 'Hero' E também são 'Person'.
Hierarquia: Person -> Hero -> Warrior
"""

class Warrior(Hero):
    def __init__(self):
        # Agora, o construtor do Warrior não define mais os atributos.
        # Ele chama o construtor do 'Hero' (nosso Pai) com os valores
        # específicos do Warrior.
        super().__init__(
            name="Warrior", 
            hp=150, 
            mana=50, 
            power_atk=60, 
            defense=60, 
            level=1
        )
        self.type_weapon = "Sword"

class Mage(Hero):
    def __init__(self):
        super().__init__(
            name="Mage", 
            hp=100, 
            mana=150, 
            power_atk=80, 
            defense=30, 
            level=1
        )
        self.type_weapon = "Staff"


class Archer(Hero):
    def __init__(self):
        super().__init__(
            name="Archer", 
            hp=120, 
            mana=80, 
            power_atk=70, 
            defense=40, 
            level=1
        )
        self.type_weapon = "Bow"
