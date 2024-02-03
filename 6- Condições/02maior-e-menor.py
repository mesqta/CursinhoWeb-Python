primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero: '))
terceiro = int(input('Terceiro numero: '))

menor = primeiro
# Maiores Valores
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

maior = primeiro
# Maior Valores
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')