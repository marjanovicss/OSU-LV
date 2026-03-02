import numpy as np
import matplotlib.pyplot as plt

Crna = np.zeros((50, 50))
Bijela = np.ones((50, 50))

CrnoBijela = np.hstack([Crna, Bijela])
BijelaCrna = np.hstack([Bijela, Crna])
Komplet = np.vstack([CrnoBijela, BijelaCrna])
plt.imshow(Komplet, cmap = "gray")
plt.show()