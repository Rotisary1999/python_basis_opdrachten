# Opdracht 4 condities
# Naam student: Roisin
# Groep:



# Lijst met beschikbare toppings
beschikbare_toppings = ["olijven", "kaas", "salami", "pepperoni", "ansjovis"]

# Input van de gebruiker voor het kiezen van een topping
gekozen_topping = input(f"Kies je topping uit deze lijst: { beschikbare_toppings }: ")

# Prijslijst voor de toppings
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Zoek de prijs van de gekozen topping
gekozen_prijs = None
for topping, prijs in toppings:
    if topping == gekozen_topping:
        gekozen_prijs = prijs
        break

# Als de gekozen topping niet beschikbaar is, print dan een foutmelding
if gekozen_prijs is None:
    print("De gekozen topping is niet beschikbaar.")
else:
    # Print de gekozen topping en de prijs
    print(f"Je hebt gekozen voor {gekozen_topping} en de prijs is {gekozen_prijs:.2f} euro.")
