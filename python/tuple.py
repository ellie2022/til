"""#tuple immutable
numbers = (1, 2, 3)
#numbers[0] = 10    error! 못바꿈
print(numbers[0])

#unpacking : tuple과 list에서 모두 사용가능함
coordinates = (1,2,3)
x,y,z = coordinates #x,y,z에 차례로 coordinates의 값이 담긴다.
print(f'{x}, {y}, {z}')

coord1 = [4,5,6]
x,y,z = coord1
print(f'{x}, {y}, {z}')

#Dictionaries {}를 사용함 - json?
#key:value pairs
#key should be unique
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified" : True
}
print(customer["name"])
print(customer.get("birthdate", "Jan 1 1980"))
print(customer)

customer["birthdate"] = "Jan 1, 1980"
print(customer)

number_text = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}
phone_number = input("Phone: ")
string_type = ""
for item in phone_number:
    string_type += number_text.get(item, "!") + ' '
print(string_type)
"""
#emojis
"""message = input("> ")
words = message.split(" ")
print(words)

emojis = {
    ":)": "😊",
    ":(": "😒",
    ";)": "😉",
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
"""
"""def greet_user(name):
    print(f'Hi {name} !')
    print('Welcom aboard')

print("Start")
greet_user("Jane")
greet_user("Mathew")
print("Finish")

def square(number):
    return number * number

print(square(3))
"""
#emojis in function
"""def redrawMessage(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😒",
        ";)": "😉",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("> ")
output = redrawMessage(message)
print(output)
"""

#exception handling
try:
    age = int(input("age: "))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("age cannot be 0")
except ValueError:
    print("Invalid value")