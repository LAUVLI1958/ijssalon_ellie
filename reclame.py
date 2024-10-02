# functie: twee parameters. Het resultaat wordt in een lijst toegevoegd. operatoren +,-,* en / worden uitgevoerd 
def mijn_functie_2(a,b):
    rekenlijst=[]
    rekenlijst.append(a+b)
    rekenlijst.append(a-b)
    rekenlijst.append(a*b)
    rekenlijst.append(a/b)
    return rekenlijst

# de functie bestaat uit drie parameters en geeft met de aangeroepen argumenten een string terug
def aanbieding_1(smaak,prijs,korting):
    # prijs min de korting geeft bedrag na korting
    bedrag_na_korting = prijs - (prijs * korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {bedrag_na_korting} euro."
    return uitvoer
    
print(aanbieding_1("aardbei",4,0.1))

# gemaakte functie: het totaal van inkomsten per dag opgeteld met de voorgedefinieerde functie sum, vervolgens btw\
# en dat gemeld in een string 
def inkomsten_totaal(inkomsten,btw):

    totaal = sum(inkomsten)
    bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return uitvoer

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09
print(inkomsten_totaal(inkomsten,btw))

# functie maximale en minimale waarden in een lijst en die wordt getoond
def laag_en_hoog(mijn_lijst):
    minimaal = min(mijn_lijst)
    maximaal = max(mijn_lijst)
    uitvoer_lijst = []
    uitvoer_lijst.append(minimaal)
    uitvoer_lijst.append(maximaal)
    return uitvoer_lijst

mijn_lijst=[220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(mijn_lijst))

#functie geeft het gemiddelde van een lijst en als teruggeefwaarde en string. Mijn_lijst is dezelfde als bij laag_en_hoog.
def gemiddelde(mijn_lijst):
    totaal_bedrag = sum(mijn_lijst)
    aantal_bedragen = len(mijn_lijst)
    bedrag_gemiddeld = int(totaal_bedrag/aantal_bedragen)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag_gemiddeld} euro."
    return uitvoer

print(gemiddelde(mijn_lijst))

#functie die gebruikt maakt van een andere door gebruiker gedefinieerde functie (laag_en_hoog)
def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

invoer_lijst = [10,5,3,2,1,2,9]
print(meervoudig(invoer_lijst))

'''
Met deze functie roep je de functie laag_en_hoog aan met als argument de parameter invoer_lijst_2. Er worden 2 waarden gekozen,
waarmee mijn_functie_2 wordt uitgevoerd.
De teruggeefwaarde wordt opgeslagen in variabele korte_lijst
'''
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

invoer_lijst_2 = [50,75,100,60,62,81]
print(combinatie(invoer_lijst_2))
