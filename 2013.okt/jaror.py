def feladat(szam):
    print(f"\n{szam}. feladat")

jarmuvek=[]
with open("jarmu.txt", "r", encoding="UTF-8")as fajl:
    for sor in fajl:
        sor= sor.strip().split()
        jarmu={
            "ora": int(sor[0]),
            "perc":int(sor[1]),
            "msp":int(sor[2]),
            "ido_msp":int(sor[0])*3600+ int(sor[1])*60+int(sor[2]),
            "rendszam":sor[3]
        }
        jarmuvek.append(jarmu)
        jarmu={}

print(f"{jarmuvek=}")


feladat(2)
ora=set()
for jarmu in jarmuvek:
    ora.add(jarmu["ora"])

print(f"Legalább {len(ora)} órát dolgoztak")

feladat(3)

for i in range(min(ora), max(ora)+1):
    for jarmu in jarmuvek:
        if jarmu["ora"]== i:
            print(f"{jarmu['ora']} {jarmu['rendszam']}")
            break

feladat(4)

autobusz=0
kamion=0
motor=0
auto=0

for jarmu in jarmuvek:
    if jarmu["rendszam"][0] =="B":
        autobusz+=1

    elif jarmu["rendszam"][0] =="K":
        kamion+=1

    elif jarmu["rendszam"][0] =="M":
        motor+=1

    else:
        auto+=1

print(f"{autobusz} db autóbusz kategóriájú, {kamion} db kamion kategóriájú, {motor} db motor kategóriájú jármű és {auto} db"
      f"személygépjármű haladt el")

feladat(5)
leghosszabb=0
eleje=""
vege=""

for index in range(0, len(jarmuvek)-1):
    szunet= jarmuvek[index+1]['ido_msp']-jarmuvek[index]['ido_msp']

    if szunet>leghosszabb:
        leghosszabb=szunet
        eleje= f'{jarmuvek[index]["ora"]}:{jarmuvek[index]["perc"]}:{jarmuvek[index]["msp"]}'
        vege=f'{jarmuvek[index+1]["ora"]}:{jarmuvek[index+1]["perc"]}:{jarmuvek[index+1]["msp"]}'

print(f"{eleje} - {vege}")

feladat(6)

felismert= input("Adja meg a felismert rendszámot (7 karakter)! ")

egyezes=0

for jarmu in jarmuvek:
    for szam in range(0, 7):
        if jarmu["rendszam"][szam] == felismert[szam] or felismert[szam]=="*":
            egyezes+=1

    if egyezes==7:
        print(jarmu["rendszam"])

    egyezes = 0









