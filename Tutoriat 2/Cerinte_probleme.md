
# PROBLEMA 1 : Prelucrare text

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


---


# 💻 PROBLEMA 2: Cuvinte cu Lungimi Egale

## 📝 Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Sunt formate din litere mici (`a`-`z`).
* **Separatorii:** Sunt spațiul (` `) și setul de caractere: `.,!?:;-`.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Găsirea Perechii Adiacente** | Se afișează cele două cuvinte consecutive cu aceeași lungime, separate printr-un spațiu. Dacă nu există, se afișează mesajul **`NU`**. |

---

## 🔑 Restricții

* Se afișează doar **prima pereche** întâlnită.

---

## 💡 Exemple

### Exemplul 1 (Găsit)

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `ce face acum el la mare.` | `face acum` |

### Exemplul 2 (Negăsit)

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `o floare mica si frumoasa.` | `NU` |

# 💻 PROBLEMA 3: Cuvinte Prefixe

## 📝 Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Sunt formate din litere mici (`a`-`z`).
* **Separatorii:** Sunt spațiul (` `) și setul de caractere: `.,!?:;-`.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Identificarea Cuvintelor care sunt Prefix** | Se afișează, pe rânduri separate, cuvintele care sunt prefixe ale altor cuvinte din text, în **ordinea apariției** în textul original. |

---

## 🔑 Restricții

* Un cuvânt **nu** este considerat prefix al lui însuși.
* Fiecare cuvânt care îndeplinește condiția se afișează o singură dată.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `a avea acel ceas, a acorda atentie.` | `a` <br> `ace` <br> `acorda` |

### Exemplul 2

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `initial, initiative, toate inima.` | `initial` |

---



# 💻 PROBLEMA 4: Decodare Text

## 📝 Descriere și Reguli

Se citește un text codificat.

* **Cuvintele:** Pot conține litere mari/mici, cifre și simboluri.
* **Separatorii:** Spațiul (` `) este singurul separator.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Regula de Decodificare | Ieșire la Consolă |
| :--- | :--- | :--- |
| **Filtrare Cuvinte** | Dacă un cuvânt **conține cel puțin o cifră**, el este eliminat. Dacă **nu conține nicio cifră**, el este păstrat și afișat. | Cuvintele păstrate, separate printr-un spațiu, în ordinea apariției lor. |

---

## 🔑 Restricții

* Operația de filtrare se aplică strict pe cuvinte individuale.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `ana are 3 mere si 5 pere` | `ana are si pere` |

### Exemplul 2

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `A1b este codat corect` | `este codat corect` |


---



# 💻 PROBLEMA 5: Cuvinte 22


## 📝 Descriere și Reguli

Se citește un text urmat de o literă.

* **Cuvintele:** Sunt formate din litere mici (`a`-`z`).
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.
* **Litera $C$:** Este o literă mică citită separat.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Filtrare după Frecvență** | Se afișează, pe rânduri separate, cuvintele din text care conțin litera $C$ de **exact două ori**. |

---

## 🔑 Restricții

* Cuvintele se afișează în ordinea apariției lor în text.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `a` <br> `ana are mere si banane` | `ana` <br> `banane` |
| `r` <br> `barometru caramida arici` | `caramida` |


---

# 💻 PROBLEMA 6: Cuvinte 1

## 📝 Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Litere mici (`a`-`z`).
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Filtrare Capete Egale** | Se afișează, pe rânduri separate, cuvintele care încep și se termină cu aceeași literă. |

---

## 🔑 Restricții

* Cuvintele se afișează în ordinea apariției lor.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `ala are mere si pere` | `ala` <br> `mere` <br> `pere` |

---


# 💻 PROBLEMA 7: Poziții

## 📝 Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Litere mici (`a`-`z`).
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Filtrare după Poziție** | Se afișează, pe rânduri separate, cuvintele care se află pe poziții impare (1, 3, 5, etc.) în text. |

---

## 🔑 Restricții

* Numărarea cuvintelor începe de la 1.
* Cuvintele se afișează în ordinea apariției lor.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `maria are mere si pere` | `maria` <br> `mere` <br> `pere` |

---


# 💻 PROBLEMA 8: Cuvinte 21

## 📝 Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Litere mici (`a`-`z`).
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.
* **Vocalele:** `a, e, i, o, u`.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Filtrare după Număr de Vocale** | Se afișează, pe rânduri separate, cuvintele din text care conțin **cel puțin două vocale**. |

---

## 🔑 Restricții

* Cuvintele se afișează în ordinea apariției lor.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `ana are mere si pere` | `ana` <br> `are` <br> `mere` <br> `pere` |


---


# 💻 PROBLEMA 9: Vocale

## 📝 Descriere și Reguli

Se citește un text compus din litere și separatori.

* **Vocalele:** `a, e, i, o, u`.
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Numărare Vocale** | Se afișează numărul total de vocale din text. |

---

## 🔑 Restricții

* Numărarea se face pe întregul text, nu doar pe cuvinte.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `mama are mere` | `6` |


---


# 💻 PROBLEMA 10: Cuvinte 2


## 📝 Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Litere mici (`a`-`z`).
* **Vocalele:** `a, e, i, o, u`.
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Filtrare Consoane Pure** | Se afișează, pe rânduri separate, cuvintele care conțin **doar consoane**. |

---

## 🔑 Restricții

* Cuvintele se afișează în ordinea apariției lor.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `frate meu a facut un test` | `frate` <br> `test` |

---

# 💻 PROBLEMA 11: Inițiale

## 📝 Descriere și Reguli

Se citește un text compus din cuvinte și separatori.

* **Cuvintele:** Litere mici (`a`-`z`).
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Afișare Inițiale** | Se afișează, pe un singur rând, inițialele fiecărui cuvânt, separate printr-un spațiu. |

---

## 🔑 Restricții

* Inițiala este prima literă a cuvântului.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `ana are mere si pere` | `a a m s p` |



---


# 💻 PROBLEMA 12: ProSir

## 📝 Descriere și Reguli

Se citește pe o linie un cuvânt $C$, iar pe următoarea linie, textul $T$ de prelucrat.

* **Cuvântul $C$:** Cuvântul care trebuie eliminat.
* **Cuvintele în $T$:** Litere mici (`a`-`z`).
* **Separatorii:** Spațiul (` `) și setul: `.,!?:;-`.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Filtrare Cuvânt Specific** | Se afișează textul rezultat după eliminarea tuturor aparițiilor cuvântului $C$. Spațiile și separatorii trebuie să rămână corect (adică nu trebuie să existe spații sau separatori dubli). |

---

## 🔑 Restricții

* Eliminarea se face pe cuvinte, nu pe subșiruri.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `cel` <br> `cel mai bun, cel mai frumos.` | `mai bun, mai frumos.` |


---


# 💻 PROBLEMA 13: A1Z26 (Codificare)

## 📝 Descriere și Reguli

Se citește un text care conține litere mari și mici, precum și separatori.

* **Literele:** A-Z și a-z.
* **Regula:** Literele se mapează la poziția lor în alfabet (ignând majusculele/minusculele): $A/a \rightarrow 1, B/b \rightarrow 2, \dots, Z/z \rightarrow 26$.
* **Separatorii:** Spațiul (` `) și alte caractere.

---

## ✨ Cerințe Funcționale ($T$)

| Operație Cerută | Ieșire la Consolă |
| :--- | :--- |
| **Codificare Alfanumerică** | Se afișează textul codificat, unde fiecare literă este înlocuită cu numărul corespunzător poziției sale, iar numerele sunt separate printr-un spațiu. Separatorii originali sunt ignorați. |

---

## 🔑 Restricții

* Se codifică **doar** literele.
* Ieșirea va conține **doar numere**, separate prin spații.

---

## 💡 Exemple

### Exemplul 1

| Intrare (Consolă) | Ieșire (Consolă) |
| :--- | :--- |
| `Ana are mere.` | `1 14 1 1 18 5 13 5 18 5` |



---







