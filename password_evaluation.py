from __init__ import *
import re
from password_evaluator import *

def evaluate(password:str)->list:
    """
    Returns strength according to length of pass
    """
    score, length, upper_case, lower_case, special, digits = evaluate_score(password)
    if 9 >= score >= 0:
        return [score, "WEAK", password], length, upper_case, lower_case, special, digits
    elif 17 >= score >= 10:
        return [score, "AVERAGE", password], length, upper_case, lower_case, special, digits
    else:
        return [score, "STRONG", password], length, upper_case, lower_case, special, digits
