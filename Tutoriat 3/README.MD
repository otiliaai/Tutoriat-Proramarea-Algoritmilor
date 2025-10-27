# Introducere în Liste (Lists) în Python
---

## 1. Ce Este o Listă în Python?

O **listă** este o colecție de elemente, declarată ca fiind:

1.  **Ordonată:** Elementele au o ordine bine definită (index) și această ordine nu se schimbă decât dacă este modificată explicit.
2.  **Mutabilă:** Poate fi modificată după ce a fost creată (elementele pot fi adăugate, șterse sau schimbate).
3.  **Heterogenă:** Poate conține elemente de tipuri de date diferite (e.g., `int`, `str`, `float`, sau chiar alte liste).

### Sintaxă:

Listele sunt definite folosind **paranteze drepte** (`[]`).

```python
# Listă goală
lista_goala = []

# Listă cu numere
numere = [10, 20, 30, 40]

# Listă cu elemente mixte
student = ["Ion Popescu", 19, 9.75, True]

# Listă de liste (matrice simplă)
matrice = [[1, 2], [3, 4]]
```


## 2. Accesarea Elementelor (Indexare & Slicing)

Elementele unei liste sunt accesate pe baza **indexului** lor, care începe întotdeauna de la **0**.

### A. Indexarea Simplă

| Elementul | Index (pozitiv) | Index (negativ) |
| :---: | :---: | :---: |
| `10` | $\mathbf{0}$ | $\mathbf{-4}$ |
| `20` | $1$ | $-3$ |
| `30` | $2$ | $-2$ |
| `40` | $\mathbf{3}$ | $\mathbf{-1}$ |

```python
numere = [10, 20, 30, 40]

# Accesarea primului element
print(numere[0])    # Ieșire: 10

# Accesarea ultimului element (folosind indexul negativ)
print(numere[-1])   # Ieșire: 40
```

### B. Slicing (Felierea)

Slicing-ul permite extragerea unei **sub-liste** (o porțiune) dintr-o listă, folosind sintaxa: `lista[start:stop:pas]`.

* **`start`**: Indexul de la care începe sub-lista (inclusiv).
* **`stop`**: Indexul la care se oprește sub-lista (**exclusiv**).
* **`pas`**: Intervalul de săritură (implicit este 1).

```python
litere = ["a", "b", "c", "d", "e", "f"]

# Primele trei elemente
print(litere[0:3])    # Ieșire: ['a', 'b', 'c']

# Toate elementele de la indexul 2 până la sfârșit
print(litere[2:])     # Ieșire: ['c', 'd', 'e', 'f']

# Toate elementele din listă (copie a listei)
print(litere[:])      # Ieșire: ['a', 'b', 'c', 'd', 'e', 'f']

# Elementele cu pas de 2
print(litere[::2])    # Ieșire: ['a', 'c', 'e']

```

## 3. Modificarea Listelor (Mutabilitate)

Listele suportă adăugare, ștergere și înlocuire de elemente, deoarece sunt **mutabile**.

### A. Adăugarea Elementelor

| Metodă | Descriere | Exemplu |
| :--- | :--- | :--- |
| **`.append(element)`** | Adaugă un element la **sfârșitul** listei. (Cea mai frecventă) | `lista.append("nou")` |
| **`.insert(index, element)`** | Adaugă un element la o **poziție specificată**. | `lista.insert(1, "pozitie")` |
| **`.extend(lista_noua)`** | Adaugă **toate elementele** unei alte liste la lista curentă. | `lista.extend([1, 2])` |

### B. Modificarea și Ștergerea Elementelor

| Metodă/Operator | Descriere | Exemplu |
| :--- | :--- | :--- |
| **Înlocuire** | Se schimbă valoarea unui element folosind indexul. | `lista[0] = "schimbat"` |
| **`.remove(valoare)`** | Elimină **prima apariție** a unei valori specificate. | `lista.remove("b")` |
| **`.pop(index)`** | Elimină și **returnează** elementul de la index. Fără argument, elimină ultimul element. | `ultimul = lista.pop()` |
| **`del`** | Șterge un element pe baza indexului sau o întreagă secțiune (*slicing*). | `del lista[2]` sau `del lista[1:3]` |

```python
materii = ["Algebra", "Analiza", "Fizica"]
```

# 1. Adăugare la sfârșit
materii.append("Programare")
# ["Algebra", "Analiza", "Fizica", "Programare"]

# 2. Modificare
materii[1] = "Analiza Matematică"
# ["Algebra", "Analiza Matematică", "Fizica", "Programare"]

# 3. Ștergere după valoare
materii.remove("Fizica")
# ["Algebra", "Analiza Matematică", "Programare"]

# 4. Ștergere după index (și returnare)
materii.pop(0)
# ["Analiza Matematică", "Programare"]


## 4. Funcții Utile pentru Liste

Aceste funcții și metode sunt folosite des pentru a obține informații sau a manipula conținutul unei liste.

| Funcție/Metodă | Descriere | Exemplu |
| :--- | :--- | :--- |
| **`len(lista)`** | Returnează **numărul de elemente** din listă. | `lungime = len(materii)` |
| **`in` (Operator)** | Verifică dacă o valoare **există** în listă (returnează `True`/`False`). | `"Python" in materii` |
| **`.index(valoare)`** | Returnează **indexul** primei apariții a valorii. **Atenție:** dă eroare dacă valoarea nu există. | `idx = materii.index("Programare")` |
| **`.count(valoare)`** | Returnează de câte ori apare o valoare în listă. | `nr_a = litere.count('a')` |
| **`.sort()`** | **Sortează** lista pe loc (direct în listă). Modifică lista originală. | `numere.sort()` |
| **`sorted(lista)`** | Returnează o **listă nouă sortată**, lăsând lista originală neschimbată. | `noua = sorted(numere)` |
| **`.reverse()`** | Inversează ordinea elementelor **pe loc** (direct în listă). | `lista.reverse()` |

---
