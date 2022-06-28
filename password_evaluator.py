import string

def evaluate_score(password):
    """
    Evaluate `password` and returns multiple utilities
    """
    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])

    characters = [upper_case, lower_case, special, digits]
    length = len(password)

    score = 0
    # adding score on the basis of length of password.

    if length > 4:
        score += 2

    if length > 8:
        score += 2

    if length > 10:
        score += 2

    if length > 12:
        score += 2

    if length > 16:
        score += 2

    if length > 18:
        score += 2

    # adding score on the variety of characters used

    if sum(characters) > 1:
        score += 3

    if sum(characters) > 2:
        score += 4

    if sum(characters) > 3:
        score += 6

    return score, length, upper_case, lower_case, special, digits
