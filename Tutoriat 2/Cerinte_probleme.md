# ✍️ TextCuv: Analiza Textului ($T$)

## 📝 Cerințe și Ieșiri

Programul citește de la **Intrarea Standard** (Consolă) un parametru $T$ (între 1 și 6), urmat de textul de analizat. Rezultatul se afișează la **Ieșirea Standard**.

| $T$ | Sarcina de Rezolvat | Formatul Ieșirii la Consolă |
| :---: | :--- | :--- |
| **1** | Numărul total de cuvinte și lista lor. | Numărul total, urmat de cuvinte (câte unul pe rând). |
| **2** | Cuvântul cel mai mic **lexicografic**. | Cuvântul unic. |
| **3** | Numărul de cuvinte care conțin secvența **`ini`**. | Numărul (integer). |
| **4** | Fiecare cuvânt **oglindit** (inversat). | Cuvintele inversate (câte unul pe rând). |
| **5** | Numărul de cuvinte care se **termină** cu litera **`a`**. | Numărul (integer). |
| **6** | **Lungimea minimă** și **lungimea maximă** a unui cuvânt. | Lungimea minimă, spațiu, Lungimea maximă. |

---

## 🔑 Restricții

* **Cuvinte:** Doar litere mici (`a`-`z`).
* **Separatori:** Spațiul (` `) și setul: `.,!?:;-`.
* Lungime Text $\le 1000$.
* Lungime Cuvânt $\le 50$.

---

## 💡 Exemple

### Exemplul 1: $T=1$ (Listare)

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `1` <br> `...destul de rece? desigur!` | `4` <br> `destul` <br> `de` <br> `rece` <br> `desigur` |

### Exemplul 2: $T=2$ (Lexicografic Minim)

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `2` <br> `avem parte de exclamatii, accente si mirari.` | `accente` |

### Exemplul 3: $T=4$ (Oglindire)

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `4` <br> `...destul de rece? desigur!` | `lutsed` <br> `ed` <br> `ecer` <br> `rugised` |

### Exemplul 4: $T=6$ (Lungimi Min/Max)

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `6` <br> `este frumoasa, desteapta si devreme acasa.` | `2 9` |
