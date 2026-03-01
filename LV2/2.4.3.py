import numpy as np
import matplotlib.pyplot as plt

def ProsvijetliSliku(slika):
    plt.figure()
    plt.imshow(slika, cmap = "grey", alpha = 0.5)
    plt.show()

def PrikazDrugeCetvrtinePoDuzini(slika):
    CetvrtinaSlike = slika[:, slika.shape[1] // 4 : slika.shape[1] // 2]
    plt.imshow(CetvrtinaSlike, cmap='gray')
    plt.show()

def ZarotirajSliku(slika):
    ZarotiranaSlika = np.rot90(slika, k = 3)
    plt.figure()
    plt.imshow(ZarotiranaSlika, cmap = "grey")
    plt.show()

def ZrcaliSliku(slika):
    ZrcalnaSlika = np.fliplr(slika)
    plt.figure()
    plt.imshow(ZrcalnaSlika, cmap = "grey")
    plt.show()

slika = plt.imread("road.jpg")
print("Napišite \"a\" za prosvjetljivanje slike.")
print("Napišite \"b\" za prikaz samo druge četvrtine slike po dužini.")
print("Napišite \"c\" za rotiranje slike za 90° u smjeru kazaljke na satu.")
print("Napišite \"d\" za zrcalnu sliku.")

while True:
    KorisnickiUnos = input()
    if KorisnickiUnos == "a":
        ProsvijetliSliku(slika)
    elif KorisnickiUnos == "b":
        PrikazDrugeCetvrtinePoDuzini(slika)
    elif KorisnickiUnos == "c":
        ZarotirajSliku(slika)
    elif KorisnickiUnos == "d":
        ZrcaliSliku(slika)
    else:
        break