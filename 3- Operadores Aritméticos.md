## Operadores Aritméticos

Abaixo, eu deixarei uma lista de operadores aritméticos usados em Python, junto com as funções deles

### Operadores:
```python
+ : Adição 
- : Subtração
* : Multiplicação
/ : Divisão
// : Divisão Inteira (quebra para baixo)
% : Resto da divisão (quebra para cima)
** : Potência
```

No caso acima, esses operadores são operadores aritméticos e eles precisam de operandos para funcionar. No caso, eu irei deixar números na frente deles para operar. No caso, irei colocar o operando 5 na frente deles, mas pode ser qualquer outro número ou até mesmo variáveis que contenham números. Mas nesse caso, eu irei usar apenas números. Mas ainda não terminei de explicar. E no caso abaixo, eles são operadores binários, então irei colocar mais outro número porem na frente deles, que no caso, número 2. E um operador binário precisa de dois operandos.

### Operandos:
```python
5+2 = 7
5-2 = 3
5*2 = 10
5/2 = 2.5
5//2 = 2
5%2 = 1
5**2 = 25
```
<hr>

### Ordem de Precedencia:
Quais são os operadores executados em sequência? Em primeiro lugar? Veja abaixo a ordem de precedência:
```python
Primeiro: ()
Segundo: **
Terceiro: * / // %
Quarto: + -
Quinto: << >> & ^
Sexto: < <= > >= != ==
(Nenhum outro operador tem prioridade acima disso.)
```
No exemplo abaixo, eu irei fazer alguns códigos simples com a ordem de precedência:
```python
5 + 3 * 2 = 9
# Primeiro ocorre a multiplicação e depois a adição
5 - 3 * 2 = -4
# O Python segue a regra da ordem de precedência
5 + 3 * 2 - 4 = 8
# Aqui ele executa a multiplicação, depois a adição e por fim a subtração
5 / 3 * 2 = 6.6
# Ele começa pela divisão e vai até encontrar um resultado final ou outro operador que tenha mais prioridade
5 // 3 * 2 = 4
# Ele começa pela divisão inteira e vai até encontrar algo que possa ser dividido novamente
5 % 3 * 2 = 2
# Ele começa pela modulo (resto) e vai até encontrar algo para calcular o módulo
5 ** 3 = 125
# Ele calcula a exponenciação do número antes de qualquer outro cálculo
5 + (10 + 4) ** 2 = 29
# Ele executa as operações dentro dos parênteses antes das outras
```
<hr>

### Comandos:
**[Script: Antecessor e Sucessor](./3-%20Operadores%20Aritméticos/01antecessor-sucessor.py)**

**[Script: Aritimetica](./3-%20Operadores%20Aritméticos/02aritmetica.py)**

<hr>