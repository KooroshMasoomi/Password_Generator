from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choices
from os import system
import sys

UPPERCASE = True

LOWERCASE = False

NUMBERS = True

SYMBOLS = False

letters = ""

if len(sys.argv) == 1:
    LENGTH = 10
elif len(sys.argv[1:]) == 1:
    if sys.argv[1].isdigit():
        LENGTH = int(sys.argv[1:][0])
    else:
        print("The input is not a number!")
elif len(sys.argv[1:]) > 1:
    print("The entry is more than one item!")

settings = {
    "UPPERCASE": ascii_uppercase if UPPERCASE else False,
    "LOWERCASE": ascii_lowercase if LOWERCASE else False,
    "NUMBERS": digits if NUMBERS else False,
    "SYMBOLS": punctuation if SYMBOLS else False,
}

if list(settings.values()).count(False) == 4:
    print("All settings options are disabled, cannot generate password!")
    system("pause")
    exit(1)
else:
    for option in settings.keys():
        if settings[option]:
            letters += settings[option]

result = "".join(choices(list(letters), k=LENGTH))
            
if __name__ == "__main__":
    print(result)
