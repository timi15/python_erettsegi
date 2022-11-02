import random


def feladatszam(szam):
    print(f"{szam}. feladat")

feladatok=[]
szamlalo=1
adatok=[]
with open("felszam.txt", "r")as fajl:
    for sor in fajl:
        adatok.append(sor.strip())

        if len(adatok)==2:

            valasz= adatok[1].strip().split()
            feladat={
                "kerdes":adatok[0],
                "valasz":int(valasz[0]),
                "pont":int(valasz[1]),
                "temakor":valasz[2],
                "hely":szamlalo
            }

            feladatok.append(feladat)
            feladat={}
            adatok=[]
            szamlalo += 1

print(f"{feladatok=}")

feladatszam(2)

print(f"{len(feladatok)} db feladat van a fájlban")




feladatszam(3)

matek=0
egy=0
ketto=0
harom=0

for feladat in feladatok:
    if feladat["temakor"] =="matematika":
        matek+=1
        if feladat["pont"]==1:
            egy+=1

        elif feladat["pont"]==2:
            ketto+=1

        else:
            harom+=1

print(f"Az adatfajlban {matek} matematika feladat van, 1 pontot er {egy} feladat, 2 pontot er {ketto} feladat, 3 pontot er {harom} feladat. ")


feladatszam(4)

legkisebb=feladat['valasz']
legnagyobb=feladat['valasz']


for feladat in feladatok:
    if feladat["valasz"]>legnagyobb:
        legnagyobb=feladat["valasz"]

    if feladat["valasz"]<legkisebb:
        legkisebb=feladat["valasz"]


print(f"A válaszok számértéke {legkisebb}-től, {legnagyobb}-ig terjed")


feladatszam(5)

temakorok=set()

for feladat in feladatok:
    temakorok.add(feladat["temakor"])

print(temakorok)

feladatszam(6)

beker_temakor=input("Milyen temakorbol szeretne kerdest kapni?")




sorszam = random.randint(1, len(feladatok))

while beker_temakor != feladatok[sorszam]["temakor"]:
    sorszam = random.randint(1, len(feladatok))


kerdes=feladatok[sorszam]["kerdes"]

beker_valasz= int(input(kerdes))

if beker_valasz==feladatok[sorszam]["valasz"]:
    print(f"A valasz {feladatok[sorszam]['pont']} pontot er.")

else:
    print("A valasz 0 pontot er. ")
    print(f"A helyes valasz: {feladatok[sorszam]['valasz']}")


feladatszam(7)

with open("tesztfel.txt", "w", encoding="UTF-8")as ki:

    feladatsor=set()

    while len(feladatsor)!=10:
        feladatsor.add(random.randint(1, len(feladatok)))


    feladatsor2=list(feladatsor.copy())

    print(feladatsor2)

    ossz_pont=0
    for index, feladat in enumerate(feladatok):
        for i in range(0, 9):
            if feladat["hely"] == feladatsor2[i]:
                ossz_pont += feladat['pont']
                print(f"{feladat['pont']} {feladat['valasz']} {feladat['kerdes']}", file=ki)

    print(f"A feladatsorra osszesen {ossz_pont} pont adhato. ", file=ki)



















