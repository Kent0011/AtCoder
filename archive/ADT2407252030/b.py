import numpy as np
import math 
import sys

def encrypt(plain_text: str, shift_num: int) -> str:
    cipher = ""    
    for char in plain_text:
        if char.isupper():
            cipher += chr((ord(char) - 65 + shift_num) % 26 + 65)
        elif char.islower():
            cipher += chr((ord(char) - 97 + shift_num) % 26 + 97)

    return cipher


s = input()
t = input()

for i in range(27):
    if t== encrypt(s,i):
        print('Yes')
        sys.exit()
print('No')