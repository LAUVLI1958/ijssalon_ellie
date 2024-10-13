# dictionary mijn_dict met keys en values

mijn_dict = {'vis':10,'vlees':25,'overig':15}

# de functie presenteer met 2 parameters 1 uit dictionary halen en 2 parameter totaal

def presenteer(dict, totaal):
    gegevens = dict
    soort = (dict).keys()
    bedrag =(dict).values()
    lengte = 26
    het_totaal=totaal
    for soort,bedrag in (dict).items():
        print(soort,":",bedrag,"euro")
    print(lengte * "=")
    print(f"totaal : {het_totaal} euro")
    print()
    return gegevens

# commando presenteer mijn_dict en totaal is 60

presenteer(mijn_dict,60)

    