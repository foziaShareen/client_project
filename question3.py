import numpy as np
import matplotlib.pyplot as plt
import random


def randomwalk1D(n):
    x, y = 0, 0

    # Generate the time points [1, 2, 3, ... , n]
    timepoints = np.arange(n + 1)
    positions = [y]

    directions = ["UP", "DOWN"]
    for i in range(1, n + 1):

        # Randomly select either UP or DOWN
        step = random.choice(directions)

        # Move the object up or down
        if step == "UP":
            y += 1
        elif step == "DOWN":
            y -= 1

        # Keep track of the positions
        positions.append(y)

    return timepoints, positions


rw1 = randomwalk1D(2500)
rw2 = randomwalk1D(2500)
rw3 = randomwalk1D(2500)
rw4 = randomwalk1D(2500)
rw5 = randomwalk1D(2500)

plt.plot(rw1[0], rw1[1], 'r-', label="rw1")
plt.plot(rw2[0], rw2[1], 'g-', label="rw2")
plt.plot(rw3[0], rw3[1], 'b-', label="rw3")
plt.plot(rw4[0], rw4[1], 'c-', label="rw4")
plt.plot(rw5[0], rw5[1], 'm-', label="rw5")


plt.show()