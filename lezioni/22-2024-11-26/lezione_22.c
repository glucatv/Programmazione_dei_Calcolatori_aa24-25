#include <stdio.h>
#include <stdlib.h>

float *crea_array_di_float(int, float);
float *copia_array_di_float(float*, int); // float *copia_array_di_float(float[], int)  

int main(){
    float *p; /*puntatore a float*/
    
    float f = 3.14;
    
    p = &f;
    
    printf("%f, %f\n", f, *p);
    
    *p = 0;
    
    p = malloc( sizeof(float) );
    
    printf("sizeof(float) = %d\n", sizeof(float));
    
    printf("valore di p = %p\n", p);
    
    *p = 2.71;
    
    printf("%f, %f\n", f, *p);
    
    free(p);
    p = malloc( 2*sizeof(float) );
    
    if ( p == NULL ) /* allocazione effettuata */
        return -1;
        
    *p = 0.1;
    *(p+1) = 0.2; /* p+1 e' l'indirizzo del float successivo a quello puntato da p
                    il suo valore dipende da sizeof(float) */
    
    float f0 = *p, f1 = *(p+1);
    
    printf("%f, %f\n", f0, f1);
    
    printf("%f\n", *(p+2) ); /* possibile segmentation fault, memoria non allocata*/
    
    printf("%f, %f\n", p[0], p[1]); /* equivalente a *p e *(p+1)*/ 
    
    
    free(p);
    
    p = crea_array_di_float(10, 2.71);
    
    for(int i = 0; i < 10; i++)
        printf("%f\n", p[i]);
    
    free(p);    
        
    float b[10] = {0};
    
    p = copia_array_di_float(b, 10);
    
    for(int i = 0; i < 10; i++)
        printf("%f\n", p[i]);
}

/*
 * VERSIONE ERRATA, 

float *crea_array_di_float(int n, float v){
    float a[n];
    
    for(int i=0; i < n; i++){
        a[i] = v;
    }
    
    return a; // a contiene l'indirizzo del primo byte della sequenza
}
*
* viene restituito l'indirizzo di una variabile locale
*/

float *crea_array_di_float(int n, float v){
    float *a =  malloc(n*sizeof(float));
    
    if (a == NULL){
        return NULL;
    }
    
    for(int i=0; i < n; i++){
        a[i] = v;
    }
    
    return a; // a contiene l'indirizzo del primo byte della sequenza
}

float *copia_array_di_float(float *a, int n){
    float *b =  malloc(n*sizeof(float));

    if(b == NULL)
        return NULL;

    for(int i=0; i < n; i++){
        b[i] = a[i];
    }
    
    return b;
}
