# Anotações Ana #

###Classe Card:
#    Objetivo: 
        Representar uma carta do baralho, composta por rank (valor numérico) e o suit (naipe) de todas as possíveis combinações do baralho. 
#    Por que uma classe e não apenas uma função?
        Porque a carta de baralho é o elemento primordial e 'imutável' do jogo, ou seja, haverá uma quantidade limitada de ranks e suites e combinações respectivas. Em forma de classe, poderemos acrescentar ou remover qualquer informação relevante para a construção desta carta, que será pertinente em diversas situações dos demais códigos que compõem o jogo como um todo. Ou seja, a classe vai guardar as informações definidas do que é uma carta e eu posso acessar essas informações em outros códigos, apenas importando esta classe. Se tudo isso tivesse estruturado em forma de função, as informações referentes a cada carta teria que estar armazenada em variáveis. 
#    Onde será usada?
        A classe Card está sendo usada diversas vezes:
            - Classe Deck (serve para compor o que seria o baralho completo, ou seja, todas as combinações de ranks e suit, que geram todas as cartas do baralho. Pode-se dizer que representa então 52 cartas, construídas com a Classe Card).
            - Classe Hand (serve para especificar as cartas que os jogadores vão receber ao longo do jogo, ou seja, a função Card que cria cada carta do baralho, é usada na Classe Hand para representar a mão dos jogadores - as cartas que eles têm).

#   Pontos importantes (código):
        Cria-se inicialmente um Dicionário (RANKS) que armazena objetos do tipo Tupla. Essas Tuplas contém as informações dos símbolos alphanumérios bem como os valores respectivos que cada carta pode ter. 
        Em seguida, temos uma Lista (SUITS) que armazena os suits (naipes) existentes em um baralho. 
        A função __init__ (construtor) serve para 'guardar' o estado da carta quando a Classe é chamada (instanciada). Ou seja, ela vai guardar as informações pertinentes à carta criada (por exemplo, um 7 de ouro, 2 de espadas, etc). Além disso, faz uma verificação muito importante de verificar se o atributo de naipe passado (suit) realmente existe na Lista previamente declarada, e não deixa passar caso não exista.
        Em seguida, é feita outra função para armazenar o valor da carta (rank) e também é feita a verificação se o valor é válido, ou seja, se consta no Dicionário (RANKS). 
        DÚVIDA: Por que a verificação de rank ficou na função de Value e não na de init, junto com a verificação do suit?
            - O chat comentou que o ideal seria alterar a verificação de rank para junto da verificação de suit, junto ao init. 

        Por último, é utilizado uma função __repr__ que serve para deixar a formatação da carta gerada mais amigável, ou seja, deixar bonitinho o naipe junto ao rank. 
