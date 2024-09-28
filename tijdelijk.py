from helper import decoreer

def print_aanbieding():
   # dictionary prijzen aangemaakt
   prijzen = {"aardbei" : 3,
            "vanille" : 4,
            "chocolade" : 5
            }

   # formule aanbieding prijs aardbei maal 0.8
   aanbieding = prijzen["aardbei"] * 0.8

   # reclametekst met formatted string met de formule aanbieding
   reclame_tekst =f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}"

   # reclametekst prijs aangepast tot 2 decimalen achter de komma
   reclame_tekst2 = reclame_tekst [:63]

   # in hoofdletters geprint
   reclame_tekst3 = reclame_tekst2.upper()

   # reclametekst voor drukker in een list van alle woorden
   reclame_tekst4 = reclame_tekst3.split()

   '''
   reclametekst onder elkaar, waarbij elementen die vijf of meer karakters hebben in hoofdletters
   minder dan 5 in kleine letters
   '''  
   for el in reclame_tekst4:
     if  (len(el)) < 5:

      print(el.lower())
     else:
      print(el.upper())

decoreer("Aanbieding")
print_aanbieding()



    





