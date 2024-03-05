## Módulos

Na área de módulos, agora iremos usar algumas importações básicas do Python para criarmos comandos e funções com eles e entender o porquê são importantes em grandes casos

No Python, você pode importar uma biblioteca inteira ou apenas uma função dela. Nesse caso, eu irei usar a biblioteca de matemática chamada `"math"`, e dentro dela existem várias funções matemáticas que podemos usar sem criar muitos códigos. Por exemplo, ao invés de criar um código inteiro para tabuada ou raiz quadrada, eu posso ocupar poucas linhas apenas usando a biblioteca `math` no código. Lembrando que se eu importar apenas `"math"`, estarei importando TUDO que está dentro da biblioteca. Mas para eu usar apenas uma função da biblioteca math de raiz quadrada, irei usar apenas o `"sqrt"`.

Então, usarei:
```python
from math import sqrt
```
Nesse caso, estou pegando apenas a função de raiz quadrada para dentro do meu código, possibilitando usar apenas ela. Mas caso você queira usar a biblioteca math toda, é só usar:
```python
import math
```
E quando você estiver escrevendo seu código e precisar de alguma coisa dela, você poderá usar tranquilamente.

O `from` é usado apenas para especificar o que e qual função você quer da tal biblioteca.

A biblioteca math, como você pode ver, tem a funcionalidade `sqrt`, porém existem várias outras funções. Afinal, ela é uma biblioteca com várias funções que podem ser aproveitadas em vários códigos.

### Funções:

A biblioteca padrão do Python chamada `math` possui diversas funções matemáticas. Algumas das principais são:
- `acos(x)` : Retorna o arco cosseno de x (número real) obtido em radianos.
- `asin(x)` : Retorna o arco seno de x obt
- `atan(x)` : Retorna o arctangente de x obtido em radianos.
- `ceil(x)`  : Arredonda um número real `x` para cima (`inf`)
- `cos(x)`   : Calcula o coseno de x obtido em radianos.
- `degrees(x)`: Converte x de radianos para graus.
- `exp(x)`    : Calculo a exponencial de x.
- `floor(x)`  : Arredonda um número real `x` para baixo (`-inf`).
- `log(x[, base])`: Retorna o logaritmo natural ou de base `base` de `x`.

entre outros.

<hr>

#### Codigo:
**[Raiz Quadrada SQRT](./4-%20Módulos/01sqrt.py)**

Veja que diferente do codigo "**[Raiz Quadrada sem import](./2-%20Tipos%20Primitivos/06raiz-quadrada.py)**" Foi bem simples de utilizar. Eu não precisei fazer um comando completo para obter o resultado da raiz quadrada, pois a função `sqrt` já faz tudo para mim.

**[Embaralhar nomes](./4-%20Módulos/02embaralhar-nomes.py)** - Usamos livraria random.

**[Sortear um nome](./4-%20Módulos/03sorteando-um-nome.py)** - Usamos livraria random.

<hr>
Recomendo que você entre e estude mais sobre as importações e funções delas no site do Python e em outras comunidades.
<hr>
