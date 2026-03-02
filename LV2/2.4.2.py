import numpy as np
import matplotlib.pyplot as plt

def DohvatiBrojOsoba(podatci):
    print(f"{len(podatci)}")

def DohvatiOdnosVisineiMase(podatci):
    Masa = podatci[:, 2]
    Visina = podatci[:, 1]
    plt.scatter(Masa, Visina, alpha = 0.5)
    plt.show()

def DohvatiOdnosVisineiMaseZaSvakuPedesetuOsobu(podatci):
    Masa = podatci[::50, 2]
    Visina = podatci[::50, 1]
    plt.scatter(Masa, Visina, alpha = 0.5)
    plt.show()

def DohvatiMinMaxAvgVisinu(podatci):
    Visina = podatci[:, 1]
    print(f"Min:{np.min(Visina)} Max:{np.max(Visina)} Avg:{np.mean(Visina)}")

def DohvatiMinMaxAvgVisinuMZ(podatci):
    Muskarci = (podatci[:, 0] == 1)
    Zene = (podatci[:, 0] == 0)
    print(f"Muskarci: Min:{np.min(podatci[Muskarci, 1])} Max:{np.max(podatci[Muskarci, 1])} Avg:{np.mean(podatci[Muskarci, 1])}")
    print(f"Zene: Min:{np.min(podatci[Zene, 1])} Max:{np.max(podatci[Zene, 1])} Avg:{np.mean(podatci[Zene, 1])}")

podatci = np.loadtxt("data.csv", delimiter=",", skiprows= 1)
DohvatiBrojOsoba(podatci)
DohvatiOdnosVisineiMase(podatci)
DohvatiOdnosVisineiMaseZaSvakuPedesetuOsobu(podatci)
DohvatiMinMaxAvgVisinu(podatci)
DohvatiMinMaxAvgVisinuMZ(podatci)