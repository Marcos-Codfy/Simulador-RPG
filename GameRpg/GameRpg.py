# GameRpg.py
import random
import time
import os  # Importa a biblioteca 'Operating System' para limpar a tela

# --- HABILITA CORES ANSI NO TERMINAL WINDOWS ---
# (No Linux/macOS isso não é necessário, mas não causa mal)
os.system("")
# ---------------------------------------------

# --- Constantes de Cor ANSI ---
COLOR = {
    "RED": "\033[91m",    # Vermelho claro
    "GREEN": "\033[92m",  # Verde claro
    "RESET": "\033[0m"   # Reseta a cor para o padrão
}
# --------------------------------

# Importamos as classes CONCRETAS (Hero.py e Enemy.py não precisam de mudanças)
# (Certifique-se que os arquivos Hero.py e Enemy.py estão na mesma pasta)
# from Hero import Warrior, Mage, Archer
# from Enemy import Goblin, Orc, Dragon

# --- Classes de Exemplo (para o código rodar sozinho) ---
# Você pode apagar esta seção se já tiver os arquivos Hero.py e Enemy.py
class Person:
    def __init__(self, name, hp, mana, attack_power):
        self.name = name
        self.hp_max = hp
        self.hp = hp
        self.mana = mana
        self.attack_power = attack_power
    def is_alive(self):
        return self.hp > 0
    def Atack(self):
        return random.randint(self.attack_power - 5, self.attack_power + 5)
    def Defend(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

class Warrior(Person):
    def __init__(self):
        super().__init__("Warrior", 150, 50, 20)
class Mage(Person):
    def __init__(self):
        super().__init__("Mage", 100, 150, 10)
class Archer(Person):
    def __init__(self):
        super().__init__("Archer", 120, 80, 15)

class Goblin(Person):
    def __init__(self):
        super().__init__("Goblin", 80, 0, 12)
class Orc(Person):
    def __init__(self):
        super().__init__("Orc", 180, 0, 18)
class Dragon(Person):
    def __init__(self):
        super().__init__("Dragon", 300, 100, 25)
# --- Fim das Classes de Exemplo ---


# --- Funções Auxiliares de Desenho ---

def clear_screen():
    """Limpa o ecrã do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_message_box(message=""):
    """
    Desenha a caixa de mensagem "robusta" no fundo, com linhas duplas.
    """
    largura = 92 # Ajustado para a largura total das duas caixas (45 + 2 + 45)
    print("╔" + "═" * largura + "╗")
    print("║" + " " * largura + "║")
    # .upper() dá destaque à mensagem, .center() centraliza
    print("║" + message.upper().center(largura) + "║")
    print("║" + " " * largura + "║")
    print("╚" + "═" * largura + "╝")

# --- MUDANÇA 1: Adicionado 'is_final_screen' ---
def create_status_box(title, character_list, width, is_final_screen=False):
    """
    Esta função auxiliar CRIA uma caixa de status como uma lista de strings.
    Ela não imprime, apenas retorna as linhas.
    'is_final_screen' controla a cor verde para os vivos.
    """
    box_lines = []
    inner_width = width - 2 # Largura interna da caixa (sem as bordas ║) = 43
    
    # 1. Topo da Caixa
    box_lines.append("╔" + "═" * inner_width + "╗")
    
    # 2. Título
    box_lines.append("║" + title.center(inner_width) + "║")
    
    # 3. Divisória do Título
    box_lines.append("╠" + "═" * inner_width + "╣")
    
    # 4. Linhas de Personagem
    for char in character_list:
        status = "VIVO" if char.is_alive() else "DERROTADO"
        
        # Alinhamento por colunas (como corrigido anteriormente)
        col_name = f"{char.name:<8}" 
        col_hp = f"| HP: {char.hp:3}/{char.hp_max:3}"
        col_mp = f"| MP: {char.mana:3}"
        col_status = f"| {status:<8}"
        stats_line = f"{col_name}{col_hp}{col_mp}{col_status}"
        
        # Monta a linha completa COM BORDAS
        full_line = "║" + stats_line.ljust(inner_width) + "║"
        
        # --- MUDANÇA 2: Lógica de Coloração ---
        # A cor é aplicada NA LINHA INTEIRA (com bordas),
        # DEPOIS do '.ljust()', para não quebrar o alinhamento.
        
        if char.is_alive():
            if is_final_screen:
                # Se for a tela final, os vivos ficam VERDES
                full_line = f"{COLOR['GREEN']}{full_line}{COLOR['RESET']}"
        else:
            # Se estiver derrotado, fica VERMELHO (em qualquer tela)
            full_line = f"{COLOR['RED']}{full_line}{COLOR['RESET']}"
        
        box_lines.append(full_line)
        # --- Fim da Lógica de Coloração ---
            
    # 5. Fundo da Caixa
    box_lines.append("╚" + "═" * inner_width + "╝")
    
    return box_lines

# --- MUDANÇA 3: Adicionado 'is_final_screen' ---
def draw_battle_scene(heroes, enemies, message="", is_final_screen=False):
    """
    Esta é a nossa função de "renderização".
    Ela desenha as duas caixas lado a lado e a mensagem em baixo.
    """
    clear_screen()
    
    box_width = 45 # Largura de CADA caixa
    
    # 1. Gerar as duas caixas como listas de strings
    # --- MUDANÇA 4: Passa 'is_final_screen' para a função de criar ---
    hero_box_lines = create_status_box("--- GRUPO DOS HERÓIS ---", heroes, box_width, is_final_screen)
    enemy_box_lines = create_status_box("--- GRUPO DOS INIMIGOS ---", enemies, box_width, is_final_screen)
    
    # 2. Descobrir qual caixa é mais alta
    max_height = max(len(hero_box_lines), len(enemy_box_lines))
    
    # 3. "Preencher" a caixa mais baixa para que ambas tenham a mesma altura
    while len(hero_box_lines) < max_height:
        hero_box_lines.insert(-1, "║" + " " * (box_width - 2) + "║")
        
    while len(enemy_box_lines) < max_height:
        enemy_box_lines.insert(-1, "║" + " " * (box_width - 2) + "║")

    # 4. Imprimir as caixas, linha por linha, lado a lado
    print("\n" * 3) # Adiciona espaço no topo
    
    for i in range(max_height):
        # (Usa 2 espaços normais para o alinhamento)
        print(f"{hero_box_lines[i]}  {enemy_box_lines[i]}")
        
    print("\n" * 2) # Adiciona espaço entre a UI e a mensagem

    # 5. Desenha a caixa de mensagem em baixo
    draw_message_box(message)


# --- Instanciando Heróis e Inimigos ---
heroes = [Warrior(), Mage(), Archer(), Warrior()]
enemies = [Goblin(), Orc(), Goblin(), Dragon()]

# --- Mensagem Inicial ---
# (is_final_screen = False por padrão)
draw_battle_scene(heroes, enemies, "A BATALHA VAI COMEÇAR!")
input("\nPressione ENTER para continuar...")


# --- Simulação de Combate (O NOVO LOOP PRINCIPAL) ---
turn = 1
while any(hero.is_alive() for hero in heroes) and any(enemy.is_alive() for enemy in enemies):
    
    living_heroes = [h for h in heroes if h.is_alive()]
    living_enemies = [e for e in enemies if e.is_alive()]

    # --- Vez dos Heróis ---
    # (is_final_screen = False por padrão)
    draw_battle_scene(heroes, enemies, f"--- Turno {turn}: Vez dos Heróis ---")
    time.sleep(2) 

    if living_heroes:
        for hero in living_heroes:
            if not living_enemies: break 
            
            target = random.choice(living_enemies)
            damage = hero.Atack()
            
            # (is_final_screen = False por padrão)
            draw_battle_scene(heroes, enemies, f"{hero.name} ataca {target.name}...")
            time.sleep(1.2)
            
            target.Defend(damage)
            # (is_final_screen = False por padrão)
            draw_battle_scene(heroes, enemies, f"{hero.name} causou {damage} de dano em {target.name}!")
            time.sleep(1.5) 

            if not target.is_alive():
                if target in living_enemies:
                    living_enemies.remove(target)
                
                # (is_final_screen = False por padrão)
                draw_battle_scene(heroes, enemies, f"!!! {target.name} foi derrotado !!!")
                time.sleep(2)
    
    # --- Vez dos Inimigos ---
    living_heroes = [h for h in heroes if h.is_alive()]
    living_enemies = [e for e in enemies if e.is_alive()]

    if living_enemies and living_heroes:
        # (is_final_screen = False por padrão)
        draw_battle_scene(heroes, enemies, f"--- Turno {turn}: Vez dos Inimigos ---")
        time.sleep(2)

        for enemy in living_enemies:
            if not living_heroes: break 
            
            target = random.choice(living_heroes)
            damage = enemy.Atack()

            # (is_final_screen = False por padrão)
            draw_battle_scene(heroes, enemies, f"{enemy.name} ataca {target.name}...")
            time.sleep(1.2)
            
            target.Defend(damage)
            # (is_final_screen = False por padrão)
            draw_battle_scene(heroes, enemies, f"{enemy.name} causou {damage} de dano em {target.name}!")
            time.sleep(1.5)

            if not target.is_alive():
                if target in living_heroes:
                    living_heroes.remove(target)
                # (is_final_screen = False por padrão)
                draw_battle_scene(heroes, enemies, f"!!! {target.name} foi derrotado !!!")
                time.sleep(2)
    
    turn += 1

# --- Fim do Combate ---
clear_screen()
print("\n" * 5) 

heroes_alive = [hero for hero in heroes if hero.is_alive()]

if heroes_alive:
    # Imprime a mensagem de vitória em VERDE
    print(f"{COLOR['GREEN']}{'*************************************'.center(92)}{COLOR['RESET']}")
    print(f"{COLOR['GREEN']}{'* VITÓRIA DOS HERÓIS!          *'.center(92)}{COLOR['RESET']}")
    print(f"{COLOR['GREEN']}{'*************************************'.center(92)}{COLOR['RESET']}")
else:
    # Imprime a mensagem de derrota em VERMELHO
    print(f"{COLOR['RED']}{'*************************************'.center(92)}{COLOR['RESET']}")
    print(f"{COLOR['RED']}{'* OS INIMIGOS VENCERAM!        *'.center(92)}{COLOR['RESET']}")
    print(f"{COLOR['RED']}{'*************************************'.center(92)}{COLOR['RESET']}")

print("\n\n--- STATUS FINAL ---\n")

# --- MUDANÇA 5: Chamada final ---
# Aqui, nós explicitamente dizemos para a função que é a tela final
draw_battle_scene(heroes, enemies, "FIM DE JOGO", is_final_screen=True)

print("\n") 
input("Pressione ENTER para sair.")
