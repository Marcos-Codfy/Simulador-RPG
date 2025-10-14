class Person:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mana = 0
        self.power_atk = 0
        self.defense = 0
        self.level = 0
        self.type_weapon = ""

    def Atack(self):
        return self.power_atk

    def Defend(self, damage):
        # A defesa vai ser usada para reduzir o dano
        final_damage = damage - self.defense
        # não pode causar dano negativo
        if final_damage < 0:
            final_damage = 0
        self.hp -= final_damage
        # A vida não pode ser negativa
        if self.hp < 0:
            self.hp = 0
    # Verifica se o personagem está vivo, se o HP maior que 0 - Retorna True, istó é, ainda está vivo
    def is_alive(self):
        return self.hp > 0

 
