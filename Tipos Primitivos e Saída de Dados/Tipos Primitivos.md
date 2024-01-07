Toda linguagem de programação possui 4 tipos primitivos, e o Python não é diferente. No entanto, o Python tem mais do que esses 4 tipos, embora os 4 tipos que vou mostrar sejam fundamentais e importantes para a linguagem.

Input & Int:

No input, mesmo que tenhamos digitado um número dentro dele, ele não é considerado um número; é considerado uma string.

Agora, ao utilizar o int, tudo que está dentro dele é convertido para um número inteiro. Por exemplo:
```python
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

soma = numero1 + numero2
print('A soma é:', soma)
```
Agora, esteja ciente dos 4 primitivos:
```python
int - números inteiros
float - números reais ou de ponto flutuante
str - valores caracteres ou strings
bool - valores lógicos ou booleanos
```
Vamos pegar alguns exemplos de números inteiros:
```python
# Exemplos de int
inteiro_positivo = 7
inteiro_negativo = -4
inteiro_nulo = 0
grande_inteiro = 5410

# Exemplos de floats
flutuante_positivo = 4.5
flutuante_negativo = -15.543
flutuante_nulo = 0.056

# Exemplos de booleanos
verdadeiro = True
falso = False

# Exemplo de string
texto = 'Olá'

# Imprimindo os valores
print("Números inteiros:", inteiro_positivo, inteiro_negativo, inteiro_nulo, grande_inteiro)
print("Números flutuantes:", flutuante_positivo, flutuante_negativo, flutuante_nulo)
print("Booleanos:", verdadeiro, falso)
print("String:", texto)
```
```python
algo = input('Escreva algo: ')

print(algo, 'O tipo é: ', type(algo))
print(algo, 'Tem numeros?: ', algo.isnumeric())
print(algo, 'Tem letras?: ', algo.isalpha())
print(algo, 'Tem letras e numeros?: ', algo.isalnum())
print(algo, 'Tem numeros de 0 a 9?: ', algo.isdecimal())
print(algo, 'Possui todos as palavras em minúsculo?: ', algo.islower())
print(algo, 'Possui espaços apenas espaços em branco?: ', algo.isspace())
print(algo, 'Possui apenas letras maiúsculas?: ', algo.isupper())
print(algo, 'Possui a primeira palavra maiúscula e o restante minúsculas?: ', algo.istitle())
```