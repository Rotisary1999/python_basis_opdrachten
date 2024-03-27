# Opdracht 1 functies
# Naam student:
# Groep:

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

def volledige_naam (lijst_met_namen):
    for persoon in lijst_met_namen:
        for key, value in persoon.items():
            print(f" {value}")


volledige_naam(namen)