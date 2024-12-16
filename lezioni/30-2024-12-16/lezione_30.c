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

int main(){
    clista L = clista_vuota();
    
    for(int i = 0; i < 10; i++){
        L = clista_in0(L, i);
    }
    
    clista_mostra(L);
    
    
    while( L!= NULL ){
        L = clista_out0(L);
        clista_mostra(L);
    }
    
    
    for(int i = 0; i < 10; i++){
        L = clista_in0(L, i);
    }
    
    clista_mostra(L);
    
    L = clista_out(L, 5);
    
    clista_mostra(L);
    
    
    L = clista_out(L, 9);
    
    clista_mostra(L);
    
    L = clista_out(L, 0);
    
    clista_mostra(L);
    
    
    clista L1 = clista_vuota();
    L1 =clista_in0(L1, 0);
    
    clista_mostra(L1);
    
    L1 = clista_out(L1, 0);
    
    clista_mostra(L1);
    
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
