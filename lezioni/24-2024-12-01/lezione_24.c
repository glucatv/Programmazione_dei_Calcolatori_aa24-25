#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int str_cmp(char*, char*);

int str_len(char *a){
    int c = 0;
    while( a[c] != '\0')
        c++;
    return c;
    
    
    /*
     * Complessita' temporale lineare nella lunghezza della stringa
     * 
     * */
}

int main(){
    /* '\0' carattere di fine stringa */
    char a[] = "una stringa"; /* array composto dai caratteri mostrati + carattere \0*/
    
    char b0[1000];
    char *b1;  
    
    char stringa_vuola[] = ""; /*l'array contiene \0 in posizione 0*/

    
    printf("%d\n", sizeof(a));
    
    printf("%s\n", a);
    
    a[3] = '\0'; /* definisce la stringa "ana" */
    
    printf("str_len(\"%s\") = %d\n", a, str_len(a));
    
    printf("str_len(\"%s\") = %d\n", a, strlen(a)); /* funzione di string*/
    
    strcpy(b0, a);
    
    printf("str_len(\"%s\") = %d\n", b0, strlen(b0));
    
    b1 = malloc(sizeof(char)*(strlen(a)+1));
    strcpy(b1, a); /*costo temporale lineare nella lunghezza della stringa a*/
    printf("str_len(\"%s\") = %d\n", b1, strlen(b1));
    
    /*
     * Esercizio: scrive una funzione col seguente prototipo
     * 
     * char *clona(char *a);
     * 
     * che copia a in una nuova stringa allocata dinamicamente e ne
     * ritorna l'indirizzo.
     * 
     * Ritorna NULL se l'operazione non e' possibile
     * 
     * */
     
     /* testare se a e b0 sono uguali:
      * 
      * a e b0 sono diversi come array ma uguali come stringhe
      * 
      * testare se la stringa a e' uguale alla stringa b0
      * 
      * a == b0 ?? NO, confronto tra indirizzi
      * 
      * */
      
      char c[] = "programmazione";
      char d[] = "programma";
      char e[] = "prolog";
      char f[] = "prolog";
      
      printf("%d\n", str_cmp(c, d) );
      printf("%d\n", str_cmp(d, e) );
      printf("%d\n", str_cmp(f, e) );
     
}

int str_cmp(char *a, char *b){
    /*
     * a e b sono due stringhe. Ritorna -1 se a precede b nell'ordinamento lessicografico
     * ovvero se i e' la prima posizione in cui a e b divergono allora a[i] < b[i]
     * 
     * ritorna +1 quando b precede a
     * 
     * ritorna 0 quando a e b sono uguali
     * 
     * */
    
    int i = 0;
    
    while ( i < strlen(a) && i < strlen(b) && a[i] == b[i] )  // !!!! attenzione, vedere commento sotto
        i++;
        
    if (i == strlen(a)) {
        if ( i < strlen(b) )
            return -1;
        else
            return 0;
    }
    
    if (i == strlen(b))
        return +1;
        
    /*  a[i] != b[i] */
    
    if (a[i] < b[i])
        return -1;
    else
        return +1;


    /*
     * ATTENZIONE!!!
     * Costo temporale quadratico dovuto alle strlen al'interno del while
     * 
     * come riparare??
     * 
     * int na = strlen(a), nb = strlen(b)
     * 
     * e usare na e nb dove serve
     * 
     * In string c'e' strcmp che fa la stessa cosa, il costo temporale
     * è lineare. 
     * 
     * */
}   
