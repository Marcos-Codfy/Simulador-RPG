# GameRpg.py
import random
import time
import os  # Importa a biblioteca 'Operating System' para limpar a tela

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

def create_status_box(title, character_list, width):
    """
    Esta função auxiliar CRIA uma caixa de status como uma lista de strings.
    Ela não imprime, apenas retorna as linhas.
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
        
        # --- CORREÇÃO DE ALINHAMENTO DE COLUNA ---
        # Construímos a string em colunas de largura fixa
        
        # Coluna 1: Nome (8 caracteres de largura, alinhado à esquerda)
        col_name = f"{char.name:<8}" 
        
        # Coluna 2: HP (14 caracteres de largura)
        # (Os :3 garantem que 1, 80, 150 ocupem o mesmo espaço)
        col_hp = f"| HP: {char.hp:3}/{char.hp_max:3}"
        
        # Coluna 3: MP (9 caracteres de largura)
        col_mp = f"| MP: {char.mana:3}"
        
        # Coluna 4: Status (11 caracteres de largura)
        col_status = f"| {status:<8}" # 8 para "DERROTADO" + 3 para "| "
        
        # Juntamos todas as colunas
        stats_line = f"{col_name}{col_hp}{col_mp}{col_status}"
        # ------------------------------------------------
        
        # O comprimento total agora é 8 + 14 + 9 + 11 = 42
        # .ljust(43) adicionará 1 espaço ao final, totalizando 43.
        box_lines.append("║" + stats_line.ljust(inner_width) + "║")
        
    # 5. Fundo da Caixa
    box_lines.append("╚" + "═" * inner_width + "╝")
    
    return box_lines

def draw_battle_scene(heroes, enemies, message=""):
    """
    Esta é a nossa função de "renderização".
    Ela desenha as duas caixas lado a lado e a mensagem em baixo.
    """
    clear_screen()
    
    box_width = 45 # Largura de CADA caixa
    
    # 1. Gerar as duas caixas como listas de strings
    hero_box_lines = create_status_box("--- GRUPO DOS HERÓIS ---", heroes, box_width)
    enemy_box_lines = create_status_box("--- GRUPO DOS INIMIGOS ---", enemies, box_width)
    
    # 2. Descobrir qual caixa é mais alta
    max_height = max(len(hero_box_lines), len(enemy_box_lines))
    
    # 3. "Preencher" a caixa mais baixa para que ambas tenham a mesma altura
    # Isto garante que os '╚═╝' fiquem alinhados
    while len(hero_box_lines) < max_height:
        # Insere uma linha em branco (║ ║) antes da última linha (╚═╝)
        hero_box_lines.insert(-1, "║" + " " * (box_width - 2) + "║")
        
    while len(enemy_box_lines) < max_height:
        # Insere uma linha em branco (║ ║) antes da última linha (╚═╝)
        enemy_box_lines.insert(-1, "║" + " " * (box_width - 2) + "║")

    # 4. Imprimir as caixas, linha por linha, lado a lado
    print("\n" * 3) # Adiciona espaço no topo
    
    for i in range(max_height):
        # --- CORREÇÃO 2 ---
        # Garante que está usando DOIS ESPAÇOS NORMAIS (ASCII 32)
        # entre as duas caixas para o alinhamento correto.
        print(f"{hero_box_lines[i]}  {enemy_box_lines[i]}")
        # ------------------
        
    print("\n" * 2) # Adiciona espaço entre a UI e a mensagem

    # 5. Desenha a caixa de mensagem em baixo
    draw_message_box(message)


# --- Instanciando Heróis e Inimigos ---
heroes = [Warrior(), Mage(), Archer(), Warrior()]
enemies = [Goblin(), Orc(), Goblin(), Dragon()]

# --- Mensagem Inicial ---
draw_battle_scene(heroes, enemies, "A BATALHA VAI COMEÇAR!")
input("\nPressione ENTER para continuar...")


# --- Simulação de Combate (O NOVO LOOP PRINCIPAL) ---
turn = 1
while any(hero.is_alive() for hero in heroes) and any(enemy.is_alive() for enemy in enemies):
    
    # Filtra apenas os vivos (igual ao seu código)
    living_heroes = [h for h in heroes if h.is_alive()]
    living_enemies = [e for e in enemies if e.is_alive()]

    # --- Vez dos Heróis ---
    # 1. Desenha o estado inicial do turno
    draw_battle_scene(heroes, enemies, f"--- Turno {turn}: Vez dos Heróis ---")
    time.sleep(2) # Pausa para o jogador ler

    if living_heroes:
        for hero in living_heroes:
            if not living_enemies: break # Se todos os inimigos morreram
            
            target = random.choice(living_enemies)
            damage = hero.Atack()
            
            # --- "Animação" de Mensagem (Sem Arte) ---
            
            # 2. FRAME 1: Anuncia o ataque
            draw_battle_scene(heroes, enemies, f"{hero.name} ataca {target.name}...")
            time.sleep(1.2)
            
            # 3. FRAME 2: Aplica o dano e mostra o resultado
            target.Defend(damage) # Aplica o dano
            draw_battle_scene(heroes, enemies, f"{hero.name} causou {damage} de dano em {target.name}!")
            time.sleep(1.5) # Pausa para ler o resultado

            # 4. FRAME 3: Verifica se o alvo foi derrotado
            if not target.is_alive():
                if target in living_enemies:
                    living_enemies.remove(target)
                
                draw_battle_scene(heroes, enemies, f"!!! {target.name} foi derrotado !!!")
                time.sleep(2)
    
    # --- Vez dos Inimigos ---
    living_heroes = [h for h in heroes if h.is_alive()]
    living_enemies = [e for e in enemies if e.is_alive()]

    if living_enemies and living_heroes:
        draw_battle_scene(heroes, enemies, f"--- Turno {turn}: Vez dos Inimigos ---")
        time.sleep(2)

        for enemy in living_enemies:
            if not living_heroes: break 
            
            target = random.choice(living_heroes)
            damage = enemy.Atack()

            # "Animação" de Mensagem para o inimigo
            draw_battle_scene(heroes, enemies, f"{enemy.name} ataca {target.name}...")
            time.sleep(1.2)
            
            target.Defend(damage)
            draw_battle_scene(heroes, enemies, f"{enemy.name} causou {damage} de dano em {target.name}!")
            time.sleep(1.5)

            if not target.is_alive():
                if target in living_heroes:
                    living_heroes.remove(target)
                draw_battle_scene(heroes, enemies, f"!!! {target.name} foi derrotado !!!")
                time.sleep(2)
    
    turn += 1

# --- Fim do Combate ---
clear_screen()
print("\n" * 5) # Centra a mensagem final

heroes_alive = [hero for hero in heroes if hero.is_alive()]

# Mensagens de vitória/derrota corrigidas (apenas espaços normais)
if heroes_alive:
    print("*************************************".center(92))
    print("* VITÓRIA DOS HERÓIS!          *".center(92))
    print("*************************************".center(92))
else:
    print("*************************************".center(92))
    print("* OS INIMIGOS VENCERAM!        *".center(92))
    print("*************************************".center(92))

print("\n\n--- STATUS FINAL ---\n")
# Mostra a UI final lado a lado
draw_battle_scene(heroes, enemies, "FIM DE JOGO")

print("\n") # Espaço extra
input("Pressione ENTER para sair.")
