# IBM Hackathon
# Project - Password Hacks


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
    profile = {}

    def details(self):
        print("\r\n[+] Insert The Information About The Victim To Make A Dictionary")
        print("[+] If You Don't Know All The Info, Just Hit Enter \r\n")

        name = input("> First Name : ").lower()
        while name == " " or name == "":
            print("\r\n[-] You Must Enter At Least A Name")
            name = input("> First Name : ").lower()
        self.profile["name"] = str(name)

        self.profile["surname"] = input("> Last Name : ").lower()
        self.profile["nickname"] = input("> Nickname : ").lower()
        birthdate = input("> Birthdate (DDMMYYYY) : ")
        while len(birthdate) !=0 and len(birthdate)!=8:
            print("\r\n[-] You Must Enter 8 digiys for birthday! ")
            birthdate = input("> Birthdate (DDMMYYYY) : ")
        self.profile["birthdate"] = str(birthdate)

        print("\r\n")

        self.profile["pet"] = input("> Pet's Name : ").lower()
        self.profile["college"] = input("> College Name : ").lower()
        print("\r\n")

        # self.profile["mobile"] = input("> Enter Mobile Number (+91) : ")
        self.profile["words"] = [""]
        words1 = input(
            "> Do You Want To Add Some Key Words About The Target ? Y/N : "
        ).lower()
        words2 = ""
        if words1 == "y":
            words2 = input("> Enter Words, Separated by comma : ").replace(" ", "")
        self.profile["words"] = words2.split(",")

        self.profile["special_char"] = [""]
        special_char = input(
            "> Do You Want To Add Special Chars At The End Of Words ? Y/N : "
        ).lower()
        special_char2 = ""
        if special_char == "y":
            special_char2 = input(
                "> Enter Special Characters, Separated by comma : "
            ).replace(" ", "")
        self.profile["special_char"] = special_char2.split(",")

        self.profile["random_num"] = input(
            "> Do You Want To Add Some Random Numbers At The End Of Words ? Y/N : "
        ).lower()

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

    def concatStringsRandomNumbers(self, sequence, start, stop):
        for mystr in sequence:
            for num in range(start, stop):
                yield mystr + str(num)

    def print_to_file(self, file_name, combinations):
        output_file = open(file_name, "w")
        for k in combinations:
            # output_file.writelines(combinations[k])
            for v in combinations[k]:
                try:
                    output_file.write(v + "\n")
                except:
                    pass
        print(f"File Name Is {file_name}\n\n")
        output_file.close()
        # print(combinations)

    def generate_wordlist(self):
        print("[+] Generating Dictionary - ")

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

        # Birthdays combinations 
        birthday_combination = [
            birthdate_yyyy,
            birthdate_dd,
            birthdate_mm,
        ]

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

        name_combination = [
            self.profile["name"],
            self.profile["surname"],
            self.profile["nickname"],
            nameUP,
            surnameUP,
            nicknameUP,
        ]

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

        tot_combinations = {}
        tot_combinations[1] = list(
            self.combine(name_combinations, birthday_combinations)
        )
        tot_combinations[2] = list(self.combine(name_combinations, birthday_combinations, self.profile["special_char"]))
        tot_combinations[3] = list(self.combine(word, birthday_combinations))
        tot_combinations[4] = list(self.combine(word, birthday_combinations, self.profile["special_char"]))
        if self.profile["random_num"] == "y":
            numfrom = 0
            numto = 1000
            tot_combinations[5] = list(
                self.concatStringsRandomNumbers(word, numfrom, numto)
            )
            tot_combinations[6] = list(
                self.concatStringsRandomNumbers(name_combinations, numfrom, numto)
            )
            tot_combinations[7] = list(
                self.concatStringsRandomNumbers(combination_pet_college, numfrom, numto)
            )
            tot_combinations[8] = list(
                self.concatStringsRandomNumbers(reverse_n, numfrom, numto)
            )
        tot_combinations[9] = list(self.combine(reverse_n, birthday_combinations))
        tot_combinations[10] = list(self.combine(reverse_n, birthday_combinations, self.profile["special_char"]))
        if len(self.profile["special_char"]) > 0:
            tot_combinations[11] = list(
                self.combine(name_combinations, self.profile["special_char"])
            )
            tot_combinations[12] = list(
                self.combine(combination_pet_college, self.profile["special_char"])
            )
            tot_combinations[13] = list(
                self.combine(word, self.profile["special_char"])
            )
            tot_combinations[14] = list(
                self.combine(reverse_n, self.profile["special_char"])
            )

        self.print_to_file(self.profile["name"] + ".txt", tot_combinations)


# person1 = Profile()
# person1.details()
# person1.generate_wordlist()
