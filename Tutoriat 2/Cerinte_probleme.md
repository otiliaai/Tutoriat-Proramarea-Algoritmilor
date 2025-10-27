

# PROBLEMA 1
---
## 📝 Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Sunt formate exclusiv din litere mici (`a`-`z`).
* **Separatorii:** Sunt spațiul (` `) și setul de caractere: `.,!?:;-`.

---

## ✨ Cerințe Funcționale ($T$)

Programul citește mai întâi $T$ și apoi textul. Rezultatul se afișează la Ieșirea Standard (Consolă).

| $T$ | Sarcina de Rezolvat | Ieșire la Consolă |
| :---: | :--- | :--- |
| **1** | **Numărare și Listare** | Numărul total de cuvinte, urmat de lista cuvintelor (câte unul pe rând). |
| **2** | **Cuvântul Minim Lexicografic** | Cuvântul care apare primul în ordine alfabetică. |
| **3** | **Căutare Subșir** | Numărul de cuvinte care conțin secvența **`ini`**. |
| **4** | **Oglindire** | Fiecare cuvânt din text, afișat **inversat** (oglindit), câte unul pe rând. |
| **5** | **Terminație Specifică** | Numărul de cuvinte care se termină cu litera **`a`**. |
| **6** | **Lungimi Extrerme** | Lungimea minimă urmată de lungimea maximă (separate printr-un spațiu). |

---

## 🔑 Restricții

* Lungimea Textului $\le 1000$ de caractere.
* Lungimea fiecărui Cuvânt $\le 50$ de caractere.

---

## 💡 Exemple

### Exemplul 1: $T=1$ (Listare)

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `1` <br> `...destul de rece? desigur!` | `4` <br> `destul` <br> `de` <br> `rece` <br> `desigur` |

### Exemplul 2: $T=4$ (Oglindire)

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `4` <br> `...destul de rece? desigur!` | `lutsed` <br> `ed` <br> `ecer` <br> `rugised` |

### Exemplul 3: $T=6$ (Min/Max)

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `6` <br> `este frumoasa, desteapta si devreme acasa.` | `2 9` |
