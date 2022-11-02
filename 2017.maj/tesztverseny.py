lista=[]
szotar={}

megoldas=None
with open("valaszok.txt", "r", encoding="UTF-8") as fajl:
    megoldas= fajl.readline().strip()
    for sor in fajl:
        sor= sor.strip().split()
        szotar["az"]= sor[0]
        szotar["valasz"]= sor[1]

        lista.append(szotar)
        szotar={}

print(megoldas)
print(lista)

print(f"2. feladat: A vetélkedőn {len(lista)} versenyző indult.")

print("3. feladat", end= " ")
beker= input("A versenyző azonosítója = ")

for szotar in lista:
    if szotar["az"] == beker:
        print(szotar["valasz"])

print("4. feladat")
print(megoldas)
for szotar in lista:
    if szotar["az"] == beker:
        for i,v in enumerate(megoldas):
            if v== szotar["valasz"][i]:
                print("+", end="")
            else:
                print(" ",end="")

print()

print("5. feladat")

feladat= int(input("A feladat sorszáma ="))
helyes=0


for szotar in lista:
    if megoldas[feladat-1]==szotar["valasz"][feladat-1]:
        helyes+=1


arany = helyes/len(lista)*100

print(f"A feladatra {helyes} fő, a versenyzők {round(arany,2)}%-a adott helyes választ. ")


print("6. feladat")



osszPont = []
for szotar in lista:
        aktErtek=0
        for j in range(13, -1, -1):
            for i, v in enumerate(megoldas):
                if szotar["valasz"][i]== v and i==j:
                    if j==13:
                        aktErtek+=6

                    elif j>=10 :
                        aktErtek+=5

                    elif j>=5:
                        aktErtek+=4

                    else:
                        aktErtek+=3

        osszPont.append(aktErtek)

print(osszPont)

with open("pontok.txt", "w", encoding="UTF-8") as ki:
    i=0
    for szotar in lista:
        print(szotar["az"],osszPont[i], file=ki)
        i+=1

print("7. feladat")
masolat= osszPont.copy()

masolat.sort()
masolat.reverse()
#print(masolat)

elso= masolat[0]

masodik=0
harmadik=0

for i in range(0, len(masolat)-1):
    if masolat[i]!= masolat[i+1]:
        if masodik==0:
            masodik=masolat[i+1]
        else:
            harmadik=masolat[i+1]
            break



i=0
for szotar in lista:
    if osszPont[i]==elso:
        print(f"1. díj ({elso} pont): " +szotar["az"])
    i+=1

i=0
for szotar in lista:
    if osszPont[i]==masodik:
        print(f"2. díj ({masodik} pont): " +szotar["az"])
    i+=1


i=0
for szotar in lista:
    if osszPont[i]==harmadik:
        print(f"3. díj ({harmadik} pont): " +szotar["az"])
    i+=1








