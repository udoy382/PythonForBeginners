import random

# for i in range(3):
    # print(random.random())
    # print(random.randint(10, 20))


# members = ["Maryam", "Fariha", "Mitu", "Amy", "Nadiya"]
# leader = random.choice(members)
# print(leader)

# Exerice Solutions

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())