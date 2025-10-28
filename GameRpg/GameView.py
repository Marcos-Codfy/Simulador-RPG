import os

# --- Constantes de Cor ANSI ---
COLOR = {
    "RED": "\033[91m",    # Vermelho claro
    "GREEN": "\033[92m",  # Verde claro
    "RESET": "\033[0m"    # Reseta a cor para o padrão
}
# --------------------------------

class GameView:
    """
    Esta classe é responsável por TUDO que é desenhado na tela.
    Ela não sabe as regras da batalha
    """
    
    def __init__(self, heroes, enemies):
        """
        O View precisa saber quem são os participantes para poder desenhá-los.
        """
        self.heroes = heroes
        self.enemies = enemies
        # HABILITA CORES ANSI NO TERMINAL WINDOWS
        os.system("") 

    def clear_screen(self):
        """Limpa o ecrã do console."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_message_box(self, message=""):
        """
        Desenha a caixa de mensagem "robusta" no fundo, com linhas duplas.
        """
        largura = 92 # Ajustado para a largura total (45 + 2 + 45)
        print("╔" + "═" * largura + "╗")
        print("║" + " " * largura + "║")
        print("║" + message.upper().center(largura) + "║")
        print("║" + " " * largura + "║")
        print("╚" + "═" * largura + "╝")

    def _create_status_box(self, title, character_list, width, is_final_screen=False):
        """
        (Método privado) Cria uma caixa de status como uma lista de strings.
        """
        box_lines = []
        inner_width = width - 2 # 43
        
        box_lines.append("╔" + "═" * inner_width + "╗")
        box_lines.append("║" + title.center(inner_width) + "║")
        box_lines.append("╠" + "═" * inner_width + "╣")
        
        for char in character_list:
            status = "VIVO" if char.is_alive() else "DERROTADO"
            
            # Alinhamento por colunas
            col_name = f"{char.name:<8}"  
            col_hp = f"| HP: {char.hp:3}/{getattr(char, 'hp_max', char.hp):3}"
            col_mp = f"| MP: {char.mana:3}"
            col_status = f"| {status:<8}"
            stats_line = f"{col_name}{col_hp}{col_mp}{col_status}"
            
            full_line = "║" + stats_line.ljust(inner_width) + "║"
            
            # Lógica de Coloração
            if char.is_alive():
                if is_final_screen:
                    full_line = f"{COLOR['GREEN']}{full_line}{COLOR['RESET']}"
            else:
                full_line = f"{COLOR['RED']}{full_line}{COLOR['RESET']}"
            
            box_lines.append(full_line)
                
        box_lines.append("╚" + "═" * inner_width + "╝")
        return box_lines

    def draw_battle_scene(self, message="", is_final_screen=False):
        """
        Esta é a nossa função de "renderização".
        Ela desenha as duas caixas lado a lado e a mensagem em baixo.
        """
        self.clear_screen()
        
        box_width = 45 # Largura de CADA caixa
        
        # 1. Gerar as duas caixas usando os participantes armazenados
        hero_box_lines = self._create_status_box(
            "--- GRUPO DOS HERÓIS ---", self.heroes, box_width, is_final_screen
        )
        enemy_box_lines = self._create_status_box(
            "--- GRUPO DOS INIMIGOS ---", self.enemies, box_width, is_final_screen
        )
        
        # 2. Descobrir qual caixa é mais alta
        max_height = max(len(hero_box_lines), len(enemy_box_lines))
        
        # 3. "Preencher" a caixa mais baixa
        while len(hero_box_lines) < max_height:
            hero_box_lines.insert(-1, "║" + " " * (box_width - 2) + "║")
            
        while len(enemy_box_lines) < max_height:
            enemy_box_lines.insert(-1, "║" + " " * (box_width - 2) + "║")

        # 4. Imprimir as caixas, linha por linha, lado a lado
        print("\n" * 3) # Adiciona espaço no topo
        
        for i in range(max_height):
            print(f"{hero_box_lines[i]}  {enemy_box_lines[i]}")
            
        print("\n" * 2) # Adiciona espaço entre a UI e a mensagem

        # 5. Desenha a caixa de mensagem em baixo
        self.draw_message_box(message)
