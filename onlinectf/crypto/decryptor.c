#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void decrypt(FILE *input, FILE *output) {
	char k[] = "CENSORED";
	char c, p, t = 0;
	int i = 0;

	while ((c = fgetc(input)) != EOF) {
		// /c = (p + (k[i % strlen(k)] ^ t) + i*i) & 0xff;
		p = (c ) - ((k[i % strlen(k)] ^ t) + i*i);
		t = p;
		i++;1
		fputc((char)p, output);
	}
	printf("File decrypted.");
}
int main(int argc, char **argv) {
	if (argc != 3) {
		printf("USAGE: %s INPUT OUTPUT\n", argv[0]);
		return 0;
	}
	FILE* input  = fopen(argv[1], "rb");
	FILE* output = fopen(argv[2], "wb");
	if (!input || !output) {
		printf("Error\n");
		return 0;
	}

	char k[] = "CENSORED";
	char c, p, t = 0;
	int i = 0;
	int counter = 0;
	int counter2 = -1;
	while ((c = fgetc(input))) {
		counter ++;
		counter2 ++;
		// /c = (p + (k[i % strlen(k)] ^ t) + i*i) & 0xff;
		p = (c ) - ((k[i % strlen(k)] ^ t) + i*i);
		t = p;
		i++;
		printf("Char d: \t\t %2x \t %c  \n", p, (char)p);
		printf("----------------------\n");
		fputc(p, output);
		if (counter2 > 1000)
			break;

	}
	printf("Counter: %d\n", counter);
	printf("File decrypted..");
	
	//decrypt(input, output);
	fclose(input);
	fclose(output);

	return 0;
}
