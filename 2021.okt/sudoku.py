def feladatok(szam):
    print(f"{szam}. feladat")

bemenet= input("Adja meg a bemeneti fájl nevét!")
sor= int(input("Adja meg egy sor számát!")) -1
oszlop= int(input("Adja meg egy oszlop számát!")) -1


tablazat=[]
lepesek=[]
with open(bemenet, "r", encoding="UTF-8") as fajl:
    for adatsor in fajl:
        adatsor= adatsor.strip().split()
        ertekek=[]

        for adat in adatsor:
            ertekek.append(int(adat))

        if len(ertekek)==9:
            tablazat.append(ertekek)

        else:
            lepesek.append(ertekek)

print(tablazat)
print(lepesek)

feladatok(3)
if tablazat[sor][oszlop]==0:
    print("Az adott helyet még nem töltötték ki.")
else:
    print(f"Az adott helyen szereplő szám: {tablazat[sor][oszlop]}")
    print(f'A hely a(z) {3 * (sor // 3) + (oszlop // 3) + 1} résztáblához tartozik.')

feladatok(4)

nullakSzama=0
for s in tablazat:
    for ertekek in s:
        if ertekek==0:
            nullakSzama+=1

arany= (nullakSzama/81)*100
print(f"Az üres helyek aránya:{round(arany,2)}%")

feladatok(5)

for lepes in lepesek:
    szerepel = False
    szam = lepes[0]
    sor = lepes[1] - 1
    oszlop = lepes[2] - 1
    print(f'A kiválasztott sor: {lepes[1]} oszlop: {lepes[2]} a szám: {lepes[0]}')

    if tablazat[sor][oszlop]:
        print('A helyet már kitöltötték.')
    else:
        if szam in tablazat[sor]:
            print('Az adott sorban már szerepel a szám.')
        else:
            for s in tablazat:
                if s[oszlop]==szam:
                    szerepel=True
                    break

            if szerepel:
                print('Az adott oszlopban már szerepel a szám.')
            else:
                for s in range(3 * (sor // 3), 3 * (sor // 3) + 3):
                    for o in range(3 * (oszlop // 3), 3 * (oszlop // 3) + 3):
                        if tablazat[s][o] == szam:
                            szerepel = True
                if szerepel:
                    print('A résztáblázatban már szerepel a szám.')
                else:
                    print('A lépés megtehető.')














