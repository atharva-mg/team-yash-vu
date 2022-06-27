from __init__ import *
import re
from password_evaluator import *

def evaluate(password:str)->list:
    score = evaluate_score(password)
    if 9 >= score >= 0:
        return [score, "WEAK", password]
    elif 17 >= score >= 10:
        return [score, "AVERAGE", password]
    else:
        return [score, "STRONG", password]
        # if 6>=len(password)>0:
        #     return ["2","WEAK",password]
        # if re.findall('[\!\@\#\`\~\$\^\&\*\(\)\[\]\{\}\_\-\=\+\'\"\;\:\.\,\>\<\/\?]',password):
        #     if re.findall('[0-9]',password):
        #         if re.findall('[A-Z]',password):
        #             return ["0", "STRONG", password]
        #         else: return ["1", "AVERAGE", password]
        #     else: return ["1", "AVERAGE",password]
        # else: return ["2", "WEAK", password]
        
# l = []
# l.append(evaluate("yaSh%^1264"))
# l.append(evaluate("yah%^"))
# l.append(evaluate("y@#46687"))
# l.append(evaluate("yggcytPI%^1264"))
# l.append(evaluate("asdaad'aa!@1323"))

# print(l)
# l.sort()
# print("\n\n",l)
