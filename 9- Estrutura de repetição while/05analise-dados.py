'''
    Nesse codigo estaremos realizando um cadastro de uma pessoa com tal idade e sexo
    com a repetição while
'''

while True:
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