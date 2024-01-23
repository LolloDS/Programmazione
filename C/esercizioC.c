#include <stdio.h>
#include <stdlib.h>

float count_numbers(char *str) {
    float sum = 0;
    float num;
    int n;

    for (int i = 0; str[i] != '\0';) {
        if (sscanf(str + i, "%f%n", &num, &n) == 1) {
            sum += num;
            i += n;
        } else {
            i++;
        }
    }

    return sum;
}

char* read_string() {
    int size = 10;
    char* str = malloc(size * sizeof(char));
    int c;
    int i = 0;

    while ((c = getchar()) != '\n' && c != EOF) {
        str[i++] = c;
        if (i == size) {
            size *= 2;
            str = realloc(str, size * sizeof(char));
        }
    }

    str[i] = '\0';
    return str;
}

int main() {
    printf("Inserisci una stringa: ");
    char* str = read_string();

    float sum = count_numbers(str);

    printf("La somma dei numeri e': %.2f\n", sum);

    free(str);
    return 0;
}