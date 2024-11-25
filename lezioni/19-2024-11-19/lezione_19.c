float my_abs(float a){
    if (a < 0) {
        return -a;
    } else
        return a;
}


int main(){
    int x = 20; /* Dichiarazione ed inizializzazione di variabile*/
    float g;  /* Dichiarazione */
    
    g = 5; // inizializzazione

    while ( my_abs( g*g - x ) > 0.00001 ) {
        g = ( g + x/g )/2;
    }

    printf( "La radice quadrata di %d = %f\n", x, g );  // stampa dell'output
}
