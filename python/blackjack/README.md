# Etapa 1 — Cartas e Baralho (deck de 52 cartas)

## Objetivo: 
Conseguir criar um baralho padrão, embaralhar e comprar (puxar) cartas.

### Requisitos

Classe Card com atributos rank: str, suit: str, método __str__ (ex.: "A♠") e uma propriedade value (2-10 = número, J/Q/K = 10, A = 11 por enquanto).

Classe Deck que monta um baralho de 52 cartas, embaralha e tem o método draw() que devolve uma carta.

Reembaralhar automaticamente quando o baralho tiver ≤ 10 cartas.

### Sugestão de interface
```python
class Card: ...
class Deck:
    def __init__(self, rng: random.Random | None = None): ...
    def draw(self) -> Card: ...
```

## Dicas

Use tuplas globais:
```python
SUITS = ("♠","♥","♦","♣"),
RANKS = ("A","2",...,"K")
```

Use um dicionário de valores:
```python
{**{str(i): i for i in range(2,11)}, **{"J":10,"Q":10,"K":10,"A":11}}
```

## Concluído quando

Imprimir 5 cartas compradas mostra 5 cartas diferentes.

Após comprar mais 46 cartas, o baralho se reembaralha automaticamente na próxima compra.

# Etapa 2 — Valor da Mão (Ás pode valer 1 ou 11)

## Objetivo: 
Calcular o melhor valor de blackjack para uma lista de cartas.

### Requisitos

Função hand_value(cards: list[Card]) -> int

Some tudo contando Ás como 11.

Enquanto o total > 21 e ainda houver Ás, subtraia 10 (transforma um Ás = 1).

Testes rápidos

A♠, 9♦ → 20

A♠, 9♦, A♥ → 21

A♠, K♣, 9♦ → 20 (Ás passa a 1)

# Etapa 3 — Detecção de Blackjack (natural)

## Objetivo: 
Detectar se a mão tem um blackjack natural (duas cartas totalizando 21).

### Requisitos

Função is_blackjack(cards: list[Card]) -> bool.

### Testes

A + 10 (ou J/Q/K) com duas cartas → True

A + 9 + A → False

# Etapa 4 — Dar as Cartas (sem input ainda)

## Objetivo:
Dar duas cartas para o jogador e duas para o dealer, mostrando a carta aberta do dealer.

### Requisitos

Função deal_round(deck: Deck) -> tuple[list[Card], list[Card]]

Retorna (player, dealer)

Imprime:

Dealer mostra: <carta_aberta>

Sua mão: c1, c2 (total X)

### Testes

Jogador e dealer recebem 2 cartas.

Os totais batem com hand_value.

# Etapa 5 — Turno do Jogador (Hit / Stand)

## Objetivo: 
Permitir que o jogador escolha h (hit/pedir) ou s (stand/parar).

Se pedir, comprar uma carta e mostrar o novo total.
Parar se estourar (> 21) ou escolher Stand.

### Requisitos

Função player_turn(deck, player_cards) -> str retornando "bust" ou "stand".

Aceitar apenas h / s (ignorar maiúsculas/minúsculas, repromptar se inválido).

Ao pedir, imprimir a carta e o novo total.

### Testes

“h” adiciona cartas, “s” encerra.

Estouro (> 21) mostra mensagem e retorna "bust".

# Etapa 6 — Turno do Dealer (parar em 17)

## Objetivo: 
Dealer revela a carta escondida e compra até atingir 17 ou mais.
Por enquanto, para em todo 17 (hard ou soft).

### Requisitos

Função dealer_turn(deck, dealer_cards) -> None

Imprimir cada carta comprada e o total final.

### Testes

Dealer com 16 compra.

Dealer com 17 para.

Totais conferem com hand_value.

# Etapa 7 — Comparar Resultados (sem dinheiro ainda)

## Objetivo: 
Decidir entre GANHA / PERDE / EMPATE, considerando estouro e naturais.

### Requisitos

Função compare(player_cards, dealer_cards) -> str, retornando "win" | "lose" | "push" | "blackjack".

Regras:

Se o jogador estourar → lose

Se o dealer estourar → win

Caso contrário, compara totais

Ambos blackjack → push

Só jogador blackjack → blackjack

Só dealer blackjack → lose

### Testes

Testar mãos fabricadas cobrindo todos os casos.

# Etapa 8 — Banca e Aposta Fixa (+ Blackjack 3:2)

## Objetivo: 
Adicionar dinheiro e pagamentos simples.

### Requisitos

Variáveis: bankroll (saldo) e base_bet (aposta fixa).

Antes de cada rodada, subtrair a aposta.

Ao finalizar:

"win" → +2×aposta

"lose" → 0

"push" → +aposta

"blackjack" → +aposta + 1.5×aposta (int(bet*1.5) para evitar float)

Mostrar o saldo atualizado.

### Testes
Saldo inicial 200, aposta 10:

win → 210

lose → 190

push → 200

blackjack → 215

# Etapa 9 — Laço Principal (de várias rodadas)

## Objetivo: 
Juntar tudo num jogo completo.

### Requisitos

Função play_round() que:
1️⃣ cobra a aposta
2️⃣ distribui as cartas
3️⃣ verifica naturais
4️⃣ executa o turno do jogador
5️⃣ executa o turno do dealer (se jogador não estourar)
6️⃣ compara e liquida o resultado

Laço while bankroll >= base_bet: perguntando “Apostar 10? (s/n)”

Permitir sair no meio da mão digitando q; devolver a aposta dessa rodada.

### Testes

Jogar várias rodadas até parar ou ficar sem saldo.

Sair no meio devolve a aposta corretamente.