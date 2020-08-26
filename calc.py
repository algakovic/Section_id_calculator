#!/usr/bin/env python
# A simple section Id calculator for Phantasy Star Online

import sys

name = input('Please provide a character name: ')
if len(name) > 12:
    print("Error! Only 12 characters allowed!")
    sys.exit()

ASCII_codes = [ord(i) for i in list(name)]

sum_codes = 0
for code in ASCII_codes:
    sum_codes += code

ref = int(str(sum_codes)[-1])

id_dict = {
0: 'VIRIDIA',
1: 'GREENILL',
2: 'SKYLY',
3: 'BLUEFULL',
4: 'PURPLENUM',
5: 'PINKAL',
6: 'REDRIA',
7: 'ORAN',
8: 'YELLOWBOZE',
9: 'WHITILL'
}

print(id_dict[ref])



'''
- Characters names can only be 12 characters in length including spaces 
- There are 95 Characters available on the system
X Characters need to be represented by their ASCII code
X ASCII codes must be summed
- One's digit must reference a dictionary of Section_id values
'''
