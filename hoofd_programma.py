#uit bestand importeer het zelfgemaakte pakket (functie) onderstreep

from helper import onderstreep

# voer onderstaande commando's uit

uitvoer = onderstreep("AANBIEDING")
uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")

print()

for el in uitvoer:
    print(el)