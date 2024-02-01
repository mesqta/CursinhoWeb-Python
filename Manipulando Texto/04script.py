nome1 = input('Qual nome da garota que voce mais ama Drigo?: ').strip()

if nome1 == 'nicoly':
    print('Drigo: oi {}, eu ainda te amo <3'.format(nome1))
    print('-=-' * 20)
else:
    resposta = input('Se não é uma e nem outra... quem é?: ').strip()
    if resposta == 'rola':
        r = input('Hm... então voce gosta de rola Drigo? :O... ')
        if r == 'sim':
            print('Ok... sem problemas')
        else:
            print('Voce é muito viado!')