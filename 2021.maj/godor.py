

godrok=[]

with open("melyseg.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        sor= sor.strip()
        godrok.append(int(sor))

print(godrok)

print("1. feladat")
print("A fájl adatainak száma:",len(godrok))

print("2. feladat")
tavolsagertek= int(input("Adjon meg egy távolságértéket! "))
print(f"Ezen a helyen a felszín {godrok[tavolsagertek]} méter mélyen van. ")

print("3. feladat")
db=0
for i in godrok:
    #print(godrok[i])
    if i==0:
        db+=1

szazalek=db/len(godrok)
szazalek=round(szazalek*100, 2)
print(f"Az érintetlen terület aránya {szazalek}%. ")



#print("4. feladat")


with open("godrok.txt", "w", encoding="utf-8") as ki:


    godor=[]
    egyGodor=[]

    for i in range(1, len(godrok)):
        if godrok[i-1] ==0 and godrok[i]!=0:
            egyGodor.append(godrok[i])

        if godrok[i-1] !=0 and godrok[i]!=0:
            egyGodor.append(godrok[i])

        if godrok[i-1]!=0 and godrok[i]==0:
            godor.append(egyGodor)
            egyGodor=[]

    for egyGodor in godor:
        print(" ".join(list(map(str, egyGodor))), file=ki)

print("5. feladat")
print(f"A gödrök száma: {len(godor)}")

print("6. feladat")

if godrok[tavolsagertek]!=0:

    akteleje=0
    aktvege=0
    monoton=True



    for i in range(0, tavolsagertek):
        if godrok[i]==0:
            akteleje=i

    akteleje+=2  # indexelés, rákövetkező adat miatt +2


    for i in range(tavolsagertek, len(godrok)):
        if godrok[i]==0:
            aktvege=i
            break

    print("a)")
    print(f"A gödör kezdete: {akteleje} méter, a gödör vége {aktvege} méter")

    resz=[]

    for i in range(akteleje-1,aktvege):
        resz.append(godrok[i])



    maxIndex = 0
    for index, value in enumerate(resz) :
        if resz[maxIndex] < value:
            maxIndex=index



    osszeg=0
    for i in resz:
        osszeg+=i

    for i in range(maxIndex, len(resz)):
        if i < i+1:
            monoton=False

    for i in range(0, maxIndex):
        if i > i+1:
            monoton=False

    print(maxIndex)
    print(akteleje)
    print(aktvege)

    print("b)")
    if monoton:
        print("Folyamatosan mélyül.")

    else:
        print("Nem mélyül folyamatosan")

    print("c)")
    print(f"A legnagyobb mélysége {resz[maxIndex]} méter.")

    print("d)")
    terfogat = osszeg * 10
    print(f"A térfogata {terfogat} m^3.")

    print("e)")

    print(f"A vízmennyiség {terfogat - (len(resz)) * 10} m^3. ")


else:
    print("Az adott helyen nincs gödör")





























