import string

password = "SaMpLEPASSword12@"  # input the password provided by user.


def evaluate_score(password):

    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])

    characters = [upper_case, lower_case, special, digits]
    length = len(password)

    score = 0
    # with open ("Common.txt", "r") as f : #provide wordlist
    #     common = f.read().splitlines()

    # if password in common :
    #     print ("Password is found in common list. Score is 0") #if the password is found in any provided wordlist, password will score 0 points.
    #     exit()

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
    # print(f"Password Has {str(sum(characters))} Different Character Types") #Tells how many different types of characters are used.

    # print(f"Password Length is {str(length)} characters long, your password scored {str(score)}/25 points.") #Shows us final results.
