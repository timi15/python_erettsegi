naplo = {}
diak = []
with open('naplo.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        if sor[0] == '#':
            datum_sor = sor.strip().split()
            datum = datum_sor[1] + ' ' + datum_sor[2]
            naplo[datum] = {}
        else:
            bejegyzes = sor.strip().split()
            nev = bejegyzes[0] + ' ' + bejegyzes[1]
            naplo[datum][nev] = bejegyzes[2]

print(f"{naplo=}")


