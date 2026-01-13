# Rezolvare subiecte colocviu și examen

-----


## SUBIECT EXAMEN(2025)

### Cerințele examenului:
1.  **Subiectul I** este obligatoriu.
2.  Dintre subiectele II, III și IV trebuie alese **CEL MULT DOUĂ**.

### 1. Subiectul I - `subiect_1.py`
Acest fișier conține rezolvarea celor trei subpuncte obligatorii:
* **a) Funcția `consoane_comune`**: Primește un număr variabil de cuvinte și returnează numărul maxim de cuvinte care au exact aceeași mulțime de consoane.
* **b) List Comprehension (`prefix_5`)**: Filtrarea unei liste de numere astfel încât să rămână doar cele care nu sunt multipli de 5 și nu au prefixe multipli de 5.
* **c) Analiza complexității**: Determinarea complexității (în cel mai defavorabil caz) pentru o funcție recursivă dată `f(s)`, care împarte șirul în jumătăți (Divide et Impera).

### 2. Subiectul II (Metoda Greedy) - `subiect_2.py`
**Problema:** Alimentarea mașinilor cu canistre de benzină.
* **Descriere:** Se dau $n$ mașini cu necesar de benzină și $m$ canistre cu capacități date. O mașină poate primi o singură canistră.
* **Obiectiv:** Maximizarea numărului de mașini care ajung la destinație.
* **Complexitate:** $O(N \log N)$ (bazată pe sortarea mașinilor și a canistrelor).
* **Output:** Numărul de mașini și perechile `Mașină -> Canistră`.

### 3. Subiectul III (Programare Dinamică) - `subiect_3.py`
**Problema:** Tăierea barei de metal (Rod Cutting Problem variation).
* **Descriere:** Un meșteșugar are o bară de lungime $L$ și comenzi pentru bucăți de lungimi $l_i$ cu prețuri $p_i$.
* **Obiectiv:** Maximizarea câștigului total prin tăierea barei.
* **Complexitate:** $O(k \cdot L)$, unde $k$ este numărul de tipuri de bucăți și $L$ lungimea barei.
* **Output:** Câștigul maxim și lungimile bucăților tăiate (afișate crescător).

### 4. Subiectul IV (Backtracking) - `subiect_4.py`
**Problema:** Generare coduri PIN "mega-sigure".
* **Descriere:** Generarea codurilor de lungime $n$ care:
    * Nu au cifre nule.
    * Nu au cifre alăturate egale.
    * Orice cifră apare de cel mult $p$ ori.
* **Output:** Toate codurile care respectă condițiile și numărul total al acestora.


------ 

## SUBIECT COLCVIU(2025)
