#include<time.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//
// note-se que não foi usado nem o CLOCK_PER_SEC nem o algoritimo do quicksort que está no pdf, pois
// eu não consegui implementar o CLOCK_PER_SEC (meu antivirus apagava o arquivo e me impedia de fazer a analise)
// já o quicksort eu tentei fazer por conta própria para meios de estudo e desafio
//

#define REP 5
const unsigned short N[] = {1000, 5000, 10000}; // Máximo de 65535

long long comparacoes;

// Algoritimos de ordenação
void bubbleSort(int arr[], int n) {
    comparacoes = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            comparacoes++;
            if (arr[j] > arr[j + 1]) {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}

void insertionSort(int arr[], int n) {
    comparacoes = 0;
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0) {
            comparacoes++;
            if (arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            } else break;
        }
        arr[j + 1] = key;
    }
}

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int particiona(int arr[], int inicio, int fim) {
    int pivo = arr[fim]; // escolhe último elemento como pivô
    int i = inicio - 1;

    for (int j = inicio; j < fim; j++) {
        comparacoes++;
        if (arr[j] < pivo) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[fim]);
    return i + 1;
}

void quickSort(int arr[], int inicio, int fim) {
    if (inicio < fim) {
        int pivot = particiona(arr, inicio, fim);
        quickSort(arr, inicio, pivot - 1);
        quickSort(arr, pivot + 1, fim);
    }
}

// funções para gerar os arrays no tamanho especificado
void gera_random(int arr[], int n) {
    for (int i = 0; i < n; i++) arr[i] = rand();
}

void gera_sorted(int arr[], int n) {
    for (int i = 0; i < n; i++) arr[i] = i;
}

void gera_reverse(int arr[], int n) {
    for (int i = 0; i < n; i++) arr[i] = n - i;
}

void gera_half_sorted(int arr[], int n) {
    for (int i = 0; i < n; i++) arr[i] = (int) (n - i) + 1;
}

static void run_test(const unsigned short array_size) {
    printf("\n---------------- %d elementos ----------------\n", array_size);

    int *base = malloc(sizeof(int) * array_size); //
    int *vetor = malloc(sizeof(int) * array_size); //

    const char *tipos[4] = {"Sorted", "Half-sorted", "Reverse", "Random"};
    void (*geradores[4])(int *, int) = {gera_sorted, gera_half_sorted, gera_reverse, gera_random};
    void (*algoritmos[3])(int *, int) = {bubbleSort, insertionSort, NULL}; // quicksort tratado separadamente
    const char *nomes_alg[3] = {"Bubble", "Insertion", "Quick"};

    for (int t = 0; t < 4; t++) {
        geradores[t](base, array_size);
        printf("\n-- Lista %s --\n", tipos[t]);

        // Bubble e Insertion
        for (int a = 0; a < 2; a++) {
            long double tempos[REP];
            long long comps[REP];

            long double somaTempos = 0;
            long long somaComparacoes = 0;

            for (int r = 0; r < REP; r++) {
                for (int i = 0; i < array_size; i++) vetor[i] = base[i];

                struct timespec inicio, fim;

                clock_gettime(CLOCK_MONOTONIC, &inicio);
                algoritmos[a](vetor, array_size);
                clock_gettime(CLOCK_MONOTONIC, &fim);

                tempos[r] = (fim.tv_sec - inicio.tv_sec) * 1000.0 + (fim.tv_nsec - inicio.tv_nsec) / 1000000.0;
                comps[r] = comparacoes;

                somaTempos += tempos[r];
                somaComparacoes += comps[r];
            }

            printf("%s Sort:\n", nomes_alg[a]);
            for (int r = 0; r < REP; r++)
                printf("Repeticao %d: %.6Lf ms, %lld comparacoes\n", r + 1, tempos[r], comps[r]);
            printf("Media: %.6Lf ms, %lld comparacoes\n\n", somaTempos / REP, somaComparacoes / REP);
        }

        // QuickSort
        long double tempos[REP];
        long long comps[REP];

        long double somaTempos = 0;
        long long somaComparacoes = 0;

        for (int r = 0; r < REP; r++) {
            for (int i = 0; i < array_size; i++) vetor[i] = base[i];

            comparacoes = 0;

            struct timespec inicio, fim;
            clock_gettime(CLOCK_MONOTONIC, &inicio);
            quickSort(vetor, 0, array_size - 1);
            clock_gettime(CLOCK_MONOTONIC, &fim);

            tempos[r] = (fim.tv_sec - inicio.tv_sec) * 1000.0 + (fim.tv_nsec - inicio.tv_nsec) / 1000000.0;
            comps[r] = comparacoes;

            somaTempos += tempos[r];
            somaComparacoes += comps[r];
        }

        printf("Quick Sort:\n");
        for (int r = 0; r < REP; r++)
            printf("Repeticao %d: %.6Lf ms, %lld comparacoes\n", r + 1, tempos[r], comps[r]);
        printf("Media: %.6Lf ms, %lld comparacoes\n", somaTempos / REP, somaComparacoes / REP);
    }

    free(base);
    free(vetor);
}

int main() {
    srand(42); // define a seed dos valores aleatórios
    for (int i = 0; i < sizeof(N) / sizeof(N[0]); i++) {
        run_test(N[i]);
    }
    return 0;
}
