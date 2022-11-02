def feladatok(szama):
    print(f"{szama}. feladat")

lista=[]
szotar={}

paros=[]
paratlan=[]

with open("kerites.txt", "r", encoding="UTF-8") as fajl:
    for sor in fajl:
        sor= sor.strip().split()
        szotar["paros0paratlan1"]= int(sor[0])
        szotar["szelesseg"]= int(sor[1])
        szotar["kerites"]= sor[2]
        lista.append(szotar)

        if szotar["paros0paratlan1"]==0:
            paros.append(szotar)

        else:
            paratlan.append(szotar)
        szotar={}

print(lista)
print(paros)
print(paratlan)

feladatok(2)
print(f"Az eladott telkek száma: {len(lista)}")

feladatok(3)

utolso=0
hazszamParos=0
hazszamParatlan=1

for szotar in lista:
    utolso= szotar["paros0paratlan1"]
    if szotar["paros0paratlan1"]==1:
        hazszamParatlan+=2
    else:
        hazszamParos+=2


if utolso ==1:
        print("A páratlan oldalon adták el az utolsó telket. ")
        print(f"Az utolsó telek házszáma: {hazszamParatlan} ")
else:
        print("A páros oldalon adták el az utolsó telket. ")
        print(f"Az utolsó telek házszáma: {hazszamParos} ")

feladatok(4)

elozoszin=""
hazszam=-1

for i in range(0, len(paratlan)-1):
     if elozoszin==paratlan[i]["kerites"] and paratlan[i]["kerites"]!="#" and paratlan[i]["kerites"] !=":" and elozoszin!=":" and elozoszin!="#":
         print(f"A szomszédossal egyezik a kerítés színe: {hazszam}")
         break
     hazszam+=2
     elozoszin= paratlan[i]["kerites"]

beker= int(input("Adjon meg egy házszámot! "))

szin1=""
szin2=""


halmaz=set()
for szotar in lista:
    if szotar["kerites"]!= "#" and szotar["kerites"]!=":":
        halmaz.add(szotar["kerites"])

#print(halmaz)

if beker%2==1:
    hazszam = -1
    for i in range(0, len(paratlan)):
        hazszam += 2
        if beker == hazszam:
            print("A kerítés színe / állapota: ", paratlan[i]["kerites"])
            szin1= paratlan[i-1]["kerites"]
            szin2=paratlan[i+1]["kerites"]



else:
    hazszam=0
    for i in range(0, len(paros)):
        hazszam+=2
        if beker==hazszam:
            print("A kerítés színe / állapota: ", paros[i-1]["kerites"]) # paros[i-1] azért mert az utolsó ház páros
            szin1 = paros[i - 2]["kerites"]
            szin2 = paros[i]["kerites"]




#print(szin1)
#print(szin2)


if szin1!="#" and szin1!=":":
    halmaz.remove(szin1)
if szin2!="#" and szin2!=":":
    halmaz.remove(szin2)



print("Egy lehetséges festési szín: ",halmaz.pop())


feladatok(6)

with open("utcakep.txt", "w", encoding="UTF-8") as ki:
    for i in range(0, len(paratlan)):
        hossz = paratlan[i]["szelesseg"]
        for x in range(0, hossz, 1):
            print(paratlan[i]["kerites"], end="", file=ki)


    print(file=ki)

    index=-1
    for i in range(0, len(paratlan)):
        index += 2
        print(index, end="", file=ki)
        hossz=paratlan[i]["szelesseg"]

        if index>11:
            hossz-1
        if index>99:
            hossz-1


        for x in range(0, hossz-1, 1):
            print(" ",end="", file=ki)


