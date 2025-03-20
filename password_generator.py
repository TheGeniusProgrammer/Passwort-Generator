import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User-Enter
length = int(input("Password length: "))
print("Generated Password:", generate_password(length))
