lista= []
szotar={}

adatok=[]
with open("beosztas.txt", "r", encoding="UTF-8") as fajl:
    for sor in fajl:
        adatok.append(sor.strip())
        if len(adatok)==4:
            szotar["tanar"]=adatok[0]
            szotar["tantargy"]= adatok[1]
            szotar["osztaly"]=adatok[2]
            szotar["oraszam"]= int(adatok[3])

            lista.append(szotar)
            szotar={}
            adatok=[]

print(lista)
print("2. feladat")
print(f"A fájlban {len(lista)} bejegyzés van. ")


print("3. feladat")
hetiora=0
for szotar in lista:
    hetiora+=szotar["oraszam"]

print(f"Az iskolában a heti összóraszám: {hetiora}")

print("4. feladat")
tanarHeti=0
tanar= input("Egy tanár neve= ")
for szotar in lista:
    if szotar["tanar"]==tanar:
        tanarHeti+=szotar["oraszam"]

print(f"A tanár heti óraszáma: {tanarHeti}")

print("5. feladat")
with open("of.txt", "w", encoding="UTF-8") as ki:
    for szotar in lista:
        if szotar["tantargy"]=="osztalyfonoki":
           print(szotar["osztaly"], "-", szotar["tanar"], file=ki)

print("6. feladat")

osztaly= input("Osztály= ")
tantargy= input("Tantárgy= ")
db=0
for szotar in lista:
    if osztaly==szotar["osztaly"] and tantargy==szotar["tantargy"]:
        db+=1

if db>1:
    print("Csoportbontásban tanulják. ")
else:
    print("Nem csoportbontásban tanulják")

print("7.feladat")

halmaz=set()

for szotar in lista:
    halmaz.add(szotar["tanar"])

print(f"Az iskolában {len(halmaz)} tanár tanít")
