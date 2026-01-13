# SUBIECTUL 1

# a) Functia consoane_comune
def consoane_comune(*args):
    """
    Primeste un numar variabil de cuvinte si returneaza numarul maxim de cuvinte
    care au exact aceeasi multime de consoane.
    """
    def get_consoane(cuvant):
        vocale = "aeiouAEIOU"
        # Set comprehension pentru a obtine consoanele unice
        consoane = {c for c in cuvant if c.isalpha() and c not in vocale}
        # Returnam un tuple sortat pentru a putea fi folosit ca cheie in dictionar
        return tuple(sorted(list(consoane)))

    frecventa = {}
    
    for cuv in args:
        cheie = get_consoane(cuv)
        if cheie in frecventa:
            frecventa[cheie] += 1
        else:
            frecventa[cheie] = 1
            
    # Returnam maximul din valori. Daca lista e goala, returnam 0.
    if not frecventa:
        return 0
    return max(frecventa.values())

# b) List comprehension prefix_5
prefix_5 = [x for x in lista_numere if x % 5 != 0 and all(int(str(x)[:i]) % 5 != 0 for i in range(1, len(str(x))))]

# c) Complexitatea functiei recursive f(s)
"""
RASPUNS PENTRU C:
Analiza complexității:
Funcția f(s) împarte problema în subprobleme de dimensiune n/2 (unde n este lungimea șirului).
În fiecare apel recursiv, se fac următoarele operații:
1. Calculul mijlocului și verificări (timp constant O(1)).
2. Slicing (felierea șirului): s[:m+1] sau s[m+1:]. În Python, copierea unei felii de șir de lungime k costă O(k). Aici costă O(n).
3. Un singur apel recursiv pe jumătate din șir (fie pe stânga, fie pe dreapta, în funcție de `if c in "aeiou"`).

Recurența este: T(n) = T(n/2) + O(n)
Aceasta este o serie geometrică: n + n/2 + n/4 + ... care converge la 2n.

Complexitatea maximă (Worst Case): O(n) - Liniară.
"""
