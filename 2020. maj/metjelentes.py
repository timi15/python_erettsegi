lista =[]
szotar={}

with open("tavirathu13.txt", "r", encoding="UTF-8") as fajl:
    for sor in fajl:
        sor= sor.strip().split()
        szotar["telepules"]= sor[0]
        szotar["ido"]=sor[1]
        szotar["szelirany"]=sor[2]
        szotar["homerseklet"]=int(sor[3])

        ora = szotar["ido"][0:2]
        perc = szotar["ido"][2:4]
        szotar["ido"]= f"{ora}:{perc}"

        lista.append(szotar)
        szotar={}

print(lista)

print("2. feladat")
kod= input("Adja meg egy település kódját! Település: " )

utolsoAdat=0
for szotar in lista:
    if kod==szotar["telepules"]:
        utolsoAdat=szotar["ido"]

print(f"Az utolsó mérési adat a megadott településről {utolsoAdat}-kor érkezett. ")

print("3. feladat")

minTelepules=None
minIdo=None
minHomerseklet = lista[0]["homerseklet"]

maxTelepules=None
maxIdo=None
maxHomerseklet = lista[0]["homerseklet"]


#print(minHomerseklet, maxHomerseklet)

for szotar in lista:
    if minHomerseklet> szotar["homerseklet"]:
        minHomerseklet= szotar["homerseklet"]
        minTelepules = szotar["telepules"]
        minIdo = szotar["ido"]


    if maxHomerseklet< szotar["homerseklet"]:
        maxHomerseklet= szotar["homerseklet"]
        maxTelepules = szotar["telepules"]
        maxIdo = szotar["ido"]

print(f"A legalacsonyabb hőmérséklet: {minTelepules} {minIdo} {minHomerseklet} fok.")
print(f"A legmagasabb hőmérséklet: {maxTelepules} {maxIdo} {maxHomerseklet} fok.")

print("4. feladat")
db=0
for szotar in lista:
    if szotar["szelirany"] == "00000":
        db+=1
        print(szotar["telepules"], " ", szotar["ido"])

if db==0:
    print("Nem volt szélcsend a mérések idején.")


halmaz=set()

for szotar in lista:
    halmaz.add(szotar["telepules"])


print("5. feladat")

for i in halmaz:

    meresDb=0
    osszeg=0
    o1=False
    o7 = False
    o13 = False
    o19= False
    min = 100
    max = -100

    for szotar in lista:

        ora = szotar["ido"][0:2]
        perc = szotar["ido"][2:4]

        if szotar["telepules"]==i and ora=="01":
            meresDb+=1
            o1=True
            osszeg+=szotar["homerseklet"]

        if szotar["telepules"]==i and ora=="07":
            meresDb+=1
            o7=True
            osszeg+=szotar["homerseklet"]


        if szotar["telepules"]==i and ora=="13":
            meresDb+=1
            o13=True
            osszeg+=szotar["homerseklet"]


        if szotar["telepules"]==i and ora=="19":
            meresDb+=1
            o19=True
            osszeg+=szotar["homerseklet"]

        if szotar["telepules"] == i:
            if szotar["homerseklet"]<min:
                min=szotar["homerseklet"]


            if szotar["homerseklet"]>max:
                max=szotar["homerseklet"]

    if o1 and o7 and o13 and o19:
        atlag=round(osszeg/meresDb, 0)
        print(f"{i} Középhőmérséklete: {int(atlag)}; Hőmérséklet-ingadozás: {max-min}")

    else:
        print(f"{i} NA; Hőmérséklet-ingadozás: {max - min}")





print("6. feladat")




for i in halmaz:
    fajlnev = i
    with open(f"{fajlnev}.txt", "w", encoding="UTF-8") as ki:
        print(i, "\n", file=ki)
        for szotar in lista:
            if i ==szotar["telepules"]:
                    if szotar["telepules"] == fajlnev:
                        szelerosseg= szotar["szelirany"][3:]
                        abra=int(szelerosseg)*"#",
                        print( szotar["ido"], abra, file=ki)

print("A fájlok elkészültek. ")
























