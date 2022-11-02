def hetnapja(ev, honap, nap):
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if honap < 3:
        ev -= 1
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev //
                      400 + honapok[honap - 1] + nap) % 7]
    return hetnapja


lista=[]
szotar={}

adatok=[]
with open("lista.txt", "r", encoding="UTF-8") as fajl:
    for sor in fajl:
        adatok.append(sor.strip())
        if len(adatok)==5:
            szotar["datum"]= adatok[0]
            szotar["cim"]= adatok[1]
            szotar["evadResz"]= adatok[2]
            szotar["hossz"]= int(adatok[3])
            szotar["latta1nem0"]= adatok[4]

            lista.append(szotar)
            szotar={}
            adatok=[]

print(lista)

print("2. feladat")
darab=0
for szotar in lista:
    if szotar["datum"]!="NI":
        darab+=1

print(f"A listában {darab} db vetítési dátummal rendelkező epizód van. ")

print("2. feladat")
latta=0
for szotar in lista:
    if szotar["latta1nem0"] == "1":
        latta+=1
arany= latta/len(lista)*100

print(f"A listában lévő epizódok {round(arany,2)}%-át látta. ")

print("3. feladat")

osszes=0
for szotar in lista:
    if szotar["latta1nem0"] =="1":
        osszes+=szotar["hossz"]

nap = osszes // (24 * 60)
ora = osszes % (24 * 60) // 60
perc = osszes % 60

print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött. ")

print("5. feladat")
beker= input("Adjon meg egy dátumot! Dátum= ")
for szotar in lista:
    if szotar["datum"]<= beker and szotar["latta1nem0"]=="0":
        print(szotar["evadResz"], "\t", szotar["cim"])


print("7. feladat")

vizsgalt_nap = input('Adja meg a hét egy napját (például cs)! Nap=')
filmek = set()
for szotar in lista:
    if 'NI' not in szotar['datum']:
        epizod_datuma = szotar['datum'].split('.')
        epizod_napja = hetnapja(int(epizod_datuma[0]), int(epizod_datuma[1]), int(epizod_datuma[2]))
    if vizsgalt_nap == epizod_napja:
        filmek.add(szotar["cim"])
if len(filmek):
    for elem in filmek:
        print(elem)
else:
    print('Az adott napon nem kerül adásba sorozat.')




