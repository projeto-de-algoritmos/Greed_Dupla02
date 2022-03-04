#include <stdio.h>
#include <stdlib.h>


int * getInput(int n) {
    int pos;
    int *explorers = malloc(n * sizeof(int));   // Aloca array dinamico com tamanho N.
    if (explorers == NULL) exit(EXIT_FAILURE);

    for(int i = 0; i < n; i++)                  // Se certifica que as posições estão zeradas.
        explorers[i] = 0;

    for(int i = 0; i < n; i++) {                // Adiciona 1 a posição do vetor correspondente
        scanf("%d", &pos);                      // ao nivel de experiencia do explorador.
        explorers[pos - 1]++;
    }

    return explorers;
}

int main() {
    int testCases, nExplorers, count, *explorers, mostInex, groups, set;

    scanf("%d", &testCases);

    while(testCases--) {
        groups = 0, set = 0, count = 0, mostInex = 0;       // Zera as variaveis que são utilizadas
        scanf("%d", &nExplorers);                           // em tora iteração

        explorers = getInput(nExplorers);

        while(count < nExplorers) {
            if (explorers[count] > 0) {                     // Se existe 1 ou mais exploradores com
                if (mostInex < count + 1)                   // experiencia correspondente a posição j+1
                    mostInex = count + 1;
                if (set + explorers[count] >= mostInex) {   // Se a quantidade de pessoas no grupo atual
                    groups++;                               // mais a quantidade de pessoas na posição atual
                    explorers[count] -= (mostInex - set);   // for maior que o necessario para formar um grupo
                    mostInex = 0;                           // soma o necessário e fecha um grupo.
                    set = 0;
                    if (explorers[count] == 0) count++;
                } else {
                    set += explorers[count];
                    explorers[count] = 0;
                    count++;
                }
            } else
                count++;
        }
        printf("%d\n", groups);
        free(explorers);
    }

    return 0;
}
