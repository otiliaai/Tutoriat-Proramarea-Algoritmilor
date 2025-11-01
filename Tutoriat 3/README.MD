## 📘 Introducere

În Python, **colecțiile de date** sunt structuri care permit stocarea și gestionarea mai multor valori într-o singură variabilă.  
Ele sunt esențiale în programare, deoarece facilitează organizarea, procesarea și analizarea datelor.

Cele mai importante tipuri de colecții sunt:
- **Liste (`list`)** – colecții ordonate și modificabile.
- **Tupluri (`tuple`)** – colecții ordonate, dar nemodificabile.
- **Seturi (`set`)** – colecții neordonate, fără elemente duplicate.
- **Dicționare (`dict`)** – perechi cheie-valoare.

Acest curs se concentrează pe **liste** și **tupluri**, cele mai frecvent folosite tipuri de colecții în Python.

---

## 1. Liste (Lists)

### 1.1 Ce este o listă?

O **listă** este o colecție **ordonată**, **mutabilă** și **heterogenă** (poate conține elemente de tipuri diferite).

#### 🧩 Exemple:
```python
# Listă goală
lista_goala = []

# Listă de numere
numere = [10, 20, 30, 40]

# Listă mixtă
student = ["Ion Popescu", 19, 9.75, True]

# Listă de liste (matrice simplă)
matrice = [[1, 2], [3, 4]]
