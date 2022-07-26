#several ways to import packages :
#import ecommerce.shipping
#ecommerce.shipping.calc_shipping()

#from ecommerce.shipping import calc_shipping
#calc_shipping()

#from ecommerce import shipping
#ecommerce.shipping.calc_shipping()  NameError!
#shipping.calc_shipping()

#generating random values (search 'python 3 module index')
"""import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Ellie', 'Taylor', 'Linzi']
leader = random.choice(members)
print(leader)
"""
import random


class Dice:

    """def roll(self):
        numbers = (1, 2, 3, 4, 5, 6)
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        return num1, num2
    """
    # teacher's solution
    """def roll(self):
        first = random.randint(1, 6) #randint는 a,b를 포함해서, randrange는 b는제외
        second = random.randint(1, 6)
        return first, second
    """
    # enhanced exercise
    def __init__(self, turns):
        self.turns = turns

    def roll(self):
        values = []
        for i in range(self.turns):
            values.append(random.randint(1, 6))
        return values

    def roll_(self, initval):
        values = [initval for i in range(self.turns)]
        for i in range(self.turns):
            values[i] = random.randint(1, 6)
        return values



play = Dice(5)
print(play.roll())

print(play.roll_(0))