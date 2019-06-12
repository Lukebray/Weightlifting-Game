import random

class WeightLifter:
    def __init__(self, name):
        self.name = name
        self.bodyweight = round(random.uniform(50, 150), 2)
        
    def calculateLifts(self):
        self.snatch_max = round((1.067 * self.bodyweight) + 34.920, 0)
        self.clean_and_jerk_max = round((1.28 * self.bodyweight) + 40.63, 0)
        return(self.snatch_max, self.clean_and_jerk_max)


class Attempt:
    def __init__(self, weight):
        self.weight = weight

    def pass_or_fail(self):
        factor = round(random.uniform(0,1), 2)
        self.status = False
        if factor > 0.5:
            self.status = True
        else:
            self.status = False
        return(self.status)



w1 = WeightLifter("Luke") 
w1.calculateLifts()
print(w1.name)
print("{}{}{}".format("Bodyweight: ", int(w1.bodyweight), "kg"))
print("{}{}{}".format("Snatch: ", int(w1.snatch_max), "kg"))
print("{}{}{}".format("Clean and Jerk: ", int(w1.clean_and_jerk_max), "kg"))

a1 = Attempt(50)
print(a1.pass_or_fail())



