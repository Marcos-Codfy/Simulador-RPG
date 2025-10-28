# Enemy.py
from Person import Person # Importa a classe Pai

"""
CONCEITO DE HERANÇA (Inheritance):
A classe 'Enemy' herda de 'Person'.
Serve como uma classe base para todos os tipos de inimigos.
(Você já tinha feito isso, estava perfeito!)
"""
class Enemy(Person):
    def __init__(self, name, hp, mana, power_atk, defense, level):
        """
        CONCEITO DE 'super()' (Ligação):
        Chamamos o construtor __init__ da classe Person
        para que ela inicialize os atributos comuns.
        """
        super().__init__(name, hp, mana, power_atk, defense, level)
        # Atributos específicos de Inimigos poderiam vir aqui.
        # Ex: self.loot_table = ["Gold", "Potion"]

"""
CONCEITO DE HERANÇA (nível 2):
Goblin, Orc, e Dragon herdam de 'Enemy'.
Hierarquia: Person -> Enemy -> Goblin
"""

class Goblin(Enemy):
    def __init__(self):
        # Chamamos o construtor do 'Enemy' (nosso Pai) com os valores
        # específicos do Goblin.
        super().__init__(
            name="Goblin", 
            hp=80, 
            mana=0, # Goblins não usam mana
            power_atk=30, 
            defense=15, 
            level=1
        )
        # Corrigindo o atributo (era 'type_waepon')
        self.type_weapon = "Club"

class Orc(Enemy):
    def __init__(self):
        super().__init__(
            name="Orc", 
            hp=180, 
            mana=0,
            power_atk=60, 
            defense=30, 
            level=3
        )
        self.type_weapon = "Axe"

class Dragon(Enemy):
    def __init__(self):
        super().__init__(
            name="Dragon", 
            hp=300, 
            mana=100, # Dragão pode ter mana para 'Fire'
            power_atk=90, 
            defense=45, 
            level=10
        )
        self.type_weapon = "Fire"
