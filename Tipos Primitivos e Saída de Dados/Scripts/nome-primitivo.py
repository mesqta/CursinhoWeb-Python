nome = input('Escreva seu nome: ')

print('Seja bem vindo(a) {}'.format(nome), type(nome)) #O type vai verificar o tipo da string (nome)
print('O nome {} possui letra maiuscula?: '.format(nome), nome.istitle()) # Ele vai verificar se o que escrevemos tem letra maiuscula no começo