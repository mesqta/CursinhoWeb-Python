'''
    No codigo abaixo basicamente ele junta todos os aprendizados
    criei um codigo que basicamente é um painel com 3 funções cada uma diferente da outra
    usando as condições aninhadas
'''

from time import sleep
from math import sqrt, ceil, floor
pergunta = input('Olá! Voce gostaria de ver meu painel matematico?\n[sim/nao]: ').lower()

if pergunta == 'sim':
    painel = input('[1] | SOMA SIMPLES\n[2] | RAIZ QUADRADA\n[3] | TABUADA\n[opção]: ')
    if painel == '1':
        print('Voce escolheu a opção de soma simples! Aguarde...');sleep(1)
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
        soma = n1 + n2
        print('Calculando...');sleep(1)
        print(f'A soma entre {n1} e {n2} é: {soma}')
    elif painel == '2':
        print('Voce escolheu a opção de Raiz Quadrada!')
        num = int(input('Numero: '))
        print('Calculando Raiz Quadrada...');sleep(1)
        raiz = sqrt(num)
        print(f'Raiz Quadrada de {num} é: {raiz :.2f}');sleep(1)
        print(f'Raiz Quadrada de {num} para cima é: {ceil(raiz):.2f}');sleep(1)
        print(f'Raiz Quadrada de {num} para baixo é: {floor(raiz) :.2f}');sleep(1)
    elif painel == '3':
        print('Voce escolheu a opção de tabuada! aguarde...');sleep(1)
        num = int(input('Tabuada do numero '))
        for n in range (11):
            print(f'{num} x {n} = {num*n}')
    else:
        print('Opção invalida!')
else:
    if pergunta == 'nao':
        print('Ok. Até mais! :D')
    else:
        print('Resposta inválida! Tente novamente.')