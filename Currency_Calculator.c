#include <stdio.h>
int main()
{

	float USD;

	float JPY;

	float Xchg;

	float NewAmt=0;

	int Select;

	while(Select!=4)
	{	
		printf("\nThis program converts JP Yen to US Dollars or US Dollars to JP Yen\n");
		printf("\n\t1. USD\n");
		printf("\n\t2. JPY\n");
		printf("\n\t3. Quit\n");
		printf("Please enter your selection\n");
		scanf("%d", &Select);
	}

	if(Select=1)
	{
			printf("\n\tEnter US Dollar amount to convert: \n");
			scanf("%f", &USD);
			printf("\n\tEnter today's USD to JPY conversion rate: \n");
			scanf("%f", &Xchg);
			NewAmt=USD*Xchg;
		printf("\nThat amount in Japanese Yen is: ¥%.2f\n", NewAmt);
	}
	else if(Select=2)
	{
			printf("\n\tEnter Japanese Yen amount to convert: \n");
			scanf("%f", &JPY);
			printf("\n\tEnter today's JPY to USD conversion rate: \n");
			scanf("%f", &Xchg);
			NewAmt=JPY/Xchg;
		printf("\nThat amount in US dollars is: $%.2f\n", NewAmt);
		return 0;
	}
}

/** 
 * Written and created by : 
 * Ofek Mizrahi.
 * AKA - ApricotHacker.
 * (#RememberYemen)
*/

