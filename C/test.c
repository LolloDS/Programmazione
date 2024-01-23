#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char *stringa;
    int i, vocali = 0, consonanti = 0;

    printf("Inserisci una stringa: ");
    stringa = (char *)malloc(sizeof(char));

    scanf("%[^\n]", stringa);

    for (i = 0; i < strlen(stringa); i++)
    {
        if (stringa[i] == 'a' || stringa[i] == 'e' || stringa[i] == 'i' || stringa[i] == 'o' || stringa[i] == 'u' ||
            stringa[i] == 'A' || stringa[i] == 'E' || stringa[i] == 'I' || stringa[i] == 'O' || stringa[i] == 'U'){
        
            vocali++;
        }
        else if (stringa[i]!= ' ' && stringa[i]!= '\n'){
        
            consonanti++;
        }
    }
    printf("La stringa contiene %d vocali\n", vocali);
    printf("La stringa contiene %d consonanti", consonanti);

    free(stringa);
    return 0;
}
