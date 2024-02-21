'''
    No codigo abaixo importamos uma biblioteca "random" com diversas funções nela
    que no caso ele randoniza uma lista de nomes em ordem
'''
import random
nome1 = str(input('Nome: '))
nome2 = str(input('Nome: '))
nome3 = str(input('Nome: '))
nome4 = str(input('Nome: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

print(f'Ordem: {lista}')