import numpy as np
import matplotlib.pyplot as plt

def PosvijetliSliku(slika):
    plt.figure()
    plt.imshow(slika, cmap = "gray", alpha = 0.4)
    plt.show()

def DrugaCetvrtinaSlikePoSirini(slika):
    CetvrtinaSlike = slika[:, slika.shape[1] // 4 : slika.shape[1] // 2]
    plt.imshow(CetvrtinaSlike, cmap='gray')
    plt.show()

def ZarotirajZa90(slika):
    Zarotirana = np.rot90(slika, k = 3)
    plt.imshow(Zarotirana, cmap = "gray")
    plt.show()

def Zrcali(slika):
    Zrcaljena = np.fliplr(slika)
    plt.imshow(Zrcaljena, cmap = "gray")
    plt.show()

slika = plt.imread("road.jpg")
PosvijetliSliku(slika)
DrugaCetvrtinaSlikePoSirini(slika)
ZarotirajZa90(slika)
Zrcali(slika)