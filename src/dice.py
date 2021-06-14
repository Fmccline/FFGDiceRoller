'''
Dice.py
By Frank Cline

Holds all the Dice classes
'''
import random


class Die:

    def __init__(self):
        # (successes/failures, advantages/threats, triumphs, despairs)
        self.dieSides = []

    def add_side(self, side):
        self.dieSides.append(side)

    def roll(self, num=1):
        # returns a tuple with Positive/Negative values.
        # (successes/failures, advantages/threats, triumphs, despairs)
        result = [0,0,0,0]
        for _ in range(num):
            side = random.choice(self.dieSides)
            result[0] += side[0]
            result[1] += side[1]
            result[2] += side[2]
            result[3] += side[3]
        return tuple(result)


class GreenDie:

    def __init__(self):
        die = Die()
        die.add_side((1,0,0,0))
        die.add_side((0,1,0,0))
        die.add_side((1,1,0,0))
        die.add_side((2,0,0,0))
        die.add_side((0,1,0,0))
        die.add_side((1,0,0,0))
        die.add_side((0,2,0,0))
        die.add_side((0,0,0,0))
        self.die = die

    def roll(self, num=1):
        return self.die.roll(num)


class YellowDie:

    def __init__(self):
        die = Die()
        die.add_side((0,2,0,0))
        die.add_side((0,1,0,0))
        die.add_side((0,2,0,0))
        die.add_side((0,0,1,0))
        die.add_side((1,0,0,0))
        die.add_side((1,1,0,0))
        die.add_side((1,0,0,0))
        die.add_side((1,1,0,0))
        die.add_side((2,0,0,0))
        die.add_side((1,1,0,0))
        die.add_side((2,0,0,0))
        die.add_side((0,0,0,0))
        self.die = die

    def roll(self, num=1):
        return self.die.roll(num)


class BlueDie:

    def __init__(self):
        die = Die()
        die.add_side((1,1,0,0))
        die.add_side((0,2,0,0))
        die.add_side((1,0,0,0))
        die.add_side((0,1,0,0))
        die.add_side((0,0,0,0))
        die.add_side((0,0,0,0))
        self.die = die
        
    def roll(self, num=1):
        return self.die.roll(num)


class PurpleDie:

    def __init__(self):
        die = Die()
        die.add_side((0,-1,0,0))
        die.add_side((-1,0,0,0))
        die.add_side((-1,-1,0,0))
        die.add_side((0,-1,0,0))
        die.add_side((0,-2,0,0))
        die.add_side((-2,0,0,0))
        die.add_side((0,-1,0,0))
        die.add_side((0,0,0,0))
        self.die = die

    def roll(self, num=1):
        return self.die.roll(num)


class RedDie:

    def __init__(self):
        die = Die()
        die.add_side((0,-2,0,0))
        die.add_side((0,-1,0,0))
        die.add_side((0,-2,0,0))
        die.add_side((0,-1,0,0))
        die.add_side((-1,-1,0,0))
        die.add_side((-1,0,0,0))
        die.add_side((-1,-1,0,0))
        die.add_side((-1,0,0,0))
        die.add_side((-2,0,0,0))
        die.add_side((0,0,0,1))
        die.add_side((-2,0,0,0))
        die.add_side((0,0,0,0))
        self.die = die
    
    def roll(self, num=1):
        return self.die.roll(num)


class BlackDie:

    def __init__(self):
        die = Die()
        die.add_side((0,0,0,0))
        die.add_side((0,0,0,0))
        die.add_side((0,-1,0,0))
        die.add_side((-1,0,0,0))
        die.add_side((0,-1,0,0))
        die.add_side((-1,0,0,0))
        self.die = die
    
    def roll(self, num=1):
        return self.die.roll(num)
        

class Dice:
    
    GREEN = 'Green'
    YELLOW = 'Yellow'
    BLUE = 'Blue'
    PURPLE = 'Purple'
    RED = 'Red'
    BLACK = 'Black'

    @staticmethod
    def make_dice():
        dice = {
            Dice.GREEN: GreenDie(),
            Dice.YELLOW: YellowDie(),
            Dice.BLUE: BlueDie(),
            Dice.PURPLE: PurpleDie(),
            Dice.RED: RedDie(),
            Dice.BLACK: BlackDie(),
        }
        return dice

    @staticmethod
    def dice_types():
        return [Dice.GREEN, Dice.YELLOW, Dice.BLUE, Dice.PURPLE, Dice.RED, Dice.BLACK]


if __name__ == '__main__':
    blue_die = BlueDie()
    print(blue_die.roll(3))
