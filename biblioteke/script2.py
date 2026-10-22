import pandas as pd
import numpy as np   

np.random.seed(42)

radnici = ["Damjan","Vladan","Nikola","Nebojsa","Slavko","Matija","Stefan","Aleksa"]

sektori = ["IT","HR","IT","Sales","Sales","HR","IT","Sales"]
plate = np.random.randint(800,2500,size = 8)
staz_godine = np.random.randint(1,15,size = 8)

df_zaposleni = pd.DataFrame({
    "Radnik": radnici,
    "Sektor": sektori,
    "Plata": plate,
    "Staz": staz_godine
})
print("\n=== POCETNI DATAFRAME ZAPOSLENIH ===")
print(df_zaposleni)

agregacija_sektora = df_zaposleni.groupby("Sektor").agg(
    {
        "Plata": [np.mean,np.median,np.std],
        "Staz": [np.max,np.min]
    }
)
print("\n=== ANALIZA PO SEKTORIMA ===")
print(agregacija_sektora.round(2))

# ZADATAK

agregacija_sektora2 = df_zaposleni.groupby("Sektor").agg(
    {
        "Plata": [np.sum, "count"]
    }
)
print("\n=== ZADATAK ===")
print(agregacija_sektora2)

budzet_plata = df_zaposleni["Plata"].sum()
agregacija_sektora2["Udio_Sektora_%"] = (
    agregacija_sektora2[("Plata","sum")] / budzet_plata
) * 100
print(agregacija_sektora2.round(2))