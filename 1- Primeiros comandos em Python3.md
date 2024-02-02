## Primeiros comandos em Python3
## Olá Mundo:
**[Script: "Olá Mundo!"](./1-%20Primeiros%20comandos%20em%20Python3/01olá-mundo.py)**
<hr>

Para imprimir uma frase na tela na linguagem Python, usaremos a função `print()`. Aqui estão alguns exemplos de como usar essa função:
```python
print('Olá Mundo!')
```
Apenas nesta linha foi possível executar a função para imprimir uma mensagem dentro das aspas simples, o que gerou como resultado: `'Olá Mundo!'`. Podemos usar tanto aspas simples quanto aspas duplas para imprimir uma mensagem na tela, porém a grande maioria da comunidade usa apenas aspas simples.
<hr>

## Variavel
**[Script Variavel nome](./1-%20Primeiros%20comandos%20em%20Python3/02variavel.py)**
<hr>

Em Python e em qualquer tipo de linguagem de programação, podemos criar variáveis, que, no caso do exemplo abaixo, eu criei uma variável `'nome'` que em seguida recebe uma mensagem `'Alvaro'`. Podemos imprimi-la usando a função `print()` e dentro dos parênteses da função `print()` colocamos o nome da variável para chamá-la e imprimi-la. Você pode colocar qualquer tipo de nome em uma variável e dentro de uma mensagem que o Python vai imprimi-la:
```python
nome = 'Alvaroo'
print(nome)
```
Pode-se criar mais de uma variável e imprimi-las dentro de uma única função `print()`? Sim, podemos. Irei criar mais dois exemplos de como você pode fazer isso, mas para isso, eu irei manter a variável 'nome' com a mensagem do meu nome, no caso, `'Alvaro'`, e irei criar as variáveis `'peso'` e `'altura'`. Então, irá ficar:
```python
nome = 'Alvaroo'
peso = 55.54
altura = 1.50
print(nome, peso, altura)
```
ou:
```python
nome = 'Alvaroo'
peso = 55.54
altura = 1.50
print(nome)
print(peso)
print(altura)
```
Continuando, como você pode ver, eu criei 3 funções `print()` com cada nome das variáveis e uma contendo uma função `print()`, porém contendo os nomes das variáveis em sequência de vírgulas. Ambas funcionam, mas o que vale é a sua lógica e como você vai fazer o programa funcionar.

Veja que eu adicionei mais duas variáveis como eu disse e então elas vão receber e imprimir as informações dentro das aspas simples. E você me pergunta... como o computador salva essas informações? Simples, na memória RAM do computador.

Mas enfim, as variáveis não podem ter o mesmo nome e caso tenham, pode ocorrer um erro ou conflito no seu programa. Então, caso você queira adicionar uma variável semelhante a outra, basta você criar assim:
```python
nome = 'Alvaroo'
segundo_nome = 'Gleber'
print(nome, segundo_nome)
```
Você pode perceber que os números, que no caso estão na variável peso e altura, não possuem aspas simples, apenas números. Porque é exatamente isso que eu quero que a máquina imprima, então o nome sempre será aquilo que a variável armazenou.
## Interatividade
**[Script Interatividade](./1-%20Primeiros%20comandos%20em%20Python3/03interatividade.py)**
<hr>

Bom, agora usamos uma função chamada `input` onde ela é chamada para fazer a pergunta sobre a mensagem que você colocar nela. Por exemplo:

```python
qual seu nome?
qual sua idade?
```
E tudo o que você for respondendo, ela vai armazenando e depois você poderá imprimir as coisas que você escreveu nela usando sempre a função print.

Lembre-se que a função `input` inclui parênteses `()`, então o que você for escrever deve estar dentro deles junto com as aspas simples `('')`.
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