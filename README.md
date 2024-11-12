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
