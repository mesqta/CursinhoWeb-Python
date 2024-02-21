nome = input('Digite o seu nome: ')

lista_nomes = ['Alvaro', 'Pedro', 'Ana']

if nome not in lista_nomes:
    print('Acesso negado!')
else:
    print(f'Seja bem vindo(a) {nome}')