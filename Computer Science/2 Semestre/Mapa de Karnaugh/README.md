# Mapa de Karnaugh (2 Variáveis)

Este projeto demonstra duas abordagens diferentes para a simplificação de funções lógicas usando o Mapa de Karnaugh para duas variáveis.

O foco principal é ilustrar o a performance entre um cálculo algorítmico (Simplificação) e a consulta direta a um cache pré-calculado (Dicionário), especialmente à medida que o número de variáveis de entrada cresce.

---

## Conceito e Estrutura

A classe `Kmap` aceita uma lista de 4 mintermos na ordem binária tradicional: `[m0, m1, m2, m3]`, que correspondem a $A'B', A'B, AB', AB$.

### 1. `resolve_for_2()` (Abordagem Algorítmica)

Este método executa o **cálculo da simplificação** em tempo de execução. Ele segue a lógica de agrupamento do K-map:

* **Busca:** Grupos de 4 $\rightarrow$ Grupos de 2 $\rightarrow$ Grupos de 1.
* **Vantagem:** Ocupa uma quantidade **minúscula** de memória, pois não armazena todas as soluções possíveis.
* **Desvantagem:** O tempo de execução (latência) aumenta logaritmicamente com o número de variáveis, pois o algoritmo se torna mais complexo (ex: Quine-McCluskey, Petrick).

### 2. `resolve_for_2_using_dict()` (Abordagem de Cache)

Este método converte a lista de mintermos em uma **chave numérica (decimal)** e a usa para consultar um dicionário (`DICT_KMAP_2`) que armazena a solução já simplificada.

* **Vantagem:** Velocidade de execução **quase instantânea** ($O(1)$) após a inicialização.
* **Desvantagem (Crítica):** O consumo de memória (cache) é **$2^{(2^N)}$**, onde $N$ é o número de variáveis.

---

## Performance entre Tempo e Espaço para mais variáveis

A escolha entre cálculo e cache é uma consideração fundamental em sistemas de lógica digital.

| Característica | Cálculo Algorítmico (`resolve_for_2`) | Consulta por Cache (`resolve_for_2_using_dict`) |
| :--- | :--- | :--- |
| **Memória (Espaço)** | **Muito Baixa** (Armazena apenas o algoritmo) | **Extremamente Alta** (Armazena $2^{(2^N)}$ soluções) |
| **Tempo de Execução (Latência)** | **Crescente** com $N$ (Maior para muitas variáveis) | **Constante** ($O(1)$ - Consulta imediata) |
| **Viabilidade para $N$ grande**| **Viável** (Mas lento para $N \ge 8$) | **Inviável** para $N \ge 8$ (Excesso de memória) |

### O Problema do Cache para Muitas Variáveis

O crescimento da memória de cache é o principal limitador para esta abordagem:

| Variáveis ($N$) | Combinações ($2^N$) | Entradas no Cache ($2^{(2^N)}$) | Tamanho Estimado do Cache (Strings) |
| :---: | :---: | :---: | :--- |
| **2** | 4 | $2^4 = 16$ | Pequeno (muito rápido) |
| **4** | 16 | $2^{16} = 65.536$ | Aceitável (rápido) |
| **8** | 256 | $2^{256} \approx 10^{77}$ | **Impossível** (Excede a memória do universo conhecido) |

**Conclusão:** Para simplificar funções lógicas com **muitas variáveis** (acima de $N=6$), o **cálculo algorítmico** (mesmo que mais lento) é a **única solução viável** devido às restrições de memória de armazenamento do cache.

---

## Como Executar

Simplesmente execute o arquivo Python:

```bash
python main.py