//kars�last�r�lacak dosya
#include<stdio.h>
 int main( void )
{
int girilen_sayi;
	int test_sonucu;
	do{
		printf( "L�tfen bir say� giriniz> " );
		scanf( "%d",&girilen_sayi );
		test_sonucu = sayi_asal_mi( girilen_sayi );
		if( !test_sonucu ) 
			printf("Girilen say� asal de�ildir!\n");
	} while( !test_sonucu );
	printf( "Girilen say� asald�r!\n" );
	return 0;
}
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