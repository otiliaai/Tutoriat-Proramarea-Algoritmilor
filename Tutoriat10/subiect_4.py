SUBIECT 4

def solve_backtracking_final():
    print("Introduceti n si p (separate prin spatiu):")
    line = input().split()
    n = int(line[0])
    p = int(line[1])

    # Folosim o lista cu un element pentru a putea modifica valoarea in recursivitate
    # fara sa folosim 'nonlocal' sau variabile globale.
    contor = [0] 

    # 3. Functia recursiva
    def back(solutie):
        # Conditia de oprire: am ajuns la lungimea n
        if len(solutie) == n:
            # Afisam solutia curenta (transformam lista in sir de caractere)
            print("".join(map(str, solutie)), end=", ")
            # Crestem numarul de solutii gasite
            contor[0] += 1
            return

        for cifra in range(1, 10):
            
            # Daca lista nu e goala si ultima cifra e egala cu cea curenta, sarim peste.
            if len(solutie) > 0 and solutie[-1] == cifra:
                continue
                
            # Daca cifra apare deja de p ori, sarim peste.
            if solutie.count(cifra) >= p:
                continue
            
            # Trimitem noua lista formata din solutia veche + cifra curenta
            back(solutie + [cifra])

    back([])
    
    print() # Doar pentru a trece la rand nou
    print(f"Numar total solutii: {contor[0]}")

if __name__ == "__main__":
    solve_backtracking_final()
