import random
import string


def generate_password(length=12, use_uppercase=False, use_lowercase=False, use_numbers=False, use_specials=False,
                      pattern="", complexity="medium"):
    # Define character sets for u, l, s, n
    char_sets = {
        'u': string.ascii_uppercase,  # Uppercase letters
        'l': string.ascii_lowercase,  # Lowercase letters
        's': string.punctuation,  # Special characters
        'n': string.digits  # Numbers
    }

    # If a pattern is provided, use it to build the character pool
    if pattern:
        character_pool = ''.join([char_sets[char] for char in pattern if char in char_sets])
    else:
        # Build character pool from checkboxes
        character_pool = ""
        if use_uppercase:
            character_pool += string.ascii_uppercase
        if use_lowercase:
            character_pool += string.ascii_lowercase
        if use_numbers:
            character_pool += string.digits
        if use_specials:
            character_pool += string.punctuation

    # Fallback if character pool is empty
    if not character_pool:
        return "Select options or provide a valid pattern!"

    # Generate password
    password = ''.join(random.choice(character_pool) for _ in range(length))

    # Adjust complexity if required
    if complexity == "high" and len(password) >= 12:
        # Ensure at least one of each selected type for high complexity
        required_chars = ""
        if 'u' in pattern or use_uppercase:
            required_chars += random.choice(string.ascii_uppercase)
        if 'l' in pattern or use_lowercase:
            required_chars += random.choice(string.ascii_lowercase)
        if 's' in pattern or use_specials:
            required_chars += random.choice(string.punctuation)
        if 'n' in pattern or use_numbers:
            required_chars += random.choice(string.digits)

        # Replace characters in the password to ensure all required types exist
        password = list(password)
        for i in range(len(required_chars)):
            password[i] = required_chars[i]
        random.shuffle(password)
        password = ''.join(password)

    return password
