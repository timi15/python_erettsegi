def feladat(szam):
    print(f"{szam}. feladat")


def orara_valt(o, p, msp, ezred_msp): # majd km / órában kell dolgozni ezért célszerű átváltani
    return o+ (p/60) +(msp+ ezred_msp/1000)/3600

jarmuvek=[]

with open("meresek.txt", "r") as fajl:
    for sor in fajl:
        sor= sor.strip().split()
        jarmu= {
            "rendszam":sor[0],
            "be": orara_valt(int(sor[1]), int(sor[2]), int(sor[3]), int(sor[4])),
            "ki": orara_valt(int(sor[5]), int(sor[6]), int(sor[7]), int(sor[8]))
        }

        jarmuvek.append(jarmu)


print(f"{jarmuvek=}")

feladat(2)
print(f"A mérés során {len(jarmuvek)} jármű adatait rögzítették. ")

feladat(3)
athaladt=0

for jarmu in jarmuvek:
    if jarmu["ki"]<9:
        athaladt+=1

print(f"9 óra előtt {athaladt} jármű haladt el a végponti mérőnél.")

feladat(4)

ora_perc= input("Adjon meg egy óra és perc értéket! ").strip().split()
#print(ora_perc)

meres_kezdete= float(ora_perc[0]) + float(ora_perc[1]) / 60
meres_vege= meres_kezdete+59.999 /3600

athaladt=0
uton=0

for jarmu in jarmuvek:
    if meres_kezdete<= jarmu["be"]<= meres_vege:
        athaladt+=1

print(f"\ta. A kezdeti méréspontnál elhaladt járművek száma: {athaladt}")

for jarmu in jarmuvek:
    if meres_vege> jarmu['be'] and meres_kezdete< jarmu['ki']:
        uton+=1

print(f"\tb. A forgalomsűrűség: {uton/10} ")

feladat(5)

max_seb=0
max_seb_jarmu={}
leelozott=0

for jarmu in jarmuvek:
    sebesseg= 10 / (jarmu["ki"]-jarmu["be"])

    if sebesseg> max_seb:
        max_seb= sebesseg
        max_seb_jarmu=jarmu

for jarmu in jarmuvek:
    if jarmu["be"]<max_seb_jarmu["be"] and jarmu["ki"]>max_seb_jarmu["ki"]:
        leelozott+=1

print("A legnagyobb sebességgel haladó jármű")
print(f"\trendszáma: {max_seb_jarmu['rendszam']} ")
print(f"\tátlagsebessége: {round(max_seb)} km/h")
print(f"\táltal lehagyott járművek száma: {leelozott}")

feladat(6)

gyorshajtott=0

for jarmu in jarmuvek:
    sebesseg = 10 / (jarmu["ki"] - jarmu["be"])
    if sebesseg>90:
        gyorshajtott+=1

#print(gyorshajtott)
print(f"A járművek {gyorshajtott / len(jarmuvek) * 100:.2f}%-a volt gyorshajtó. ")

feladat(7)

def birsag(sebesseg):
    if sebesseg<=121:
        return 30000

    elif sebesseg<=136:
        return 45000

    elif sebesseg<=150:
        return 60000

    else:
        return 200000

with open("buntetes.txt", "w", encoding="UTF-8")as ki:
    for jarmu in jarmuvek:
        sebesseg = 10 / (jarmu["ki"] - jarmu["be"])
        if sebesseg>=104:
            print(f"{jarmu['rendszam']} {round(sebesseg)} km/h {birsag(sebesseg)} Ft ", file=ki)

print("A fájl elkészült. ")
