from random import random, randint, choice ,choices
class Die:
    def __init__(self):
        self.sides = 6
    def roll_dice(self):
        self.sides = randint(1,6)
        print(self.sides)
    def roll_dice_10(self):
        self.sides = randint(1,10)
        print(self.sides)
    def roll_dice_20(self):
        self.sides = randint(1,20)
        print(self.sides)
get_die = Die()
get_die.roll_dice()
get_die.roll_dice_10()
get_die.roll_dice_20()

#  Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select 4 numbers or letters from the list and print a message saying that
# any ticket matching these 4 numbers or letters wins a prize

Lottery = (88,47,53,96,74,25,16,51,66,32,'i','t','s','p','m')
win = []



ticket = []

active = True
while active:
    for i in range(0,4):
        get_win  = choice(Lottery)
        win.append(get_win)

    print(win)
    for n in range(0,4):
        get_ticket = choice(Lottery)
        ticket.append(get_ticket)
    print(ticket)

    if get_win == get_ticket :
        active = False
        print("The winner has been found")