#3. PASSWORD GENERATOR

import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters for better security.")
        return ""

    # Define character sets
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # special characters like !@#$

    # Combine all characters
    all_chars = letters + digits + symbols

    # Ensure the password includes at least one of each character type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password with random choices
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the password list and convert to string
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Secure Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"\nYour generated password: {password}")
    except ValueError:
        print("Please enter a valid number.")

# Run the password generator
main()

