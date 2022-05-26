# Python_generalConcepts

:us: Introduction general concepts of Computer Science and Python.

:brazil: Introdução de conceitos gerais de Ciência da Comptuação e Python.

# Lógica de Programação
## Introdução a Ciência da Computação
### Evolução dos Computadores

* 1ª Geração (1940 – 1959) 
   * ENIAC era destinado apenas para funções de cálculo, pesava 30 toneladas e ocupava 180m².
   * Problemas com superaquecimento dos componentes, ao invés de microprocessadores eles utilizavam grandes válvulas elétricas e resistores que consumiam cerca de 200 mil Watts de energia.
   * Não continham linguagem padronizada, cada máquina possuía seu próprio código.  
 
![ENIAC](https://user-images.githubusercontent.com/101336111/170498375-0983d61a-88e5-4e15-9973-373d7ea031bd.jpg)

* 2ª Geração (1959 – 1965)
   * Criados em 1047, os transistores passaram a serem utilizados na construção dos novos computadores. Sua base é o silício, utilizado hoje dia em placas e componentes eletrônicos.
   * O IBM7094 pesava 890 kg e sua primeira instalação foi em dezembro de 1959.
   * Mais de 180 instruções que permitem executar operações aritméticas.

![ibm7094](https://user-images.githubusercontent.com/101336111/170499346-c80dcb59-7e56-4c5e-a275-647820380f64.JPG)

* 3ª Geração (1965 – 1970)
   * Evolução dos semicondutores de silício aumenta a velocidade e eficiência dos computadores.
   * Surgiram os teclados para digitalização de comandos.
   * Monitores que permitiam a visualização de sistemas operacionais (primitivos).
   * Capacidade de upgrades nos computadores.

![IBM360](https://user-images.githubusercontent.com/101336111/170499395-f0435f11-c4f8-4805-841a-a413a1699aba.jpg)

* 4ª Geração (1971 - Atualmente)
   * Utilização dos microprocessadores, pequenos chips de controle e processamento que modificou a história da computação.
   * Intel lançou o primeiro microprocessador, o Intel 4004 em 1971.
   * O Apple I em 1976 foi o primeiro computador pessoal a ser vendido totalmente montado.

![appleI](https://user-images.githubusercontent.com/101336111/170499415-41ba839c-c609-4c19-9925-4e64fa8c9b5a.jpg)

* Supercomputadores 
   * Tem altíssima velocidade de processamento e capacidade de memória.
   * São utilizados em aplicações que demandam grande quantidade de processamento, como desenvolvimento científico, aeroespacial e militar.

![columbia](https://user-images.githubusercontent.com/101336111/170499448-ba7b8a34-566d-472d-b70f-87023ea6c418.jpg)

* Hoje em dia
   * Processadores multi-core.
   * Computação de portátil com os celulares e tablets.
   * Facilidade de transporte dos Notebooks.
   * Armazenamento e compartilhamento de informações na Nuvem.
   * Internet e globalização das informações.

![computadoratual](https://user-images.githubusercontent.com/101336111/170499496-42d01874-12f4-4e9b-820e-47490de3180f.jpg)

### Software e Hardware

* O hardware é a parte física de um computador
* São as placas de circuitos elétricos projetadas com materiais e componentes eletrônicos.
* É a unidade central de processamento, memória e dispositivos de entrada e saída.
* Periféricos como monitor de vídeo, mouse e teclado são tipos de hardware.
* O software é um conjunto de informações que faz com que o computador execute determinada tarefa.
* É a inteligência embarcada de um computador.
* Controla as ações no hardware.
* É desenvolvido por meio de algoritmos de programação.

### Algorítmo

* É definido como uma sequencia finita de ações executáveis.
* Na ciência da computação, é representado por um código em uma linguagem de programação.
* Pode ter a finalidade de solucionar determinados problemas.
* Suas ações são executadas ordenadamente.
* Diferentes algoritmos podem ter a mesma funcionalidade, porém terem diferentes complexidades computacionais.
* Pode ser estruturado através de um fluxograma de ações.
* Existem diferentes níveis de aplicação e diferentes linguagens de programação.

### Linguagens de Programação

* Conjunto de regras para implementação de um código fonte que pode ser compilado e transformado em um programa de computador.
* Linguagens de alto nível são escritas por programadores e posteriormente compiladas para linguagem de baixo nível que são interpretadas e executadas pelo microprocessador.
* Baixo nível (alguns exemplos)
   * Linguagem de máquina
   * Linguagem Assembly
* Alto nível (alguns exemplos)
   * C/C++
   * Java
   * MatLab
   * Python
   * R
   * Basic

## Introdução ao Python
### Ambiente de programação

* Local onde iremos escrever as instruções que serão executadas pelo programa.
* Compila o programa e exibe seus resultados.
* Possibilita execução linha por linha para a verificação da lógica e possíveis erros (breakpoints).
* Importar arquivos e bibliotecas.
* Explora os valores e tipos das variáveis compiladas.
* Imprime as imagens geradas pelo algoritmo.
* Através do Anaconda Prompt podemos executar linhas de comando e instalar e remover bibliotecas de funções.

### Tipos de variáveis e dados

* Variáveis numéricas
   * int: números inteiros.
   * float: números com casa decimal.
   * complex: números com parte real e imaginária.
* Cadeia de caracteres
   * string: é uma sequencia de caracteres endereçada e imutável com características:
      * Vazia (“”)
      * Indexação
      * Concatenação
* Lista
   * Sequencia ou coleção ordenada de elementos/itens identificados por um índice.
   * Diferentemente das strings, seus itens podem ser de tipos diferentes.
   * Seus elementos são delimitados por colchetes.
* Tupla
   * Uma lista imutável e pode conter vários elementos que são delimitados por parêntesis.
* Dicionário
   * É um tipo de coleção de elementos indexados na forma de mapeamento X.Y entre chaves {}.
   * X é o índice e Y é o valor associado a este índice.
   * Conceito de chaves e valores.
   * Dado um dicionário "Exemplo{...}":
      * Exemplo.keys(): retorna todos os índices (keys).
      * Exemplo.values(): retorna todos os valores (values).
* Conjunto 
   * Pode ser formada por vários elementos, sua ordem é indefinida e não podem ser indexados.
   * É semelhante ao conceito de conjunto de matemática e pode ser realizadas operações de união e intersecção entre eles.
* Lista de intervalos inteiros
   * Range: é uma classe de dados que retorna uma lista sequencial de um intervalo de números inteiros
* Vetores e matrizes
   * Listas: em Python matrizes são representadas como listas de listas.
   * Cada lista corresponde aos elementos da linha de uma matriz.
   * Funções podem ser criadas para acessar os valores de cada matriz e também realizar operações entre elas.
* Numpy Array
   * O tipo de variável array é disponível na biblioteca Numpy e é muito utilizado para representar vetores e matrizes.
   * As funções da biblioteca Numpy possibilitam a matemática algébrica direta entre matrizes e vetores através dos seu comandos.

### Operadores em Python

* Aritiméticos
   * Operadores de soma `+` e subtração `-` de valores.
   * Divisão e multiplicação são representados por `/` e `*` respectivamente.
   * `//` Divide dois valores arredondando o resultado para baixo.
   * `%` obtém o resto da divisão.
   * `**` representa a exponenciação.
* Relacionais
   * Utilizados para comparar valores
   * `==` para verificar igualdade.
   * `!=` verifica se diferente.
   * `>` maior que.
   * `<` menor que.
   * `>=` maior ou igual a.
   * `<=` menor ou igual a.
* Atribuição
   * Muito utilizados em lógicas de looping.
   * `=` atribui um valor a uma variável.
   * `+=` recebe seu valor atual mais outro.
   * `-=` recebe seu valor atual menos outro.
   * A mesma lógica vale para `/=`, `//=`, `%=` e `*=`.
* Lógicos
   * Expressões Booleanas que caracterizam verdadeiro e falso, ou 0 e 1.
   * Operador `and` representa o “e” lógico.
   * `or` representa o “ou” lógico.
   * `not` representa o “não” lógico.

## Operação Condicional – IF / ELSE
### Estrutura de um algoritmo

* Um algoritmo deve seguir uma lógica de desenvolvimento de um problema que será definido pelo programador.
* O programa pode conter linhas de comentários para facilitar o entendimento.
* Inicialmente são carregadas as bibliotecas e os módulos que serão utilizados pelo algoritmo.
* O Python é sensível a indentação e a estrutura das funções deve respeitar esta regra.
* A sequência das linhas de comando corresponde a sequencia de ações definidas pelo programador para que o algoritmo execute sua finalidade.

### O comando if

* É definido como uma execução condicional conhecida como "se".
* Só é executado seu comando caso alguma condição seja satisfeita.
* Caso a condição não for satisfeita o programa "pula" a função `if` e segue sua sequência.
* Utiliza as operações relacionais e lógicas para definir uma condição.
* Estrutura
```
 if condição:
    comando
````
* Caso a condição seja satisfeita o programa "entra" na função `if` e executa a(s) linha(s) de comando(s) dentro da função.
* Após executar os comandos o programa segue a sequencia natural do algoritmo. 

### O comando else

* É a continuação do comando `if`.
* Pode ser traduzido como "senão".
* "Se" uma condição for verdadeira o programa deve executar os comandos dentro da função `if`, "senão" ele deve executar os comandos dentro da função `else`.
* Pode ser combinado várias vezes com o comando `if` através do `elif`.
* Estrutura
```
if condição:
    comando
elif condição:
    comando
elif condição:
    comando
.
.
.
else
    comando
```


## Operação Condicional – FOR / WHILE
### Conceito de loop

* Executar várias vezes uma ação até que sua condição de ativação não seja mais verdadeira.
* Conceito de realimentação da informação dentro de um bloco.
* A saída do bloco de ações se torna novamente a entrada do bloco formando um laço de repetição.
* Utilizamos este conceito quando necessitamos repetir uma determinada ação durante um período específico.
* Esta técnica elimina muitas linhas de código que teriam que ser escritas caso não utilizássemos o loop, reduzindo assim o custo computacional do algoritmo.

### O comando for

* Define uma regra ou um intervalo onde "para" uma condição satisfeita, deverão ser executados os comandos do bloco.
* Altera o valor da variável comparável a cada ciclo e compara novamente com a condição estabelecida.
* Possibilita utilizar um bloco `for` dentro de outro bloco `for`, quantas vezes for necessário.
* Estrutura
```
for variável in intervalo
    comando
```
   * A cada ciclo a variável é incrementada e caso a condição seja verdadeira o bloco é executado novamente.
* Estrutura com range
```
for variável in range(str, stp, ste)
    comando
```
   * Podemos definir o início `str` e o fim `stp` do intervalo, e o passo `ste` de cada ciclo.

### O comando while

* Executa uma sequencia de comandos “enquanto” uma condição for satisfeita.
* O programador é quem define a atualização da variável a cada ciclo dentro do bloco de comandos.
* Não é caracterizado por um intervalo, mas sim por uma condição.
* Estrutura
```
while condição:
    comando
```
* Blocos de repetição como `if`, `else`, `for` e `while` muitas vezes são utilizados em conjunto dentro de um mesmo bloco.
* Se a condição `while` nunca for falsa o código pode ficar em "loop infinito".

## Debate sobre Programação
### Aplicação de programação no cotidiano e Inteligência Artificial (AI)

* Onde temos programação presente nos objetos que usamos na nossa rotina?
* Como poderíamos aplicar programação para nos auxiliar em nossas atividades?
* A programação está presente em qual área profissional?
* Como as grandes empresas utilizam da Inteligência Artificial?
   * Amazon.
   * Google.
   * Apple.
   * Magazine Luiza.
   * Banco Bradesco.

## Funções
### Otimização ou re-fatoração de um código

* Muitos códigos podem ser escritos de forma mais clara e objetiva.
* Re-fatorar um código é reescrevê-lo alterando seus comandos, mas mantendo a mesma funcionalidade.
* Diminuir a complexidade computacional e aumentar o desempenho do código.
* Fazer com que o código fique mais adaptável a novas mudanças e alterações.
* Chamada de funções para executar algum padrão de ação característica do algoritmo.
* Utilização de bibliotecas específicas com comandos diretos da aplicação.

### Criando funções

* Funções são definidas dentro do algoritmo principal e executam uma lista de comandos quando são chamadas.
* Ela recebe um parâmetro, realiza os cálculos e retorna um valor para uma variável dentro do código principal.
* Muito utilizada durante a re-fatoração de um algoritmo.
* Funções podem retornar mais de um valor.
* Quando o algoritmo está dentro de uma função, variáveis locais são criadas para realizar os cálculos e retornar a resposta.
* Variáveis locais mantém seu valor apenas dentro da função e só existem enquanto a função estiver sendo executada.

### Debugar

* É um termo utilizado na ciência da computação que representa a ação de análise do código para verificar sua funcionalidade e possíveis erros de lógica.
* Ao debugar passo a passo um programa podemos encontrar e eliminar os “bugs” de execução.
* Utilizamos a função breakpoint para analisar uma parte específica do código.
* Podemos executar linha por linha e observar a evolução do valor das variáveis em cada momento do programa.
* É possível entrar dentro dos blocos de funções e executá-las comando por comando.
* Podemos sair de dentro dos blocos de funções e retornar ao algoritmo principal a qualquer momento.

## Matrizes em Python
### Manipulação de listas
