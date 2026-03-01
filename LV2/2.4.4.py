import numpy as np
import matplotlib.pyplot as plt

Crna = np.ones((50, 50))
Bijela = np.zeros((50, 50))

CrnaBijela = np.hstack((Bijela, Crna))
BijelaCrna = np.hstack((Crna, Bijela))

Zajedno = np.vstack((CrnaBijela, BijelaCrna))
plt.imshow(Zajedno, cmap = "grey")
plt.show()

