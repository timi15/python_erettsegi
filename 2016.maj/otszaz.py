def feladat(szam):
    print(f"\n{szam}. feladat")

vasarlasok=[]
kosar={}

with open("penztar.txt", "r", encoding="UTF-8")as fajl:
    for sor in fajl:
        if sor.strip()=="F":
            vasarlasok.append(kosar)
            kosar={}

        else:
            if sor.strip() not in kosar:
                kosar[sor.strip()]=1

            else:
                kosar[sor.strip()]+=1

print(f"{vasarlasok=}")


feladat(2)
print(f"A fizetések száma: {len(vasarlasok)} ")

feladat(3)
for kor in vasarlasok:
    print(f"Az első vásárló {len(kor)} darab árucikket vásárolt")
    break

feladat(4)


vasarlas_szama=int(input("Adja meg egy vásárlás sorszámát! "))
arucikk=input("Adja meg egy árucikk nevét! ")
vasarolt_darabszam=int(input("Adja meg a vásárolt darabszámot! "))


feladat(5)
elso=0
utolso=0
megvan=True
db=0

for index, kosar in enumerate(vasarlasok):
    for aru in kosar:
        if aru== arucikk:
            db+=1

        if arucikk == aru and megvan:
            elso=index+1
            megvan=False

        if aru ==aru:
            utolso=index-1

print(f"Az első vásárlás sorszáma: {elso}")
print(f"Az utolsó vásárlás sorszáma: {utolso}")
print(f"{db} vásárlás során vettek belőle.")


feladat(6)

def ertek(darabszam):
    if darabszam==1:
        return 500
    if darabszam==2:
        return 500+450
    if darabszam>=3:
        return 500+450+400*(darabszam-2)

print(f"{vasarolt_darabszam} darab vételekor fizetendő: {ertek(vasarolt_darabszam)}")

for index, kosar in enumerate(vasarlasok):
    if index+1==vasarlas_szama:
        print(kosar)

feladat(8)
with open("osszeg.txt", "w", )as ki:
    for index, kosar in enumerate(vasarlasok):
        fizetendo = 0
        for aru in kosar:
            fizetendo += ertek(kosar[aru])
        print(f"{index+1} {fizetendo} ", file=ki)

