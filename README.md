# Programmazione dei Calcolatori con Laboratorio aa 2024-25

## Descrizione

Lo scopo del corso è introdurre agli studenti il concetto di problema computazionale e di risoluzione automatica mettendoli in grado di comprendere ed analizzare la struttura di un problema, individuare metodi di risoluzione alternativi, raffrontarli dal punto di vista dell’efficienza, implementarli mediante un opportuno linguaggio di programmazione e valutarne la correttezza.

In particolare verranno trattati i seguenti temi: risoluzione automatica dei problemi; algoritmi e programmi; modelli di calcolo; linguaggi di programmazione; tipi di linguaggi di programmazione; compilazione ed interpretazione; linguaggi imperativi; struttura di un programma; tipi di dati semplici e strutturati; variabili; strutture di controllo; puntatori; funzioni; ricorsione; operazioni di input/output; strutture di dati elementari (array, liste e dizionari).

Durante il corso verranno presentati una quantità di problemi che saranno risolti facendo riferimento ai linguaggi di programmazione Python e C.

Il corso è composto da due parti che si sovrappongono sia come contenuti che temporalmente. Una  parte fornisce una introduzione generale ai temi sopra elencati. L'altra parte è orientata alla soluzione dei problemi proposti utilizzando linguaggi di programmazione ad alto livello: a tale scopo verrà presentati il linguaggi Python e e C.

## Testi di riferimento

- John V. Guttag. *Introduzione alla programmazione con Python*. EGEA 2021
- Gianluca Rossi. *Programmazione in Python - Esercizi*. EGEA 2022 (digital book)
- Un qualsiasi manuale del linguaggio C ad esempio: *Linguaggio C* (seconda edizione) di B.Kernighan e D.Ritchie edito da Pearson Education Italia
- Gianluca Rossi. *Programmazione dei calcolatori - Appunti delle lezioni*. [Dispense](https://www.dropbox.com/s/zsu3k8ealgka0ne/dispense_programmazione.pdf?dl=1) (Per la parte sulle strutture dati dinamiche in C).

## Altre risorse

- [Canale MS-Teams](https://teams.microsoft.com/l/team/19%3aa6a29db18c834a8fb822d968ea008f10%40thread.tacv2/conversations?groupId=07158cb1-0fc1-4930-befd-80987312c5f0&tenantId=24c5be2a-d764-40c5-9975-82d08ae47d0e)

- [Video tutorial su come installare Python e Spyder su Windows](https://uniroma2-my.sharepoint.com/:v:/g/personal/gianluca_rossi_uniroma2_eu/EQwbP4aTYMxEnLrxRGZtMRYB-20LYLaXyQ19SwV6rrm6PQ?e=fxjSXS&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

- [Video tutorial su come installare Linux Debian su Windows](https://uniroma2-my.sharepoint.com/:v:/g/personal/gianluca_rossi_uniroma2_eu/EdZy3iCANylLn9JaNoP5qrsBdFFMvB-I55rUgrAKxY5h8g?e=Q8LHAw&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

## Calendario delle lezioni

* Lunedì, martedì e venerdì dalle 9:15 alle 10:45

-------------------------------

## Diario delle lezioni

**IMPORTANTE** Per accedere ai video delle lezioni bisogna iscriversi al canale Teams 👆

### Lezione 1 del 2024/10/07

Introduzione al corso. Il *metodo algoritmo*. Esempi: l'enigma di Guarini e il calcolo della radice quadrata.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%201%20del%207_10_2024-20241007_093313-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 2 del 2024/10/08

Dimostrazione di correttezza dell'algoritmo per la radice quadrata. Introduzione al linguaggio Python. L'interprete e la console. Il primo programma Python e le sue componenti: commenti; variabili; assegnazioni; funzioni incorporate (`print()`, `abs()`); ciclo `while` e condizioni; blocchi ed *indentazioni*; tipi di dato (`int`, `float`, `str` e `bool`). Tipi di dato ed operatori: la funzione incorporata `type()`; operatori tra tipi numerici (somma, differenza, moltiplicazione, divisione). Dipendenza del tipo di un'espressione dal tipo dei suoi operandi e dagli operatori coinvolti. La funzione incorporata `input()`. Le funzioni di conversione `float()` e `int()`.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%202%20del%208_10_2024-20241008_091545-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 3 del 2024/10/11

Cenni sulla *Macchina di Von Neumann*. Linguaggi ad alto livello compilati ed interpretati. L'interprete Python e l'utilizzo della console.
Assegnamenti multipli. Il tipo `bool` e gli operatori logici `and`, `or` e `not`. Gli operatori relazionali `<, <=, ==, !=, >=, >`. Gli operatori aritmetici `%` e `**`. L'operatore `+=`. Il tipo di dato stringa (`str`): confronto (ordinamento lessicografico); concatenazione; ripetizione; la funzione `len()`; indicizzazione.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%203%20del%2011_10_2024-20241011_091632-Registrazione%20della%20riunione%201.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

#### Esercizi

1. Si scriva un programma che conti e stampi quante volte compare il carattere ` ` (spazio) all'interno di una stringa legata alla variabile `a`. Il programma deve far uso soltanto dei costrutti Python fin qua studiati. *Suggerimento*: potrebbe essere utile un ciclo `while` che conta il numero di spazi consecutivi a partire da una posizione e che sia 'annidato' nel ciclo principale che scorre i caratteri della stringa.

2. Modificare il codice precedente facendo in modo che il programma conti il numero di vocali minuscole all'interno della stringa. Risolvere il problema usando l'operatore `in` di seguito descritto.
   
    Siano `x` e `y` due stringhe, `x in y` vale `True` se e solo se la stringa `x` è sottostringa di `y`. Ad esempio
   
   ```python
       'yt' in 'Python'
   ```
   
    vale `True` mentre
   
   ```python
       'a' in 'Python'
       'yht' in 'Python'
   ```
   
    valgono `False`

### Lezione 4 del 2024/10/14

Soluzione degli esercizi. L'operatore `in`. Le strutture di controllo `if...elif...else` e `for`. Valutazione del numero di operazioni eseguite da due diverse soluzioni dello stesso problema: operazioni nascoste da operazioni su dati strutturati. Le funzioni incorporate `ord()` e `chr()`.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%204%20del%202024-10-14-20241014_091327-Registrazione%20della%20riunione%201.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 5 del 2024/10/15

Conversione maiuscole/minuscole con le funzioni `ord()` e `chr()`. Definizione di **funzioni**; l'istruzione `return`; parametri delle funzioni; passaggio dei parametri per posizione e per nome; parametri opzionali e valori di default; variabili locali. Ancora sulle stringhe: indicizzazione negativa e *slicing*; come invertire una stringa. Considerazioni sull'efficienza delle operazioni precedenti nella soluzione del problema della verifica della palindromia.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%205%20del%202024-10-15-20241015_091942-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 6 del 2024/10/18

Funzioni: la funzione `help()` e le *docstring*. Costo computazionale: il tempo misurato contando il numero di operazioni elementari eseguite da un algoritmo; il caso peggiore; l'ordine di grandezza della funzione costo.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%206%20del%202024-10-18-20241018_092142-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)


### Lezione 7 del 2024-10-21

Complessità temporale, notazione *O*-grande e *Theta*-grande. Immutabilità delle stringhe. La truttura dati **tupla**: proprietà, operatori (indicizzazione, slicing, iterazione, concatenazione, ripetizione, impacchettamento e spacchettamento) e la funzione `len()`, immutabilità. La struttura dati **lista**: operatori (vedere tuple), *mutabilità*, le funzioni `len()` e `del()`, ed il *metodo* `append()`. Complessità delle funzioni ed operatori sulle strutture introdotte.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%207%20del%202024-10-21-20241021_091607-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)  


### Lezione 8 del 2024-10-22

La funzione `range()`. Il metodo `join()` del tipo `str` e come usarlo per evitare concatenazioni ripetute. L'operatore di assegnazione tra liste e *aliasing*; copiare una lista (clonazione). La funzione `id()`.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%208%20del%202024-10-22-20241022_091641-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view) 
### Lezione 9 del 2024-10-25

Approfondimento sulle funzioni: definizione, parametri formali e attuali, variabili locali e visibilità, frame o ambiente di una funzione, la pila dei frame, specifiche (descrizione dell'input e dell'output). Liste come argomento di funzione (*aliasing*). Approfondimento: correttezza di una soluzione rispetto alla specifica del problema. Ottimizzazione della complessità temporale aumentando la richiesta di spazio di memoria. Complessità spaziale: stima della quantità di **memoria supplementare** utilizzata da una soluzione.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%209%20del%202024-10-25-20241025_091455-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)


### Lezione 10 del 2024-10-28

Gli operatori di confronto tra sequenze (stringhe, tuple, liste). Le funzioni incorporate `min()` e `max()` ed l'utilizzo del parametro `key` per personalizzare il criterio di confronto fra gli elementi. Funzioni locali (definite all'interno di altre funzioni) e funzioni come parametro di funzione. La funzione `range()` per generare una sequenza di interi che partono da un valore determinato. Il problema di disegnare `n` punti su una retta: calcolo della complessità temporale e spaziale; dipendenza dall'output della complessità temporale.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2010%20del%202024-10-28-20241028_091648-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 11 del 2024-10-29

Il problema dell'ordinamento: l'algoritmo *bubble sort*; descrizione e complessità temporale; ottimizzazione dell'algoritmo. L'istruzione `break`. Adattare la funzione `bubble_sort()` per personalizzare il creterio di ordinamento attraverso una funzione di valutazione degli elementi della sequenza. Utilizzo dell'ordinamento per ottenere soluzioni più efficienti.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2011%20del%202024-10-29-20241029_091545-Registrazione%20della%20riunione%201.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 12 del 2024-11-04

L'algoritmo di *ricerca binaria* nella soluzione del problema della ricerca dell'intervallo contenente un punto: analisi, implementazione e complessità.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2012%20del%202024-11-04-20241104_091547-Registrazione%20della%20riunione%201.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 13 del 2024-11-05

Il problema della clonazione profonda di liste e una soluzione *ricorsiva*. Calcolo della complessità di soluzioni ricorsive e valutazione della memoria supplementare necessaria per i frame delle chiamate ricorsive.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2013%20del%202024-11-05-20241105_091600-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 14 del 2024-11-08

Complessità temporale e spaziale dell'algoritmo di clonazione profonda. Soluzione esercizi. L'algoritmo *merge-sort*: cenni preliminari.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2014%20del%202024-11-08-20241108_091656-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 15 del 2024-11-11

L'algoritmo di ordinamento per fusione (merge sort): analisi, implementazione e complessità.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2015%20del%202024-11-11-20241111_091933-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 16 del 2024-11-12

Personalizzazione del criterio di ordinamento con parametro `key`; ordinamento multicriterio tramite confronto tra tuple. Funzioni `lambda`. Espressioni condizionali. La funzione incorporata `sorted()` ed il metodo `sort()` delle liste.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2016%20del%202024-11-12-20241112_091755-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)


### Lezione 17 del 2024-11-15

La struttura dati **dizionario**: definizione astratta degli operatori; i dizionari in Python e complessità degli operatori. Il dizionario come struttura dati di appoggio che consente algoritmi più efficienti: esempi.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2017%20del%202024-11-15-20241115_091619-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 18 del 2024-11-18

La funzione `zip()`. I medoti `keys()`, `values()`, `items()` e `get()` della struttura `dict`. Il problema dell'intersezione tra insiemi: approfondimenti sulla complessità.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2018%20del%202024-11-18-20241118_092252-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view) 

### Lezione 19 del 2024-11-19

Differenza tra linguaggi interpretati e compilati. Alcuni utili comandi della *shell* di Linux. Introduzione al linguaggio C: la compilazione; la funzione `main()`; dichiarazioni di variabili e assegnazione; blocchi; la funzione `printf()`; ciclo `while` e le istruuzioni `if...else..`; dichiarazioni di funzioni.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2019%20del%202024-11-19-20241119_092215-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 20 del 2024-11-22

Linguaggio C: tipi di dato `int` e `float`; operatori aritmetici; conversione (*casting*) di tipo implicito; valutare il tipo di una espressione; casting esplicito; operatori relazionali; il *prototipo* delle funzioni; la direttiva `include`; in tipo di dato `char` e la codifica *ASCII*.

* [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2020%20del%202024-11-22-20241122_092435-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view) 


#### Esercizi

1. Calcolale la complessità temporale nel caso medio della funzione Python `del()` applicata ad un elemento di una lista. Nel risolvere l'esercizio si tenga conto che la cancellazione di un elemento in posizione `i` della lista `a` dichiede `(n-i)*c` operazioni per una oppotuna costante `c` dove `n = len(a)`.

2. Scrivere una funzione Python che soddisfi la seguente specifica:

    ```python
        def anagramma(a, b):
            '''
            Parametri: a, b stringhe
            Return: True se e solo se a e b sono anagrammi
            '''
    ```

3. Scrivere una funzione C avente il seguente prototipo:

    ```C
        float potenza(float x, int e);
    ```

    che ritorna il valore $x^e$.


### Lezione 21 del 2024-11-25

Soluzione degli esercizi. Gli array in C e il costrutto `for`.

- [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2021%20del%202024-11-25-20241125_091521-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 22 del 2024-11-26

Allocazione della memoria *statica* e *dinamica*; i puntatori, definizioni e gli operatori `*` e `&`; le funzioni `malloc()`, `sizeof()` e `free()`; la costante `NULL`; aritmetica dei puntatori; definizione di array con allocazione dinamica della memoria; array come input ed output di funzioni.

- [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2022%20del%202024-11-26-20241126_091534-Registrazione%20della%20riunione%201.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 23 del 2024-11-29

Come implementare in modo efficiente l'operazione di `append` su un array allocato dinamicamente: costo temporale e spaziale. La funzione di libreria `realloc()`. I costrutti `struct` e `typedef`. 

- [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2023%20del%202024-11-29-20241129_091732-Registrazione%20della%20riunione.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)  

### Lezione 24 del 2024-12-02

Le stringhe in C: definizioni; il carattere `\0` di fine stringa; allocazione statica e dinamica; le funzioni `strlen()`, `strcmp()`, `strcpy()` della libreria `string` e loro implementazione e complessità.

- [Video della lezione](https://uniroma2.sharepoint.com/sites/msteams_6c3e26/Documenti%20condivisi/Lezioni%202024-25/Recordings/Solo%20visualizzazione/Lezione%2024%20del%202024-12-02-20241202_091508-Registrazione%20della%20riunione%201.mp4?web=1&referrer=Teams.TEAMS-ELECTRON&referrerScenario=MeetingChicletGetLink.view)

### Lezione 25 del 2024-12-03

Implementazione di array dinamici in C con elementi di tipo disomogeneo: il tipo di dato `void` e l'utilizzo di puntatori a `void`; l'istruzione `switch`; l'operazione di `pop()` che elimina dalla struttura l'ultimo elemento; considerazione sull'utilizzo della memoria.

- [Video della lezione](https://uniroma2.sharepoint.com/:v:/s/msteams_6c3e26/Edw2hcGBEldMvzXHIgLQiQQBhHgsT5XjB0ziKPo-7XaDxg?e=cARwzL)

### Lezione 26 del 2024-12-06

Array dinamici: inserimento (e cancellazione per esercizio) di un elemento in posizione generica di una lista. Le funzioni `scanf()` e `sscanf()`; un modo per riconoscere i tipi.

- [Video della lezione](https://uniroma2.sharepoint.com/:v:/s/msteams_6c3e26/EYNgGQtyTUVLtt5gp8Ll4NMBJL0Rq2qKuGXaxWdI0fcWnA?e=YaMl6a)

### Lezione 27 del 2024-12-09

Esercizi in C e Python. La list comprehension in Python.

- [Video della lezione](https://uniroma2.sharepoint.com/:v:/s/msteams_6c3e26/EWATB3MlLUdNgy-6BOEMjMAB4-ZuQ0AskAgHUCzZTSwylg?e=UDZOKj)

### Lezione 28 del 2024-12-10

Verso l'implementazione della della struttura dati *dizionario* partendo dagli array.

- [Video della lezione](https://uniroma2.sharepoint.com/:v:/s/msteams_6c3e26/Ec2SgpFsjBZKqzjJbQlEhuIBTW0d_VJxtWxJNzH7oUX0sw?e=llDpad)

### Lezione 29 del 2024-12-13

La struttura dati **lista concatenata**: definizioni; operatori ed implementazione delle funzioni di ricerca ed inserimento in testa.

- [Video della lezione](https://uniroma2.sharepoint.com/:v:/s/msteams_6c3e26/EdKlAYriFjlKpgPXYiIHz6UBoy1wpo6dDEJKvgWZ3Vh4Fw?e=MRdxnl)

### Lezione 30 del 2024-12-16

Liste concatenate: operazione di cancellazione.

- [Video della lezione](https://uniroma2.sharepoint.com/:v:/s/msteams_6c3e26/ETXX4nCQm59DomddxFozdgkB9yIH7jCKLTixinS8pDOn8Q?e=Ix2FaL)

### Lezione 31 del 2024-12-17

Implementazione della struttura dati *dizionario* con array di liste concatenate.

- [Video della lezione](https://uniroma2.sharepoint.com/:v:/s/msteams_6c3e26/ET9zfMB3b6tNiNpBDjTc4JsBNjsVl1a3HeJEldWzOypHoQ?e=lcTVNc)


### Lezione 32 del 2024-12-20

Funzioni *hash*: funzione somma e DJB2. Operatori bit a bit. Esercizio risolto: implementazione della funzione di inserimento in posizione data di una lista concatenata. Gestione in C degli argomenti alla linea di comando.

- [Video della lezione](https://uniroma2.sharepoint.com/:v:/s/msteams_6c3e26/EVB5zFV18OlJq4BeVSP5aBYBdrpRmbdeoOzX5le_e_hFeg?e=exMaF6)

### Lezione 33 del 2024-12-23

**Esercizio.** Implementare la struttura dati *coda*: implementazione con array dinamici e con liste concatenate (finalizzare per esercizio).

- [Video della lezione](https://uniroma2.sharepoint.com/:v:/s/msteams_6c3e26/Ecqev6cKC7pNpXjzoOAwUXcBRCqYho6nUp0CIXKYXbrEVA?e=cwkM9a)

### Lezione 34 del 2025-01-07

Python: funzioni con numero variabile di parametri posizionali; l'operatore di *spacchettamento* `*`; moduli esterni; la libreria **matplotlib**; l'operatore `*` e la funzione `zip`; lettura e scrittura di file di testo (funzione `open()` e metodo `close()`).

**Esercizio.** Scrivere un programma che, usando una opportuna funzione in matplotlib, disegni un diagramma a barre che mostri le occorrenze di tutte le lettere all'interno di un file di testo. Si utilizzi il file `promessi_sposi.txt`. 

- [Video della lezione ... TODO]()
