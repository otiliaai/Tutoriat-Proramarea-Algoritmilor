#PROBLEMA 1
---
Se citește un text format din cuvinte și separatori.  
Cuvintele sunt formate din litere mici ale alfabetului, iar separatorii sunt spațiul și caracterele din șirul `.,!?:;-`.

---

## Cerințe
În funcție de valoarea lui `T` (1 ≤ T ≤ 6) se cere una dintre următoarele operații:

1. (`T = 1`) Afișați `n` — numărul de cuvinte din text, apoi lista cuvintelor, câte unul pe rând.  
2. (`T = 2`) Afișați cuvântul cel mai mic lexicografic.  
3. (`T = 3`) Afișați numărul de cuvinte care conțin secvența `ini`.  
4. (`T = 4`) Afișați fiecare cuvânt oglindit (inversat), câte unul pe rând.  
5. (`T = 5`) Afișați numărul de cuvinte care se termină cu litera `a`.  
6. (`T = 6`) Afișați, separate printr-un spațiu, lungimea minimă și lungimea maximă a unui cuvânt.

> Notă: după citirea lui `T`, se citește o linie întreagă care conține textul.

---

## Date de intrare
- Prima linie: numărul natural `T`  
- A doua linie: textul propriu-zis

## Date de ieșire
Programul va afișa rezultatul cerut pentru `T`.

---

## Exemple

### Exemplul 1
**Input:**
```python
1
...destul de rece? desigur!

```
**Output:**
```python
4
destul
de
rece
desigur
```
