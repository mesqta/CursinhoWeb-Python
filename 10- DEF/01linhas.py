'''
    deifnimos uma função de mostrar linha em um codigo
    lembrando que o codigo abaixo começa de baixo pra cima
    definimos a função "mostrarlinha" para usarmos em outros lugares do codigo
'''

def mostrarlinha():
    print('-=-' * 10)
    
nome = input('Digite seu nome: ').strip()

mostrarlinha()
print(f'Seja bem vindo(a) {nome}')
mostrarlinha()