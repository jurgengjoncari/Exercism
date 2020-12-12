from string import ascii_uppercase
from random import randint, choices

class Robot:
    name_list = []
    def generate(self):
        self.name = ""
        the_letters = ""
        the_letters_list = choices(ascii_uppercase, k=2)
        for letter in the_letters_list:
            the_letters += letter
        the_number = randint(100, 999)
        self.name = the_letters + str(the_number)

    def reset(self):
        Robot.generate(self)
        if self.name in Robot.name_list:
            Robot.reset(self)
        print(self.name)        
        Robot.name_list.append(self.name)

    def __init__(self):
        Robot.reset(self)