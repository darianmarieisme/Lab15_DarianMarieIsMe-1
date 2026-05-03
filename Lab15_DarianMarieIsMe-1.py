'''Lab 15 Programming Assignment Option 1
Darian Marie Bruce
This program uses a mathematical formula to plot data
05/03/2026
'''

import matplotlib.pyplot as plt
import math

x_values: list[float] = []
y_values: list[float] = []

for degree in range(0, 361):
    radians = math.radians(degree)
    x_values.append(degree)
    y_values.append(math.sin(radians))

plt.plot(x_values, y_values)

plt.title("Sine Wave")
plt.xlabel("Degrees")
plt.ylabel("sin(x)")

plt.grid(True)

plt.savefig("sine_wave.png")
plt.show()