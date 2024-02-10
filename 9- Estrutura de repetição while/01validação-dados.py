sexo = str(input('Informe seu sexo: [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('Sexo inválido. Tente novamente: [M/F]: ').upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')