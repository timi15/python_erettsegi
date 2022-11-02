def feladat(szam):
    print(f"{szam}. feladat")


tanulok=[]
adatok=[]
with open("tancrend.txt", "r", encoding="UTF-8") as fajl:
    for sor in fajl:
        adatok.append(sor.strip())

        if len(adatok)==3:
            paros={
                "tanc":adatok[0],
                "lany": adatok[1],
                "fiu":adatok[2]
            }

            tanulok.append(paros)
            paros={}
            adatok=[]

#print(f"{tanulok=}")

feladat(2)

elso=""
utolso=""

for paros in tanulok:
    elso= paros["tanc"]
    break

for paros in tanulok:
    utolso= paros["tanc"]


print(f"Az elsőként bemutatott tánc a {elso}.")
print(f"Az utlóként bemutatott tánc a {utolso}.")


feladat(3)
samba=0
for paros in tanulok:
    if paros["tanc"]=="samba":
        samba+=1

print(f"A szambát bemutató párok száma {samba}")


feladat(4)

for paros in tanulok:
    if paros["lany"]=="Vilma":
        print(paros["tanc"])


feladat(5)

beker=input("Adjon meg egy tánc típus ")
tancolt=False


for paros in tanulok:
    if paros["lany"]=="Vilma" and paros["tanc"]==beker:
        tancolt=True
        print(f"A {beker} bemutatóján Vilma párja {paros['fiu']} volt.")

if not tancolt:
    print(f"Vilma nem táncolt {beker}-t.")


feladat(6)
fiuk=set()
lanyok=set()

for paros in tanulok:
    fiuk.add(paros["fiu"])
    lanyok.add(paros["lany"])

with open("szereplok.txt", "w", encoding="UTF-8")as ki:
    print("Lányok: ",end="", file=ki)
    for lany in lanyok:
        print(lany, end=", ",  file=ki)

    print(f"\nFiúk: ",end="", file=ki)
    for fiu in fiuk:
        print(fiu, end=", ", file=ki)

feladat(7)

fiuk = {}
lanyok = {}

for paros in tanulok:
    if paros['fiu'] not in fiuk:
        fiuk[paros['fiu']] = 1
    else:
        fiuk[paros['fiu']] += 1


    if paros['lany'] not in lanyok:
        lanyok[paros['lany']] = 1
    else:
        lanyok[paros['lany']] += 1


#print(f"{lanyok=}")
#print(f"{fiuk=}")

legtobbL=0
legtobbLneve=""

for lany in lanyok:
    if lanyok[lany] >legtobbL:
        legtobbL=lanyok[lany]
        legtobbLneve=lany

legtobbF=0
legtobbFneve=""

for fiu in fiuk:
    if fiuk[fiu]>legtobbF:
        legtobbF=fiuk[fiu]
        legtobbFneve=fiu

print(f"A legtöbbször szerepelt fiú neve {legtobbFneve}")
print(f"A legtöbbször szerepelt lány neve {legtobbLneve}")





