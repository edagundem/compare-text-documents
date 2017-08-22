#include <stdio> 
#include <conio> 
void main(void) 
{ 
int toplam,sayac,girilen_deger; 
sayac=0; 
toplam=0; 
int sayi_asal_mi( int sayi )
{
	int i;
	for( i = 2; i <= sayi/2; i++ ) {
	// Sayi asal degilse, i'ye tam olarak 
	// bolunur.
		if( sayi%i == 0 ) return 0;
	}
	// Verilen sayi simdiye kadar hicbir 
	// sayiya bolunmediyse, asaldir ve 
	// geriye 1 doner.
	return 1;
}
for (i=0;i<6000;i++) 
dizi[i]=random(3)+1; 

for (i=0;i=<6000;i++) 
deg[dizi[i]-1]++; 
clrscr(); 
for (i=0;i<3;i++) 
printf(" %d den bulunan adet...: %d n",i+1,deg[i]); 
getch(); 
} 