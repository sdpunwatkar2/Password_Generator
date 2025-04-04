import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔐 Password Generator")
    length = int(input("Enter password length: "))
    upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include special characters? (y/n): ").lower() == 'y'

    pwd = generate_password(length, upper, digits, symbols)
    print(f"Your generated password: {pwd}")
