# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
   miles = kilometers / 1.609344
   return miles


def miles_naar_kilometers(miles):
    kilometers = miles * 1.609344
    return kilometers

kilometers = 1223
miles = 867

print(kilometers_naar_miles(kilometers))
print(miles_naar_kilometers(miles))