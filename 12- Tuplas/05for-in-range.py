nomes = 'Alvaro', 'Vitor', 'Gustavo', 'Jose'

for nome in range(0, len(nomes)):
    print(nome+1)

'''
    O que ocorre neste trecho de código?
    1. A variável "nomes" é uma lista contendo os nomes dos alunos: Alvaro, Vitor, Gustavo e Jose.
    2. O laço for percorrendo a variável "nomes", utilizando um índice (numero).
       - Para cada iteração do laço, o valor do índice é impresso na tela.
    3. A função "len()" retorna o número de elementos da lista "nomes".
       - Portanto, o limite superior do intervalo definido para o laço for é o comprimento da lista "nomes".
           -> Isso significa que o loop vai rodar até o final da lista, imprimindo todos os números de 1 a 4.
    4. A saída esperada deste trecho de código seria:
       1
       2
       3
       4
'''