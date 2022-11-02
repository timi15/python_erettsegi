lista=[]
szotar={}

with open("fogado.txt", "r", encoding="UTF-8") as fajl:
    for sor in fajl:
        sor = sor.strip().split()
        szotar["nev"] =f"{sor[0]} {sor[1]}"
        szotar["idopont"]=sor[2]
        szotar["foglalas"]= sor[3]

        lista.append(szotar)
        szotar={}

print(lista)

print("2.feladat")
print(f"Foglalások száma: {len(lista)}")

print("3. feladat")
tanar= input("Adjon meg egy nevet: ")
db=0
for szotar in lista:
    if szotar["nev"]== tanar:
        db+=1
print(f"{tanar} néven {db} időpontfoglalás van. ")

print("4. feladat")
beker=input("Adjon meg egy érvényes időpontot (pl. 17:10): ")

nevek=[]
fajlnev=None
for szotar in lista:
    if beker== szotar["idopont"]:
        nevek.append(szotar["nev"])
        ido=szotar["idopont"].split(":")
        fajlnev= f"{ido[0]}{ido[1]}"


nevek.sort()
for i in nevek:
    print(i, end="\n")

with open(f'{fajlnev}.txt', "w", encoding="UTF-8") as ki:
    for i in nevek:
        print(i,end="\n", file=ki)

print("5. feladat")

legkorabbTanar=None
legkorabbIdo=""
legkorabbFoglalas=None

for szotar in lista:
    if szotar["idopont"]> legkorabbIdo:
        legkorabbIdo = szotar["idopont"]
        legkorabbTanar= szotar["nev"]
        legkorabbFoglalas= szotar["foglalas"]

        break

print(f"Tanár neve: {legkorabbTanar}")
print(f"Foglalt időpont: : {legkorabbIdo}")
print(f"Foglalás ideje: {legkorabbFoglalas}")

print("6. feladat")



for i in range(0,6):
    szabad = True
    idoStr="16:00"
    if i>0:
        idoStr = "16:" + str(i * 10)

    for szotar in lista:
        if szotar["nev"] == "Barna Eszter"and szotar["idopont"] ==idoStr:
            szabad= False

    if szabad:
        print(idoStr)



for i in range(0,6):
    szabad = True
    idoStr="17:00"
    if i>0:
        idoStr = "17:" + str(i * 10)

    for szotar in lista:
        if szotar["nev"] == "Barna Eszter"and szotar["idopont"] ==idoStr:
            szabad= False

    if szabad:
        print(idoStr)



utolso=""
ora=0
perc=0
for szotar in lista:

    if szotar["nev"]=="Barna Eszter":
        if utolso< szotar["idopont"]:
            utolso= szotar["idopont"]
            ido = utolso.split(":")
            ora=int(ido[0])
            perc=int(ido[1])


if perc==50:
    ora+=1
    print(f"Barna Eszter legkorábban távozhatott: {ora}:00")

else:
    print(f"Barna Eszter legkorábban távozhatott: {ora}:{perc+10} ")





