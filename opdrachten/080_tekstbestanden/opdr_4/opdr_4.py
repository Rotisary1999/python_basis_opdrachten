# Opdracht 4 Tekst opslaan
# Naam student: Roisin
# Groep:


# Party enquete


#Zet de vragen in een lijst (type list)
enquete_vragen = [
"Wat is je voornaam?\n" ,
"Wat is je achternaam?\n" ,
"Wat neem je mee aan drank?\n" ,
"Wat neem je mee om te eten?\n" ,
]



#Geef de vragen genummerd weer op het scherm
for nummer, vraag in enumerate(enquete_vragen, start=1):
    antwoord = input(f"{nummer}. {vraag} ")

#De antwoorden worden opgeslagen in een dictionary

# Stap 5: Schrijf antwoorden naar een tekstbestand
bestandsnaam = "feestgangers_antwoorden.txt"

with open(bestandsnaam, 'w') as bestand:
    for antwoorden in enquete_vragen:
        for vraag, antwoord in antwoorden.items():
            bestand.write(f"{vraag}: {antwoord}\n")
        bestand.write("\n")

print(f"De antwoorden zijn opgeslagen in {bestandsnaam}.")