## Condições:

### Condições - Expressões Relacionais:
- `==` Igual a
- `!=` Diferente de
-  `>=` Maior ou igual a
- `<=` Menor ou igual a
-  `>` Maior que
-  `<` Menor que

#### Exemplo de "`==`":
```python
num1 = 5
num2 = 3
if num1 == num2: # Se num1 for igual a num2, retornará True.
    print("Os números são iguais.")
else:
    print("Os números não são iguais.")
```
#### Exemplos de "">=" e "<=":
```python
num1 = 7
num2 = 4
if num1 >= num2: # Se núm1 for maior ou igual a núm2, retornará True.
    print(f"{num1} é maior ou igual a {num2}.")

Ou podemos usar o operador menor ou igual (`<=`) da seguinte maneira:

num1 = 7
num2 = 4
if num1 <= num2: # Se núm1 for maior ou igual a núm2, retornará True.
    print(f"{num1} é maior ou igual a {num2}.")

print(f"{num1} é menor ou igual a {num2}.")
```
#### Exemplos de "!="
```python
frase1 = "Eu amo Python."
frase2 = "Python é bom."
if frase1 != frase2: # Se frase1 for diferente de frase2, retornará True.
    print("As frases são diferentes.")
else:
    print("As frases são iguais.")
```
#### Exemplos de ">" e "<"
```python
n1 = 8
n2 = 3
if n1 > n2: # Se n1 for maior que n2, retornará True.
    print(f"{n1} é maior do que {n2}")
elif n1 < n2: # Senão se n1 for menor que n2, retornará True.
    print(f"{n1} é menor do que {n2}")
else:
    print(f"{n1} é igual a {n2}")
```
---
### Condições - Expressões Lógicas:
-  `and`: Se ambas as condições forem verdadeiras
-  `or`: Se alguma das condições for verdadeira
-  `not`: Nega uma condição
-  `in` : Verifica se um valor existe em uma lista. Ex.: `if x in y:`
- `not in` : Verifica se um valor não existe em uma lista. Ex.: `if x not in y:`

#### Exemplo de "`and`":
```python
x = 5
y = 6
z = 9

if x == 5 and y == 6:
    print("x é 5 e y é 6.")
```
#### Exemplo de "`or`":
```python
numero = int(input("Digite um número entre 0 e 10: "))

if numero == 0 or numero == 1 or numero == 7:
    print("O número é zero ou um ou sete.")
```
#### Exemplo de "`not`":
```python
frase = input("Diga algo: ")

if not "oi" in frase.lower(): # O .lower() serve para tornar a busca case insensível.
    print("Não tem o texto 'oi'.")
```
#### Exemplo de "`in`":
```python
x = [1,2,3]
y = "Olá"
z = True
print(f'{y} está em x? {y in x}\n')
print(f'"Olá" está em x? {"Olá" in x}\n')
print(f'True está em x? {z in x}\n')
```
#### Exemplo de "`not in`":
```python
nome = input('Digite o seu nome: ')

lista_nomes = ['Alvaro', 'Pedro', 'Ana']

if nome not in lista_nomes:
    print('Acesso negado!')
else:
    print(f'Seja bem vindo(a) {nome}')
```
---
### Situação:
Vamos supor que você está indo para a casa da sua avó. Nessa sua condição, você tem o ponto de partida, que no caso é o seu ponto de começo, e o seu destino que é a casa da sua avó.

E nessa sua ida, você tem dois caminhos para chegar na casa dela. Um tem um caminho mais estreito e o outro tem o caminho mais simples e rápido para chegar na casa dela. Veja que ambos chegam ao mesmo destino.

Se no caso você pegar o caminho 1 (mais estreito), você irá demorar a chegar na casa dela.

Senão, se você não pegar o caminho 1 (mais estreito), você irá fazer o caminho 2 (mais fácil).

Vou simplificar em um código:
```python
alvaroo.siga()

if alvaroo.siga():
    print('Voce seguiu o caminho mais estreito')
else:
    print('Voce seguiu o caminho mais fácil')
alvaroo.chegou()
```
O exemplo acima é chamado de condição.

Veja que o comando foi seguido em uma ordem de cima para baixo, mas nem sempre algum programa em Python segue essa lógica.

Outro exemplo:
```python
idade = int(input('Qual sua idade?: '))

if idade < 18:
    print('Você é menor de idade')
else:
    print('Voce é maior de idade')
```

## Comandos:
**[Adivinhação](./6-%20Condições/01adivinhação.py)** - Comando para adivinhar um numero que a maquina pensou.

**[Maior e Menor](./6-%20Condições/02maior-e-menor.py)** - Comando basico de identificar um valor alto e valor baixo.