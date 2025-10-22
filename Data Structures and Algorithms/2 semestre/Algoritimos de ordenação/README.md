# CP1.2-Data-Structures-and-Algorithms

---

## Esse repositório é apenas para fins de estudo.

O programa implementa e compara a performance de três algoritmos clássicos de ordenação: **Bubble Sort**, **Insertion Sort** e **Quick Sort**. Além de realizar análises de desempenho medindo tempo de execução, número de comparações e número de trocas para diferentes tipos de dados de entrada.

---

# Sumário
- [Objetivo](#objetivo)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Algoritmos Implementados](#algoritmos-implementados)
- [CLOCK_MONOLITIC para analise de desempenho em milisegundos](#clock_monotonic-para-analise-de-desempenho-em-milisegundos)
- [Tipos de dados de teste](#tipos-de-dados-de-teste)
- [Análise](#analise)
- [Como Executar](#como-executar)
- [Rodando (windows ou linux)](#rodando-windows-ou-linux)

---

## Objetivo

Comparar empiricamente a eficiência dos algoritmos de ordenação através de:
- Medição de tempo de execução (em milissegundos)
- Contagem de comparações entre elementos

---

## Tecnologias Utilizadas

- **Linguagem:** C
- **Compilador:** GCC (ou compatível)
- **Bibliotecas:**
    - `stdio.h` - Entrada e saída
    - `stdlib.h` - Alocação de memória e funções utilitárias
    - `time.h` - Medição de tempo precisa
    - `string.h` - Manipulação de strings

---

## Algoritmos Implementados

### 1. Bubble Sort
- **Complexidade:** O(n²)
- **Tipo:** Algoritmo de comparação simples
- **Estabilidade:** Estável

<image src="exemplo1.png"></image>

### 2. Insertion Sort
- **Complexidade:** O(n²) no pior caso, O(n) no melhor caso
- **Tipo:** Algoritmo de inserção
- **Estabilidade:** Estável

<image src="exemplo2.png"></image>

### 3. Quick Sort
- **Complexidade:** O(n log n) em média, O(n²) no pior caso
- **Tipo:** Algoritmo de divisão e conquista
- **Estabilidade:** Não estável

<image src="exemplo3.png"></image>

<image src="exemplo7.png"></image>

---

## CLOCK_MONOTONIC para analise de desempenho em milisegundos
<image src="exemplo4.png"></image>

---

## Tipos de Dados de Teste
O programa testa os algoritmos com quatro tipos diferentes de arranjos de dados:

1. **Sorted (Ordenado):** Elementos já em ordem crescente
2. **Half-sorted (Meio ordenado):** Elementos quase em ordem crescente
3. **Reverse (Reverso):** Elementos em ordem completamente invertida
4. **Random (Aleatório):** Elementos dispostos aleatoriamente

<image src="exemplo6.png"></image>

---

## Análise dos resultados
### Bubble Sort
- **Ideia:** percorre a lista várias vezes comparando elementos adjacentes e trocando quando necessário.
- **Uso ideal:** didático, útil apenas em listas muito pequenas.

### Insertion Sort
- **Ideia:** simula como organizamos cartas na mão; insere cada elemento na posição correta de uma lista parcialmente ordenada.
- **Uso ideal:** listas pequenas ou quase ordenadas; também usado dentro de outros algoritmos.

### QuickSort
- **Ideia:** algoritmo de **divide e conquista**; escolhe um pivô, divide a lista em menores/maiores e ordena recursivamente.
- **Uso ideal:** listas grandes; muito eficiente e amplamente usado em bibliotecas padrão.

---

## Como Executar
- Configure os inputs no arquivo `main.c` (REP para repetições, N para tamanho do vetor)
- Compile o programa

<image src="exemplo5.png"></image>
- Execute o programa

### Compilação
```bash
gcc main.c -o main
```

### Rodando (windows ou linux)
````bash
./main
````