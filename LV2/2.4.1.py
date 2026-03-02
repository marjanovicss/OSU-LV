import numpy as np
import matplotlib.pyplot as plt

style = dict(
    color = "red",
    marker = "o",
    markersize = 4,
    linestyle = "dashdot",
    markerfacecolor = "black",
    markeredgecolor = "grey",
    linewidth = 1,
)

x_os = np.array([1, 3, 3, 2, 1])
y_os = np.array([1, 1, 2, 2, 1])
plt.plot(x_os, y_os, **style)
plt.axis([0, 4, 0, 4])
plt.xlabel("x os")
plt.ylabel("y os")
plt.title("Primjer")
plt.show()