def feladat(szam):
    print(f"{szam}. feladat")

melysegek = []
with open('melyseg.txt', 'r') as fajl:
    for index, egy_sor in enumerate(fajl):
        if index > 1:
            sor = list(map(int, egy_sor.strip().split()))
            melysegek.append(sor)

print(f"{melysegek=}")

feladat(2)
sor_beker= int(input("A mérés sorának azonosítója= "))-1
oszlop_beker=int(input("A mérés oszlopának azonosítója= "))-1

print(f"A mért mélység az adott helyen {melysegek[sor_beker][oszlop_beker]} dm")


feladat(3)

felszin=0
ossz_melyseg=0

for sor in melysegek:
    for ertek in sor:
        ossz_melyseg+=ertek
        if ertek>0:
            felszin+=1

arany=(ossz_melyseg/felszin)/10
print(f"A tó felszíne: {felszin} m2, átlagos mélysége: {round(arany, 2)} m ")

feladat(4)

legmelyebb_ertek=0

for sor in melysegek:
    for ertek in sor:
        if legmelyebb_ertek<ertek:
            legmelyebb_ertek=ertek


print(f"A tó legnagyobb mélysége: {legmelyebb_ertek} dm")

print("A legmélyebb helyek sor-oszlop koordinátái: ")

for i, sor in enumerate(melysegek):
    for j, ertek in enumerate(sor):
        if melysegek[i][j] == legmelyebb_ertek:
            print(f"({i+1}; {j+1})", end="\t")

print()
feladat(5)

hossz=0

for i, sor in enumerate(melysegek):
    for j, ertek in enumerate(sor):
        if ertek > 0:
            if sor[j-1] == 0:
                hossz += 1

            if sor[j+1] == 0:
                hossz += 1

            if melysegek[i - 1][j] == 0:
                hossz += 1

            if melysegek[i + 1][j] == 0:
                hossz += 1

print(f'A tó partvonala {hossz} m hosszú')

feladat(6)
beker=int(input("A vizsgált szelvény oszlopának azonosítója= "))

with open("diagram.txt", "w")as ki:
    for i, sor in enumerate(melysegek):
        print(f"{i + 1:02d}", '*' * round(sor[beker - 1] / 10), file=ki)






