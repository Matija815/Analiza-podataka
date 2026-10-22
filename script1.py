import pandas as pd
import numpy as np  

# 1. Extraktujemo (ucitavamo) podatke za obradu
sirovi_podaci = [
    {"transakcija_id": 101, "korisnik": "Petar", "iznos": 150.0, "grad": "novi Sad"},
    {"transakcija_id": 102, "korisnik": "Matija", "iznos": np.nan, "grad": "novi Sad"},
    {"transakcija_id": 103, "korisnik": "Lana", "iznos": 180.0, "grad": "trebinje"},
    {"transakcija_id": 104, "korisnik": "Vladan", "iznos": 165.0, "grad": "trebinje"},
    {"transakcija_id": 105, "korisnik": "Slavko", "iznos": 120.0, "grad": "novi Sad"},
    {"transakcija_id": 106, "korisnik": "Petar", "iznos": 150.0, "grad": "novi Sad"}
]
#Pretvaramo u pandas dataframe

df = pd.DataFrame(sirovi_podaci)
print("--- SIROVI PODACI ---")
print(df)

# Transformacija (ciscenje i obrada)

#A) Uklanjanje duplikata
df = df.drop_duplicates(subset=["korisnik"], keep="first")

#B) Sredjivanje teksta (Standardizacija gradova na velika slova)
df["grad"] = df["grad"].str.title()

#C) Rijesavanje nedostajucih vrijednosti (popunjavamo prosjekom ili nulom)
prosjecan_iznos = df["iznos"].mean()
df["iznos"] = df["iznos"].fillna(prosjecan_iznos)

#D) Filtriranje losih podataka (iznos mora biti veci od 0)
df = df[df["iznos"] > 0]

print("\n--- OCISCENI PODACI ---")
print(df)
