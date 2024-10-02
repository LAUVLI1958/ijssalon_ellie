# functie: vermenigvuldig met hetzelfde getal
def mijn_functie_1(a):
    return a * a
     
# het ingevulde argument wordt toegekend aan parameter a en levert de teruggeefwaarde
print(mijn_functie_1(2))
print(mijn_functie_1(4))
print(mijn_functie_1(10))
print(mijn_functie_1(12))

# functie: twee parameters. Het resultaat wordt in een lijst toegevoegd. operatoren +,-,* en / worden uitgevoerd 
def mijn_functie_2(a,b):
    rekenlijst=[]
    rekenlijst.append(a+b)
    rekenlijst.append(a-b)
    rekenlijst.append(a*b)
    rekenlijst.append(int(a/b))
    return rekenlijst

# de ingevulde argumenten worden toegekend aan parameter a en b en levert de teruggeefwaarden in een lijst
print(mijn_functie_2(12,3))
print(mijn_functie_2(12,2))
print(mijn_functie_2(10,5))
print(mijn_functie_2(100,20))






