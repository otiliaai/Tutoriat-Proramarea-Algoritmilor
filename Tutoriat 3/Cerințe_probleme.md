# Probleme: List Comprehensions

**List comprehensions** în Python oferă o modalitate concisă și eficientă de a crea liste noi.

---

### Problema 1: Pătratele numerelor

**Enunț:** Creează o listă nouă care să conțină pătratele numerelor întregi de la a la b.

**Soluție:**

### Input:
```python
3 5
```

### Output:
```python
[9,16,25]
```

### Problema 2: Numere pare

**Enunț:** Folosind o listă dată, creează o listă nouă care să conțină doar numerele pare.

```python
# Input:
[1,3,54,65,789,3,4,6]
```

```python
# Output:
[54,4,6]
```

### Problema 3: Cuvinte cu o anumită lungime

**Enunț:** Dintr-o listă de cuvinte, extrage doar cuvintele care au mai puțin de 5 litere.

**Soluție:**

```python
cuvinte = ["apple", "banana", "cherry", "kiwi", "mango"]
cuvinte_scurte = [cuvant for cuvant in cuvinte if len(cuvant) < 5]
print(cuvinte_scurte)
# Output: ['kiwi']

### Problema 4: Conversie litere mari

**Enunț:** Convertește toate cuvintele dintr-o listă în majuscule.

**Soluție:**

```python
fructe = ["mere", "banane", "cirese"]
fructe_uppercase = [fruct.upper() for fruct in fructe]
print(fructe_uppercase)
# Output: ['MERE', 'BANANE', 'CIRESE']

### Problema 8: Crearea unui dicționar din două liste

**Enunț:** Folosește list comprehension (sau dictionary comprehension, care este înrudită) pentru a crea un dicționar din două liste, una conținând cheile și alta valorile corespunzătoare. Presupune că listele au aceeași lungime.

**Soluție (folosind dictionary comprehension):**

Deși este o "dictionary comprehension" și nu o "list comprehension", este o extindere logică și folosește un principiu similar.

```python
chei = ["unu", "doi", "trei"]
valori =
dictionar = {chei[i]: valori[i] for i in range(len(chei))}
print(dictionar)
# Output: {'unu': 1, 'doi': 2, 'trei': 3}

### Problema 9: Citirea datelor dintr-un fișier și filtrarea lor

**Enunț:** Ai un fișier text numit `note.txt` care conține pe fiecare linie numele unui student și nota sa (separate prin spațiu). Folosind list comprehension, citește fișierul și creează o listă care să conțină numele studenților care au obținut o notă mai mare sau egală cu 9.

**Conținutul fișierului `note.txt` (presupus):**

```text
Ion 7
Maria 9
Petru 6
Elena 10
George 8
Ana 9

text_amestecat = "Am 2 mere si 5 banane, costa 12 lei."

# Folosim metoda .isdigit() pentru a verifica dacă un caracter este o cifră
numere_extrase = [int(char) for char in text_amestecat if char.isdigit()]

print(numere_extrase)
# Output:

### Problema 11: Aplicarea unei funcții pe elementele unei liste și filtrarea simultană

**Enunț:** Ai o listă de numere. Creează o listă nouă care să conțină doar rădăcinile pătrate ale numerelor care sunt divizibile cu 4.

**Soluție:**

```python
import math

numere =
# list comprehension care aplică math.sqrt() DOAR numerelor care trec testul "if"
radacini_filtrate = [math.sqrt(x) for x in numere if x % 4 == 0]

print(radacini_filtrate)
# Output: [2.0, 3.0, 4.0, 5.0, 6.0]


### Problema 12: Generarea unui pachet de cărți de joc (Nested List Comprehension)

**Enunț:** Folosește un "nested list comprehension" pentru a genera un pachet complet de 52 de cărți de joc. Pachetul trebuie să fie o listă de șiruri de caractere (`strings`), unde fiecare element combină valoarea cărții cu simbolul suitei (ex: "2 de Inimă Roșie", "Rege de Pică").

**Soluție:**

```python
simboluri = ["Inimă Roșie", "Caro", "Pică", "Trefle"]
valori = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Damă", "Rege"]

# Iterăm prin fiecare simbol în bucla exterioară, apoi prin fiecare valoare în cea interioară
pachet_carti = [
    f"{valoare} de {simbol}" 
    for simbol in simboluri 
    for valoare in valori
]

# Afișăm primele 5 cărți pentru verificare
for carte in pachet_carti[:5]:
    print(carte)


### Problema 14: Filtrarea elementelor în funcție de poziția lor (Index)

**Enunț:** Ai o listă de orașe. Vrei să creezi o listă nouă care să conțină doar orașele care se află la un index par (0, 2, 4, etc.) în lista originală *și* care au o lungime a numelui mai mare de 5 caractere.

**Soluție:**

Pentru a accesa și indexul în timpul iterației cu list comprehension, folosim funcția încorporată `enumerate()`.

```python
orase = ["Bucuresti", "Brasov", "Cluj", "Timisoara", "Sibiu", "Constanta"]

# Folosim enumerate() pentru a obține indexul (idx) și valoarea (oras)
# Condiția principală: idx % 2 == 0 (index par)
# Condiția secundară: len(oras) > 5 (lungime nume > 5)
orase_filtrate = [
    oras 
    for idx, oras in enumerate(orase) 
    if idx % 2 == 0 and len(oras) > 5
]

print(orase_filtrate)
# Output: ['Bucuresti', 'Timisoara', 'Constanta']

### Problema 15: Transformarea unei liste de dicționare (List of Dictionaries)

**Enunț:** Ai o listă de dicționare, unde fiecare dicționar reprezintă un produs cu numele și prețul său. Vrei să creezi o singură listă care să conțină doar numele produselor care costă mai mult de 50 RON.

**Soluție:**

```python
produse = [
   ,
   ,
   ,
   ,
   
]

# Iterăm prin fiecare dicționar (produs) din lista principală
# Verificăm condiția pe cheia 'pret'
# Dacă trece, extragem și adăugăm în lista finală doar valoarea cheii 'nume'
produse_scumpe = [
    produs['nume'] 
    for produs in produse 
    if produs['pret'] > 50
]

print(produse_scumpe)
# Output: ['Laptop', 'Mouse Gaming', 'Monitor']
