#include <stdio.h>
#include <stdlib.h>


typedef struct  {
    char tipo; /* 'i' intero; 'f' float; 's' stringa */
    void *dato;
} elemento;


struct lista {
    elemento *a;
    int c;  /* capacita'  */
    int n;  /* dimensione, numero di elementi */
};
typedef struct lista lista;


lista init();
lista append(lista, elemento);
void mostra(lista);
lista pop(lista);

elemento intero(int);
elemento fpoint(float);
elemento stringa(char*);

int main(){
    lista L = init();
    
    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );
    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );
    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );
    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );

    mostra(L);

    
    while(L.n > 0){
        L = pop(L);
        mostra(L);
    }
    
    
    
}

lista init(){
    lista lista_vuota = {NULL, 0, 0};
    return lista_vuota;
}

lista append(lista L, elemento e){
    if (L.n == L.c) {
        L.c = 2*(L.c+1); 
        L.a = realloc( L.a, L.c*sizeof(elemento) );
    }
    
    L.a[L.n] = e;
    L.n++;
    
    return L;
}

void mostra(lista L){
    int i;
    
    printf("==================================\n");
    
    for(i = 0; i < L.n; i++){
        /* stampa L.a[i] */
        /*
         * if( L.a[i].tipo == 'i' )
            printf("%d\n", *((int*)L.a[i].dato) );
        */
        switch  (L.a[i].tipo) {
            case 'i':
                printf("%d\n", *((int*)L.a[i].dato) );
                break;
            case 'f':
                printf("%f\n", *((float*)L.a[i].dato) );
                break;
            case 's':
                printf("%s\n", (char*)L.a[i].dato );
                break;
            //default:
                /* se non vero i precedenti*/
        }
    }
    
    printf("dimensione %d, capacita' %d\n", L.n, L.c);
}

lista pop(lista L){
    if(L.n > 0 ){
        L.n--;
        if (L.n < L.c/4){
            L.c = L.c/2;
            L.a = realloc(L.a, (L.c)*sizeof(elemento)); 
        }
        if (L.a[L.n].tipo != 's')
            free(L.a[L.n].dato);
    }
    return L;
}

elemento intero(int d){
    elemento e = {'i', NULL};
    
    e.dato = malloc(sizeof(int));
    *((int*)e.dato) = d;
    
    return e;
}

elemento fpoint(float d){
    elemento e = {'f', NULL};
    
    e.dato = malloc(sizeof(float));
    *((float*)e.dato) = d;
    
    return e;
}

elemento stringa(char *d){
    elemento e = {'s', NULL};
    
    e.dato = d;
    
    return e;
}
