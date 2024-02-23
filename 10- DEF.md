## def:

### função "def" em Python
-  A palavra-chave def é usada para definir uma função em Python. Uma função é um bloco de código que é executado quando é chamado pelo seu nome.

#### Exemplo:
```python
def linha():
    print("-=-" * 15)

nome = input('Digite seu nome: ')

linha()
print(f'Seja bem vindo(a) {nome}!')
linha()
```
No exemplo acima, defini uma função para exibir uma linha entre a mensagem acima e abaixo dela. Como não há uma função específica em Python para fazer isso, criei uma usando `def`.

#### Soma de Dois Números

Este é um simples exemplo em Python que demonstra a definição e uso de uma função para calcular a soma de dois números.

##### Como Funciona:

O programa define uma função chamada soma que recebe dois números como parâmetros, os soma e imprime o resultado.

#### Exemplo:
```python
def soma(a, b):
    soma = a + b
    print(soma)

soma(3, 5)
soma(6, 5)
soma(12, 5)
soma(24, 5)
```

#### Mensagem Entre Linhas

Este é um simples exemplo em Python que demonstra a definição e uso de uma função para exibir uma mensagem entre linhas de traços para destacá-la visualmente.

##### Como Funciona:

O programa define uma função chamada mensagem que recebe uma mensagem como parâmetro. A função então imprime a mensagem entre linhas de traços para enfatizá-la.

#### Exemplo:
```python
def mensagem(msg):
    print('-=-' * 20)
    print(msg)
    print('-=-' * 20)
    
mensagem('Python Descomplicado')
```