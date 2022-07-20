"""
age = 20
price = 19.95
name = input("What is your name? ")
birth_year = input("Enter your birth year : ")
age = 2022 - int(birth_year)
is_new = False
print("Your age is " + str(age)) # str를 넣지 않으면 에러발생함!
print("Hello, " + name + " !")
print(is_new)
"""
"""
print("Addition")
first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum: " + str(sum))
"""
"""
course = "Python for Beginners"
#print(course.upper()) # course의 값이 바뀌는 것은 아님
#print(course.find('Y')) #인덱스값을 리턴하고, 없으면 -1리턴
print(course.replace('for', '4')) #여기서도 실제 course의 값은 그대로임. string immutable
print(course)

print('Python' in course)
print('java' in course)

result = 10/3
result = 10//3
print(result)
"""
"""
weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == 'L':
    converted = weight *  0.453592
    print("Weight in Kg: " + str(converted))
else:
    converted = weight / 0.453592
    print(("Weight in Lbs: " + str(converted)))
"""
"""
i = 1
while i <= 1_0: #오호! 신기하네
    print(i * '*')
    i += 1
"""
"""
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
numbers.append("7" '8')
numbers.append("num7")
numbers.append(78)
print(numbers)
print('78' in numbers)
print(len(numbers))
"""
"""
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)
"""
"""
#numbers = range(5, 10, 2)
for number in range(5,10):
    print(number)
"""
"""name = input("Name: ")
name_len = len(name)
print("Name len: " + str(name_len))
if (name_len < 3):
    print("Name must be at least 3 characters.")
elif (name_len > 50):
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")
"""
"""
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input("Guess: ")
    if (int(guess) != secret_number):
        guess_count += 1
    else:
        break
else:
    print("Sorry, you failed!")
"""
# Checkup test program
command_prompt = '>'
command = ''
car_started = False
while command != 'quit':
    command = input(command_prompt)
    command = command.lower()
    if (command == 'help'):
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit program")
        # 이 부분은 멀티라인 방식으로 바꿀수 있음
    elif (command == 'start'):
        if car_started:
            print("Car is already started..")
        else:
            print("Car started.. Ready to go!")
            car_started = True
    elif (command == 'stop'):
        if car_started:
            print("Car stopped")
            car_started = False
        else:
            print("Car is already stopped")
    elif (command == 'quit'):
        print("Exiting..")
    else:
        print("I don't understand that...")
