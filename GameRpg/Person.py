"""
Este arquivo define a CLASSE BASE para todas as entidades vivas no jogo.
Em POO, esta é a 'Superclasse' ou 'Classe Pai'.
"""
class Person:
    """
    O método __init__ é o CONSTRUTOR da classe.
    """
    def __init__(self, name, hp, mana, power_atk, defense, level):
        # Atributos que todas as 'Person' (Pessoas) terão
        self.name = name
        self.hp = hp

        self.hp_max = hp 
   
        
        self.mana = mana
        self.power_atk = power_atk
        self.defense = defense
        self.level = level
        self.type_weapon = "" # Subclasses irão sobrescrever isto

    def Atack(self):
        """
        CONCEITO DE POLIMORFISMO (Polymorphism)
        """
        return self.power_atk

    def Defend(self, damage):
        """
        Este método calcula o dano recebido.
        """
        final_damage = damage - self.defense
        
        if final_damage < 0:
            final_damage = 0
            
        self.hp -= final_damage
        
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        """
        Método auxiliar para verificar se o personagem está vivo
        """
        return self.hp > 0
