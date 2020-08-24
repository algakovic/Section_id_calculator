#!/usr/bin/env python
# This is a Section_ID Calculator for Gamecube Phantasy Star Online Character Names

name = input("Provide a name: ") # Ask for name input

ASCII_values = [ord(i) for i in list(name)] # Obtain ASCII values for each character in name

result = 0
for i in ASCII_values:
    result += i

print(result)


'''
Calculation:
X For loop over the list
X Convert each iterable in list to ASCII
X Sum ASCII conversion
- Retreive the ones digit from the resulting sum

Show Result:
- Reference an Index to return complimentary Section_ID
'''

section_id_dict = {
0: 'Viridia',
1: 'Greenill',
2: 'Skyly',
3: 'Bluefull',
4: 'Purplenum',
5: 'Pinkal',
6: 'Redria',
7: 'Oran',
8: 'Yellowboze',
9: 'Whitill'
}

