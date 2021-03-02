from random import randint

class Die():
    """Простая модель игральной кости"""
    def __init__(self, sides=6):
        """Инициирует атрибуты класса"""
        self.sides = sides
    def roll_die(self):
        """Кидает кость"""
        return randint(1, self.sides)
        
# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
# Make a 6-sided die, and show the results of 10 rolls.
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)