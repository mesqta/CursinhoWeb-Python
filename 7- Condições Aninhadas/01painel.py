import math
from time import sleep

nome = input('Qual seu nome?: ').strip().capitalize()
idade = input(f'Otimo {nome}, agora qual é a sua idade?: ')
confirmar = input(f'Seu nome é "{nome}" e a sua idade {idade}? [sim/nao]: ').lower()

if confirmar == 'sim':
    pergunta = input(f'Seu nome é {nome} e voce tem {idade} anos, deseja continuar? [sim/nao]: ').lower()
elif confirmar == 'nao':
    print('Você pode voltar quando quiser.')
else:
    print('Resposta inválida.')
    
if pergunta == 'sim':
    painel = input('Otimo, voce gostaria de ver meu painel com 2 funções mátematicas? [sim/nao]: ').lower()
elif pergunta == 'nao':
    print('Você pode voltar quando quiser.')
else:
    print('Resposta inválida.')
    
if painel == 'sim':
    mostrar = input('[1] | SOMA\n[2] | RAIZ QUADRADA\n[OPÇÃO]: ')
    if painel == 'nao':
        print('Você pode voltar quando quiser.')
else:
    print('Resposta inválida.')
    
#  PAINEL COM FUNÇÕES MATEMÁTICAS
if mostrar == '1':
    print('Você escolheu a soma!')
    n1 = int(input('Primeiro numero: '))
    n2 = int(input('Segundo numero: '))
    soma = n1 + n2
    print('Calculando...')
    sleep(2)
    print(f'O resultado entre {n1} e {n2} é: {soma}')
    resultado = input('Resultado está certo? [sim/nao]: ').lower()
    if resultado == 'sim':
        print('Excelente!')
    elif resultado == 'nao':
        print('Desculpe, irei corrigir brevemente.')
else:
    print('Resposta inválida.')
#    PAINEL DA RAIZ QUADRADA
    if mostrar == '2':
        print('Você escolheu a Raiz quadrada!')
        num = int(input('Digite um numero: '))
        raiz = math.sqrt(num)
        print('Calculando...')
        sleep(2)
        print(f'A raiz quadrada de {num} é: {raiz :.2f}')
        print(f'A raiz quadrada de {num} para cima é: {math.ceil(raiz ) :.2f}')
        print(f'A raiz quadrada de {num} para baixo é: {math.floor(raiz) :.2f}')
        resultado = input('Resultado está certo? [sim/nao]: ').lower()
        if resultado == 'sim':
            print('Excelente!')
        elif resultado == 'nao':
            print('Desculpe, irei corrigir brevemente.')
    else:
        print('Resposta inválida.')