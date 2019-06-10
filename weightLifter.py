import random

class WeightLifter:
    def __init__(self, name, strength, skill, luck):
        self.name = name
        self.strength = strength
        self.skill = skill
        self.luck = luck

    def calculateLifts(self):
        self.snatch = self.strength * self.skill
        self.clean_and_jerk = (self.strength * self.skill) * 1.3
        return(self.snatch, self.clean_and_jerk)
            
competitor_amount = 5
competitors = {}
for x in range(competitor_amount):
    skill = random.randint(1,11)
    strength = random.randint(1,11)
    luck = 1

    lifter = WeightLifter("Lifter " + str(x), strength, skill, luck)
    lifter.calculateLifts()
    competitors[lifter.name] = lifter.snatch

winner = max(competitors, key=competitors.get)
print("The winner of the snatch is " + winner + " with an " + str(competitors[winner]) + "kg lift!")


