# Função strip remove os espaços no começo e no fim da string.
nome = str(input('Digite algum nome: ')).strip()
# função lower transforma todos os caracteres em minúsculo, upper para maiúsculo e capital
print('Nome minúsculo:  {}'.format(nome.lower()))
# função upper é o contrário de lower 
print('Nome maiúsculo:  {}'.format(nome.upper()))
# função capitalize coloca a primeira letra do nome em maiúsculo e as outras em min
print('Primeira letra do Nome Maiúscula:  {}'.format(nome.capitalize()))
# função title pega todas as palavras do nome e coloca a primeira em maiúscula e as restantes em minis
print('Todas as Palavras com a Primeira Letra Maiúscula:  {}'.format(nome.title()))
# função count conta quantos caractéres estão na string e len serve pra contar quantas letras tem a frase
print('Quantas letras ao todo? {}'.format(len(nome)-nome.count(' ')))