#include <stdio.h>
#include <stdlib.h>

float *copia_array_di_float(float *, int);

/*
 * 
 * Array dinamico
 * 
 * */
struct lista_f {
    float *a;
    int c;  /* capacita'  */
    int n;  /* dimensione, numero di elementi */
};
typedef struct lista_f lista_f; 

lista_f init();
lista_f append(lista_f, float);


int  main(){
    struct lista_f L;
    lista_f L1;
    int i;
    
    L.c = 10;
    L.n = 0;
    L.a = malloc(L.c*sizeof(float));

    L.a[0] = 3.14;
    L.a[1] = 2.71;
    L.n += 2;
    
    for(i=0; i < L.n; i++){
        printf("%f\n", L.a[i]);
    }
    
    L1 = init();
    for(i = 0; i < 20; i++){
        L1 = append(L1, i*10);
        printf("%d, %d\n", L1.n, L1.c);
    }
    
    for(i = 0; i < 20; i++){
        printf("%f\n", L1.a[i]);
    }
    
}

lista_f init(){
    lista_f lista_vuota = {NULL, 0, 0};  /* NULL valore del primo campo, 0 valore del secondo campo...*/
    return lista_vuota;
}

lista_f append(lista_f L, float e){
    if (L.n == L.c) {
        L.c = 2*(L.c+1); 
        L.a = realloc( L.a, L.c*sizeof(float) );
    }
    
    L.a[L.n] = e;
    L.n++;
    
    return L;
}



int main1(){
    int i, n = 10;
    float *a = malloc(n*sizeof(float)); /* tempo O(1) */
    
    for( i = 0; i < n; i++){
        a[i] = 10+i;
    }
    
    n++;
    a = realloc( a, n*sizeof(float) ); /* tempo nel caso peggiore O(n) se richiede copia, altrimenti O(1) */
    
    a[n-1] = 0;
    
    for( i = 0; i < n; i++){
        printf("%f\n", a[i]);
    }
    
    free(a);
    
    int m = 100;
    n = 1;
    a = malloc(1*sizeof(float));
    a[0] = 10;
    
    for(i = 0; i < m; i++){
        /* Nel caso peggiore tempo O(n**2).
         * Osservazione: il costo di n append() in Python e', nel caso peggiore, O(n)
         * */
        n++;
        a = realloc( a, n*sizeof(float) );
        a[n-1] = n;
    }
    
    for(i = 0; i < n; i++){
        printf("%f ", a[i]);
    }
    printf("\n");
    
}






int main0(){
    
    float v[200] = {0,1,2};
    
    int i, n = sizeof(v)/sizeof(float);
    
    float *w = copia_array_di_float(v, n);
    
    for(i = 0; i < n; i++){
        printf("%f\n", w[i]);
    }
 
}



float *copia_array_di_float(float *a, int n){
    float *b =  malloc(n*sizeof(float));
    
    //printf("%d\n", sizeof(a)/sizeof(float));

    if(b == NULL)
        return NULL;

    for(int i=0; i < n; i++){
        b[i] = a[i];
    }
    
    return b;
}
