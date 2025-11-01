# Probleme: List Comprehensions

**List comprehensions** în Python oferă o modalitate concisă și eficientă de a crea liste noi.

---

## Problema 1: Pătratele numerelor

Creează o listă nouă care să conțină pătratele numerelor întregi de la a la b.

**Soluție:**

### Input:
```python
3 5
```

### Output:
```python
[9,16,25]
```

## Problema 2: Numere pare

Folosind o listă dată, creează o listă nouă care să conțină doar numerele pare.

### Input:
```python
[1,3,54,65,789,3,4,6]
```

### Output:
```python
[54,4,6]
```

## Problema 3: Cuvinte cu o anumită lungime

Dintr-o propoziție, extrage doar cuvintele care au mai puțin de n litere.
Pe prima linie se va citi propoziția, iar pe linia următoare n. Să se întoarcă lista cuvintelor care respectă cerința și **-1** dacă nu există nici un cuvânt.

### Input:
```python
Îmi place să fiu un programator
3
```

### Output: 
```python
["să","un"]
```

## Problema 4: Conversie litere mari

Convertește toate cuvintele dintr-o listă în majuscule.

### Input:
```python
["mere", "banane", "cirese"]
```

### Output: 
```python
['MERE', 'BANANE', 'CIRESE']
```

## Problema 5: Elevi eminenți

Un fișier text numit `note.txt` care conține pe fiecare linie numele unui student și nota sa (separate prin spațiu). Folosind list comprehension, citește fișierul și creează o listă care să conțină numele studenților care au obținut o notă mai mare sau egală cu 9.

### Input:
`note.txt`
```python
Ion 7
Maria 9
Petru 6
Elena 10
George 8
Ana 9
```

### Output: 
```python
["Maria", "Elena", "Ana"]
```

## Problema 6: Extragere cifre

Se citește o propoziție și se cere formarea unei liste care conține toate cifrele din acea propoziție.

### Input:

```python
Am 2 mere si 5 banane, costa 12 lei.
```

### Output:
```python
[2,5,1,2]
```


## Problema 7

Ai o listă de numere. Creează o listă nouă care să conțină doar rădăcinile pătrate ale numerelor care sunt divizibile cu 4.

### Input:
```python
[4,17,64,99]
```

### Output:
```python
[2.0,8.0]
```

## Problema 8: Orașele

Se dă o listă de orașe. Vrei să creezi o listă nouă care să conțină doar orașele care se află la un index par (0, 2, 4, etc.) în lista originală *și* care au o lungime a numelui mai mare de 5 caractere.

### Input:
```python
orase = ["Bucuresti", "Brasov", "Cluj", "Timisoara", "Sibiu", "Constanta"]
```
### Output: 
```python
['Bucuresti', 'Timisoara', 'Constanta']
```
