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


int main(){
    lista L = init();
    char buffer[1024];
    int n = 0;
    
    while( n < 5 ){
        printf("Inserisci un intero, un float o una stringa e premi invio: ");
        scanf("%s", buffer);
        
        //printf("%d\n", strlen(buffer));
        
        /*
        if(buffer[0] == '\0') // buffer e' la stringa vuota oppure strlen(buffer)==0
            break;
        */
        switch( cerca_tipo(buffer) ){
            case 'i':
                int a;
                sscanf(buffer, "%d", &a);
                L = append(L, intero(a));
                break;
            case 'f':
                float f;
                sscanf(buffer, "%f", &f);
                L = append(L, fpoint(f));
                break;
            default:
                char *s = malloc(sizeof(char)*(strlen(buffer)+1));
                strcpy(s, buffer);
                
                L = append( L, stringa(s) ); 
        }
        n++;
    }
    

    mostra(L);

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

lista insert(lista L, elemento e, int p){
    int i;
    
    if(p < 0){
        p = 0;
    }
    
    L = append(L, e);
    
    for( i = L.n-1; i > p; i--){
        L.a[i] = L.a[i-1];
        L.a[i-1] = e;
    }
    
    
    return L;
    
    /*
     * Complessita' temporale O(L.n - p) e quindi O(n) nel caso peggiore
     * 
     * */
    
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

