from curses.ascii import islower
from re import L
import sys
from time import sleep
from colorama import Fore, Back, init, Style
import random
from __init__ import BANNEr, gen_wordlist_start
from password_evaluation import evaluate
from password_guesser import *

init(autoreset=True)


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
    choice = input(Fore.CYAN+"> Enter your choice: "+Fore.GREEN)

    if choice == "1":
        person = Profile()
        person.details()
        person.generate_wordlist()
        read = open(person.profile["name"] + ".txt", "r")
        result = []
        for line in read:
            result.append(evaluate(line.strip("\n")))
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
        result = evaluate(str(input("> Enter password you want to evaluate: ")))
        print("Password:\t"
                + result[2]
                + "\t\tStrength:\t"
                + result[1]
                + "\tScore:  "
                + str(result[0])
                + "\n")
    elif choice == "3":
        sys.exit()
    else:
        print("[-] Enter Valid Choice")
        sys.exit()
