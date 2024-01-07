algo = input('Digite algo: ')

print('Tipo primitivo é:', type(algo))
print('O {} Tem a primeira letra maiuscula?'.format(algo), algo.istitle())
print('O {} Tem numeros?'.format(algo), algo.isnumeric())
print('O {} Possui apenas letras maiúsculas?'.format(algo), algo.isupper())