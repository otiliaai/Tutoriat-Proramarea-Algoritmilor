## 1. NrXDivImp

Folosind metoda **Divide et Impera**, scrieți funcția recursivă cu antetul:

```python
int NrXDivImp(int a[], int st, int dr, int x)
```

care primind ca parametri un vector `a` de numere întregi și trei numere întregi `st`, `dr` și `x`, returnează numărul de apariții ale numărului `x` în secvența `a[st], a[st+1], ..., a[dr]`.

###  Restricții și precizări

* `st ≤ dr`
* Numele funcției este **NrXDivImp**.
* Vectorul `a` este indexat de la **1**.

###  Exemplu

Dacă `a = (2, 5, 1, 5, 3, 5, 5, 5, 7, 6)`, atunci:

* `NrXDivImp(a, 1, 6, 5)` returnează **3** (deoarece în secvența `2, 5, 1, 5, 3, 5` numărul `5` apare de `3` ori).
* `NrXDivImp(a, 9, 10, 5)` returnează **0**.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 2. AlternDivImp

Folosind metoda Divide et Impera, scrieți funcția recursivă cu antetul:

```python
int AlternDivImp(int a[], int st, int dr)
```
care primind ca parametri un vector `a` de numere naturale și două numere întregi `st` și `dr`, returnează `1` dacă în secvența `a[st], a[st+1], ..., a[dr]` numerele impare alternează cu cele pare, sau returnează `0` dacă există cel puțin două numere alăturate de aceeași paritate.

###  Restricții și precizări

* `st ≤ dr`
* Numele funcției este **AlternDivImp**.
* Vectorul `a` este indexat de la **1**.

### Exemplu

Dacă `a = (1,2,3,4,5,6,7,8,9,11)`, atunci :

* `AlternDivImp(a, 1, 10) = 0`, deoarece numerele 9 și 11 aflate pe poziții alăturate au aceeași paritate
* `AlternDivImp(a, 1, 8) = 1`

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 3. QuickSort

Folosind metoda Divide et Impera, scrieți funcția recursivă cu antetul:

```python
void QuickSort(int a[], int st, int dr)

```
care primind ca parametri un vector `a` de numere întregi și două numere întregi `st` și `dr`, ordonează crescător elementele din secvența `a[st], a[st+1], ..., a[dr]` folosind algoritmul QuickSort.

### Restricții și precizări

* `st ≤ dr`
* Numele funcției este **AlternDivImp**.
* Vectorul `a` este indexat de la **1**.
* Se va utiliza metoda de partiționare specifică algoritmului QuickSort.

### Exemplu
input:

```python
12
10 0 -1 -3 1 -4 9 3 -1 -4 3 -4

```

output:

```python
-4 -4 -4 -3 -1 -1 0 1 3 3 9 10

```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 4. SumPrimDEI

Se consideră un șir cu `n` elemente, numere naturale. Folosind metoda `Divide et Impera`, determinați suma elementelor prime din acest șir.

### Exemplu
input:

```python
6
4 11 8 4 3 5 

```

output:

```python
19

```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 5. CntImpare

Se consideră un șir cu `n` elemente, numere naturale. Folosind metoda `Divide et Impera`,  determinați câte elemente impare sunt în acest șir.

### Exemplu
input:

```python
6
4 1 8 4 3 5 

```

output:

```python
3

```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 6. ExistaPrimeDivImp

Se consideră un șir cu `n` elemente, numere naturale. Folosind metoda `Divide et Impera`,  să se verifice dacă în şir există elemente prime.

### Exemplu
input:

```python
5
21 8 6 10 8

```

output:

```python
NU

```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







