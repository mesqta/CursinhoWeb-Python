'''
    O mesmo codigo porém com a função DEF
'''

def linha():
    print('-=-' * 10)

while True:
    linha()
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
        
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resposta == 'N':
        break
print('Terminado!')