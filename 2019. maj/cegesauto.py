lista=[]
szotar={}

with open("autok.txt", "r", encoding="UTF-8") as fajl:
    for sor in fajl:
        sor= sor.strip().split()
        szotar["nap"] = int(sor[0])
        szotar["ido"] = sor[1]
        szotar["rendszam"] =sor[2]
        szotar["azonosito"] =int(sor[3])
        szotar["km"]= int(sor[4])
        szotar["ki0be1"] = int(sor[5])

        lista.append(szotar)

        szotar={}

print(lista)

print("2. feladat")
utolso=0
nap=0
for szotar in lista:
    if szotar["ki0be1"]==0:
        utolso= szotar["rendszam"]
        nap = szotar["nap"]

print(f"{nap}. nap rendszám: {utolso}")

print("3. feladat ")

beker= int(input("Nap: "))
print("Forgalom a(z) 4. napon:")

for szotar in lista:
    if szotar["nap"]==beker:
        if szotar["ki0be1"] ==0:
            print(szotar["ido"], szotar["rendszam"], szotar["azonosito"], " ki" )

        else :
            print(szotar["ido"], szotar["rendszam"], szotar["azonosito"], " be" )

print("4. feladat")

nemBent=0

for szotar in lista:
    if szotar["ki0be1"] ==0:
        nemBent+=1

    else:
        nemBent-=1

print(f"A hónap végén {nemBent} autót nem hoztak vissza.")


print("5. feladat")

for i in range(0,10):
    rendsz2= "CEG30"
    rendsz2=rendsz2+str(i)
    elso=-1
    utolso=0
    for szotar in lista:
        if szotar["rendszam"] ==rendsz2:
            if elso ==-1:
                elso = szotar["km"]
            else:
                utolso = szotar["km"]

    print(f"{rendsz2} {utolso-elso} km")

print("6. feladat")

maxKm=0
maxNev=""


for index, szotar in enumerate(lista):
    if szotar["ki0be1"]==0:
        aktKm= szotar["km"]
        aktAz= szotar["azonosito"]
       # print(aktAz, aktKm)
        aktIndex= index
        print(aktIndex)
        for j in range(0, len(szotar)):
            print(j)
            if aktIndex<j:
                if szotar["azonosito"][j] == aktAz:
                    if szotar["km"][j]-aktKm > maxKm:
                        maxKm= szotar["km"][j]-aktKm
                        maxNev= aktAz
                        print(maxKm, " ", maxNev)
                    break
        

print(f"Leghosszabb út: {maxKm} km, személy: {aktAz}")


rendszam= input("Rendszám: ")

with open(f"{rendszam}_menetlevel.txt", "w", encoding="UTF-8") as kiir:
    for szotar in lista:
        if rendszam == szotar["rendszam"]:
            if szotar["ki0be1"] ==0:
                print(str(szotar["azonosito"]) +"\t" +str(szotar["nap"])+". " +szotar["ido"] +"\t"+ str(szotar["km"])+" km", end="\t", file=kiir)


            else:
                print(str(szotar["nap"]) + ". " + szotar["ido"] + "\t" + str(szotar["km"])+ " km", file=kiir)
