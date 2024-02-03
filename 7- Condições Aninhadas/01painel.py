import math
nome = input('Qual seu nome?: ').strip().capitalize()
idade = input(f'Otimo {nome}, agora qual é a sua idade?: ')
confirmar = input(f'Seu nome é "{nome}" e a sua idade {idade}? [sim/nao]: ').lower()

if confirmar == 'sim':
    perguntar = input(f'{nome} Voce gostaria de ver meu painel matematico? [sim/nao]: ').lower()
    if perguntar == 'sim':
        painel = input('[1] | SOMA SIMPLES\n[2] | RAIZ QUADRADA\n[OPÇÕES]: ')
        if painel == '1':
            print(f'{nome} Voce selecionou soma simples!')
            n1 = int(input('Primeiro numero: '))
            n2 = int(input('Segundo numero: '))
            soma = n1 + n2
            print(f'O resultado entre {n1} e {n2} é: {soma}')
            feed = input('A soma esta correta? [sim/nao]: ').lower()
            if feed == 'sim':
                print('Muito bom, obrigado por confiar em mim.')
            elif feed == 'nao':
                print('Irei melhorar meu codigo :C')
        else:
            print('Opção invalida!')
        if painel == '2':
            print(f'{nome} Voce selecionou a Raiz Quadrada!')
            n1 = int(input('Digite um numero: '))
            raiz = math.sqrt(n1)
            print(f'A Raiz quadrada de {n1} é:  {raiz :.2f}')
            print(f'Para cima: {math.ceil(raiz) :.2f}')
            print(f'Para baixo: {math.floor(raiz) :.2f}')
            feed = input('Está correto? [sim/nao]: ').lower()
            if feed == 'sim':
                print('Que bom que meu comando está certo! :D')
            elif feed == 'nao':
                print('Então vou corrigi-lo em breve :v')
        else:
            print('Opção invalida!')
    elif perguntar == 'nao':
        print('Tudo bem, até mais!')
else:
    print('Você digitou errado tente novamente!')