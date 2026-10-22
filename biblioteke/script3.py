import pandas as pd 
import numpy as np  

# Tabela radnika i sektora u kojima rade
df_radnici = pd.DataFrame({
    "Radnik_ID": [101,102,103,104,105],
    "Ime": ["Damjan","Vladan","Slavko","Nikola","Petar"],
    "Sektor": ["IT","HR","IT","Sales","Sales"],
    "Plata": [1800,1200,2100,1500,1600]
})

# Druga tabela,informacije o sektorima (budzet i bonusi)
df_sektori_info = pd.DataFrame({
    "Sektor": ["IT","Sales","Marketing"],
    "Bonus_%": [15,10,20],
    "Grad": ["Beograd","Novi Sad","Nis"]
})

print("\n=== RADNICI ===")
print(df_radnici)
print("\n=== SEKTORI INFO ===")
print(df_sektori_info)

# Spajanje tabela pomocu LEFT JOIN-a
df_spojeno = pd.merge(df_radnici,df_sektori_info,on="Sektor",how="left")
print("\n=== SPOJENI DATAFRAME LEFT JOIN-om")
print(df_spojeno)

# ZADATAK
df_spojeno["Bonus_%"] = df_spojeno["Bonus_%"].fillna(0)
print("\n=== SA KOLONOM Bonus_% ===")
print(df_spojeno)

df_spojeno["Ukupna_Zarada"] = (
    df_spojeno["Plata"] + (df_spojeno["Plata"] * (df_spojeno["Bonus_%"] / 100))
)

print("\n=== SA KOLONOM Ukupna_Zarada ===")
print(df_spojeno)

filtrirana_tabela = df_spojeno[(df_spojeno["Ukupna_Zarada"] > 1700) & (df_spojeno["Grad"] =="Beograd")]
print("\n=== FILTRIRANA TABELA ===")
print(filtrirana_tabela)