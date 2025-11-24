# Divide et Impera ---

## 1. Conceptul de bază

Divide et Impera este o tehnică de proiectare a algoritmilor construită
pe următorii pași:

1.  **Divide** --- Problema este împărțită în mai multe subprobleme de
    același tip, de regulă de dimensiuni similare.
2.  **Conquer** --- Subproblemele sunt rezolvate independent; dacă devin
    suficient de mici, se rezolvă direct.
3.  **Combine** --- Soluțiile subproblemelor sunt combinate pentru a
    forma soluția finală.

Această tehnică este în mod natural recursivă și eficientă atunci
când: - subproblemele nu se suprapun, - divizarea reduce semnificativ
dimensiunea problemei.

------------------------------------------------------------------------

## 2. Forma generală a unui algoritm Divide et Impera

Pseudocodul standard este:

    function DIVIMP(P):
        if P este suficient de mică:
            return soluție_directă(P)

        împarte P în P1, P2, ..., Pk
        soluții = []
        pentru fiecare Pi:
            soluții.append(DIVIMP(Pi))

        return combină(soluții)

Elemente importante: - „dimensiune mică" înseamnă adesea 1 element, 0
elemente sau un prag fix. - operația de combinare depinde de problemă:
poate fi o interclasare, o suma, un maxim etc.

------------------------------------------------------------------------

## 3. Relațiile de recurență

Complexitatea algoritmilor Divide et Impera este determinată prin:

\[ T(n) = a `\cdot `{=tex}T`\left`{=tex}(rac{n}{b}ight) + f(n) \]

unde: - **a** = numărul subproblemelor, - **b** = factorul de împărțire
al dimensiunii, - **f(n)** = costul divizării și combinării.

------------------------------------------------------------------------

## 4. Teorema Master

Pentru recurența standard, se compară funcția ( f(n) ) cu (
n\^{`\log`{=tex}\_b a} ):

-   **Caz 1:** dacă ( f(n) = O(n\^{c}) ) unde ( c \< `\log`{=tex}\_b a
    ), atunci\
    \[ T(n) = O(n\^{`\log`{=tex}\_b a}) \]

-   **Caz 2:** dacă ( f(n) = `\Theta`{=tex}(n\^{`\log`{=tex}\_b a}) ),
    atunci\
    \[ T(n) = O(n\^{`\log`{=tex}\_b a} `\log `{=tex}n) \]

-   **Caz 3:** dacă ( f(n) = `\Omega`{=tex}(n\^c) ) cu ( c \>
    `\log`{=tex}\_b a ) și condiție de regularitate, atunci\
    \[ T(n) = O(f(n)) \]

------------------------------------------------------------------------

## 5. Proprietăți și avantaje

-   eficiență ridicată pentru probleme care se împart uniform și nu
    produc subprobleme suprapuse;
-   permite optimizări avansate (ex.: folosirea unui prag pentru a
    schimba la algoritmi iterativi);
-   structură recursivă naturală, ușor de implementat.

------------------------------------------------------------------------

## 6. Aplicații clasice 

-   algoritmi eficienți pentru găsirea minimului/miximului prin
    comparări structurate;
-   multiplicarea rapidă a matricilor (ex. algoritmul lui Strassen);
-   transformări rapide (ex. FFT);
-   algoritmi geometrici (divide & conquer pentru determinarea cuplului
    de puncte cele mai apropiate);
-   metode pentru determinarea elementelor statistice (ex. selecția
    medianei utilizând tehnici de partiționare).

------------------------------------------------------------------------

## 7. Observații importante

-   dacă subproblemele nu sunt echilibrate sau se suprapun,
    complexitatea poate deveni exponențială;
-   folosirea unei strategii bune de divizare (pivot, mediana medianelor
    etc.) este crucială pentru performanță;
-   mulți algoritmi optimizați folosesc combinații între Divide et
    Impera și tehnici iterative.
