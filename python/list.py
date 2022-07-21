
"""names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[:])

#exercise : to find the largest number in a list
numbers = [3,6,34,13,53,51,426,36, -32, 2]
largest_number = numbers[0];
for item in numbers:
    if item > largest_number:
        largest_number = item
print(largest_number)
"""
#2D list
"""
[
    1 2 3
    4 5 6
    7 8 9
]
"""
"""matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for item in row:
        print(item)
print(matrix[0][2])
#methods
numbers = [5, 2, 1, 7, 4, 5]
print(numbers)
numbers.append(20)
print(numbers)
numbers.insert(3, 10)
print(numbers)
numbers.remove(5)
print(numbers)
print(numbers.index(4))
is_exist = 50 in numbers
print(is_exist)
numbers2 = numbers.copy()
"""
#exercise : to remove the duplicateds in a list
our_list = [4, 5, 6, 'tammy', 'sarah', 5, 6, 7, 5, 'tammy']
print(our_list)
unique_list = []
for item in our_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
