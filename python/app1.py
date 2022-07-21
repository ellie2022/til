# nested loop
"""for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

#my solution
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    stritem = ''
    while item > 0:
        stritem += 'x'
        item -= 1
    else:
        print(stritem)

#teacher's solution
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
"""
import utils
import converters
#from utils import find_max  <---- to import functions explicitly
numbers = [4,5,6,2,64,32,-2]
max_number = utils.find_max(numbers)
print(max_number)

kg = input("kg? ")
print(f'{kg}kg is {converters.kg_to_lbs(kg)} lbs')

lbs = input("lbs? ")
print(f'{lbs}lbs is {converters.lbs_to_kg(lbs)} kg')