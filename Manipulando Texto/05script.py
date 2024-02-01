import random
nome = input('Qual seu nome?: ')

r = input('Máquina: Olá {}, como voce esta se sentindo? \nR: '.format(nome))
if r == 'feliz':
    print('Máquina: Que bom que voce esta feliz {}.'.format(nome))
else:
    r2 = input('Máquina: O que aconteceu? \nR: ')
    if r2:
        r3 = input('Máquina: Poxa... espero que voce supere essa sua tristeza! \nVoce quer fazer alguma coisa? \nR: ')
        if r3 == 'sim':
            adv = input('Otimo. vamos fazer uma coisa que eu criei? \nR: ')
            if adv == 'sim':
                print('vamos lá! \nEu criei um sistema de embaralhar 4 nomes')
                nome1 = str(input('Nome: ')).strip()
                nome2 = str(input('Nome: ')).strip()
                nome3 = str(input('Nome: ')).strip()
                nome4 = str(input('Nome: ')).strip()
                lista = [nome1, nome2, nome3, nome4]
                random.shuffle(lista)
                print('A ordem é: {}'.format(lista))
                adv2 = input('Voce gostou do jogo {}? '.format(nome))
                if adv2 == 'sim':
                    print('que bom que voce gostou :D')
                else:
                    print('Que pena... irei melhorar na proxima')
            else:
                print('Que pena... fiz um sistema muito legal mas enfim... se mate então :D')