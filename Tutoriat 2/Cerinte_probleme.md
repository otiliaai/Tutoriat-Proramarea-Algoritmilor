

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

## 🎯 Obiectiv

Implementarea unui program care identifică și listează toate cuvintele din text care sunt prefixe ale altor cuvinte din același text.

---

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

## 🎯 Obiectiv

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
