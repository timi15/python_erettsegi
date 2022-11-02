lista=[]
szotar={}

with open("ajto.txt","r", encoding="UTF-8") as file:
    for sor in file:
        sor= sor.strip().split()
        szotar['óra']= int(sor[0])
        szotar['perc']=int(sor[1])
        szotar['azonosito']= int(sor[2])
        szotar['irany']= sor[3]

        lista.append(szotar)
        szotar={}

#print(lista)

print('2. feladat')

print( "Az első belépő: ", lista[0]['azonosito'])

utolso=0
for szotar in lista:
    if szotar['irany']=='ki':
        utolso=szotar['azonosito']
print("Az utolsó belépő: ", utolso)

print("3. feladat")
with open('athaladas.txt', 'w', encoding='UTF-8') as athaladas:
    szemelyek=[]
    for i in range (1, 100):
        db=0
        for szotar in lista:
            if szotar['azonosito']== i:
                db=db+1
        szemelyek.append(db)
        if db>0:
            print(i, " ", db,file=athaladas)

print('4.feladat')

#print(szemelyek)
print("A végén a társalgóban voltak:", end=" ")
for i in range (0, 99):
   if szemelyek[i]%2==1:
       print(i+1, end=" ")



print("\n")
print("5. feladat")

bent=0
max=0
ora=0
perc=0

# az if ágakon mindig végig fut a program

for szotar in lista:
    if szotar['irany']=="be":
        bent+=1

    elif szotar['irany']=="ki":
        bent-=1

    if bent>max:
        max=bent
        ora= szotar['óra']
        perc= szotar['perc']


print("Például ",ora," : ", perc,"-kor voltak a legtöbben a társalgóban. ")


print("6. feladat")

azonosito= int (input("Adja meg a személy azonosítóját! "))

print("7. feladat")

for szotar in lista:
    if azonosito == szotar['azonosito'] :
        print(szotar['óra'],": ",  szotar['perc'], end=" ")
        if szotar['irany'] =="be":
            print("-", end=" ")
        elif szotar['irany'] =="ki":
            print()

print()
print("8. feladat")

osszperc=0
allapot=""
for szotar in lista:
    if azonosito == szotar['azonosito']:
        if szotar['irany'] =="be":
            beido= szotar['óra']*60+ szotar['perc']
            allapot="be"

        elif szotar['irany'] =="ki":
            kiido=szotar['óra']*60+ szotar['perc']
            osszperc=osszperc+(kiido-beido)
            allapot = "ki"

if allapot=="be":
    kiido= int(15)*60+ int(00)
    osszperc = osszperc + (kiido - beido)
    print(f"A(z) {azonosito}. személy összesen {osszperc} percet volt bent, a megfigyelés végén a társalgóban volt. ")


if allapot=="ki":
    print(f"A(z) {azonosito}. személy összesen {osszperc} percet volt bent, a megfigyelés végén a társalgón kívül volt. ")
































