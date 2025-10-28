import random
import time

class Battle:
    """
    Esta classe é o "Controlador".
    Ela contém a LÓGICA da batalha (regras, turnos, ataques).
    Ela NÃO sabe como desenhar, mas diz ao 'View' O QUE desenhar.
    """
    
    def __init__(self, heroes, enemies, view):
        self.heroes = heroes
        self.enemies = enemies
        self.view = view  # Recebe o objeto GameView
        self.turn = 1

    # --- Métodos de verificação de estado ---
    
    def _any_hero_alive(self):
        return any(hero.is_alive() for hero in self.heroes)

    def _any_enemy_alive(self):
        return any(enemy.is_alive() for enemy in self.enemies)

    def _get_living_heroes(self):
        return [h for h in self.heroes if h.is_alive()]

    def _get_living_enemies(self):
        return [e for e in self.enemies if e.is_alive()]

    # --- Métodos de execução de turno ---

    def _execute_hero_turn(self, living_heroes, living_enemies):
        self.view.draw_battle_scene(f"--- Turno {self.turn}: Vez dos Heróis ---")
        time.sleep(2)  

        for hero in living_heroes:
            if not living_enemies: break  
            
            target = random.choice(living_enemies)
            damage = hero.Atack() # Polimorfismo
            
            self.view.draw_battle_scene(f"{hero.name} ataca {target.name}...")
            time.sleep(1.2)
            
            target.Defend(damage) # Polimorfismo
            self.view.draw_battle_scene(f"{hero.name} causou {damage} de dano em {target.name}!")
            time.sleep(1.5)  

            if not target.is_alive():
                if target in living_enemies:
                    living_enemies.remove(target)
                self.view.draw_battle_scene(f"!!! {target.name} foi derrotado !!!")
                time.sleep(2)

    def _execute_enemy_turn(self, living_heroes, living_enemies):
        self.view.draw_battle_scene(f"--- Turno {self.turn}: Vez dos Inimigos ---")
        time.sleep(2)

        for enemy in living_enemies:
            if not living_heroes: break  
            
            target = random.choice(living_heroes)
            damage = enemy.Atack() # Polimorfismo

            self.view.draw_battle_scene(f"{enemy.name} ataca {target.name}...")
            time.sleep(1.2)
            
            target.Defend(damage) # Polimorfismo
            self.view.draw_battle_scene(f"{enemy.name} causou {damage} de dano em {target.name}!")
            time.sleep(1.5)

            if not target.is_alive():
                if target in living_heroes:
                    living_heroes.remove(target)
                self.view.draw_battle_scene(f"!!! {target.name} foi derrotado !!!")
                time.sleep(2)

    # --- Métodos principais do jogo ---

    def start_battle(self):
        """
        Este é o método principal que inicia e gere o loop da batalha.
        """
        self.view.draw_battle_scene("A BATALHA VAI COMEÇAR!")
        input("\nPressione ENTER para continuar...")

        while self._any_hero_alive() and self._any_enemy_alive():
            
            living_heroes = self._get_living_heroes()
            living_enemies = self._get_living_enemies()

            # Vez dos Heróis
            self._execute_hero_turn(living_heroes, living_enemies)
            
            # Atualiza listas de vivos para a vez dos inimigos
            living_heroes = self._get_living_heroes()
            living_enemies = self._get_living_enemies()

            # Vez dos Inimigos (só se ainda houver heróis e inimigos)
            if living_enemies and living_heroes:
                self._execute_enemy_turn(living_heroes, living_enemies)
            
            self.turn += 1
        
        # A batalha terminou, mostra os resultados
        self._show_final_results()

    def _show_final_results(self):
        """
        Mostra a tela de vitória ou derrota.
        """
        self.view.clear_screen()
        print("\n" * 5)  

        # Re-usa as constantes de cor do GameView
        from GameView import COLOR 

        if self._any_hero_alive():
            print(f"{COLOR['GREEN']}{'*************************************'.center(92)}{COLOR['RESET']}")
            print(f"{COLOR['GREEN']}{'* VITÓRIA DOS HERÓIS!       *'.center(92)}{COLOR['RESET']}")
            print(f"{COLOR['GREEN']}{'*************************************'.center(92)}{COLOR['RESET']}")
        else:
            print(f"{COLOR['RED']}{'*************************************'.center(92)}{COLOR['RESET']}")
            print(f"{COLOR['RED']}{'* OS INIMIGOS VENCERAM!      *'.center(92)}{COLOR['RESET']}")
            print(f"{COLOR['RED']}{'*************************************'.center(92)}{COLOR['RESET']}")

        print("\n\n--- STATUS FINAL ---\n")
        
        # Chama a renderização final, passando 'is_final_screen=True'
        self.view.draw_battle_scene("FIM DE JOGO", is_final_screen=True)

        print("\n")  
        input("Pressione ENTER para sair.")
