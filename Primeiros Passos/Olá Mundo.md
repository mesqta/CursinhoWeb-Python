# Introdução à Impressão de Mensagens em Python

Vamos supor que você queira imprimir mensagens na tela, como, por exemplo, o simples e prático `"Olá, Mundo!"`. Em qualquer linguagem de programação, você sempre começa por isso, é normal.

A primeira coisa que você deve entender em Python é que os dados podem ser demilitados de maneira específica. Por exemplo, "Olá, Mundo!" é composto por letras, números, acentos, vírgulas, e por aí vai. O demilitador padrão do Python são as aspas simples e aspas duplas. Você sempre vai abrir uma aspa no início e fechar a aspa no final da mensagem, por exemplo: `'Olá, Mundo'`. No entanto, você pode usar aspas simples ou duplas, mas a grande maioria das coisas em Python usa aspas simples.

Uma coisa simples e técnica é que todos os comandos são funções, e toda função deve ter parênteses. Na função `print`, estamos pedindo para a máquina imprimir ou escrever algo na tela "Olá, Mundo":

```python
print('Olá, Mundo')
```
A função `print()` é a principal forma de impressão de mensagens em Python.
- A palavra-chave `print` indica que o Python está pronto para imprimir algo no console (tela).
- O texto entre as aspas simples ou duplas é chamado de string e representa a mensagem que será impressa. Neste exemplo.
- As mensagens entre as aspas simples (`' '`) ou duplas (`" "`) são os
dados que serão impressos. Neste exemplo, `"Olá, Mundo"` é
a mensagem que será impressa.

# Apresentar numeros em Python
Os números não estão entre aspas em Python. Eu irei representar os dois números 50 e 40; você deve compreender que estes números são diferentes do "olá mundo" de cima. Eles não estão entre aspas duplas e aspas simples porque não são mensagens, são números. Mas qual a diferença entre mensagens e números? As mensagens são usadas para exibir informações na tela, enquanto números são utilizados para realizar cálculos.

Entre esses números `50` e `40`, podemos fazer uma operação. Iremos usar uma conta simples e somar os dois (`50 + 40`). Se você quiser exibir essa operação na tela, deverá chamar a função `print`.
```python
print('50 + 40')
```
e para voce chamar a função `print` sempre use `()` parênteses

agora veja a coposição das duas mensagens de 
```python
print('Olá, Mundo')
```
usamos aspas simples porque ele é uma mansagem
```python
print(50 + 40)
```
Um mostra uma mensagem de texto e outro mostra o resultado de um cálculo, e como ele é algo relacionado a números então você não pode usar aspas simples ou duplas.

Vou dar outro exemplo que muita gente faz.

Se você pegar o mesmo código
```python
print(50 + 40)
```
e coloca aspas simples em cada um nos nomeros e continuar com o operador de somar no meio, ficando: 
```python
print('50' + '40')
```
Esse código não irá dar erro, porém ele imprimirá os números no terminal. Sendo assim, ele não vai somar um e outro e sim juntar, tendo o resultado de `5040` no terminal.

voce deu o comando para a maquina da seguinte forma: `"me mostre 50 em seguida 40"`

E também, existe diferença entre usar o sinal de mais e uma vírgula. Haverá casos em que a vírgula funcionará melhor do que o sinal de mais, e vice-versa.

Agora, para somar de forma correta e obter o número do resultado da nossa soma que colocamos no código, usaremos:
```python
print(50+40)
```
e teremos o resultado de 90.

# Variaveis

Vamos querer registrar o nome, idade e o peso de uma pessoa. Abaixo estão as variáveis: `nome`, `idade` e `peso`

Observação: Para nomear e criar uma variável, é importante escrever tudo em minúsculo. O que estiver entre aspas pode ser escrito em maiúsculo, minúsculo, com ou sem espaços, entre outras coisas. Quando não estiver entre aspas, escreva sempre em letras minúsculas.

Agora, no caso do Python, toda variável é um objeto. Guarde esta informação, pois mais para frente, ao decorrer deste repositório, será importante, não agora, mas sim no futuro.

O objeto é um pouco mais que uma variável, ou seja, toda variável é um objeto para o Python. Toda variável pode receber valores ( `=` ), e esse `"recebe"` é simbolizado pelo sinal de igual. Então, abaixo, você está lendo:

"`nome recebe algo`"
"`idade recebe algo`"
"`peso recebe algo`"
Toda vez que você ler algum código que tem um sinal de igual, sempre vai ler algo como "recebe". Agora vamos voltar para o contexto de nome, idade e peso:

```python
nome = 'Alvaroo'
idade = 20
peso = 54.9
```
Agora vamos mostrar estes três valores na tela utilizando o print:
```python
print(nome, idade, peso)
```
Agora execute o código.

# Interatividade
Agora, vamos criar interatividade com o usuário. Vamos perguntar o nome, idade e peso da pessoa e, logo depois, usaremos o print para ter nossas respostas.

Para isso, iremos alterar algumas coisinhas do nosso código acima. Porém, para perguntar, receber e guardar a resposta, usaremos o `input` à frente do sinal de igual das nossas variáveis. Então, ficará assim:
```python
nome = input('Qual seu nome? ')
```
Vamos ler a linha: "`nome recebe o resultado de qual é seu nome`". Sendo assim, ele vai pedir seu nome e permitir que você digite, e vai guardar essa informação na variável "`nome`".
Agora vamos repetir para as duas últimas variáveis:
```python
idade = input('Qual sua idade? ')
peso = input('Qual seu peso? ')
```
O print continua sendo o mesmo: 
```python
print(nome,idade,peso)
```
Agora execute o código.
# Saída formatada
No Python 3, podemos formatar nossas mensagens usando a função `print`, como é o caso aqui.

Para isso, utilizamos as chaves `{}`, pois esse bloco será substituído pela formatação.

Vamos dar um exemplo:
```python
nome = input('Qual seu nome? ')
print('Seja bem vindo(a) {}'.format(nome))
```
para usar mais de uma chave, usamos do seguinte modo:

```python
nome = input('Qual é seu nome? ')
idade = input('Qual é a sua idade? ')

mensagem = ('Olá, bem vindo(a) {}, sua idade é {}, acertei?'.format(nome, idade))

print(mensagem)
```
No código acima, criei as `variáveis` junto com o `input` para a máquina receber as respostas e armazenar nas variáveis (`nome` e `idade`). Logo depois, criei outra variável de mensagem contendo os dados armazenados nas variáveis para, em seguida, imprimir no nosso terminal. Observe que usei mais de uma `chave`, pois incluí tanto o nome quanto a idade. Para utilizar dois `parâmetros`, basta usar uma `vírgula` e adicionar o segundo. No método format, utilizamos dentro dos parênteses o nome das variáveis conforme você as definiu. É bem simples.

agora vejamos com uma soma simples:
```python
numero1 = int(input('Primeiro numero: '))
numero2 = int(input('Segundo numero: '))

soma = (numero1+numero2)

print('A soma é {}'.format(soma))
```