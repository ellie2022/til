# nested loop

for x in range(4):
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
