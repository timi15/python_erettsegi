import random
kiserletek=[]

with open("kiserlet.txt", "r", encoding="UTF-8") as fajl:
    for sor in fajl:
        kiserletek.append(sor.strip())

print(kiserletek)

print("1. feladat")
random = random.randint(0,1)

if random==0:
    print("A pénzfeldobás eredménye: I")
else:
    print("A pénzfeldobás eredménye: F")


print("2. feladat")
tipp = input("Tippeljen! (F/I)= ")

if random==0 and tipp=="I":
    print("A tipp I, a dobás eredménye I volt")
    print("Ön eltalálta!")
elif random==1 and tipp=="F":
    print("A tipp F, a dobás eredménye F volt")
    print("Ön eltalálta!")
elif random==0 and tipp=="F":
    print("A tipp F, a dobás eredménye I volt")
    print("Ön nem találta el!")
else:
    print("A tipp I, a dobás eredménye F volt")
    print("Ön nem találta el!")

print("3. feladat")
print(f"A kísérle {len(kiserletek)} dobásból állt")

print("4. feladat")
fejDb=0
for i in kiserletek:
    if i=="F":
        fejDb+=1
szazalek= fejDb/len(kiserletek)*100
print(f"A kísérlet során a fej relatív gyakorisága {round(szazalek, 2)}% volt")

print("5. feladat")
egymasUtan=0
index=0





print("6. feladat")
resz=[]


