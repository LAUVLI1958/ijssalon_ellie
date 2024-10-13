# functie decoreer

def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print ()
    print(lengte * "*")
    print(f"* {tekst} *") 
    print(lengte * "*")
    print()

# functie fooi per persoon

def fooi_pp(bedrag,personen):
    bedrag_pp = bedrag/personen
    return f"Het bedrag per persoon is {bedrag_pp} euro"

# functie onderstreep

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

# functie som van een enkele dictionary, die de values optelt en de som als resultaat teruggeeft
 
def som (dict):
    values=(dict).values()
    optelling=sum(values)  
    return optelling





