import random
nome = input('Qual seu nome? \nR: ')

maquina = input(f'Olá! {nome}, seja bem vindo(a), voce gostaria de ver algumas opções que eu tenho? \n(sim/nao) R: ')

if maquina.lower() == 'sim':
    escolher = input(f'Olá {nome}! tenho essas opções:\n 1- embaralhar nomes \n 2- Sortear um nome \n 3- Somar \nQual voce escolheria? \nR: ')
    if escolher == '1':
        print(f'{nome} escolheu a opção de embaralhar nomes!')
        print('Escreva 4 nomes:')
        Nome1 = str(input('Nome1: '))
        Nome2 = str(input('Nome2: '))
        Nome3 = str(input('Nome3: '))
        Nome4 = str(input('Nome4: '))
        lista = [Nome1, Nome2, Nome3, Nome4]
        random.shuffle(lista)
        print(f'Nomes embaralhados: {lista}')
    elif escolher == '2':
        print(f'{nome} Voce escolheu a opção de sortear um nome!')
        print('Escreva 4 nomes para ser sorteados')
        Nome1 = str(input('Nome1: '))
        Nome2 = str(input('Nome2: '))
        Nome3 = str(input('Nome3: '))
        Nome4 = str(input('Nome4: '))
        lista = [Nome1, Nome2, Nome3, Nome4]
        sorteado = random.choice(lista)
        print(f'O nome sorteado foi: {sorteado}')
    elif escolher == '3':
        print(f'{nome} voce escolheu a soma! digite algum numero para somar')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é: {soma}')

if maquina.lower() ==  'nao':
    print(f'Ok {nome}! :D')
else:
    print('Opcao invalida! Tente novamente.')