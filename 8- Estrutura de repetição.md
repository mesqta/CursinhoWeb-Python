## Estrutura de laço:

### O que você deve saber sobre Estrutura de laço em Python:
- Laços são usados para repetir um trecho de código várias vezes.
- Existem dois tipos de estruturas de laço no Python: `while` e `for`.
---
#### função "for" e "in":
Na frente do "`for`", você pode colocar qualquer nome, pois é uma variável. Na frente da sua variável vem o "`in`", que significa "`no`" em português, e depois você abre e fecha parênteses e dois pontos "`:`".
### Exemplo:
```Python
for contagem in range(0,11):
    print(contagem)
print('fim')
```
Na frente do "`in`", eu coloquei o "`range`", que significa "`intervalo`", e logo em seguida eu pedi para a máquina o seguinte:

"Laço Contagem no intervalo de 0 até 11" (no caso, vai até 10).

Então, eu pedi para a máquina fazer uma contagem do 0 até o 10.

---
Caso eu queira contra de trás para frente basta eu usar `-1` no final do comando

#### Contagem regressiva:
```Python
for contagem in range(10, 0, -1):
    print(contagem)
print('fim')
```
#### Outros exemplos:
Ele vai contar de 0 até 10 pulando de 2 em 2:
```Python
for contagem in range(0, 11, 2):
    print(contagem)
print('fim')
```
A máquina pede para digitarmos um número e a partir do número digitado ele irá contar:
```Python
n = int(input('Digite um numero: '))

for c in range(0, n):
    print(c)
print('fim')
```
Eu crio uma outra váriavel dentro do `for` e peço para mostrar uma mensagem em `X` vezes:
```Python
for c in range(0, 11):
    msg = input('Escreva algo: ')
print('Fim')
```

## Comandos:
**[Contagem Regressiva](./8-%20Estrutura%20de%20repetição/01contagem-regressiva.py)** - Comando de contagem regressiva do 10 até o 0

**[Contagem Progressiva](./8-%20Estrutura%20de%20repetição/02contagem-progressiva.py)** - Contagem progressiva.

**[Contagem Input](./8-%20Estrutura%20de%20repetição/03contagem-input.py)** - Input pede algo para ele. repetir X vezes.

**[Contagem Input](./8-%20Estrutura%20de%20repetição/04repetição-msg.py)** - Repete a msg X vezes.