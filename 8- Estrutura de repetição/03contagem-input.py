'''
    Mesma logica dos exemplos anteriores porém a pessoa digita um numero e a contagem começa desse numero
'''

from time import sleep
n = int(input('Digite um numero: '))
for c in range(0, n):
    sleep(1)
    print(c)
print('FIM')