q/#include <stdlib.h>
#include <stdio.h>
#include <string.h>


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

	int i = 0;
	char k[] = "CENSORED";
	char c, p, d, t1=0, t2=0;
		while ((p = fgetc(input)) != EOF) {

		printf("Char p: \t\t %2x \t %c  \n", p, (char)p);	
		c = (p + (k[i % strlen(k)] ^ t1) + i*i) & 0xff;
		printf("Char c2: \t\t %2x \t %c  \n", c, (char)c);	


		d = (c ^ 0xff) - ((k[i % strlen(k)] ^ t2) + i*i);
		printf("Char d1: \t\t %2x \t %c  \n", d, (char)d);	
		d = (c) - ((k[i % strlen(k)] ^ t2) + i*i);
		printf("Char d2: \t\t %2x \t %c  \n", d, (char)d);	
		i++;
		t1 = p;
		t2 = d;
		if ((char)d == '\0')
			fputc('x', output);
		else
			fputc(d, output);
		
		printf("----------------------\n");
	}

	fclose(input);
	fclose(output);

	return 0;
	}
