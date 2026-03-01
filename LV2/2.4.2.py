import numpy as np
import matplotlib.pyplot as plt

def DohvatiBrojOsoba(podatci):
    print(f"{len(podatci)}")

def PrikaziOdnosVisineiMase(podatci):
    Visina = podatci[:, 1]
    Masa = podatci[:, 2]
    plt.scatter(Visina, Masa, alpha = 0.5)
    plt.title("Odnos visine i mase")
    plt.xlabel("Visina")
    plt.ylabel("Masa")
    plt.show()

def DohvatiMjerenjeSvakePedeseteOsobe(podatci):
    Visina = podatci[1::50, 1]
    Masa = podatci[1::50, 2]
    plt.scatter(Visina,Masa, alpha=0.5)
    plt.title("Odnos visine i mase svake pedesete osobe")
    plt.xlabel("Visina")
    plt.ylabel("Masa")
    plt.show()

def DohvatiMinMaxAvgVisinu(podatci):
    Visina = podatci[:, 1]
    Masa = podatci[:, 2]
    print(f"Min:{Visina.min()} Max:{Visina.max()} Avg:{Visina.mean()}")

def DohvatiMinMaxAvgVisinuZaMuskarce(podatci):
    PodatciMuskarac = (podatci[:,0] == 1)
    print(f"Min:{podatci[PodatciMuskarac, 1].min()} Max:{podatci[PodatciMuskarac, 1].max()} Avg:{podatci[PodatciMuskarac, 1].mean()}")

def DohvatiMinMaxAvgVisinuZaZene(podatci):
    PodatciZene = (podatci[:,0] == 0)
    print(f"Min:{podatci[PodatciZene, 1].min()} Max:{podatci[PodatciZene, 1].max()} Avg:{podatci[PodatciZene, 1].mean()}")

podatci = np.loadtxt("data.csv", delimiter=",", skiprows = 1)
podatci = podatci[1::]
podatci = np.array(podatci, float)

print("Napišite \"a\" za broj osoba na kojim su isvršena mjerenja.")
print("Napišite \"b\" kako bi se prikazao odnos visine i mase.")
print("Napišite \"c\" kako bi se prikazalo mjerenje za svaku pedesetu osobu.")
print("Napišite \"d\" kako bi se prikazala minimalna, maksimalna te srednja vrijednost visine.")
print("Napišite \"e\" kako bi prikazali minimalnu, maksimalnu te srednju vrijednost visine za muškarce.")
print("Napišite \"f\" kako bi prikazali minimalnu, maksimalnu te srednju vrijednost visine za žene.")

while True:
    KorisnickiUnos = input()
    if KorisnickiUnos == "a":
        DohvatiBrojOsoba(podatci)
    elif KorisnickiUnos == "b":
        PrikaziOdnosVisineiMase(podatci)
    elif KorisnickiUnos == "c":
        DohvatiMjerenjeSvakePedeseteOsobe(podatci)
    elif KorisnickiUnos == "d":
        DohvatiMinMaxAvgVisinu(podatci)
    elif KorisnickiUnos == "e":
        DohvatiMinMaxAvgVisinuZaMuskarce(podatci)
    elif KorisnickiUnos == "f":
        DohvatiMinMaxAvgVisinuZaZene(podatci)    
    else:
        break