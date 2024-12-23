/*
 * Progettare struttura dati tipo coda che consenta le seguenti operazioni su insiemi di stringhe
 * 
 * - Init coda vuota
 * - Inserimento di una stringa
 * - Lettura (stampa) della stringa piu' "anziana" della struttura
 * - Cancellazione della stringa piu' "anziana" della struttura
 * 
 * */

/*
 * Possibili implementazioni
 * 
 * Array dinamico (lista):
 *  - Inseriemento in testa (in fondo) costo O(1)
 *  - Lettura della stringa + anziana (l'elemento in pos 0 della lista) costo O(1)
 *  - Cancellazione dell'elemento in pos 0 richiede O(n) operazioni
 * 
 * adattamento: teniamo traccia della posizione del primo elemento della sequenza
 * che modificheremo al momento della cancellazione.
 * 
 * 
 * */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct  {
    char tipo; /* 'i' intero; 'f' float; 's' stringa */
    void *dato;
} elemento;


struct lista {
    elemento *a;
    int c;  /* capacita'  */
    int n;  /* dimensione, numero di elementi */
    int p;  /* posizione del primo elemento */
};
typedef struct lista lista;


lista init();
lista append(lista, elemento);
void mostra(lista);
lista pop(lista);
lista insert(lista, elemento, int);

elemento intero(int);
elemento fpoint(float);
elemento stringa(char*);


char cerca_tipo(char *b){
    /*
     * ritorna 'i' se e solo se b contiene solo cifre decimali
     * ritorna 'f' se e solo se b contiene cifre decimali e esattamente un .
     * ritorna 's' altrimenti
     * */
     
     int i = 0, numero_punti = 0;
     
     while ( b[i] != '\0' ){
        if ( b[i] == '.' )
            if ( numero_punti > 0 )
                return 's';
            else
                numero_punti++;
        else if ( b[i] < '0' || b[i] > '9')     // non e' un cifra decimale
            return 's';
        i++;
     }
     
     if (numero_punti == 0)
        return 'i';
    else
        return 'f';
     
}

int main(int n, char *args[]){
    lista L = init();  
    
    char *s0 = malloc(10);
    char *s1 = malloc(10);
    
    strcpy(s0, "dieci");
    strcpy(s1, "undici");
    
    
    for(int i = 1; i < n; i++){
        elemento e = {'s', args[i]};
        L = append(L, e);
    }
    
    mostra(L);

    L = pop(L);
    L = pop(L);
    elemento e0 = {'s', s0}, e1 =  {'s', s1}, e = {'s', args[0]};
    L = append(L, e);
    mostra(L);

    
    L = append(L, e0);
    L = append(L, e1);
    
    mostra(L);
}



lista init(){
    lista lista_vuota = {NULL, 0, 0, -1};
    return lista_vuota;
}

lista append(lista L, elemento e){
    if (L.n == L.c) {
        L.c = 2*(L.c+1);
        elemento *t = malloc(L.c*sizeof(elemento));
        for(int i = 0; i < L.n; i++)
            t[i] = L.a[(L.p+i)%L.n];
        free(L.a);
        L.a = t;
        L.p = 0;
    }
    
    L.a[(L.p+L.n)%L.c] = e;
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
                printf("%d\n", *((int*)L.a[(L.p+i)%L.c].dato) );
                break;
            case 'f':
                printf("%f\n", *((float*)L.a[(L.p+i)%L.c].dato) );
                break;
            case 's':
                printf("%s\n", (char*)L.a[(L.p+i)%L.c].dato );
                break;
            //default:
                /* se non vero i precedenti*/
        }
    }
    
    printf("dimensione %d, capacita' %d\n", L.n, L.c);
}

lista pop(lista L){
    if(L.n > 0 ){
        if (L.a[L.p].tipo != 's')
            free(L.a[L.p].dato);
        L.p = (L.p+1)%L.c;
        L.n--;
        if (L.n < L.c/4){
            L.c = L.c/2;
            elemento *t = malloc(L.c*sizeof(elemento));
            for(int i = 0; i < L.n; i++)
                t[i] = L.a[(L.p+i)%L.n];
            free(L.a);
            L.a = t;
            L.p = 0;
        }

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
