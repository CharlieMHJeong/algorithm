# Make a class Die with one attribute called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die(object):
    #initialize Dice
    def __init__(self, sides=6):
    #set dice sides
        self.sides = sides

    #roll the dice and display number between 1 - sides
    def roll_die(self):
        r = randint(1, self.sides)
        return r

    def nroll_dice(self, n):
    #Roll the dice n times
        l = []
        d = Die(self.sides)
        for i in range(n):
            l.append(d.roll_die())
        return l


d6 = Die(6)
r6 = d6.nroll_dice(10)
print(r6)

d10 = Die(10)
r10 = d10.nroll_dice(15)
print(r10)

d20 = Die(20)
r20 = d20.nroll_dice(10)
print(r20)
