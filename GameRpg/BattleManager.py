# BattleManager.py
import random
import time

class Battle:
    """
    Esta classe gere toda a lógica de uma batalha.
    Ela é responsável pelos turnos, ataques e verificação de status.
    """
    
    def __init__(self, heroes, enemies):
        """
        O construtor recebe as listas de participantes.
        """
        self.heroes = heroes
        self.enemies = enemies
        self.turn = 1

    def start_battle(self):
        """
        Este é o método principal que inicia e gere o loop da batalha.
        """
        print("*************************************")
        print("")
        print("*-------COMEÇA A BATALHA!----------*")
        print("")
        print("*************************************")
        time.sleep(2) 

        print("\nNossos heróis se preparam:")
        print(" -> ", [hero.name for hero in self.heroes])
        time.sleep(1)

        print("\nEles encontrarão pela frente:")
        print(" -> ", [enemy.name for enemy in self.enemies])
        time.sleep(2)
        print("\n" + "="*40 + "\n")
        time.sleep(1)

        # O loop principal da batalha
        while self._any_hero_alive() and self._any_enemy_alive():
            print(f"--- Turno {self.turn} ---")
            time.sleep(1)

            # Filtramos as listas de vivos a cada turno
            living_heroes = self._get_living_heroes()
            living_enemies = self._get_living_enemies()

            # Executa os turnos
            self._execute_hero_turn(living_heroes, living_enemies)
            self._execute_enemy_turn(living_heroes, living_enemies)

            # Exibe o status no final do turno
            self._display_turn_status()
            
            print("\n" + "="*40 + "\n")
            self.turn += 1
            time.sleep(2) # Pausa maior entre os turnos

        # Fim da batalha
        self._display_battle_results()

    # --- Métodos Auxiliares (Privados) ---
    
    def _any_hero_alive(self):
        return any(hero.is_alive() for hero in self.heroes)

    def _any_enemy_alive(self):
        return any(enemy.is_alive() for enemy in self.enemies)

    def _get_living_heroes(self):
        return [h for h in self.heroes if h.is_alive()]

    def _get_living_enemies(self):
        return [e for e in self.enemies if e.is_alive()]

    def _execute_hero_turn(self, living_heroes, living_enemies):
        print("\n-- Vez dos Heróis --")
        time.sleep(1)
        
        # Copiamos a lista de inimigos vivos para poder removê-los
        # sem afetar a iteração da lista principal
        targets_available = living_enemies.copy()
        
        for hero in living_heroes:
            if not targets_available: break # Encerra se não houver inimigos vivos
            
            target = random.choice(targets_available)
            
            damage = hero.Atack() # Polimorfismo
            
            print(f"{hero.name} ataca {target.name}...")
            time.sleep(1)
            print(f"   ...causando {damage} de dano!")
            
            target.Defend(damage) # Polimorfismo
            time.sleep(1)

            if not target.is_alive():
                print(f"   !!! {target.name} foi derrotado !!!")
                targets_available.remove(target) 
                time.sleep(1)

    def _execute_enemy_turn(self, living_heroes, living_enemies):
        print("\n-- Vez dos Inimigos --")
        time.sleep(1)
        
        # Copiamos a lista de heróis vivos
        targets_available = living_heroes.copy()

        if living_enemies:
            for enemy in living_enemies:
                if not targets_available: break
                
                target = random.choice(targets_available)
                
                damage = enemy.Atack() # Polimorfismo

                print(f"{enemy.name} ataca {target.name}...")
                time.sleep(1)
                print(f"   ...causando {damage} de dano!")
                
                target.Defend(damage) # Polimorfismo
                time.sleep(1)

                if not target.is_alive():
                    print(f"   !!! {target.name} foi derrotado !!!")
                    targets_available.remove(target)
                    time.sleep(1)
        
        print("-" * 20)
        time.sleep(1)

    def _display_turn_status(self):
        print("\n-- Status no final do turno --")
        print("HP Heróis:")
        for hero in self.heroes:
            status = "DERROTADO" if not hero.is_alive() else f"HP: {hero.hp}"
            print(f"  {hero.name}: {status}")

        print("\nHP Inimigos:")
        for enemy in self.enemies:
            # Corrigido: Estava 'hero.hp' no original, mudei para 'enemy.hp'
            status = "DERROTADO" if not enemy.is_alive() else f"HP: {enemy.hp}"
            print(f"  {enemy.name}: {status}")

    def _display_battle_results(self):
        print("\n--- A BATALHA TERMINOU ---")
        time.sleep(1)

        if self._any_hero_alive():
            print("\n*************************************")
            print("* VITÓRIA DOS HERÓIS!       *")
            print("*************************************")
            print("\nSobreviventes:")
            for hero in self._get_living_heroes():
                print(f"  - {hero.name} (HP: {hero.hp})")
        else:
            print("\n*************************************")
            print("* OS INIMIGOS VENCERAM!      *")
            print("*************************************")
            print("\nSobreviventes:")
            for enemy in self._get_living_enemies():
                print(f"  - {enemy.name} (HP: {enemy.hp})")
