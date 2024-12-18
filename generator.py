import random
import string

# This function generates a password based on the given parameters

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials, pattern=None,
                      complexity='medium'):
    # Define character sets
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digits = string.digits
    specials = string.punctuation

    # Adjust character sets based on complexity chosen by user (low, medium, high)
    if complexity == 'low':
        chars = lowercase_chars + uppercase_chars
    elif complexity == 'medium':
        chars = lowercase_chars + uppercase_chars + digits
    elif complexity == 'high':
        chars = lowercase_chars + uppercase_chars + digits + specials

    # Handle pattern-based password generation
    password = []
    if pattern:
        for ch in pattern:
            if ch == 'u' and use_uppercase:
                password.append(random.choice(uppercase_chars))
            elif ch == 'l' and use_lowercase:
                password.append(random.choice(lowercase_chars))
            elif ch == 'n' and use_numbers:
                password.append(random.choice(digits))
            elif ch == 's' and use_specials:
                password.append(random.choice(specials))
            else:
                # If the pattern is invalid, add a random character from the allowed set
                password.append(random.choice(chars))
    else:
        password = random.choices(chars, k=length)

    # Return the generated password as a string
    return ''.join(password)
