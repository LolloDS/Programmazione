#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* get_line() {
	char* line = malloc(sizeof(char));
	int len = 0;
	int c;

	while ((c = getchar()) != '\n') {
		line[len++] = c;
		line = realloc(line, (len + 1) * sizeof(char));
	}
	line[len] = '\0';

	return line;
}

void count_vowels_and_consonants(char* str, int* vowels, int* consonants) {
	*vowels = *consonants = 0;

	for (int i = 0; i < strlen(str); i++) {
		char c = tolower(str[i]);
		if (c >= 'a' && c <= 'z') {
			if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
				(*vowels)++;
			} else {
				(*consonants)++;
			}
		}
	}
}

int main() {
	printf("Enter a string: ");
	char* str = get_line();

	int vowels, consonants;
	count_vowels_and_consonants(str, &vowels, &consonants);

	printf("Length of the string: %d\n", strlen(str));
	printf("Number of vowels: %d\n", vowels);
	printf("Number of consonants: %d\n", consonants);

	free(str);
	return 0;
}