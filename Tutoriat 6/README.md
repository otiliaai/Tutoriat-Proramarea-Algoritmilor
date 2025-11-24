# Divide et Impera 

## 1. Conceptul de bază

Divide et Impera este o tehnică algoritmică bazată pe:

1. **Divide** — împărțirea problemei în subprobleme similare.
2. **Conquer** — rezolvarea subproblemelor (recursiv sau direct).
3. **Combine** — combinarea soluțiilor pentru a obține rezultatul final.

------------------------------------------------------------------------

## 2. Structura generală

```python
function DIVIMP(P):
    if P este mică:
        return soluție_directă(P)

    împarte P în P1, P2, ..., Pk
    pentru fiecare Pi:
        sol_i = DIVIMP(Pi)

    return combină(sol_i)
```
## 3. Relațiile de recurență

Complexitatea algoritmilor Divide et Impera se exprimă prin:

$$
T(n) = a \cdot T(n/b) + f(n)
$$



unde:  
- **a** = numărul subproblemelor  
- **b** = factorul de împărțire  
- **f(n)** = costul divizării + combinării

------------------------------------------------------------------------

## 4. Teorema Master



Comparăm funcția $f(n)$ cu termenul critic $n^{\log_b a}$.

### **Cazul 1** — Subdominant

Dacă $f(n) = O(n^c)$ unde $c < \log_b a$, atunci:

$$
T(n) = \Theta(n^{\log_b a})
$$



### **Cazul 2** — Echilibru

Dacă $f(n) = \Theta(n^{\log_b a})$, atunci:

$$
T(n) = \Theta(n^{\log_b a} \log n)
$$



### **Cazul 3** — Dominant

Dacă $f(n) = \Omega(n^c)$ unde $c > \log_b a$ și există o constantă $k < 1$ astfel încât:

$$
a \cdot f\left(\frac{n}{b}\right) \le k \cdot f(n)
$$

atunci:

$$
T(n) = \Theta(f(n))
$$




------------------------------------------------------------------------

## 5. Proprietăți și avantaje

* **Eficiență:** Foarte eficient pentru subprobleme **disjuncte și echilibrate**.
* **Simplitate:** Implementări naturale în recursivitate.
* **Performanță:** Adesea produce complexități optime: $$O(n)$$, $$O(n \log n)$$, $$O(\log n)$$.
* **Paralelizare:** Permite execuție simultană evidentă datorită independenței subproblemelor.
* **Scalabilitate:** Comportament excelent pentru inputuri mari.

------------------------------------------------------------------------

## 6. Exemplu de problemă (nou)

### **Determinarea elementului maxim dintr-o listă prin Divide et Impera**

**Idee:** împărțim lista în două jumătăți, găsim maximul în fiecare, apoi alegem maximul dintre cele două.

### Pseudocod:

```python
function MAXIM(A, st, dr):
    if st == dr:
        return A[st]

    mij = (st + dr) // 2
    max_st = MAXIM(A, st, mij)
    max_dr = MAXIM(A, mij+1, dr)

    return max(max_st, max_dr)
```

### Recurența:

### Exemplu 

**$$T(n) = 2T\left(\frac{n}{2}\right) + O(1)$$**

**1. Identificare parametri:**
* $$a = 2$$
* $$b = 2$$
* $$f(n) = O(1) \implies n^c = n^0 \implies c = 0$$


**2. Calculul exponentului critic:**

$$
\log_b a = \log_2 2 = 1
$$

**3. Comparație:**

Comparăm exponentul funcției ($c$) cu cel critic:

$$
c = 0 < 1 = \log_b a
$$

Deoarece $$c < \log_b a$$, ne aflăm în **Cazul 1 (Subdominant)**.

**✅ Rezultat:**

$$
T(n) = \Theta(n^{\log_b a}) = \Theta(n^1) = \Theta(n)
$$

------------------------------------------------------------------------

## 7. Aplicații clasice

- căutare binară  
- Mergesort  
- algoritmul Strassen  
- FFT  
- selecția medianei (quickselect)  
- probleme geometrice (cel mai apropiat cuplu de puncte)

------------------------------------------------------------------------
## 8. Implementare Python — Exemplu Divide et Impera

Un exemplu simplu de implementare în Python pentru găsirea maximului:

```python
def maxim(A, st, dr):
    if st == dr:
        return A[st]

    mij = (st + dr) // 2
    max_st = maxim(A, st, mij)
    max_dr = maxim(A, mij + 1, dr)

    return max(max_st, max_dr)


# Exemplu de utilizare
A = [5, 1, 8, 3, 10, 2]
print(maxim(A, 0, len(A) - 1))
```

