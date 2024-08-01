import os
import colorama
from colorama import Fore, Style, init
from click import pause

RED = Fore.LIGHTRED_EX + Style.BRIGHT
GREEN = Fore.LIGHTGREEN_EX + Style.BRIGHT
BLUE = Fore.LIGHTCYAN_EX + Style.BRIGHT
WHITE = Fore.LIGHTWHITE_EX + Style.BRIGHT
RESET = Style.RESET_ALL

def rot_cipher(text, key): # ROT Cyphering Function
    encoded_text = []
    for char in text:
        if char.isalpha():
            shift = key % 26  # Ensures the shift wraps around the alphabet
            if char.islower():
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encoded_text.append(encoded_char)
        else:
            encoded_text.append(char)  # Non-alphabetic characters are not changed
    return ''.join(encoded_text)

def rot_decipher(text, key): # ROT Decyphering Function
    return rot_cipher(text, -key)


def main(): # Main Function
    print(f'''{WHITE}
=======================================
||       {GREEN}ROT Encoder/Decoder{WHITE}         ||
=======================================
{RESET}''')
    
    while True:
        operation = input(f"{WHITE}[{GREEN}>{WHITE}] Enter {RED}'e'{WHITE} to encode or {BLUE}'d'{WHITE} to decode:{GREEN} ").lower()
        RESET
        if operation in ['e', 'd']:
            break
        else:
            print(f"\n{WHITE}[{RED}!{WHITE}] Invalid input. Please enter {RED}'e'{WHITE} to encode or {BLUE}'d'{WHITE} to decode.{RESET}")

    text = input(f"\n{WHITE}[{GREEN}>{WHITE}] Enter the text:{GREEN} ")
    RESET
    while True:
        try:
            key = int(input(f"\n{WHITE}[{GREEN}>{WHITE}] Enter the key (an integer):{GREEN} "))
            RESET
            break
        except ValueError:
            print(f"\n{WHITE}[{RED}!{WHITE}] Please enter a valid integer.{RESET}")

    if operation == 'e':
        result = rot_cipher(text, key)
        print(f"\n{WHITE}[{GREEN}>{WHITE}] Encoded text:{BLUE}", result)
        RESET
    else:
        result = rot_decipher(text, key)
        print(f"\n{WHITE}[{GREEN}>{WHITE}] Decoded text:{BLUE}", result)
        RESET

if __name__ == "__main__":
    import os; os.system('cls' if os.name == 'nt' else 'clear')
    main()
    pause('\n')
    RESET
