'''
    No codigo abaixo simplesmente é baseado em um sistema
    de cadastro de fidelidade de um restaurante
    para um cliente, onde o funcionario tem acesso e deve colocar
    seu usuario e senha
'''

from time import sleep

print('[ Bem vindo(a) ao painel de registro de fidelidade de Cliente ]');sleep(1)
print('[ Por Favor insira abaixo as informações solicitadas: ]')

lista_nomes = ['Alvaro', 'Ana', 'Bruno']
senha = ['321654']
while True:
    check_nome = input('Digite seu nome: ').strip().capitalize();sleep(1)
    while check_nome not in lista_nomes:
        print('[ PROCESSANDO... ]');sleep(3)
        print('Nome de funcionario incorreto! Tente novamente.')
        check_nome = input('Digite seu nome: ').strip().capitalize();sleep(1)
    else:
        print(f'Nome de funcionario "{check_nome} Confirmado!"')

    check_senha = input('Digite a senha: ');sleep(1)
    while check_senha not in senha:
        print('[ PROCESSANDO... ]');sleep(3)
        print('Senha Incorreta! Tente novamente.')
        check_senha = input('Digite a senha: ');sleep(1)
    else:
        print('Senha Correta! Acessando o sistema...');sleep(2)
        perguntar_cadastro = input(f'Funcionario {check_nome} Deseja cadastrar um cliente?\n[1] | SIM\n[2] | NÃO\n[OPÇÃO]: ')

    if perguntar_cadastro == '1':
        print('Preencha os dados do cliente:')
        cadastrar_nome = input('Cadastrar nome: ')
        cadastrar_idade = input('Cadastrar idade: ')
        cadastrar_cidade = input('Cadastrar cidade: ')
        print('[ PROCESSANDO... ]');sleep(3)
        print(f'Nome: {cadastrar_nome}')
        print(f'Idade: {cadastrar_idade}')
        print(f'Cidade: {cadastrar_cidade}')
        perguntar = input('Os dados estão corretos?\n[1] | SIM\n[2] | NÃO\n[OPÇÃO]: ')
        while perguntar == '2':
                print('Preencha os dados do cliente:')
                cadastrar_nome = input('Cadastrar nome: ')
                cadastrar_idade = input('Cadastrar idade: ')
                cadastrar_cidade = input('Cadastrar cidade: ')
                print('[ PROCESSANDO... ]');sleep(3)
                print(f'Nome: {cadastrar_nome}')
                print(f'Idade: {cadastrar_idade}')
                print(f'Cidade: {cadastrar_cidade}')
                perguntar = input('Os dados estão corretos?\n[1] | SIM\n[2] | NÃO\n[OPÇÃO]: ')
        else:
            if perguntar == '1':
                print('Dados salvos com sucesso!\nVocê será redirecionado para a tela principal em 5 segundos.');sleep(5)
            elif perguntar == '2':
                print('Cadastro finalizado!')