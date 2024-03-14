# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Vraag de gebruiker om de leeftijd in te voeren
leeftijd_input = int(input("Geef uw leeftijd in aantal jaar: "))

# Bepaal tot welke groep de bezoeker behoort
for groep, leeftijdsgrenzen in leeftijd.items():
    if leeftijdsgrenzen[0] <= leeftijd_input <= leeftijdsgrenzen[1]:
        groep_bezoeker = groep
        break

# Bereken de korting op basis van de groep van de bezoeker
korting = kortings_percentages[groep_bezoeker]
korting_bedrag = normale_toegangsprijs * (korting / 100)
te_betalen_bedrag = normale_toegangsprijs - korting_bedrag

# Print de output
print("U behoort tot de groep", groep_bezoeker)
print("U krijgt", korting, "% korting")
print("U betaalt daarom", te_betalen_bedrag)




