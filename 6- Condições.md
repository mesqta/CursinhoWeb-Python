## Condições:

### Condições - Expressões Relacionais:
- `==` Igual a
- `!=` Diferente de
-  `>=` Maior ou igual a
- `<=` Menor ou igual a
-  `>` Maior que
-  `<` Menor que
### Condições - Expressões Lógicas:
-  `and`: Se ambas as condições forem verdadeiras
-  `or`: Se alguma das condições for verdadeira
-  `not`: Nega uma condição

<hr>

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