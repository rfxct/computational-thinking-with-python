
# vou explicar essas primeiras linhas em sala, se você estiver vendo sozinho,
# por favor pule elas

toad = '''
.....xxxxxx.....
...xx..xxxxxx...
..x....xxxx..x..
.x....xxxxxx..x.
xxxxxxx....xxxxx
xx..xx......xxxx
x....x......xx.x
x....xx....xx..x
xx..xxxxxxxxx..x
xxxxxxxxxxxxxx.x
.xxx..x..x..xxx.
..x...x..x...x..
..x..........x..
...x........x...
....xxxxxxxx....
'''

toad2 = [['.', '.', '.', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'x', 'x', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', '.'],
         ['.', '.', 'x', '.', '.', '.', '.', 'x', 'x', 'x', 'x', '.', '.', 'x', '.', '.'],
         ['.', 'x', '.', '.', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', 'x', '.'],
         ['x', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', '.', '.', 'x', 'x', 'x', 'x', 'x'],
         ['x', 'x', '.', '.', 'x', 'x', '.', '.', '.', '.', '.', '.', 'x', 'x', 'x', 'x'],
         ['x', '.', '.', '.', '.', 'x', '.', '.', '.', '.', '.', '.', 'x', 'x', '.', 'x'],
         ['x', '.', '.', '.', '.', 'x', 'x', '.', '.', '.', '.', 'x', 'x', '.', '.', 'x'],
         ['x', 'x', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', 'x'],
         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '.', 'x'],
         ['.', 'x', 'x', 'x', '.', '.', 'x', '.', '.', 'x', '.', '.', 'x', 'x', 'x', '.'],
         ['.', '.', 'x', '.', '.', '.', 'x', '.', '.', 'x', '.', '.', '.', 'x', '.', '.'],
         ['.', '.', 'x', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.'],
         ['.', '.', '.', 'x', '.', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.'],
         ['.', '.', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', '.', '.']]


def show_matrix(matrix):
    # voce nao precisa entender esse codigo, mas pode, se quiser, eu vou comentar ele pra você
    # essa primeira linha diz que queremos usar um programa externo chamado matplotlib
    # se ele não estivesse instalado, teriamos que rodar pip install matplotlib para que ele funcionasse
    import matplotlib.pyplot as plt

    # essa funcao serve para converter uma lista de caracteres em uma lista de numeros
    # para cada posicao da string, queremos um valor 0 ou 10 na lista
    # 10 se a posicao da string for um x
    # 0 se for qualquer outra coisa
    def lineNumbersFromLineChars(lista_chars):
        lista = []
        for letra in lista_chars:
            if letra == 'x':
                lista.append(10)
            else:
                lista.append(0)
        return lista

    # agora podemos converter a matriz, linha a linha,
    # trocando sempre os caracteres por numeros
    matrix_numerica = []
    for linha in matrix:
        linha_numeros = lineNumbersFromLineChars(linha)
        matrix_numerica.append(linha_numeros)

    # essas funções sao da biblioteca matplotlib, não são interessantes de explicar hoje
    plt.imshow(matrix_numerica, cmap=plt.cm.Blues)
    plt.show()


show_matrix(toad2)

'''
A idéia desse arquivo é representar um desenho simples em AsciiART

Por exemplo, poderiamos ter 
.....xxxxxx.....
...xx..xxxxxx...
..x....xxxx..x..
.x....xxxxxx..x.
xxxxxxx....xxxxx
xx..xx......xxxx
x....x......xx.x
x....xx....xx..x
xx..xxxxxxxxx..x
xxxxxxxxxxxxxx.x
.xxx..x..x..xxx.
..x...x..x...x..
..x..........x..
...x........x...
....xxxxxxxx....

Esse desenho tem duas dimensões, largura e altura, que chamaremos, respectivamente, de X e Y.

Para tomar um exemplo mais simples:
x.x.
.x.x

Esse desenho consiste de duas linhas, cada uma com tamanho 4. Diriamos que ele tem largura 4 e
altura 2.


a1b2
c3d4

  c0  c1 c2 c3 
l0 a  1   b  2
l1 c  3   d  4


Esse desenho também. Diremos que a letra "a" está na posição (x=0,y=0), 1 está na posicao (x=1,y=0)
d está na posicao (x=2,y=1)

Ou seja, x marca deslocamentos para a direita, começando do 0;
         y marca deslocamentos para baixo, começando do 0.

Outro exemplo, considere o seguinte desenho
a1b2
c3d4
zkje
qwtm

Podemos dar nome pras colunas e linhas
  c0  c1 c2 c3 
l0 a  1   b  2
l1 c  3   d  4
l2 z  k   j  e
l3 q  w   t  m


como j está na linha de indice 2, y dele é 2
como j está na colun de indice 2, x dele é 2

como z está na linha de indice 2, y dele é 2
como z está na colun de indice 0, x dele é 0
'''

'''
Preliminares do exercicio 1e

Nosso plano é criar uma representação de um desenho.

Queremos representar o desenho.
.xa
x.x
.x.

Para isso, usaremos uma lista de listas, como a que segue
[ ['.','x','a'], 
  ['x','.','x'], 
  ['.','x','.'] ] 

Repare que a primeira linha do desenho (.xa) está representada por uma lista
['.','x','a'] dentro da minha lista de listas.

Comecemos fazendo um desenho de uma unica linha, com vários pontos. Para isso,
usaremos a funcao linha(n)


Por exemplo, linha(3) deve retornar [['.','.','.']]

Isso representa o seguinte desenho:
...

Repare: Isso é uma lista de listas, com uma unica linha dentro, e essa linha tem 3 elementos


Crie a função, abaixo
'''

def linha(largura: int):
    return [['.' for _ in range(largura)]]

'''
Agora crie uma função duas_linhas. Essa função vai receber uma largura, e devolver
duas linhas, com essa largura, na representação de listas de listas

Por exemplo, duas_linhas(4) vai produzir o desenho

....
....

Lembrando que a representação é no formato de lista de lista, o retorno será
uma lista com duas dessas: ['.','.','.','.']

Ou seja:
[['.','.','.','.'],
 ['.','.','.','.']]

 Por favor, tome o cuidado de gerar cada uma das duas linhas separadamente, para fugir de um problema chatinho que
 eu vou explicar depois
'''


def duas_linhas(largura: int):
    matriz = []
    for _ in range(2):
        matriz.extend(linha(largura))
    return matriz


'''
Agora, faça a função sete_linhas, com a mesma idéia

Por favor, tome o cuidado de gerar cada uma das sete linhas separadamente, para fugir de um problema chatinho que
 eu vou explicar depois
'''


def sete_linhas(largura):
    matriz = []

    for _ in range(7):
        matriz.extend(linha(largura))
    return matriz


'''
Agora, vamos permitir que o número de linhas varie.
Ao chamar varias_linhas(2,3), estamos especificando um desenho com largura 2 e altura 3.
Ou seja, o desenho

..
..
..

Como antes, queremos a representação como lista de listas. Ou seja, 
queremos
[['.','.'],
 ['.','.'],
 ['.','.']]

Crie a função, abaixo
'''


# na funcao abaixo, te damos um exemplo pra te ajudar.
# pode ler e rodar. Nao precisa fazer nada com ela.
# para lembrar do range e como usar ele no for, deixamos o exemplo abaixo
def alguns_ois(quantidade):  # se quantidade for 4
    for i in range(quantidade):  # range é uma "lista": [0,1,2,3]
        print('oi')  # e portanto o for vai executar esse bloco
        print('tudo bom?')  # de código
        print(f"i vale {i}")  # 4 vezes


def varias_linhas(largura, altura):
    matriz = []

    for _ in range(altura):
        matriz.extend(linha(largura))
    return matriz


'''
Agora que já sabemos criar um mapa, é hora de fazer a exibição desse mapa para o usuário.

Nossa intenção é ter uma função que exiba as listas

[['.','.'],
 ['.','.'],
 ['.','.']]

como:

..
..
..
'''

'''
Crie uma funcao mostra_lista, que recebe uma lista de caracteres e constroi uma string
adequada. Por exemplo, se ela recever a lista ['b', 'a', 'n', 'a', 'n', 'a'],
deverá retornar a string "banana"

repare que converter a lista para uma string usando a função str não faz o que a gente quer!
>>> str(['b', 'a', 'n', 'a', 'n', 'a'])
"['b', 'a', 'n', 'a', 'n', 'a']"

a gente vai ter que fazer no passo a passo mesmo, adicionando cada caractere via um for
'''


# essa funcao retorna uma string com muitos a. Especificamente, ela usa a variável qtd
# para escolher quantos. Ela está aqui para te ajudar, você pode ler e rodar,
# não precisa fazer nada nela
def muitos_a(qtd):  # se qtd for 3
    string = ""
    for i in range(qtd):  # range é a "lista" [0,1,2]
        string = string + 'a'  # coloco 3 as na minha lista (um para i=0, um para i=1, um para i=2)
    return string  # devolvo "aaa"


def mostra_lista(lista):
    resultado = ""
    for char in lista:
        resultado += char

    return resultado


'''
Crie uma funcao mostra_listas, que recebe uma de listas. Cada listinha 
dentro dela é uma lista de caracteres. 
Por exemplo, se ela recever a lista de listas 
[['b', 'a', 'n', 'a', 'n', 'a'],['n', 'a', 'b', 'a', 'n', 'a']], deverá retornar a string

banana
nabana

Repare que eu inseri duas quebras de linha, uma depois de banana e uma depois de nabana
Para colocar uma quebra de linha numa string, basta juntar '\n'. Ou seja, "banana"+"\n"
é a string banana, mas com uma quebra de linha no final

'''


# experimente esse print para ver o efeito do \n
# print("banana"+"\n"+"split"+"\n"+"!")


def mostra_listas(lista_de_listas):
    resultado = ""

    for lista in lista_de_listas:
        resultado += mostra_lista(lista) + '\n'

    return resultado


'''
No exercicio 3, queremos começar a desenhar. Ou seja, a
colocar caracteres diferentes de '.' no nosso mapa.

Mas primeiro, façamos algumas preliminares
'''

'''
Implemente uma função primeira_linha,
que devolve a primeira linha do mapa.

Ou seja, se o mapa é
mapa = [['.','b','.'],
        ['a','.','.'],
        ['.','.','c'],
        ['.','.','.']]

Então primeira_linha(mapa) devolve a lista ['.','b','.']
'''


def primeira_linha(mapa):
    return mapa[0]


'''
Implemente uma função linha_n. Ao chamar linha_n(mapa,3), pegamos, no mapa, a linha de índice 3 (lembre-se que essa é a quarta linha! A primeira tem indice 0, a segunda indice 1, a terceira indice 2)
'''


def linha_n(mapa, linha):
    return mapa[linha]


'''
Implemente um funcao posicao(mapa,x,y). Ao chamar posicao(mapa,x,y), pegamos, no mapa, a linha de índice x, e depois o elemento de indice y dessa linha

Por exemplo, considerando o mapa

[['.','.','a'],
 ['b','c','d']]

Ao chamarmos posicao(1,2), pegamos a linha de indice 1 (ou seja, ['b','c','d']) e retornamos o elemento de indice 2 (ou seja, 'd')
'''


def posicao(mapa, linha, coluna):
    return mapa[linha][coluna]


'''
Exercício 3d: Faremos uma função "coloca" para alterar o desenho. Suponha que começamos com
o seguinte desenho:

...
...
...
...

Ao fazer coloca(desenho,1,3,'a'), queremos adicionar a letra 'a' na linha de indice 1,
coluna de indice três. Ou seja, em c1 l3

   c0 c1 c2
l0  .  .  .
l1  .  .  .
l2  .  .  .
l3  .  a  .

'''


def coloca(mapa, linha, coluna, simbolo):
    mapa[linha][coluna] = simbolo
    return mapa


'''
Se voce quiser marcar uma linha inteira com o mesmo simbolo, poderá usar a função a seguir

marca_linha(mapa,linha, simbolo)

Por exemplo, se o mapa era

....
....
....

E eu fizer marca_linha(mapa,2,'x')

Terei


....
....
xxxx

'''


def marca_linha(mapa, linha, simbolo):
    for c in range(len(mapa[linha])):
        mapa[linha][c] = simbolo
    return mapa

'''
Também podemos fazer uma função analoga chamada marca_coluna

Por exemplo, se o mapa era

....
....
....

E eu fizer marca_coluna(mapa,2,'x')

Terei


..x.
..x.
..x.
'''


def marca_coluna(mapa, coluna, simbolo):
    for l in range(len(mapa)):
        mapa[l][coluna] = simbolo
    return mapa


import unittest


class TestStringMethods(unittest.TestCase):

    def test01a_linha(self):
        linha3 = linha(3)
        self.assertEqual(linha3, [['.', '.', '.']])
        linha4 = linha(4)
        self.assertEqual(linha4, [['.', '.', '.', '.']])
        linha1 = linha(1)
        self.assertEqual(linha1, [['.']])
        linha0 = linha(0)
        self.assertEqual(linha0, [[]])

    def test01b_duas_linhas(self):
        duas_linhas3 = duas_linhas(3)
        self.assertEqual(duas_linhas3, [['.', '.', '.'],
                                        ['.', '.', '.']])
        duas_linhas4 = duas_linhas(4)
        self.assertEqual(duas_linhas4, [['.', '.', '.', '.'],
                                        ['.', '.', '.', '.']])
        duas_linhas1 = duas_linhas(1)
        self.assertEqual(duas_linhas1, [['.'], ['.']])
        duas_linhas0 = duas_linhas(0)
        self.assertEqual(duas_linhas0, [[], []])

    def test01c_sete_linhas(self):
        sete_linhas3 = sete_linhas(3)
        self.assertEqual(sete_linhas3, [['.', '.', '.'],
                                        ['.', '.', '.'],
                                        ['.', '.', '.'],
                                        ['.', '.', '.'],
                                        ['.', '.', '.'],
                                        ['.', '.', '.'],
                                        ['.', '.', '.']])
        sete_linhas4 = sete_linhas(4)
        self.assertEqual(sete_linhas4, [['.', '.', '.', '.'],
                                        ['.', '.', '.', '.'],
                                        ['.', '.', '.', '.'],
                                        ['.', '.', '.', '.'],
                                        ['.', '.', '.', '.'],
                                        ['.', '.', '.', '.'],
                                        ['.', '.', '.', '.']])
        sete_linhas1 = sete_linhas(1)
        self.assertEqual(sete_linhas1, [['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.']])
        sete_linhas0 = sete_linhas(0)
        self.assertEqual(sete_linhas0, [[], [], [], [], [], [], []])

    def test01d_varias_linhas(self):
        sete_linhas3 = varias_linhas(3, 7)
        self.assertEqual(sete_linhas3, [['.', '.', '.'],
                                        ['.', '.', '.'],
                                        ['.', '.', '.'],
                                        ['.', '.', '.'],
                                        ['.', '.', '.'],
                                        ['.', '.', '.'],
                                        ['.', '.', '.']])
        cinco_linhas4 = varias_linhas(4, 5)
        self.assertEqual(cinco_linhas4, [['.', '.', '.', '.'],
                                         ['.', '.', '.', '.'],
                                         ['.', '.', '.', '.'],
                                         ['.', '.', '.', '.'],
                                         ['.', '.', '.', '.']])

    def test02a_mostra_lista(self):
        self.assertEqual(mostra_lista(['b', 'a', 'n', 'a', 'n', 'a']), "banana")
        self.assertEqual(mostra_lista(['p', 'a', 'r', 'a', 'l', 'e', 'l', 'e', 'p', 'i', 'p', 'e', 'd', 'o']),
                         "paralelepipedo")

    def test02b_mostra_listas(self):
        self.assertEqual(mostra_listas([['b', 'a', 'n', 'a', 'n', 'a'], ['n', 'a', 'b', 'a', 'z', 'o']]),
                         "banana\nnabazo\n")

    def test03a_primeira_linha(self):
        mapa = varias_linhas(3, 4)
        self.assertEqual(primeira_linha(mapa), ['.', '.', '.'])
        mapa = [['.', 'b', '.'],
                ['a', '.', '.'],
                ['.', '.', 'c'],
                ['.', '.', '.']]
        self.assertEqual(primeira_linha(mapa), ['.', 'b', '.'])

    def test03b_linha_n(self):
        mapa = varias_linhas(3, 4)
        self.assertEqual(linha_n(mapa, 0), ['.', '.', '.'])
        self.assertEqual(linha_n(mapa, 2), ['.', '.', '.'])
        mapa = [['.', 'b', '.'],
                ['a', '.', '.'],
                ['.', '.', 'c'],
                ['.', '.', '.']]
        self.assertEqual(linha_n(mapa, 0), ['.', 'b', '.'])
        self.assertEqual(linha_n(mapa, 2), ['.', '.', 'c'])

    def test03c_posicao(self):
        mapa = varias_linhas(3, 4)
        self.assertEqual(posicao(mapa, 0, 0), '.')
        self.assertEqual(posicao(mapa, 1, 2), '.')
        mapa = [['.', 'b', '.'],
                ['a', '.', '.'],
                ['.', '.', 'c'],
                ['.', '.', '.']]
        self.assertEqual(posicao(mapa, 0, 0), '.')
        self.assertEqual(posicao(mapa, 0, 1), 'b')
        self.assertEqual(posicao(mapa, 0, 0), '.')
        self.assertEqual(posicao(mapa, 1, 0), 'a')

    def test03d_coloca(self):
        mapa = varias_linhas(3, 4)
        alvo40 = "...\n...\n...\n...\n"
        self.assertEqual(mostra_listas(mapa), alvo40)
        coloca(mapa, 0, 0, 'a')
        alvo41 = "a..\n...\n...\n...\n"
        self.assertEqual(mostra_listas(mapa), alvo41)
        coloca(mapa, 0, 2, 'b')
        alvo42 = "a.b\n...\n...\n...\n"
        self.assertEqual(mostra_listas(mapa), alvo42)
        coloca(mapa, 1, 2, 'c')
        alvo43 = "a.b\n..c\n...\n...\n"
        self.assertEqual(mostra_listas(mapa), alvo43)

    def test04a_marca_linha(self):
        mapa = varias_linhas(3, 4)
        alvo40 = "...\n...\n...\n...\n"
        self.assertEqual(mostra_listas(mapa), alvo40)
        marca_linha(mapa, 0, 'a')
        alvo41 = "aaa\n...\n...\n...\n"
        self.assertEqual(mostra_listas(mapa), alvo41)
        marca_linha(mapa, 2, 'b')
        alvo42 = "aaa\n...\nbbb\n...\n"
        self.assertEqual(mostra_listas(mapa), alvo42)

    def test04b_marca_coluna(self):
        mapa = varias_linhas(3, 4)
        alvo40 = "...\n...\n...\n...\n"
        self.assertEqual(mostra_listas(mapa), alvo40)
        marca_coluna(mapa, 0, 'a')
        alvo41 = "a..\na..\na..\na..\n"
        self.assertEqual(mostra_listas(mapa), alvo41)
        marca_coluna(mapa, 2, 'b')
        alvo42 = "a.b\na.b\na.b\na.b\n"
        self.assertEqual(mostra_listas(mapa), alvo42)


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


runTests()