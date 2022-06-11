import random
def rand_walk():
    walk = 0
    for i in range(2500):
        rand = random.randint(0, 1)
        if (rand == 0):
            walk = walk + 1
        else:
            walk = walk - 1
    return walk


absolute = 0.0
numtrial = 1

for j in range(numtrial):
    walk = rand_walk()
    absolute = absolute + (walk**2)**(1 / 2.0)

print("Average Absolute Distance ", absolute / numtrial)
