# 1
#subiectul 3 colocviu 01

#a)
with open("input.txt") as f:
    m,n=f.readline().split(maxsplit=1)
    d={}
    for _ in range(int(m)):
        aux=f.readline().split(maxsplit=1)
        id_autor=int(aux[0])
        nume_autor=aux[1].rstrip("\n")

        d[id_autor]=[nume_autor,{}]

    for _ in range(int(n)):
        aux=f.readline().split(maxsplit=4)
        id_autor=int(aux[0])
        cod_carte=int(aux[1])
        an=int(aux[2])
        nr_pag=int(aux[3])
        nume_carte=aux[4].rstrip("\n")

        info_carte=an,nr_pag,nume_carte

        d[id_autor][1][cod_carte]=info_carte

print(d,sep="\n\n")

#b)

def sterge_carte(d,cod):
    for autor in d:
        if cod in d[autor][1]:
            del d[autor][1][cod]
            return d[autor][0]
        else:
            return None

cod=int(input("cod= "))

autor=sterge_carte(d,cod)
if autor!=None:
    print(f"Cartea este scr")

#c)

def carti_autor(d, id_autor):
    if id_autor not in d:
        return None
    else:
        autor=d[id_autor][0]
        carti=sorted([carte for carte in d[id_autor][1].values()], key=lambda x: (x[0], -x[1], x[2]))

    return autor, carti

id_autor =int(input("id_autor=  "))

date=carti_autor(d, id_autor)

if date==None:
    print("cod incorect")
else:
    print(date[0])
    for carte in date[1]:
        print(f"{carte[2]} { carte[0]} {carte[1]}")







# 2
with open("autori.in") as f:
    autori={}
    def sterge_carte(d,cod_carte):
        for autor,carte in d.items():
            if cod_carte in carte:
                del d[autor][cod_carte]
                return f"Cartea a fost scrisa de {autori[autor][0]} {autori[autor][1]}"
        return "Cartea nu exista"
    def carti_autor(d,cod_autor):
        L=[]
        L.append(autori[cod_autor][0]+' '+autori[cod_autor][1])
        for _,informatii in d[cod_autor].items():
            L.append((informatii[2],informatii[0],informatii[1]))
        return L
    d={}
    m,n=[int(aux) for aux in f.readline().split()]
    for _ in range(m):
        cod_autor,nume,prenume=[aux for aux in f.readline().strip().split()]
        d[cod_autor]={}
        autori[cod_autor]=[nume,prenume]
    for _ in range(n):
        cod_autor,cod_carte,an_aparitie,nr_pagini,titlu=[aux for aux in f.readline().strip().split(maxsplit=4)]
        d[cod_autor][cod_carte]=[an_aparitie,nr_pagini,titlu]
    # print(d)
    # fct=sterge_carte(d,"111")
    # if fct != "Cartea nu exista":
    #     print(fct)
    #     print(d)
    L=carti_autor(d,"11")
    for linie in L:
        print(linie)





# 3
# a) Citire
f = open("catalog.in")
linii = f.readlines()
f.close()

d = {}
n = int(linii[0].strip())
idx = 1

for i in range(n):
    rand = linii[idx].strip().rsplit(' ', 1)
    nume = rand[0]
    nr_materii = int(rand[1])
    idx += 1

    d[nume] = {}

    for j in range(nr_materii):
        parti = linii[idx].strip().split(',')
        materie = parti[0]
        note = [int(x) for x in parti[1:]]
        d[nume][materie] = note
        idx += 1


# print(d)

# b) Detalii elev
def detalii_elev(d, nume):
    if nume not in d:
        return []

    sol = []
    materii_elev = d[nume]

    for materie in materii_elev:
        note = materii_elev[materie]

        if 0 in note:
            medie = 0
        else:
            s = sum(note)
            m = s / len(note)
            if m < 5:
                medie = 0
            else:
                medie = m

        sol.append((materie, medie))

    # Sortare lexicografica dupa materie
    sol.sort(key=lambda t: t[0])
    return sol


# Testare b
nume_citit = "Ana Maria Pop"  
rez = detalii_elev(d, nume_citit)
print(rez)


# c) Clasament
def clasament(d, *nume_elevi):
    sol = []
    for nume in nume_elevi:
        if nume in d:
            situatie = detalii_elev(d, nume)
            suma_medii = 0
            corigent = 0

            for materie, medie in situatie:
                if medie == 0:
                    corigent = 1
                suma_medii += medie

            if corigent == 1:
                media_gen = 0
            else:
                media_gen = suma_medii / len(situatie)

            sol.append((nume, media_gen))

    # Sortare descrescatoare dupa medie
    sol.sort(key=lambda t: t[1], reverse=True)
    return sol


# Testare c
print(clasament(d, "Ana Maria Pop", "Mihai Popescu"))





#4
#a)
f=open("cinema.txt")
d={}
for linie in f:
    numecinema,film,ore=linie.strip().split(' % ')
    ore=[x for x in ore.split()]
    if numecinema not in d:
        d[numecinema]={}
        d[numecinema][film]=ore
    else:
        d[numecinema][film]=ore
print(d)
f.close()

#b)
def sterge_ore(d,cinema,film,ore):
    for ora in ore:
        if ora in d[cinema][film]:
            d[cinema][film].remove(ora)
    return d[cinema]

#c=input("cinema=")
#f=input("film=")
#o=input("ore=")
print(sterge_ore(d,'Cinema 1', 'Minionii 2',{'12:30','12:00'}))
print(d)

#c
def cinema_film (d,*numecinema,ora_minima,ora_maxima):
    sol=[]
    for cinema in numecinema:
        for film in d[cinema]:
            ok=1
            for o in d[cinema][film]:
                if ora_minima>o or ora_maxima<o:
                    ok=0
            if ok==1:
                tuplu=(film,cinema,d[cinema][film])
                sol.append(tuplu)
    sol.sort(key=lambda t:(t[0],-len(t[2])))
    return sol

print(cinema_film (d,'Cinema 1','Cinema 2',ora_minima="14:00",ora_maxima="22:00"))




