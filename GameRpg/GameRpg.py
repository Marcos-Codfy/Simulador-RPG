import random
import time
from Hero import Warrior, Mage, Archer
from Enemy import Goblin, Orc, Dragon

# --- Instanciando Heróis e Inimigos ---
heroes = [Warrior(), Mage(), Archer(),Warrior()]
enemies = [Goblin(), Orc(), Goblin(), Dragon()]

print("*************************************")
print("")
print("*-------COMEÇA A BATALHA!----------*")
print("")
print("*************************************")
time.sleep(2) 

print("\nNossos heróis se preparam:")
print(" -> ", [hero.name for hero in heroes])
time.sleep(1)

print("\nEles encontrarão pela frente:")
print(" -> ", [enemy.name for enemy in enemies])
time.sleep(2)
print("\n" + "="*40 + "\n")
time.sleep(1)


# --- Simulação de Combate ---
turn = 1
# O combate continua enquanto houver heróis E inimigos vivos
while any(hero.is_alive() for hero in heroes) and any(enemy.is_alive() for enemy in enemies):
    print(f"--- Turno {turn} ---")
    time.sleep(1)

    # Filtra apenas os heróis e inimigos vivos para o turno
    living_heroes = [h for h in heroes if h.is_alive()]
    living_enemies = [e for e in enemies if e.is_alive()]

    # Vez dos Heróis
    print("\n-- Vez dos Heróis --")
    time.sleep(1)
    if living_heroes:
        for hero in living_heroes:
            if not living_enemies: break # Encerra se não houver inimigos vivos
            target = random.choice(living_enemies)
            damage = hero.Atack()
            
            print(f"{hero.name} ataca {target.name}...")
            time.sleep(1)
            print(f"   ...causando {damage} de dano!")
            target.Defend(damage)
            time.sleep(1)

            if not target.is_alive():
                print(f"   !!! {target.name} foi derrotado !!!")
                living_enemies.remove(target)
                time.sleep(1)
    
    print("-" * 20)
    time.sleep(1)
    
    # Vez dos Inimigos
    print("\n-- Vez dos Inimigos --")
    time.sleep(1)
    if living_enemies:
        for enemy in living_enemies:
            if not living_heroes: break # Encerra se não houver heróis vivos
            target = random.choice(living_heroes)
            damage = enemy.Atack()

            print(f"{enemy.name} ataca {target.name}...")
            time.sleep(1)
            print(f"   ...causando {damage} de dano!")
            target.Defend(damage)
            time.sleep(1)

            if not target.is_alive():
                print(f"   !!! {target.name} foi derrotado !!!")
                living_heroes.remove(target)
                time.sleep(1)
    
    # Exibir HP no final do turno
    print("\n-- Status no final do turno --")
    print("HP Heróis:")
    for hero in heroes:
        status = "DERROTADO" if not hero.is_alive() else f"HP: {hero.hp}"
        print(f"  {hero.name}: {status}")

    print("\nHP Inimigos:")
    for enemy in enemies:
        status = "DERROTADO" if not enemy.is_alive() else f"HP: {enemy.hp}"
        print(f"  {enemy.name}: {status}")
    
    print("\n" + "="*40 + "\n")
    turn += 1
    time.sleep(2) # Pausa maior entre os turnos

# --- Fim do Combate e Sobreviventes ---
print("\n--- A BATALHA TERMINOU ---")
time.sleep(1)

heroes_alive = [hero for hero in heroes if hero.is_alive()]






if heroes_alive:
    print("\n*************************************")
    print("* VITÓRIA DOS HERÓIS!       *")
    print("*************************************")
    print("\nSobreviventes:")
    for hero in heroes_alive:
        print(f"  - {hero.name} (HP: {hero.hp})")
else:
    print("\n*************************************")
    print("* OS INIMIGOS VENCERAM!      *")
    print("*************************************")
    enemies_alive = [enemy for enemy in enemies if enemy.is_alive()]
    print("\nSobreviventes:")
    for enemy in enemies_alive:
        print(f"  - {enemy.name} (HP: {enemy.hp})")