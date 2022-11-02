def feladat(szam):
    print(f"{szam}. feladat")


epitmenyek=[]

with open("utca.txt", "r", encoding="UTF-8")as fajl:
    adok= fajl.readline().strip().split()
    adosavok={"A":int(adok[0]), "B":int(adok[1]), "C": int(adok[2])}

    for sor in fajl:
        sor= sor.strip().split()
        epitmeny = {
            "adoszam":int(sor[0]),
            "utca": sor[1],
            "hsz": sor[2],
            "adosav":sor[3],
            "alapterulet":int(sor[4])
        }

        epitmenyek.append(epitmeny)
        epitmeny={}

#print(epitmenyek)

feladat(2)
print(f"A mintában {len(epitmenyek)} telek szerepel.")


feladat(3)
beker=int(input("Egy tulajdonos adószáma: "))
van=False
for epitmeny in epitmenyek:
    if beker== epitmeny["adoszam"]:
        print(f"{epitmeny['utca']} utca {epitmeny['hsz']}")
        van=True

if not van:
    print("Nem szerepel az adatállományban")

feladat(4)

def ado(adosav, alapterulet):
    ado= alapterulet*adosavok[adosav]

    if ado<10000:
        return 0
    else:
        return ado

feladat(5)

dbA=0
osszegA=0

dbB=0
osszegB=0

dbC=0
osszegC=0

for epitmeny in epitmenyek:
    a=ado(epitmeny["adosav"], epitmeny["alapterulet"])

    if epitmeny["adosav"]=="A":
        dbA+=1
        osszegA+=a

    elif epitmeny["adosav"]=="B":
        dbB+=1
        osszegB+=a

    else:
        dbC+= 1
        osszegC +=a

print(f"A sávba {dbA} telek esik, az adó {osszegA} Ft. ")
print(f"A sávba {dbB} telek esik, az adó {osszegB} Ft. ")
print(f"A sávba {dbC} telek esik, az adó {osszegC} Ft. ")

feladat(6)

utca_sav = {}
for epitmeny in epitmenyek:
    if epitmeny['utca'] in utca_sav:
            utca_sav[epitmeny['utca']].add(epitmeny['adosav'])
    else:
            utca_sav[epitmeny['utca']] = set(epitmeny['adosav'])

print(utca_sav)
print("A több sávba sorolt utcák: ")

for utca in utca_sav:
    if len(utca_sav[utca]) > 1:
        print(utca)

feladat(7)

ado_tulajdonosonkent={}

for epitmeny in epitmenyek:
    if epitmeny["adoszam"] in ado_tulajdonosonkent:
        ado_tulajdonosonkent[epitmeny["adoszam"]] +=ado(epitmeny["adosav"], epitmeny["alapterulet"])

    else:
        ado_tulajdonosonkent[epitmeny["adoszam"]]=ado(epitmeny["adosav"], epitmeny["alapterulet"])

with open('fizetendo.txt', 'w', encoding='utf-8') as fizetendo:
    for azonosito in ado_tulajdonosonkent:
        print(azonosito, ado_tulajdonosonkent[azonosito], file=fizetendo)



