'''
    Funções de manipulação de texto e suas devidas funções
'''

nome = str(input('Digite um nome: ')).strip()

print(f'Nome normal: {nome}')
print(f'Nome tudo maiúsculo: {nome.upper()}')
print(f'Nome tudo minúsculo: {nome.lower()}')
print(f'Nome com apenas a primeira letra maiúscula: {nome.capitalize()}')
print(f'Nome com as iniciais em maiúsculo: {nome.title()}')