def feladat(szam):
    print(f"{szam}. feladat")

vonatok=[]
with open("vonat.txt", "r", encoding="UTF-8") as fajl:
    for sor in fajl:
        sor=sor.strip().split("\t")
        vonat={
            "azonosito":int(sor[0]),
            "allomasAZ":int(sor[1]),
            "ora":int(sor[2]),
            "perc":int(sor[3]),
            "idoPercben": int(sor[2])*60+int(sor[3]),
            "erkezik/indul": sor[4]
        }

        vonatok.append(vonat)
        vonat={}

print(f"{vonatok=}")


