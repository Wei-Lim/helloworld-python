import matplotlib.pyplot as plt
import sys
import numpy as np


print(sys.prefix)

msg = "Hello World!"
print(msg)

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot

type(x)