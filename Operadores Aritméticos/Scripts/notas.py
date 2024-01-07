aluno = input('Qual é o nome do aluno?: ')
bimestre1 = float(int(input('Primeira nota: ')))
bimestre2 = float(int(input('Segunda nota: ')))
nota = (bimestre1+bimestre2)/2

print(aluno, 'Nome do aluno tem letra inicial maiuscula?', aluno.istitle())
print('A nota do aluno {} foi de {}'.format(aluno, nota))