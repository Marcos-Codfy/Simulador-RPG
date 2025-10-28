# --- 1. Importações ---
# Importa as classes de Modelo (os personagens)
from Hero import Warrior, Mage, Archer 
from Enemy import Goblin, Orc, Dragon
# Importa o Controlador (a lógica)
from BattleManager import Battle
# Importa a Visualização (o desenhista)
from GameView import GameView

# --- 2. Configuração (Setup) ---
# Cria as instâncias do Modelo
heroes = [Warrior(), Mage(), Archer(), Warrior()]
enemies = [Goblin(), Orc(), Goblin(), Dragon()]

# --- 3. Inicialização ---
# 1. Cria a instância da View, dizendo o que ela deve desenhar
view = GameView(heroes, enemies)

# 2. Cria a instância do Controlador, dizendo quem luta e como desenhar
battle = Battle(heroes, enemies, view)

# --- 4. Execução ---
# Inicia a batalha. O BattleManager e o GameView cuidam de todo o resto.
battle.start_battle()
