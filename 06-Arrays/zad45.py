import matplotlib.pyplot as plt
import math

x = []
y = []

# create x values in degrees from 0 to 360
for angle in range(361):
    x.append(math.radians(angle))  # Convert degrees to radians for the sin function

# create y values using the sin function
for angle_rad in x:
    y.append(math.sin(angle_rad))

# display chart
plt.plot(x, y, label='y = sin(x)', color='blue')
plt.xlabel('Angle (radians)')
plt.ylabel('sin(x)')
plt.title('Graph of y = sin(x) for 0-360 degrees')

plt.show()
