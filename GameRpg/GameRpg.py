# GameRpg.py
import random
import time
# Importamos as classes CONCRETAS que queremos usar
from Hero import Warrior, Mage, Archer
from Enemy import Goblin, Orc, Dragon

# --- Instanciando Heróis e Inimigos ---

"""
CONCEITO: VARIÁVEL E REFERÊNCIA (Variable and Reference)

A variável 'heroes' não "contém" os objetos Warrior, Mage, etc.
Em Python, 'heroes' é uma LISTA que contém *REFERÊNCIAS* (ou "ponteiros", "apelidos")
para os objetos que estão em algum lugar na memória.

Pense nisso como:
- Warrior() cria um novo Guerreiro na memória (ex: no endereço de memória 1000).
- Mage() cria um Mago na memória (ex: no endereço 2000).

A lista 'heroes' se torna: [referência_para_1000, referência_para_2000, ...]
"""
heroes = [Warrior(), Mage(), Archer(), Warrior()]
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

    """
    CONCEITO: VARIÁVEL E REFERÊNCIA
    
    'living_heroes' é uma NOVA lista, mas ela é preenchida com as
    *MESMAS REFERÊNCIAS* da lista 'heroes' (apenas filtradas).
    
    Se o 'Warrior' (endereço 1000) está vivo, a *referência* 1000
    é copiada para a lista 'living_heroes'.
    O objeto em si NÃO é copiado.
    """
    living_heroes = [h for h in heroes if h.is_alive()]
    living_enemies = [e for e in enemies if e.is_alive()]

    # Vez dos Heróis
    print("\n-- Vez dos Heróis --")
    time.sleep(1)
    if living_heroes:
        for hero in living_heroes:
            if not living_enemies: break # Encerra se não houver inimigos vivos
            
            """
            CONCEITO: VARIÁVEL E REFERÊNCIA
            
            'target' é mais UMA referência.
            Se random.choice() escolher o 'Goblin' (ex: endereço 3000),
            a variável 'target' agora também "aponta" para o endereço 3000.
            
            'target', 'enemies[0]', e 'living_enemies[0]' podem estar
            apontando EXATAMENTE para o *MESMO* objeto na memória.
            """
            target = random.choice(living_enemies)
            
            """
            CONCEITO: POLIMORFISMO (Polymorphism)
            
            Esta é a mágica da POO!
            O Python não precisa saber se 'hero' é um 'Warrior', 'Mage' ou 'Archer'.
            Ele apenas chama o método '.Atack()'.
            
            Se 'hero' for um 'Warrior', ele usa o Atack() de 'Person'.
            Se 'hero' for um 'Mage' (e tivéssemos descomentado o método
            de ataque especial em Hero.py), o Python automaticamente
            usaria o Atack() do 'Mage'.
            
            O mesmo vale para 'target.Defend(damage)'. Não importa se 'target'
            é um 'Goblin' ou 'Dragon', o código funciona porque AMBOS
            herdaram o método .Defend() da classe 'Person'.
            """
            damage = hero.Atack() # Polimorfismo
            
            print(f"{hero.name} ataca {target.name}...")
            time.sleep(1)
            print(f"   ...causando {damage} de dano!")
            
            """
            CONCEITO: VARIÁVEL E REFERÊNCIA (EFEITO COLATERAL)
            
            Quando chamamos 'target.Defend(damage)', estamos modificando
            o objeto que está no endereço 3000.
            Como 'target' é uma REFERÊNCIA, a mudança é "global".
            O 'Goblin' original na lista 'enemies' terá seu HP reduzido,
            porque 'target' e 'enemies[0]' são apenas "apelidos"
            diferentes para o MESMO objeto.
            """
            target.Defend(damage) # Polimorfismo
            time.sleep(1)

            if not target.is_alive():
                print(f"   !!! {target.name} foi derrotado !!!")
                # Remove a *referência* da lista de vivos
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
            
            # O mesmo conceito de Referência se aplica aqui
            target = random.choice(living_heroes)
            
            # O mesmo conceito de Polimorfismo se aplica aqui
            damage = enemy.Atack() # Polimorfismo

            print(f"{enemy.name} ataca {target.name}...")
            time.sleep(1)
            print(f"   ...causando {damage} de dano!")
            
            # E o mesmo conceito de Referência/Efeito Colateral aqui
            target.Defend(damage) # Polimorfismo
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
        status = "DERROTADO" if not enemy.is_alive() else f"HP: {hero.hp}"
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
