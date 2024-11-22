#include <stdio.h>
/*
 * Contiene, tra gli altri, il prototipo di printf
 * 
 * extern int printf (const char *__restrict __format, ...);
 * 
 * */

/* prototipi delle funzioni definite altrove nel codice*/
float my_sqrt(float, int );
float my_abs(float a);
char maiuscola_to_minuscola(char);

float my_sqrt(float x, int max_iter){
    float g = x/2;
    int c = 0; 

    while ( my_abs( g*g - x ) > 0.00001 && c < max_iter  ) {
        g = ( g + x/g )/2;
        c++; /*equivalente a c = c+1 oppure c += 1*/
    }

    return g;
}

float my_abs(float a){
    if (a < 0) {
        return -a;
    } else
        return a;
}


char maiuscola_to_minuscola(char c){
    if ( c >= 'A' && c <= 'Z' ){ // c e' una maiuscola
        int d = c-'A';
        return 'a'+d;
    }
    return -1;  
}


int main(){
    /*
     * Operazioni aritmetiche
     * 
     *  +, -, *, /, %
     * 
     * */
     
     int a = 3, b = 2;
     float c = a/b; // a/b e' intero perche' a e b lo sono. Casting inplicito
     float d = 1.0*a/b;
     float e = (a/b)*1.0;
     
     float f = (float)a/b; // casting esplicito
     
     printf("%f, %f, %f, %f\n", c, d, e, f);
     
     /*
      * Operazioni relazionali
      * 
      * <, >, ==, !=, <=, >=
      * 
      * 
      * */
      
    /*
     * Operatori logici
     * 
     * && and
     * || or
     * ! not
     * 
     * */
     
     printf("Radice quadrata di 2: %f\n", my_sqrt(2, 2));
     printf("Radice quadrata di 2: %f\n", my_sqrt(2, 200));
     
     
     char ch = 'h';
     
     printf("%c, %c, %d, %d\n", ch, ch+1, ch, ch+1);
     
     printf("%c\n", maiuscola_to_minuscola('G'));
}
