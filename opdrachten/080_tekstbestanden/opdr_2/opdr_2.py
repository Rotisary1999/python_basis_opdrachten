# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

import random

def raad_het_nummer():
    # Genereer een willekeurig getal tussen 1 en 100
    te_raden_getal = random.randint(1, 100)
    pogingen = 0

    print("Welkom bij het spel 'Raad een nummertje'!")
    print("Ik heb een getal tussen 1 en 100 in gedachten. Raad welk nummer het is!")

    while True:
        gok = int(input("Doe een gok: "))
        pogingen += 1

        if gok < te_raden_getal:
            print("Hoger!")
        elif gok > te_raden_getal:
            print("Lager!")
        else:
            print(f"Gefeliciteerd! Je hebt het juiste nummer {te_raden_getal} geraden!")
            print(f"Je hebt {pogingen} pogingen nodig gehad.")
            break

def main():
    raad_het_nummer()

if __name__ == "__main__":
    main()