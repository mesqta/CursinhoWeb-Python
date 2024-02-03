## Condições Aninhadas:

### O que você deve saber sobre condições aninhadas:

Basicamente, é uma condição em que, por exemplo, um `if` está dentro de outro `if`. No caso do Python e em outras linguagens de programação, você pode pegar uma estrutura condicional e colocar dentro de outra estrutura condicional.

Assim, permitindo você ter uma estrutura condicional alinhada.

#### Exemplo de código com condição aninhada:

**[Painel de Soma e Raiz Quadrada](./7-%20Condições%20Aninhadas/01painel.py)** - Nesse Script eu uso as `if`, `elif` e `else`.

<hr>

Vale lembrar que cada estrutura aninhada em Python sempre começa com um "`if`", nunca pode começar com "`elif`" ou "`else`". Você pode colocar quantos "`elif`" quiser dentro de um "`if`", mas pode usar apenas um "`else`" uma vez. Vale lembrar também que nem sempre haverá o "`else`".

Quando você utiliza "`elif`", o "`else`" é opcional.

#### Estrutura aninhada padrão:
```python
if python():
    bloco01
elif python():
    bloco02
else:
```
#### mais de uma `elif`:
```python
if python.des():
    bloco01
elif python.com():
    bloco02
elif python.pli():
    bloco03
elif python.cado():
    bloco04
else:
```
você nunca pode usar uma elif sem um if anterior!

<hr>

