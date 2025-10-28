# ⚔️ RPG de Console ⚔️

Bem-vindo ao nosso joguinho de RPG de terminal!

Mais do que um jogo, este projeto é um ótimo exemplo de como organizar um código que estava ficando bagunçado.  
Nós transformamos um único arquivo gigante em uma equipe de arquivos que trabalham juntos — cada um com sua própria função.

E o melhor: agora ele é todo **bonitão**, com **caixas de status**, **cores** e **limpeza de tela**!

---

## 🚀 Como Rodar o Jogo

É super simples! Você só precisa ter o **Python 3** instalado.

1. Baixe os arquivos para uma pasta.
2. Abra seu terminal nessa pasta.
3. Digite o comando mágico:

```bash
python GameRpg.py
```

Pronto! Agora é só apertar **ENTER** e ver a batalha acontecer ⚔️

---

## 🏛️ A Grande Ideia: Cada um no seu quadrado!

Antes, o arquivo `GameRpg.py` era o "faz-tudo". Ele era o **chefe**, o **artista** e o **juiz** ao mesmo tempo. Era uma bagunça!

Agora, nós organizamos a casa. Pense no projeto como uma equipe:

---

### 1. 🎭 Os Personagens (`Hero.py`, `Enemy.py`, `Person.py`)
São os **atores** do nosso jogo.

- Eles só se preocupam com suas próprias informações: nome, vida, poder de ataque, etc.  
- Eles sabem se apresentar (`self.name`) e sabem se defender (`Defend()`).

---

### 2. 🎨 O Artista (`GameView.py`)
Esse cara é o **Diretor de Arte**. Ele é responsável por tudo que aparece na tela.

- Ele sabe como limpar o terminal, desenhar as caixas de status e colorir os nomes (vermelho para mortos, verde para vivos).  
- Importante: o **Artista não sabe nada sobre as regras do jogo** — ele só desenha o que o "Juiz" manda.

---

### 3. ⚖️ O Juiz (`BattleManager.py`)
Esse é o **Diretor** ou **Juiz** da batalha. Ele sabe todas as regras.

- Ele controla os turnos, decide quem ataca quem, calcula o dano e avisa quem foi derrotado.  
- Ele não sabe desenhar — quando algo acontece (ex: “Guerreiro ataca Goblin”), ele apenas pede para o **Artista** desenhar a cena.

---

### 4. 👑 O Chefe (`GameRpg.py`)
O arquivo `GameRpg.py` virou o **Chefe**.

- Ele não faz trabalho pesado — só **contrata a equipe**:  
  - Cria os personagens: `heroes = [Warrior(), ...]`  
  - Contrata o artista: `view = GameView(...)`  
  - Contrata o juiz: `battle = Battle(...)`  
- Depois, ele dá a ordem: `battle.start_battle()`  
  (Basicamente: “Podem começar!”)

---

## 🤔 Por que isso é tão legal?

Porque é **muito mais fácil de mexer!**

- Achou o jogo feio? Quer mudar as cores ou o layout?  
  👉 Só mexe no `GameView.py`. O resto do jogo nem percebe.  

- Quer que os heróis ataquem duas vezes por turno?  
  👉 Só mexe no `BattleManager.py` (o Juiz).  

- Achou o `Mage` muito fraco?  
  👉 Só mexe no `Hero.py`.  

---

O código fica **limpo**, **organizado**, e cada arquivo tem **uma única responsabilidade**.  
Assim, o projeto cresce sem virar bagunça! 😄
