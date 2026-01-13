# SUBIECTUL 3 - PROGRAMARE DINAMICA

def solve_dp():
    """
    Descriere algoritm:
    Folosim Programarea Dinamică.
    Definim vectorul dp[i] = câștigul maxim ce se poate obține pentru o bară de lungime i.
    Relația de recurență:
    dp[i] = max(dp[i - lungime_k] + pret_k) pentru toate bucățile k, unde lungime_k <= i.
    
    Pentru reconstituirea soluției, folosim un vector 'tata' (sau 'last_cut') unde memorăm 
    ce lungime am tăiat ultima oară pentru a ajunge la optimul dp[i].
    
    Complexitate:
    Avem un vector de lungime L. Pentru fiecare poziție iterăm prin k tipuri de tăieturi.
    Complexitate Timp: O(k * L) - conform cerinței.
    Complexitate Spațiu: O(L).
    """
    
    # Citire date
    try:
        # Exemplu input: "95 4" apoi "2 4 5 6" apoi "1 144 6 5"
        line1 = input("L k = ").split()
        if not line1: raise ValueError
        L, k = int(line1[0]), int(line1[1])
        
        lungimi = list(map(int, input("Lungimi: ").split()))
        preturi = list(map(int, input("Preturi: ").split()))
    except:
        # Date din exemplul PDF
        L = 47
        k = 4 # Numarul de bucati din exemplu pare sa fie 4 (lungimile 2,4,5,6 cu preturile 1,144,6,5)
              # Dar in explicatia exemplului PDF apare bucata de lungime 1 cu pret 5, si bucati de 4 cu pret 21.
              # Datele din tabelul PDF sunt contradictorii vizual, voi folosi datele din explicatia scrisa a exemplului:
              # "vinde o bucata de lungime 1 (pret 5) si doua bucati de lungime 4 (pret 21)... castig 47"
              # Pentru a respecta input-ul standard, voi implementa algoritmul general.
              # Aici folosim datele care sa dea exemplul din explicatie:
        # Reconstituim inputul logic din explicatie: L=9, lungimi=[1, 4], preturi=[5, 21] -> 2*21 + 5 = 47.
        # DAR, sa folosim exact ce e in tabelul "Date de intrare" (chiar daca e formatat ciudat):
        L = 9
        k = 4
        lungimi = [1, 2, 3, 4] # Ipoteza
        preturi = [5, 1, 1, 21] # Ipoteza pentru a da 47
        print("Atentie: Se folosesc date hardcodate pentru demo. Introduceti date manual pentru test real.")

    # Initializare
    # dp[i] = profit maxim pentru lungimea i
    dp = [-1] * (L + 1)
    dp[0] = 0
    
    # last_cut[i] = lungimea ultimei bucati adaugate pentru a obtine dp[i]
    last_cut = [0] * (L + 1)
    
    # Calcul DP
    for i in range(1, L + 1):
        for j in range(k):
            l_curent = lungimi[j]
            p_curent = preturi[j]
            
            if i >= l_curent:
                if dp[i - l_curent] != -1:
                    noul_pret = dp[i - l_curent] + p_curent
                    if noul_pret > dp[i]:
                        dp[i] = noul_pret
                        last_cut[i] = l_curent

    # Afisare castig maxim
    print(dp[L])
    
    # Reconstituire solutie
    solutie = []
    curr = L
    while curr > 0 and last_cut[curr] > 0:
        lungime_taietura = last_cut[curr]
        solutie.append(lungime_taietura)
        curr -= lungime_taietura
        
    # Cerinta: Lungimile afisate in ordine crescatoare
    solutie.sort()
    
    # Afisare lungimi (pe linii separate sau cu spatiu, tabelul e vag, punem pe linii)
    for s in solutie:
        print(s)

if __name__ == "__main__":
    solve_dp()
