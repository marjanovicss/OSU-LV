import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 3, 2, 1])
y = np.array([1, 1, 2, 2, 1])

style = dict(
    color = "red",
    marker = "o",
    markersize = 4,
    linestyle = "dashdot",
    markerfacecolor = "black",
    markeredgecolor = "black",
    linewidth = 1,
)

plt.plot(x,y, **style)
plt.axis([0, 4, 0, 4])
plt.title("Primjer")
plt.xlabel("x os")
plt.ylabel("y os")
plt.show()