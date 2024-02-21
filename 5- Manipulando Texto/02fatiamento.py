'''
    Mesma logica do codigo anterior porém fatiando uma string
'''

frase = 'Olha meu irmão não fique dizendo ao pove por aí que chupa o meu cacete. Não que isso não é brincadeira não meio que você tenha feito, mas isso não é coisa para estar dizendo as pessoas não meu irmão'

print(f'Mostra quantos caracteres tem: {len(frase)}')
print(f'Mostra quandos "o" tem na frase: {frase.count('o')}')
print(f'Frase toda maiúscula: {frase.upper()}')
print(f'Frase todo em minúscula: {frase.lower()}')
print(f'Considera apenas espaços: {frase.split()}')