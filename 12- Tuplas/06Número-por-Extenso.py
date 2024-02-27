'''
    Ao inves de criar uma Tupla voce pode usar a biblioteca num2words
    para converter os numeros em palavras
    para instalar esta biblioteca basta abrir o terminal e digitar: pip install num2words
    e depois de instalado basta utilizar as importações
'''

from num2words import num2words

while True:
    numero = int(input('Digite um numero de 0 ate 20: '))
    numero_ptbr = num2words(numero, lang='pt-br')
    if numero > 19:
        print('Voce só pode colocar um numero de 0 até 20')
    else:
        print(f'Voce digitou {numero_ptbr}')

'''
    Crie uma variavel igual a primeira porém que tenha "pt-br" nela para identificar
    depois chame a função num2words e entre parenteces chame a sua variavel "numero"
    e depois coloque a lingua como pt-br como no codigo acima.
    Depois crie um paramentro para verificar se a pessoa digitou um numero acima do que
    voce determinou no codigo
'''