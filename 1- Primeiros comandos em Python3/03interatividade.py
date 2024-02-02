# Agora irei usar a função 'input' para fazer a pergunta à pessoa
# O comando será: nome recebe input de 'Qual seu nome?'
nome = input('Qual seu nome? ')

# Nesse caso, a máquina vai perguntar e aguardar sua resposta para poder imprimir
# Agora iremos usar a função print para imprimir o nome que você colocou:
print(f'Seja bem-vindo(a), {nome}!')

# Por que tem um "f" antes das aspas simples e chaves e o nome da variável?
# O "f" antes das aspas simples e chaves indica que a string é uma f-string (formatted string literal). 
# F-strings são uma maneira de formatar strings de maneira mais simples e legível.
# Aqui é usado o conceito de Interpolação de Strings.
# então o nome da variavel dentro das chaves indica que ele vai imprimir nome que voce colocou nela.
# ou voce pode usar a função .format() ficando:
print('Seja bem vindo(a) {}'.format(nome))
# ambas tem a mesma função!