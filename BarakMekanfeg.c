#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(void)
{
	char choice;
	printf("BARAK MEKANFEG\n");
	printf("MI MEKANFEG ?(A=BARAK, B=OFEK) : ");
	scanf("%c", &choice);
	if (choice=='A')
		printf("NAHON MEOD\n");
	// Barak isn't really mekanfeg-ing.
	else if (choice=='B')
		printf("OFEK MEKANFEG\n");
	else
		printf("Invalid choice\n");
	return 0;
	system("PAUSE");
}
