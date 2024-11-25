#include <stdio.h>

float potenza(float, int);

int main(){
    printf("%f\n", potenza(2, 4));
    printf("%f\n", potenza(2, -4));
    printf("%f\n", potenza(2, 0));
    
    /*
     * 
     * ARRAY
     * 
     * 
     * */
     
    int a[10]; /*un array di 10 int indefinito*/
    int b[6] = {0, 1, 5, 1, 2, 4}; // array di 6 interi definiti
    int c[] = {4, 1, 4}; // array di 3 interi definiti
    int d[101] = {0, 1, 2}; /* definisco esplicitamente i primi 3 elementi,
                           da  d[3] in poi gli elementi sono 0
     */
    
    int i;
    
    for(i = 0; i < 10; i++){
        printf("%d\n", d[i]);
    }
    
    
    
    /*
     *      
     * 
     * equivalente a
     *                    
    int i = 0;
    
    while(i < 10){
        printf("%d\n", d[i]);
        i++;
    }
     *
     * 
     * */
     
     d[9] = 10;
     
     
     printf("============================\n");
     
    for(i = 0; i < 10; i++){
        printf("%d\n", a[i]);
    }
    
}

float potenza(float x, int e){
    int pe;
    float pow = 1;
    
    if (e < 0)
        pe = -e;
    else
        pe = e;
        
    while (pe > 0){
        pow *= x;
        pe--;
    }
    
    if ( e < 0 )
        pow = (1.0)/pow;
        
    return pow;
}
