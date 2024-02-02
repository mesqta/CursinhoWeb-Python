## Tipos Primitivos
**[Script Interatividade](./2-%20Tipos%20Primitivos/01interatividade.py)**
<hr>

### Função input()
A função `input()` em Python é uma função integrada (built-in) que permite que um programa solicite entrada do usuário durante a execução. Quando esta função é chamada, o programa pausa a execução e aguarda o usuário inserir dados através do teclado. Após o usuário pressionar Enter, o que foi digitado é retornado como uma string.

Bom, agora usaremos a função `input` onde ela é chamada para fazer a pergunta sobre a mensagem que você colocar nela. Por exemplo:

```python
qual seu nome?
qual sua idade?
```
E tudo o que você for respondendo, ela vai armazenando e depois você poderá imprimir as coisas que você escreveu nela usando sempre a função `print()`.

Lembre-se que a função `input()` inclui parênteses `()`, então o que você for escrever deve estar dentro deles junto com as aspas simples `('')`.
```python
nome = input('')
```
fica:
```python
nome = input('Qual seu nome?: ')
```
ou:
```python
primeiro_nome = input('Qual seu nome?: ')
segundo_nome = input('Qual seu sobrenome?: ')
print(f'Seu nome é {primeiro_nome} e seu sobrenome {segundo_nome}.')
```

Então basicamente a função `print` vai imprimir o que está dentro das aspas, mas a função `input()`
pega o que estiver digitado na tela.
## Terminal:
```python
Qual seu nome?:
```
O usuario digita: Alvaroo
```python
Qual seu sobrenome?:
```
o usuario digita: Mesquita
```python
Terminal: Seu nome é Alvaroo e seu sobrenome Mesquita.
```
<hr>

Basicamente, as informações que você deu para a máquina foram armazenadas na memória e depois foram impressas para você usando a função `print()`.
<hr>
Agora, pegue esses exemplos e crie como você quiser as coisas que você precisa. No caso, irei criar uma função para perguntar meu nome, sobrenome, idade e peso. Tudo o que eu responder será armazenado e, quando chegar à função print, será impresso e mostrará o que você digitou.
<hr>

## Codigo:
```python
nome = input('Qual seu nome?: ')
sobrenome = input('Qual seu sobrenome?: ')
idade = input('Qual sua idade?: ')
peso = input('Qual seu peso?: ')
print(f'Seu nome é {nome} e seu sobrenome {sobrenome}')
print(f'Voce tem {idade} de idade e pesa {peso}')
```
Eu criei duas funções `print()` para não prolongar muito o código, mas irá funcionar do mesmo jeito e você pode fazer tudo em uma print só.
```python
print(f'Seu nome é {nome} e seu sobrenome {sobrenome}, voce tem {idade} de idade e pesa {peso}')
```
<hr>

## Comandos básicos:
**[Nome e Sobrenome](./2-%20Tipos%20Primitivos/02nome-sobrenome.py)** - Pega o nome e sobrenome e junta tudo.
**[Nome Sobrenome e cidade](./2-%20Tipos%20Primitivos/02nome-sobrenome.py)** - Quase a mesma coisa do de cima porém inclui a cidade.
<hr>

### Função int()
A função `int()` é chamada quando eu quero converter algum número para um número inteiro. Então, qualquer código que estiver dentro dos parênteses da função `int()` está sendo convertido para um número INTEIRO.

Os 4 tipos primitivos mais básicos que existem no Python são:
```python
int - Números inteiros
float - Números flutuantes
bool - Números booleanos
str - strings ou Caractere
```
### Exemplos:
```python
Númerios inteiros: 7 -8 10 102 154 (numeros em gerais)

Números Flutuante: 3.14 6.62 9.81 (numeros com casa decimal)

Bool: True False (valores booleanos)

String: 'Olá Mundo!' "Python é incrível!" (textos entre aspas simples ou duplas).
```
## Comandos básicos de soma:
**[Soma](./2-%20Tipos%20Primitivos/02nome-sobrenome.py)** - Soma Simples.

**[Tabuada](./2-%20Tipos%20Primitivos/05multiplicação.py)** - Tabuada Simples.
<hr>

### Método .format():

O método `.format()` é usado para formatar strings em Python. Ele permite inserir valores de variáveis dentro de uma string formatada, substituindo espaços reservados por valores reais. Os espaços reservados são representados por chaves `{}` na string e os valores são passados como argumentos para o método `.format()`.

### Exemplo:
```python
nome = "Alvaroo"
idade = 19
print('Olá, meu nome é {} e minha idade {}'.format(nome, idade))
```
f-strings (format strings):
```python
nome = "Alvaroo"
idade = 19
print(f'Olá, meu nome é {nome} e minha idade {idade}')
```
As `f-strings` são uma maneira mais recente e conveniente de formatar strings em Python, introduzidas a partir da versão 3.6. Elas permitem inserir valores de variáveis diretamente em uma string prefixada com f. Dentro de uma f-string, você pode inserir variáveis ou expressões diretamente entre chaves `{}`.