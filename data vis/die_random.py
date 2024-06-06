from random import randint
class Die :
    def __init__(self,die_sides = 6):
        self.die_side = die_sides
    def roll_dice(self):
        return randint(1,self.die_side)
    