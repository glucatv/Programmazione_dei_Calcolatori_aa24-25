#include <stdio.h>
#include <stdlib.h>

typedef struct nodo {
    float dato;
    struct nodo *succ, *prec;
} nodo;

typedef nodo *clista; // lista concatenata


clista clista_vuota();
void clista_mostra(clista);
nodo *clista_in0(clista, float);
nodo *clista_cerca(clista, float);
nodo *clista_out0(clista);
nodo *clista_out(clista, float);
nodo *clista_in(clista, float, int);

int main(int n, char *args[]){
    clista L = clista_vuota();

    for(int i = 1; i < n; i++){
        float v;
        if ( sscanf(args[i], "%f", &v) == 1) 
            L = clista_in0(L, v);
    }

    clista_mostra(L);
    
    L = clista_in(L, 100, 0);
    L = clista_in(L, 200, 6);
    L = clista_in(L, 300, 1000);
    clista_mostra(L);
}


clista clista_in(clista a, float v, int i){
    nodo *p = a;
    
    if (i < 0)
        return a;
    
    if (i == 0 || p == NULL)
        return clista_in0(a, v);
        
    
    
    while ( i != 1 && p->succ != NULL ){
        p = p->succ;
        i--;
    }
    
    /* p punta all'elemento in posizione i-1 oppure all'ultimo elemento,
     * aggiungo il nuovo nodo in posizione 1 da p*/
     
    nodo *q = clista_in0(p->succ, v);
    
    p->succ = q;
    q->prec = p;
    
    return a;
     
}

clista clista_vuota(){
    return NULL;
}

void clista_mostra(clista a){
    nodo *p;
    
    p = a;
    
    printf("Contenuto della lista: ");
    
    while( p != NULL ){ //non raggiungo il fine lista
        printf("%5.2f, ", (*p).dato  ); // stampo il dato del nodo puntato da p
        p = p->succ; // equivalente a p = (*p).succ;
    }
    
    printf("\n");
}


nodo *clista_in0(clista a, float v){
    nodo *p = malloc(sizeof(nodo));
    p->dato = v;
    p->succ = a;
    p->prec = NULL;
    if (a != NULL)
        a->prec = p;
    a = p;
    return a; // oppure return p 
}

nodo *clista_cerca(clista a, float k){
    nodo *p = a;
    
    while( p != NULL && p->dato != k ){
        p = p->succ;
    }
    
    return p;
}


clista clista_out0(clista a){
    clista p = a;
    if( a == NULL)
        return NULL;
    a = a->succ;
    if (a != NULL)
        a->prec = NULL;
    free(p);
    return a;
}

clista clista_out(clista a, float k){
    nodo *p = clista_cerca(a, k);
    if (p == NULL)
        return a;
    
    nodo *q = p->prec;
    
    if ( q == NULL){ // p e' il primo nodo della lista ovvero p == a
        return clista_out0(p);
    }
    
    q->succ = clista_out0(q->succ);
    if (q->succ != NULL)
        q->succ->prec = q;
    
    return a;
        
}
