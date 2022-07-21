"""class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")

    def move(self):
        print("move")


point1 = Point(10, 20)
point1.move()
#point1.x = 10
#point1.y = 20
print(f'x: {point1.x}, y: {point1.y}')

point2 = Point(30, 40)
point2.draw()
point2.x = 50
print(point2.x)
print(point2.y)
"""
#exercise
"""class Person:
    def __init__(self, name, talkative):
        self.name = name
        self.is_talkative = talkative

    def talk(self):
        print(f"{self.name} is talking...")


person1 = Person("Jane", True)
print(person1.name)
print(f'is talkative? : {person1.is_talkative}')
person1.talk()

person2 = Person("Bob", False)
person2.talk()
"""

#inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.be_annoying()