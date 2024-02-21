'''
    A estrutura de repetição FOR é utilizada para realizar a iteração em um conjunto de dados
    ou seja, ela executa um bloco de código várias vezes
    no codigo abaixo é basicamente uma contagem regressiva
'''

from time import sleep
for contagem in range(10, 0, -1):
    sleep(1)
    print(contagem)
sleep(1);print('FIM')