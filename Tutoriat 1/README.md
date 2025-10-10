# Programarea Algoritmilor – Tutorial 1


## 1. Introducere în Python
 Ce este Python?

Creat de Guido van Rossum (1991).

Limbaj interpretat, multi-paradigmă (procedural, orientat obiect, funcțional).

Popular pentru simplitate, citibilitate și suport extins de biblioteci.

Documentație oficială: docs.python.org

## Instalare

🔗 [Python.org – Download](https://www.python.org/downloads/)

💡 IDE-uri recomandate:

PyCharm

VS Code

Jupyter Notebook

## 2. Tipuri de date fundamentale
| Tip de date | Clasă internă | Exemple | Descriere |
|--------------|----------------|-----------|------------|
| `NoneType` | `NoneType` | `None` | absența unei valori |
| `int` | `int` | `5`, `0b101`, `0x1F` | numere întregi |
| `float` | `float` | `3.14`, `-2.5e3` | numere reale |
| `complex` | `complex` | `2+3j` | numere complexe |
| `bool` | `bool` | `True`, `False` | valori logice |
| `str` | `str` | `'text'`, `"abc"` | șiruri de caractere |
| `list` | `list` | `[1, 2, 3]` | secvență mutabilă |
| `tuple` | `tuple` | `(1, 2, 3)` | secvență imutabilă |
| `set` | `set` | `{1, 2, 3}` | mulțime fără duplicate |
| `dict` | `dict` | `{"a": 1, "b": 2}` | perechi cheie: valoare |

## 3. Variabile și conversii

Python nu cere declararea tipului – tipul este determinat dinamic.

Poți folosi funcțiile type() și id() pentru a inspecta o variabilă.

a = 10
b = "10"
print(type(a), type(b))  # <class 'int'> <class 'str'>
print(int(b) + 5)        # conversie string -> int


Regulă: un nume de variabilă trebuie să înceapă cu literă sau _, fără spații sau simboluri.

## 4. Afișare și citire
### Afișare
print("Salut", "Python", sep=" | ", end="!!!\n")

### f-strings (format modern)
nume = "Ana"
varsta = 20
print(f"{nume} are {varsta} ani.")

### Citire
n = int(input("Introdu un număr: "))
print(f"Pătratul lui {n} este {n**2}")

## 5. Operatorii principali
### -Aritmetici

+ - * / // % **

a, b = 7, 2
print(a / b, a // b, a % b, a ** b)

### -Relaționali

< <= > >= == != is in

print(3 in [1, 2, 3])     # True
print("a" is "a")         # True (aceeași referință)

### -Logici

not, and, or

x = 0
print(not x)  # True (0 e considerat False)

### -Pe biți

~, &, |, ^, <<, >>

print(5 & 3, 5 | 3, 5 ^ 3)

## 6. Instrucțiuni de control
### -Atribuire
x = 5
x += 3
a, b = 1, 2
a, b = b, a  # interschimbare

### -Condiționale (if, elif, else)
x = int(input("x = "))
if x < 0:
    print("Negativ")
elif x == 0:
    print("Zero")
else:
    print("Pozitiv")


🔸 Operator ternar:

paritate = "Par" if x % 2 == 0 else "Impar"

### -Repetiții (while, for)

### -Buclă while

n = 123
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Suma cifrelor =", s)


### -Buclă for

for i in range(5):
    print(i, end=" ")


### -Range personalizat

for i in range(2, 10, 2):  # start=2, stop=10, pas=2
    print(i)

## Alte instrucțiuni utile

continue → sare peste iterația curentă
break → oprește complet bucla
else → se execută doar dacă bucla s-a terminat natural
pass → “placeholder” fără acțiune

for i in range(10):
    if i == 3:
        continue
    if i == 8:
        break
    print(i)
else:
    print("Bucla s-a terminat normal.")

## 7. Funcții și expresii utile pentru începători
| Funcție | Descriere | Exemplu |
|----------|------------|----------|
| `len()` | lungimea unei secvențe | `len("abc") → 3` |
| `sum()` | suma elementelor numerice | `sum([1, 2, 3]) → 6` |
| `max()`, `min()` | maxim / minim | `max(4, 2, 7)` |
| `abs()` | valoare absolută | `abs(-5)` |
| `round()` | rotunjire | `round(3.14159, 2)` |
| `sorted()` | sortare | `sorted([3, 1, 2]) → [1, 2, 3]` |
| `type()`, `isinstance()` | verificare tip | `isinstance(3, int)` |


## 8. Probleme 

1️⃣ Paritate
```python
n = int(input("n = "))
print("Par" if n % 2 == 0 else "Impar")
```


2️⃣ Maximul dintre 3 numere
```python
a, b, c = map(int, input("a b c = ").split())
print("Maximul este", max(a, b, c))
```


3️⃣ Factorial
```python
n = int(input("n = "))
f = 1
for i in range(1, n + 1):
    f *= i
print(f"{n}! = {f}")
```


4️⃣ Număr prim
```python
n = int(input("n = "))
for d in range(2, n // 2 + 1):
    if n % d == 0:
        print("Nu e prim")
        break
else:
    print("Este prim")
```


5️⃣ Suma numerelor pozitive până la 0
```python
s = 0
while True:
    x = int(input("x = "))
    if x == 0:
        break
    s += x
print("Suma =", s)
```
