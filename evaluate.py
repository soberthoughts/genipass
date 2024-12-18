import re


def evaluate_password_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 2
    if len(password) >= 16:
        score += 3

    # Check for variety
    if re.search(r'[0-9]', password):  # Contains numbers
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Contains special characters
        score += 1
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):  # Mix of upper and lower case
        score += 1

    # Check for weaknesses
    common_patterns = ['password', '1234', 'qwerty', 'abc', '1111']
    for pattern in common_patterns:
        if pattern in password.lower():
            score -= 2  # Penalty for common patterns

    # Categorize strength
    if score <= 3:
        return "Weak"
    elif 4 <= score <= 6:
        return "Medium"
    else:
        return "Strong"
