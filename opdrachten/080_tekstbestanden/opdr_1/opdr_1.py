# Opdracht 1 while-loops
# Naam student: Roisin
# Groep:

# Jouw code komt hier

def uitvoeren_enquete():
    antwoorden = []

    print("Welkom bij de enquête!")

    # Vraag 1
    antwoord1 = input("Wat vind je van de huidige regering? ")
    antwoorden.append(antwoord1)

    # Vraag 2
    antwoord2 = input("Wat vind je van de Python-lessen tot nu toe? ")
    antwoorden.append(antwoord2)

    # Vraag 3
    antwoord3 = input("Wat vind jij de mooiste stad van Nederland? ")
    antwoorden.append(antwoord3)

    # Opslaan van de antwoorden in een tekstbestand
    with open("enquete_resultaten.txt", "a") as f:
        f.write("Antwoorden:\n")
        f.write(f"1. Wat vind je van de huidige regering? - {antwoord1}\n")
        f.write(f"2. Wat vind je van de Python-lessen tot nu toe? - {antwoord2}\n")
        f.write(f"3. Wat vind jij de mooiste stad van Nederland? - {antwoord3}\n")
        f.write("\n")

    print("Bedankt voor het invullen van de enquête!")

def main():
    uitvoeren_enquete()

if __name__ == "__main__":
    main()