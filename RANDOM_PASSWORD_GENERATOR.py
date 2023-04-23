import random
import string

def generate_password(length):
    # Define all the possible characters that can be included in the password
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    # Combine all the characters into a single string
    all_chars = letters + digits + punctuation

    # Use random.sample to select a random set of characters of the specified length
    password = ''.join(random.sample(all_chars, length))

    return password

# Generate a password with length of 8 characters
password = generate_password(8)
print("HERE IS THE RANDOM PASSWORD THAT IS BEEN GENERATED:")
print(password)
