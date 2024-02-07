from time import sleep
nome = input('Qual seu nome?\nR: ').capitalize().strip()

lista_nomes = ['Alvaro', 'Eduardo', 'Rodrigo', 'Gabriel', 'Amanda']

if nome in lista_nomes:
    print('[ Acesso liberado! ]');sleep(1)
    opção = input(f'{nome} O que voce gostaria de fazer?\n[1] | Registrar nome\n[OPÇÃO]: ').lower()
    if opção == '1':
        print(f'Senhor(a) {nome} Voce escolheu a opção de registar um nome no Sistema Prisional');sleep(1)
        registrar_nome = input('Registrar Nome: ').capitalize().strip().title()
        registrar_idade = input('Registrar Idade: ').strip()
        registrar_cor = input('Registrar Cor: ').capitalize().strip()
        registrar_nacionalidade = input('Registrar Nacionalidade: ').capitalize().strip()
        registarar_estado = input('Registrar Estado: ').capitalize().strip()
        registrar_cidade = input('Registrar Cidade: ').capitalize().strip()
        print('-=-' * 20);sleep(1)
        print(f'Nome registrado: {registrar_nome}');sleep(1)
        print(f'Idade registrado: {registrar_idade}');sleep(1)
        print(f'Cor registrada: {registrar_cor}');sleep(1)
        print(f'Nacionalidade registrada: {registrar_nacionalidade}');sleep(1)
        print(f'Estado: {registarar_estado}');sleep(1)
        print(f'Cidade: {registrar_cidade}');sleep(1)
        print('-=-' * 20);sleep(1)
        pergunta_registro = input('O registro acima está correto?\n[sim/nao]: ').lower().strip()
        if pergunta_registro == 'sim':
            print('Registro concluido!')
        elif pergunta_registro == 'nao':
            print('Refaça o Registro!')
        else:
            print('Opção incorreta!')
    else:
        print('Opção incorreta, Tente novamente!')
else:
    print('[ Acesso negado! ]')