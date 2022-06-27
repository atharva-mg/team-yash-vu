# IBM Hackathon
# Project - Password Hacks
from colorama import Fore, Back, init, Style
from time import sleep
class Profile:
    # profile = {
    #     "name": "Hasnain",
    #     "surname": "Merchant",
    #     "nickname": "Has",
    #     "birthdate": "20092001",
    #     "college": "Vishwakarma",
    #     "pet": "Lallu",
    #     "words": ["hacker", "boy", "bro"],
    #     "special_char": "n",
    #     "random_num": "n"
    # }
    
    # A Profile Dictionary To Store User Data
    profile = {}

    # Function To Add Details Of User
    def details(self):
        print(Fore.GREEN+"\n[+] Insert The Information About The Victim To Make A Dictionary\n[+] If You Don't Know All The Info, Just Hit Enter key\n")

        # Insert Name Of Victim
        name = input(Fore.BLUE+"> First Name : "+Fore.GREEN).lower()
        while name == " " or name == "":
            print(Fore.RED+"\n[-] You Must Enter At Least A Name")
            name = input(Fore.BLUE+"> First Name : "+Fore.GREEN).lower()
        self.profile["name"] = str(name)

        # Insert Surname of Victim
        self.profile["surname"] = input(Fore.BLUE+"> Last Name : "+Fore.GREEN).lower()
        
        # Insert Nickname of Victim
        self.profile["nickname"] = input(Fore.BLUE+"> Nickname : "+Fore.GREEN).lower()
        
        # Insert Birthdate of Victim
        birthdate = input(Fore.BLUE+"> Birthdate (DD/MM/YYYY) : "+Fore.GREEN)
        while len(birthdate) !=0 and len(birthdate)!=8:
            print(Fore.RED+"\n[-] You Must Enter 8 digiys for birthday! ")
            birthdate = input(Fore.BLUE+"> Birthdate (DDMMYYYY) : "+Fore.GREEN)
        self.profile["birthdate"] = str(birthdate)

        print("\n")

        # Enter Additional Details of the Victim

        # Enter Victim's Pet Name (if any)
        self.profile["pet"] = input(Fore.BLUE+"> Pet's Name : "+Fore.GREEN).lower()
        
        # Enter College Name of Victim
        self.profile["college"] = input(Fore.BLUE+"> College Name : "+Fore.GREEN).lower()
        print("\n")

        # Additional Words Of the Victim (e.g, hacker, pentester)
        self.profile["words"] = [""]
        words1 = input(
            Fore.BLUE+"> Do You Want To Add Some Key Words About The Target ? Y/N : "+Fore.GREEN
        ).lower()
        words2 = ""
        if words1 == "y" or words1 == "Y":
            words2 = input(Fore.BLUE+"> Enter Words, Separated by comma : "+Fore.GREEN).replace(" ", "")
        self.profile["words"] = words2.split(",")

        # Add Special Characters (@, #, $, etc) (if any)
        self.profile["special_char"] = [""]
        special_char = input(
            Fore.BLUE+"> Do You Want To Add Special Chars At The End Of Words ? Y/N : "+Fore.GREEN
        ).lower()
        special_char2 = ""
        if special_char == "y" or special_char == "Y":
            special_char2 = input(
                Fore.BLUE+"> Enter Special Characters, Separated by comma : "+Fore.GREEN
            ).replace(" ", "")
        self.profile["special_char"] = special_char2.split(",")

        # Add Random Number (if any)
        self.profile["random_num"] = input(
            Fore.BLUE+"> Do You Want To Add Some Random Numbers At The End Of Words ? Y/N : "+Fore.GREEN
        ).lower()


    # Function To Combine Sequence and Start with Special Character
    def combine(self, sequence, start, special=""):
        if len(special) > 0:
            for symb in special:
                for mystr in sequence:
                    for mystr1 in start:
                        yield mystr + symb + mystr1
        else:
            for mystr in sequence:
                for mystr1 in start:
                    yield mystr + special + mystr1

    # Function To Concatinate Random Numbers with String
    def concatStringsRandomNumbers(self, sequence, start, stop):
        for mystr in sequence:
            for num in range(start, stop):
                yield mystr + str(num)


    # Function To Write Wordlist To File
    def print_to_file(self, file_name, combinations):
        output_file = open(file_name, "w")
        for k in combinations:
            for v in combinations[k]:
                try:
                    output_file.write(v + "\n")
                except:
                    pass
        print(Fore.GREEN+"[+] SUCCESSFULLY CREATED A DICTIONARY FILE\n")
        print(f"{Fore.GREEN}File Name Is -{Fore.YELLOW} {file_name}")
        print(Fore.GREEN+"File Name Is - "+Fore.YELLOW+self.profile["name"]+"_eval.txt\n\n")
        output_file.close()

    # Function To Generate Wordlist
    def generate_wordlist(self):
        print("\n[+] Generating Dictionary.....")
        sleep(3)

        # Birthdays first
        birthdate_yyyy = self.profile["birthdate"][-4:]
        birthdate_dd = self.profile["birthdate"][:2]
        birthdate_mm = self.profile["birthdate"][2:4]

        # Converting First Letters To Uppercase
        nameUP = self.profile["name"].title()
        surnameUP = self.profile["surname"].title()
        nicknameUP = self.profile["nickname"].title()
        collegeUP = self.profile["college"].title()
        petUP = self.profile["pet"].title()

        wordsUP = []
        wordsUP = list(map(str.title, self.profile["words"]))

        word = self.profile["words"] + wordsUP

        # Reverse Names
        reverse_name = self.profile["name"][::-1]
        reverse_nameUP = nameUP[::-1]
        reverse_nickname = self.profile["nickname"][::-1]
        reverse_nicknameUP = nicknameUP[::-1]

        reverse_n = [reverse_name, reverse_nameUP, reverse_nickname, reverse_nicknameUP]

        # Birthdays Combinations 
        birthday_combination = [
            birthdate_yyyy,
            birthdate_dd,
            birthdate_mm,
        ]

        # Birthday Combinations(Final)
        birthday_combinations = []
        for bds1 in birthday_combination:
            birthday_combinations.append(bds1)
            for bds2 in birthday_combination:
                if birthday_combination.index(bds1) != birthday_combination.index(bds2):
                    birthday_combinations.append(bds1 + bds2)

        # String Combinations
        combination_pet_college = [
            self.profile["pet"],
            petUP,
            self.profile["college"],
            collegeUP,
        ]

        # Name Combination
        name_combination = [
            self.profile["name"],
            self.profile["surname"],
            self.profile["nickname"],
            nameUP,
            surnameUP,
            nicknameUP,
        ]

        # Name Combinations (Final)
        name_combinations = []
        for combinations1 in name_combination:
            name_combinations.append(combinations1)
            for combinations2 in name_combination:
                if name_combination.index(combinations1) != name_combination.index(
                    combinations2
                ) and name_combination.index(
                    combinations1.title()
                ) != name_combination.index(
                    combinations2.title()
                ):
                    name_combinations.append(combinations1 + combinations2)

        # Total Combinations (A Dictionary)
        tot_combinations = {}
        # Combine Name's With Birthday's
        tot_combinations[1] = list(
            self.combine(name_combinations, birthday_combinations)
        )
        # Combine Name's With Birthday's and Special Characters
        tot_combinations[2] = list(self.combine(name_combinations, birthday_combinations, self.profile["special_char"]))
        # Combine Words With Birthday's
        tot_combinations[3] = list(self.combine(word, birthday_combinations))
        # Combine Words With Birthday's and Special Characters
        tot_combinations[4] = list(self.combine(word, birthday_combinations, self.profile["special_char"]))
        # If Random Number's Selected, add Random Numbers to Strings 
        if self.profile["random_num"] == "y":
            # Start Range
            numfrom = 0
            # End Range
            numto = 1000

            # Combine Words With Random Number Range
            tot_combinations[5] = list(
                self.concatStringsRandomNumbers(word, numfrom, numto)
            )
            # Combine Name With Random Number Range
            tot_combinations[6] = list(
                self.concatStringsRandomNumbers(name_combinations, numfrom, numto)
            )
            # Combine Pet, College Details With Random Number Range
            tot_combinations[7] = list(
                self.concatStringsRandomNumbers(combination_pet_college, numfrom, numto)
            )
            # Combine Reverse Strings With Random Number Range
            tot_combinations[8] = list(
                self.concatStringsRandomNumbers(reverse_n, numfrom, numto)
            )
        
        # Combine Reverse Strings with Birthday's
        tot_combinations[9] = list(self.combine(reverse_n, birthday_combinations))
        # Combine Reverse Strings with Birthday's and Special Character
        tot_combinations[10] = list(self.combine(reverse_n, birthday_combinations, self.profile["special_char"]))
        
        # If There are More Than one Special Characters ,append at End
        if len(self.profile["special_char"]) > 0:
            # Combine Name's with Special Character
            tot_combinations[11] = list(
                self.combine(name_combinations, self.profile["special_char"])
            )
            # Combine Pet/College With Special Character
            tot_combinations[12] = list(
                self.combine(combination_pet_college, self.profile["special_char"])
            )
            # Combine Word's With Special Character
            tot_combinations[13] = list(
                self.combine(word, self.profile["special_char"])
            )
            # Combine Reverse String's With Special Character
            tot_combinations[14] = list(
                self.combine(reverse_n, self.profile["special_char"])
            )

        # Store Words To Dictionary
        self.print_to_file(self.profile["name"] + ".txt", tot_combinations)
