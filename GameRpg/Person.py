# Person.py
"""
Este arquivo define a CLASSE BASE para todas as entidades vivas no jogo.
Em POO, esta é a 'Superclasse' ou 'Classe Pai'.

Ela contém todos os atributos e métodos que são COMUNS a
TODAS as 'Person' (Heróis E Inimigos).
"""
class Person:
    """
    CONCEITO DE HERANÇA (Inheritance):
    Esta é a classe base. As futuras classes Hero e Enemy irão herdar dela.
    
    O método __init__ é o CONSTRUTOR da classe. Ele é chamado
    automaticamente quando um novo objeto é criado (instanciado).
    
    Removemos os valores padrão (como self.hp = 0) e agora
    o construtor ESPERA receber os valores das classes filhas.
    """
    def __init__(self, name, hp, mana, power_atk, defense, level):
        # Atributos que todas as 'Person' (Pessoas) terão
        self.name = name
        self.hp = hp
        self.mana = mana
        self.power_atk = power_atk
        self.defense = defense
        self.level = level
        # Definimos um valor padrão aqui. As subclasses irão sobrescrevê-lo.
        self.type_weapon = ""

    def Atack(self):
        """
        CONCEITO DE POLIMORFISMO (Polymorphism):
        Este é o método de ataque base. 
        
        Subclasses (como Mage) podem 'sobrescrever' (override) este método
        para ter um comportamento diferente (ex: usar mana para um ataque mágico).
        
        No nosso caso, estamos mantendo simples: o ataque é o poder de ataque.
        """
        return self.power_atk

    def Defend(self, damage):
        """
        Este método calcula o dano recebido.
        'self' é uma referência ao objeto ATUAL (ex: o Goblin específico
        que está sendo atacado).
        """
        # A defesa reduz o dano
        final_damage = damage - self.defense
        
        # Regra de negócio: não se pode 'curar' com um ataque
        if final_damage < 0:
            final_damage = 0
            
        self.hp -= final_damage
        
        # Regra de negócio: a vida não pode ficar negativa
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        """
        Método auxiliar para verificar se a pessoa está viva.
        Retorna True (Verdadeiro) se HP > 0, e False (Falso) caso contrário.
        """
        return self.hp > 0