'''
    No codigo abaixo basicamente é uma tabuada mais "simplificada" e pratica
'''

while True:
    numero = int(input('Digite algum numero: '))
    if numero < 0:
        break
    print('-=-' * 20)
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero*c}')
    print('-=-' * 20)
print('-=- ENCERRADO -=-')