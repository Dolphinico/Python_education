from random import randint

class Die():
    """Простая модель игральной кости"""
    def __init__(self, side):
        """Инициирует атрибуты класса"""
        self.side = 6
    def roll_die(self):
        """Кидает кость"""
        x = randint(1, 6)
        print(x)

dice = Die("")
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()

