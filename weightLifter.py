import random

class WeightLifter:
    def __init__(self, name):
        self.name = name
        self.bodyweight = round(random.uniform(50, 150), 2)
        
    def calculateLifts(self):
        self.snatch_max = round((1.067 * self.bodyweight) + 34.920, 0)
        self.clean_and_jerk_max = round((1.28 * self.bodyweight) + 40.63, 0)
        return(self.snatch_max, self.clean_and_jerk_max)

lifters = []

w1 = WeightLifter("Luke") 
w1.calculateLifts()
lifters.append(w1)
print(w1.name)
print("{}{}{}".format("Bodyweight: ", int(w1.bodyweight), "kg"))
print("{}{}{}".format("Snatch: ", int(w1.snatch_max), "kg"))
print("{}{}{}".format("Clean and Jerk: ", int(w1.clean_and_jerk_max), "kg"))

def attempt_func():
    remaining = 3
    successes = []
    fails = []
    while remaining > 0:
        att = int(input("What is att? "))
        print(att)
        factor = round(random.uniform(0,1), 2)
        if factor > 0.5:
            print("Good lift")
            successes.append(att)
            remaining = remaining - 1
        else:
            print("No lift")
            fails.append(att)
            remaining = remaining - 1
    print("SUCCESSES", successes)
    print("FAILS", fails)

for x in lifters:
    attempt_func()

        





