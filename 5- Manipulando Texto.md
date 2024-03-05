## Cadeia de Texto:
Na cadeia de texto, eu irei usar a frase "Python Descomplicado" para explicar melhor sobre as funcionalidades específicas dentro dos códigos em Python.

```python
frase = 'Python Descomplicado'
```
A forma que está escrita acima é a forma de atribuição de uma string dentro de uma variável.

Agora vamos para os segredos:

Quando fazemos esse tipo de atribuição, o Python armazena esses dados, no caso a frase, na memória do computador. Só que essa frase não vai inteira, e o que ele faz é criar pequenos espaços dentro da memória do computador, e dentro desses espaços ele vai colocar cada uma das letras.

Se você perceber, na frase acima tem apenas um espaço entre "Python" e "Descomplicado".

Voltando, cada um desses espaços que o computador cria, ele cria um índice do 0 até o tamanho do final da frase.

A frase "Python Descomplicado" tem 20 letras, contando do `0` até o fim dela.

<hr>

### Fatiamento:
```python
frase = 'Python Descomplicado'
```
Fatiar uma string significa pegar pedaços dela, porém no Python o fatiamento fica muito simples.

No exemplo abaixo, estou pedindo pelo caractere da posição `7` vá até o final. Então, basicamente, eu pedi para a máquina mostrar apenas o `"Descomplicado"`:
```python
frase = 'Python Descomplicado'

frase = [7]
```
No outro exemplo abaixo, estou pedindo para mostrar a mensagem do `0` até o `6`, que no caso apenas `"Python"`:
```python
frase = 'Python Descomplicado'

frase = [0:6]
```
No exemplo abaixo, estou pedindo para mostrar a mensagem do `0` até o `6`, porém pulando de `2` em `2`:
```python
frase = 'Python Descomplicado'

frase = [0:6:2]
```
No exemplo abaixo, estou pedindo para a máquina começar do início e terminar no `6`, então ele vai pegar apenas a frase `"Python"` e terminar por aí:
```python
frase = 'Python Descomplicado'

frase = [:6]
```
No exemplo abaixo, estou pedindo para começar do `6` até o final. Caso eu não saiba o final da `string`, então ele começa do `"Descomplicado"` até o final.
```python
frase = 'Python Descomplicado'

frase = [6:]
```
No exemplo abaixo, estou pedindo para o código começar do início e ir até o final. Por isso os dois "`::`". Em seguida, ele vai pulando de 3 em 3 até o final.
```python
frase = 'Python Descomplicado'

frase = [0::3]
```

<hr>

### Análise:

Analisar uma string é saber algumas informações sobre ela, como o tamanho dela, quantas letras ela tem, com que letra ela começa e com que letra ela termina, qual é a primeira palavra inteira, entre outros.

### Funções:

Função `len()` mostra quantos caracteres tem uma string:
```python
frase = 'Python Descomplicado'

print(len(frase))
terminal: 20
```
Função `count()` conta quantas vezes aparece um caractere ou uma substring na string. Se não encontrar nada retorna 0:
```python
frase = 'Python Descomplicado'

print(frase.count('o'))
terminal: 3
```
A mesma função, porém começando do índice 6 e indo até o final da frase, teremos apenas dois "o"s, pois o Python não considera o último número:
```python
frase = 'Python Descomplicado'

print(frase.count('o', 6, 21))
terminal: 2
```
Função `find()`, retorna a posição em que um elemento aparece na string (ou -1 se não encontrar):
```python
frase = 'Python Descomplicado'

print(frase.find('complicado'))
terminal: 10
```

### Transformação:
A função `replace()` substitui o valor de um caractere por outro:
```python
frase = 'Python Descomplicado'

print(frase.replace('Python', 'Android'))
terminal: Android Descomplicado
```
A função `upper()` transforma todas as letras para maiúsculas e `lower()` para minúsculas:
```python
frase = 'Python Descomplicado'

print(frase.upper())
terminal: PYTHON DESCOMPLICADO
```
```python
frase = 'Python Descomplicado'

print(frase.lower())
terminal: python descomplicado
```

A função `capitalize()` deixa a primeira letra da frase em Maiúscula e as demais em Minúsculas:
```python
frase = 'Python Descomplicado'

print(frase.capitalize())
terminal: Python descomplicado
```
A função `title()` deixa a primeira letra de cada palavra em Maiúscula e as demais em Minúsculas:
```python
frase = 'Python Descomplicado'

print(frase.title())
```
A função `strip()` remove os espaços no começo e fim da string, além dos caracteres especiais (exceto os números):
```python
frase = 'Python Descomplicado'

print(frase.strip())
```
A função `rstrip()` remove os espaços vazios do final da string, enquanto `lstrip()` remove dos espaços vazios do começo:
```python
frase = 'Python Descomplicado'

print(frase.rstrip())
```
```python
frase = 'Python Descomplicado'

print(frase.lstrip())
```

### Divisão:

Vamos dividir strings usando a função `split()`. A função dela é focada em espaços em frases, então ela irá considerar apenas os espaços na mensagem. Basicamente, onde estiver espaços, ele vai criar uma divisão. Então, praticamente, em cada divisão que ele faz, a frase sempre recomeça do `0` ao `X` da mensagem.

```python
frase = 'Python Descomplicado'

print(frase.split())
terminal: ['Python', 'Descomplicado']
```

### Junção:

A função `join()` é usada para juntar uma lista de strings em um único string, separando-os com um caractere específico (padrão é espaço):
```python
frase = 'Python Descomplicado'

print('-'.join(frase))
terminal: Python-Descomplicado
```

<hr>

## Comandos:
**[Nomes](./5-%20Manipulando%20Texto/01nomes.py)** - Usei as mesmas funções que expliquei aqui.

**[Fatiamento](./5-%20Manipulando%20Texto/02fatiamento.py)** - Usei as mesmas funções que expliquei aqui sobre fatiamento.