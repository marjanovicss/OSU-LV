import pandas as pd

data = pd.read_csv("data_C02_emission.csv")

'''
A
'''
print(f"DataFrame sadrži {len(data)} mjerenja.\n")
print(f"Tipovi podataka: {data.dtypes}.\n")
print(f"Izostale vrijednosti: {data.isnull().sum()}.\n")
print(f"Duplicirane vrijednosti: {data.duplicated().sum()}.\n")
bez_izostalih_vrijednosti = data.dropna()
bez_dupliciranih_vrijednosti = data.drop_duplicates()
#print(bez_izostalih_vrijednosti)
#print(bez_dupliciranih_vrijednosti)
data["Make"] = data["Make"].astype("category")
data["Model"] = data["Model"].astype("category")
data["Vehicle Class"] = data["Vehicle Class"].astype("category")
data["Transmission"] = data["Transmission"].astype("category")
data["Fuel Type"] = data["Fuel Type"].astype("category")
print(data.info())
'''
A
'''

'''
B
'''
largest = data.sort_values(by = "Fuel Consumption City (L/100km)",ascending = False ).head(3)
smallest = data.sort_values(by = "Fuel Consumption City (L/100km)",ascending = False ).tail(3)
print(largest[["Make", "Model", "Fuel Consumption City (L/100km)"]])
print(smallest[["Make", "Model", "Fuel Consumption City (L/100km)"]])
'''
B
'''

'''
C
'''
motor = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
print('Broj vozila koji imaju velicinu motora izmedu 2.5 i 3.5 L',len(motor))
print('Prosjecna CO2 emisija: ', round(motor['CO2 Emissions (g/km)'].mean(), 2))
'''
C
'''
motor = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
print('Broj vozila koji imaju velicinu motora izmedu 2.5 i 3.5 L',len(motor))
print('Prosjecna CO2 emisija: ', round(motor['CO2 Emissions (g/km)'].mean(), 2))
'''
C
'''

'''
D
'''
audi = data[data['Make']== 'Audi']
print('Audi mjerenja: ',len(audi))
audi_cylinders = audi[audi['Cylinders'] == 4]
print('Prosjecna CO2 emisija audia: ', round(audi_cylinders['CO2 Emissions (g/km)'].mean(), 2))
'''
D
'''

'''
E
'''
print(data.groupby('Cylinders').size())
print(round(data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean(), 2))
'''
E
'''
'''
F
'''
print('Dizel')
print(round(data[data["Fuel Type"] == "D"]["Fuel Consumption City (L/100km)"].mean(), 2))
print(round(data[data["Fuel Type"] == "D"]["Fuel Consumption City (L/100km)"].median(), 2))
print('Benzin')
print(round(data[data["Fuel Type"] == "X"]["Fuel Consumption City (L/100km)"].mean(), 2))
print(round(data[data["Fuel Type"] == "X"]["Fuel Consumption City (L/100km)"].median(), 2))
'''
F
'''
'''
G
'''
max_diesel_car = (data[(data["Fuel Type"] == "D") & (data["Cylinders"] == 4)]).sort_values(
by="Fuel Consumption City (L/100km)",
ascending=False).head(1)
print(max_diesel_car[["Make","Model","Fuel Consumption City (L/100km)"]])
'''
G
'''
'''
H
'''
manual = data[data["Transmission"].str.startswith("M")]
print('Broj auta s rucnim mjenjacem: ',len(manual))
'''
H
'''
'''
I
'''
corr = data.corr(numeric_only= True)
print(corr)
'''
I
'''