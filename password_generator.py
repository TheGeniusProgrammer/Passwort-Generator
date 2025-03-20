import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Nutzer-Eingabe
length = int(input("Passwortlänge: "))
print("Generiertes Passwort:", generate_password(length))
