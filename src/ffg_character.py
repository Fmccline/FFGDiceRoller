from dice import Dice


class FFGCharacter:

    def __init__(self, name):
        self.name = name
        self.dice = Dice.make_dice()
        self.available_dice = {
            Dice.GREEN: 0,
            Dice.YELLOW: 0,
            Dice.BLUE: 0,
            Dice.PURPLE: 0,
            Dice.RED: 0,
            Dice.BLACK: 0
        }
    
    def set_dice(self, dice_type, amount):
        self.available_dice[dice_type] = amount

    def set_name(self, name):
        self.name = name

    def get_dice(self, dice_type):
        return self.available_dice.get(dice_type)