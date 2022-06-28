import sys
from time import sleep
from colorama import Fore, init
import random
from password_evaluation import evaluate
from password_guesser import *

init(autoreset=True)
BANNEr = [
"""
██████╗  █████╗ ███████╗███████╗    ██╗  ██╗ █████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝    ██║  ██║██╔══██╗╚██╗██╔╝
██████╔╝███████║███████╗███████╗    ███████║███████║ ╚███╔╝ 
██╔═══╝ ██╔══██║╚════██║╚════██║    ██╔══██║██╔══██║ ██╔██╗ 
██║     ██║  ██║███████║███████║    ██║  ██║██║  ██║██╔╝ ██╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                                                       
"""
]

if __name__ == "__main__":
    bIndex = random.randint(0, len(BANNEr) - 1)
    print(Fore.GREEN + BANNEr[bIndex])
    print(
        f"""
\n{Fore.YELLOW}+-------------------------------+
| {Fore.RED}Select one of the following:\t{Fore.YELLOW}|
|-------------------------------|
| {Fore.GREEN}1{Fore.YELLOW} | {Fore.GREEN}Enter Target Details.\t{Fore.YELLOW}|
| {Fore.GREEN}2{Fore.YELLOW} | {Fore.GREEN}Evaluate Password.\t{Fore.YELLOW}|
| {Fore.GREEN}3{Fore.YELLOW} | {Fore.GREEN}Exit.\t\t\t{Fore.YELLOW}|
+---+---------------------------+"""
    )
    choice = input(Fore.CYAN + "> Enter your choice: " + Fore.GREEN)

    if choice == "1":
        person = Profile()
        person.details()
        person.generate_wordlist()
        read = open(person.profile["name"] + ".txt", "r")
        result = []
        for line in read:
            res, length, upper_case, lower_case, special, digits = evaluate(
                line.strip("\n")
            )
            result.append(res)
        result.sort(reverse=True)
        read.close()
        # print(result)
        out_file = open(person.profile["name"] + "_eval.txt", "w")

        for i in result:
            out_file.write(
                "Password:\t"
                + i[2]
                + "\t\tStrength:\t"
                + i[1]
                + "\tScore:  "
                + str(i[0])
                + "\n"
            )
    elif choice == "2":
        result, length, upper_case, lower_case, special, digits = evaluate(
            str(
                input(
                    Fore.BLUE + "\n> Enter password you want to evaluate: " + Fore.GREEN
                )
            )
        )
        if result[1] == "WEAK":
            result[1] = Fore.RED + "WEAK"
            result[0] = Fore.RED + str(result[0])
        elif result[1] == "AVERAGE":
            result[1] = Fore.YELLOW + "AVERAGE"
            result[0] = Fore.YELLOW + str(result[0])
        elif result[1] == "STRONG":
            result[1] = Fore.GREEN + "STRONG"
            result[0] = Fore.GREEN + str(result[0])
        if 0 <= length <= 9:
            length = Fore.RED + "    LENGTH\t\t" + str(length)
        elif 10 <= length <= 17:
            length = Fore.YELLOW + "    LENGTH\t\t" + str(length)
        else:
            length = Fore.GREEN + "    LENGTH\t\t" + str(length)
        print()
        if upper_case:
            print(Fore.GREEN + "[+] UPPER CASE\t\t✓")
        else:
            print(Fore.RED + "[-] UPPER CASE\t\t✖")
        if lower_case:
            print(Fore.GREEN + "[+] LOWER CASE\t\t✓")
        else:
            print(Fore.RED + "[-] LOWER CASE\t\t✖")
        if special:
            print(Fore.GREEN + "[+] SPECIAL CASE\t✓")
        else:
            print(Fore.RED + "[-] SPECIAL CASE\t✖")
        if digits:
            print(Fore.GREEN + "[+] DIGIT\t\t✓")
        else:
            print(Fore.RED + "[-] DIGIT\t\t✖")

        print(length + "\n")

        print(
            "Password:\t"
            + result[2]
            + "\nStrength:\t"
            + result[1]
            + Fore.WHITE
            + "\nScore:\t\t"
            + result[0]
            + "\n"
        )
    elif choice == "3":
        sys.exit()
    else:
        print("[-] Enter Valid Choice")
        sys.exit()
