# Opdracht 1 while-loops
# Naam student: Roisin
# Groep:

# Jouw code komt hier

antwoord1 = input ("Wat vind je van de huidige regering?\n")
antwoord2 = input ("Wat vind je van de Python-lessen tot nu toe?\n")
antwoord3 = input ("Wat vind jij de mooiste stad van Nederland?\n")

fo = open('antwoorden.txt', 'w')
fo.write("Vraag 1: " + antwoord1 + "\n")
fo.write("Vraag 2: " + antwoord2 + "\n")
fo.write("Vraag 3: " + antwoord3 + "\n")
fo.close() 