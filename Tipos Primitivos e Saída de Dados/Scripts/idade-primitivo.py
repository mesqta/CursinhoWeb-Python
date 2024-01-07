nome = input('Qual seu nome?: ')
idade = input('Qual é sua idade?: ')

print('Seu nome é {} correto?'.format(nome), type(nome))
print('Voce tem: {} de idade'.format(idade), type(idade))
print('Tem letra maiuscula?: ', nome.istitle())
print('Tem numero?: ', idade.isnumeric())