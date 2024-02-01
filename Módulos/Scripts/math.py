import math
numero = int(input('Digite algo: '))
raiz = math.sqrt(numero)

print('Normal: A raiz quadrada de {} é: {:.2f}'.format(numero, raiz))
print('Para cima: A raiz quadrada de {} é: {:.2f}'.format(numero, math.ceil(raiz)))
print('Para Baixo: A raiz quadrada de {} é: {:.2f}'.format(numero, math.floor(raiz)))