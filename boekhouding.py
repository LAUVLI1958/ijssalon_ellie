#importeer uit standaard Library het pakket csv  

import csv

#importeer uit bestand helper alle functies en variabelen
         
from helper import *

#importeer uit bestand presentatie de functie presenteer

from presentatie import presenteer

# dictionary inkomsten (key-value pairs)

inkomsten = {
             "Aardbeien-ijs-totaal": 1000,
             "Vanille-ijs-totaal": 2000,
             "Chocolade-ijs-totaal": 1500,
             "Waterijsjes-totaal": 750
             }

# variabele totaal_inkomsten en gebruik de functie som voor de totale som

totaal_inkomsten=som(inkomsten)

# gebruik de functie presenteer met de parameters inkomsten en totaal_inkomsten

presenteer(inkomsten,totaal_inkomsten)

# voeg het volgende commando toe die een csvfile maakt van boekhouding dictionary inkomsten

with open('boekhouding.csv','w',newline='')as csvfile:
          for key, value in inkomsten.items():
                  writer =csv.writer(csvfile,delimiter='.')
                  writer.writerow([key,value])

