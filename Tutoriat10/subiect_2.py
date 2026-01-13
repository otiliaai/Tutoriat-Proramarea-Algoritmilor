# SUBIECTUL 2 - GREEDY

def solve_greedy():
    """
    Descriere algoritm:
    Folosim metoda Greedy. Sortăm mașinile crescător după necesarul de benzină și 
    canistrele crescător după capacitate.
    Parcurgem mașinile și pentru fiecare încercăm să găsim cea mai mică canistră disponibilă
    care satisface nevoia (capacitate >= necesar).
    
    Complexitate:
    - Sortare mașini: O(N log N)
    - Sortare canistre: O(M log M)
    - Parcurgere liniară (merge-like): O(N + M)
    Complexitate totală: O(N log N) (presupunând N și M comparabile), care se încadrează în cerință.
    """
    
    # Citire date (simulare citire tastatura conform cerintei, aici hardcodat pt exemplu)
    # In examen folositi input()
    # Exemplu input:
    # n = 8
    # M = [20, 15, 10, 82, 30, 58, 70, 15]
    # m = 6
    # C = [10, 5, 40, 17, 90, 25]
    
    print("Introduceti datele (sau lasati implicit exemplul din cod):")
    try:
        line1 = input("n = ")
        n = int(line1)
        # Citim M unul cate unul sau pe linie, subiectul zice "citeste n, M1...Mn"
        # Presupunem citire linie cu linie pentru simplitate in Python
        M = []
        print(f"Introduceti {n} valori pentru necesarul masinilor:")
        for _ in range(n):
            M.append(int(input()))
            
        line_m = input("m = ")
        m = int(line_m)
        print(f"Introduceti {m} valori pentru canistre (separate prin spatiu daca e cazul sau enter):")
        # Exemplul arata canistre pe o linie sau mai multe. Sa zicem una cate una.
        C = []
        for _ in range(m):
            C.append(int(input())) 
    except:
        # Datele din exemplul PDF hardcodate pentru testare rapida daca nu se introduce nimic
        n = 8
        M = [20, 15, 10, 82, 30, 58, 70, 15]
        m = 6
        C = [10, 5, 40, 17, 90, 25]

    # Pastram indicii originali pentru afisare (M1, M2... C1, C2...)
    masini = []
    for i in range(n):
        masini.append({'id': i+1, 'nevoie': M[i]})
        
    canistre = []
    for i in range(m):
        canistre.append({'id': i+1, 'cap': C[i]})
        
    # Pas 1: Sortare (Esența Greedy)
    # Sortam masinile dupa nevoie crescator
    masini.sort(key=lambda x: x['nevoie'])
    # Sortam canistrele dupa capacitate crescator
    canistre.sort(key=lambda x: x['cap'])
    
    rezultat = [] # Va stoca perechi (id_masina, id_canistra)
    masini_rezolvate = 0
    
    index_canistra = 0
    
    # Pas 2: Iterare si selectie
    for masina in masini:
        # Cautam prima canistra care poate satisface masina curenta
        while index_canistra < m and canistre[index_canistra]['cap'] < masina['nevoie']:
            index_canistra += 1
            
        if index_canistra < m:
            # Am gasit o canistra potrivita
            c = canistre[index_canistra]
            rezultat.append((masina['id'], c['id']))
            masini_rezolvate += 1
            # Trecem la urmatoarea canistra (o canistra se foloseste o singura data)
            index_canistra += 1
        else:
            # Nu mai avem canistre suficient de mari pentru restul masinilor (care sunt si mai mari)
            # Putem marca restul ca nerezolvate
            pass

    # Pas 3: Afisare
    print(masini_rezolvate)
    
    # Trebuie sa afisam pentru TOATE masinile, in ordinea originala M1, M2...
    # Dictionar rapid pentru lookup
    alocari = {id_m: id_c for id_m, id_c in rezultat}
    
    for i in range(1, n + 1):
        if i in alocari:
            print(f"M{i}->C{alocari[i]}")
        else:
            print(f"M{i}-> niciuna")

if __name__ == "__main__":
    solve_greedy()
