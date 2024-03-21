# Opdracht 3 Tekst opslaan
# Naam student: Roisin
# Groep:

def encrypteer(tekst):
    encrypted_text = ""
    for karakter in tekst:
        # Controleer of het karakter een letter is
        if karakter.isalpha():
            # Bepaal de code van het karakter
            code = ord(karakter.lower())
            # Verschuif de code 5 posities in het alfabet (met omloop)
            verschoven_code = (code - ord('a') + 5) % 26 + ord('a')
            # Voeg het versleutelde karakter toe aan de versleutelde tekst
            encrypted_text += chr(verschoven_code) if karakter.islower() else chr(verschoven_code).upper()
        else:
            # Voeg het karakter ongewijzigd toe aan de versleutelde tekst als het geen letter is
            encrypted_text += karakter
    return encrypted_text

def decrypteer(encrypted_text):
    decrypted_text = ""
    for karakter in encrypted_text:
        # Controleer of het karakter een letter is
        if karakter.isalpha():
            # Bepaal de code van het karakter
            code = ord(karakter.lower())
            # Verschuif de code 5 posities terug in het alfabet (met omloop)
            verschoven_code = (code - ord('a') - 5) % 26 + ord('a')
            # Voeg het gedecodeerde karakter toe aan de gedecodeerde tekst
            decrypted_text += chr(verschoven_code) if karakter.islower() else chr(verschoven_code).upper()
        else:
            # Voeg het karakter ongewijzigd toe aan de gedecodeerde tekst als het geen letter is
            decrypted_text += karakter
    return decrypted_text

def main():
    tekst = input("Voer de tekst in die je wilt encrypten: ")
    versleuteld = encrypteer(tekst)
    print("Versleutelde tekst:", versleuteld)

    decrypted_text = decrypteer(versleuteld)
    print("Gedecodeerde tekst:", decrypted_text)

if __name__ == "__main__":
    main()


