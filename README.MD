# Phantasy Star Online episode I&II: Section_id_calculator

When creating a new character a section Id will be calculated based on UNICODE/ASCII code alphanumeric transoformations
This calculator allows you to input a name and returns the Section ID the name will generate. 
It is intended for use as a quality of life tool.

## Usage
Clone the repository to a directory and within the same directory run the following command in your terminal:

./sec_id

Methodology:
# Feature List

- [x]  Asks for Input name
- [x]  Calculates section id based on name input
- [x]  Returns section id
- [x]  Simple Calculator Program

Calculations are based on blueprints found in the GAMEFAQ guide written by SuperSteve<sup>1</sup>

- Character name is turned into ASCII code values
- Code values are summed
- The last digit in the sum is used to index a 'section id: value' dictionary

## References
1. https://gamefaqs.gamespot.com/dreamcast/198288-phantasy-star-online/faqs/12520
