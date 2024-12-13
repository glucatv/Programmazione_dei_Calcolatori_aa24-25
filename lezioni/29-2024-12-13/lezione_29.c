#include <stdio.h>
#include <stdlib.h>

typedef struct nodo {
    float dato;
    struct nodo *succ;
} nodo;

typedef nodo *clista; // lista concatenata


clista clista_vuota();
void clista_mostra(clista);
nodo *clista_in0(clista, float);
nodo *clista_cerca(clista, float);

int main(){
    clista L0 = clista_vuota();
    clista L;
    
    clista_mostra(L0);
    
    nodo q = {3.14, NULL};
    nodo p = {0.0, NULL};
    
    L0 = &q;  // q in testa alla lista
    
    p.succ = &q; // alt. p.succ = L
    L0 =&p;
    
    clista_mostra(L0);
    
    L = clista_vuota();
    
    for(int i = 0; i < 10; i++){
        L = clista_in0(L, i);
    }
    
    clista_mostra(L);
    
    nodo *point = clista_cerca(L, 6.1);
    
    if (point != NULL)
        printf("%f\n", point->dato);
    else
        printf("Non trovato\n");
}


clista clista_vuota(){
    return NULL;
}

void clista_mostra(clista a){
    nodo *p;
    
    p = a;
    
    printf("Contenuto della lista: ");
    
    while( p != NULL ){ //non raggiungo il fine lista
        printf("%f, ", (*p).dato  ); // stampo il dato del nodo puntato da p
        p = p->succ; // equivalente a p = (*p).succ;
    }
    
    printf("\n");
}


nodo *clista_in0(clista a, float v){
    nodo *p = malloc(sizeof(nodo));
    p->dato = v;
    p->succ = a;
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
