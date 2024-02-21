'''
    Deixando o codigo mais pratico e usando a biblioteca de matematica "math"
    conseguimos importar uma função que já faz o calculo sem precisarmos escrever um codigo do zero
    a função "sqrt" é uma função da biblioteca math para fazer calculos de Raiz Quadrada
'''

from math import sqrt
numero = int(input('Escreva um numero: '))
raiz = sqrt(numero)

print(f'A raiz de {numero} é {raiz :.2f}')