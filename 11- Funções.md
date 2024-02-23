## Interactive Help

- A "ajuda interativa" em Python, também conhecida como "Interactive Help", é uma ferramenta que vem integrada ao Python para ajudar os usuários a entenderem como usar diferentes funções e comandos na linguagem de programação Python.

- Imagine que você está aprendendo a cozinhar e tem um livro de receitas que explica como fazer diferentes pratos. A "ajuda interativa" em Python funciona de maneira semelhante. Quando você não sabe como usar uma função específica ou não entende o que um comando faz, pode pedir ajuda diretamente no próprio ambiente Python.

- Por exemplo, se você quiser saber como usar a função "print" para exibir uma mensagem na tela, pode simplesmente digitar `help(print)` no console do Python e pressionar Enter. O Python então mostrará informações sobre como usar a função "print" e o que ela faz. Essas informações são como as instruções em um livro de receitas que explicam como preparar um prato específico.

- Então, basicamente, a "ajuda interativa" em Python é uma ferramenta útil para aprender sobre as diferentes funções e comandos disponíveis na linguagem Python, fornecendo explicações e exemplos de uso diretamente no ambiente de programação.

## docstrings

- As "docstrings" em Python são basicamente strings de documentação, ou seja, são pedaços de texto que você pode adicionar dentro do seu código Python para documentar o que uma função ou classe faz. É como escrever um pequeno manual explicando como usar essa parte específica do código.

Por exemplo, se você escrever uma função que calcula a média de uma lista de números, você pode adicionar uma "docstring" logo abaixo da definição da função para explicar o que ela faz, como ela funciona e como deve ser usada.

```python
def calcular_media(lista):
    """
    Esta função calcula a média de uma lista de números.

    Parâmetros:
    lista (list): Uma lista de números.

    Retorna:
    float: A média dos números na lista.
    """
    total = sum(lista)
    media = total / len(lista)
    return media
```

Neste exemplo, a "docstring" está entre três aspas triplas (`"""`). Ela descreve o propósito da função, explica os parâmetros que ela recebe (no caso, uma lista de números) e o que ela retorna (a média dos números na lista).

As "docstrings" são muito úteis porque ajudam outros programadores (e até você mesmo no futuro) a entenderem o seu código mais facilmente. Além disso, algumas ferramentas e IDEs (Ambientes de Desenvolvimento Integrado) podem usar essas "docstrings" para gerar automaticamente documentação ou fornecer informações úteis durante o desenvolvimento.

## Argumentos opcionais

- Em Python, os argumentos opcionais são parâmetros de uma função que têm um valor padrão atribuído a eles. Isso significa que, quando você chama essa função, você pode optar por fornecer um valor para esses argumentos ou simplesmente deixá-los com seus valores padrão.

Por exemplo, vamos criar uma função chamada `saudacao` que recebe dois argumentos: `nome` e `saudacao_padrao`. O segundo argumento, `saudacao_padrao`, será opcional e terá um valor padrão de "Olá".

```python
def saudacao(nome, saudacao_padrao="Olá"):
    mensagem = saudacao_padrao + ", " + nome + "!"
    print(mensagem)
```
Aqui, `saudacao_padrao` é um argumento opcional porque ele tem um valor padrão definido como "Olá". Isso significa que se você chamar a função `saudacao` sem fornecer o segundo argumento, ele automaticamente usará "Olá" como saudação padrão.
```python
saudacao("Maria")  # Saída: Olá, Maria!
saudacao("João", "Oi")  # Saída: Oi, João!
```
Como você pode ver nos exemplos acima, ao chamar a função `saudacao`, você pode optar por fornecer ou não o segundo argumento (`saudacao_padrao`). Se não fornecer, a saudação padrão será "Olá". Se fornecer, a saudação padrão será substituída pelo valor fornecido.

Os argumentos opcionais são úteis quando você deseja que uma função tenha um comportamento padrão, mas também permita personalizações conforme necessário.

## Escopo de variáveis



## Retorno de resultados