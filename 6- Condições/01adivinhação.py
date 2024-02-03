import random
pensador = random.randint(0, 10)
numero = int(input('Tente adivinhar um numero de 0 a 10: '))

if numero == pensador:
    print('Parabéns! Você acertou o número!')
elif numero > 10:
    print('Voce só pode escolher entre 0 até 10')
else:
    print(f'Voce errou! eu pensei no numero {pensador}')