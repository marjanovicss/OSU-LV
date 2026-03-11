import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("LV3/data_C02_emission.csv")

fig, axs = plt.subplots(3, 2, figsize=(12, 12))

"""
Pomocu histograma prikažite emisiju C02 plinova. Komentirajte dobiveni prikaz.
"""
data["CO2 Emissions (g/km)"].plot(kind="hist", ax=axs[0,0])
axs[0,0].set_xlabel("CO2 Emissions")
axs[0,0].set_ylabel("Broj vozila")

# Velika vecina vozila spada u emisiju C02 plinova izmedju 200 i 300 g/km

"""
Pomocu dijagrama raspršenja prikažite odnos izmedu gradske potrošnje goriva i emisije
C02 plinova. Komentirajte dobiveni prikaz. Kako biste bolje razumjeli odnose izmedu
velicina, obojite tockice na dijagramu raspršenja s obzirom na tip goriva.
"""
colors = {"X" : "blue", "Z" : "red", "D" : "green", "E" : "yellow", "N" : "black"}
data.plot.scatter(
x="Fuel Consumption City (L/100km)",
y="CO2 Emissions (g/km)",
c=data["Fuel Type"].map(colors),
ax=axs[0,1]
)

# Vidljiva linearna korelacija - sto je visa potrosnja goriva veca je i emisija CO2
# x - benzin - linearan odnos - srednja potrosnja
# z - premioum benzin - veca gradska potrosnja sugerira da su skuplji auti - zadnja tocka outlier je neki super auto...
# d - dizel - iako dizelasi trose manjeg litara vise emitiraju CO2 od benzinaca x
# e - etanol - dosta trose goriva ali imaju puno manju emisiju od ostalih

"""
Pomocu kutijastog dijagrama prikažite razdiobu izvangradske potrošnje s obzirom na tip
goriva. Primjecujete li grubu mjernu pogrešku u podacima?
"""
data.boxplot(
column="Fuel Consumption Hwy (L/100km)",
by="Fuel Type",
ax=axs[1,0]
)

# gruba mjerna pogreska se vidi kod z tipa goriva gdje jedna tockica znatno odskace od drugih ali s obzirom da je z gorivo to moze bit buggati koji trosi oko 30.3L/100km i koristi z

"""
Pomocu stupcastog dijagrama prikažite broj vozila po tipu goriva.
Koristite metodu groupby.
"""
data.groupby("Fuel Type").size().plot(kind="bar", ax=axs[1,1])

"""
Pomocu stupcastog grafa prikažite na istoj slici prosjecnu
C02 emisiju vozila s obzirom na broj cilindara
"""
data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean().plot(kind="bar", ax=axs[2,0])
axs[2,0].set_ylabel("CO2 emissions")



plt.tight_layout()
plt.show()