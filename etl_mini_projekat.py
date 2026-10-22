import pandas as pd
import numpy as np   

porudzbine = [
    {"porudzbina_id": 1, "kupac_id": 101, "grad": "  beograd ", "kolicina": 2, "cijena": 100.0},
    {"porudzbina_id": 2, "kupac_id": 102, "grad": "novi sad", "kolicina": np.nan, "cijena": 150.0},
    {"porudzbina_id": 3, "kupac_id": 101, "grad": "Beograd", "kolicina": 5, "cijena": 100.0},
    {"porudzbina_id": 4, "kupac_id": 103, "grad": " BEOGRAD ", "kolicina": 1, "cijena": 200.0},
    {"porudzbina_id": 5, "kupac_id": 102, "grad": "novi sad", "kolicina": 3, "cijena": 150.0}
]
df_porudzbine = pd.DataFrame(porudzbine)

kupci = [
    {"id_kupca": 101, "ime": "Ana", "status": "Premium"},
    {"id_kupca": 102, "ime": "Marko", "status": "Standard"},
    {"id_kupca": 103, "ime": "Ivana", "status": "Premium"}
]

df_kupci = pd.DataFrame(kupci)

# A)

df_porudzbine["grad"] = df_porudzbine["grad"].str.strip()
df_porudzbine["grad"] = df_porudzbine["grad"].str.title()
df_porudzbine["kolicina"] = df_porudzbine["kolicina"].fillna(1.0)
df_porudzbine["ukupno"] = df_porudzbine["kolicina"] * df_porudzbine["cijena"]
print(df_porudzbine)

# B)

df_spojeno = pd.merge(df_porudzbine,df_kupci,left_on="kupac_id",right_on="id_kupca",how="inner")
df_spojeno = df_spojeno.drop(columns=["kupac_id"])

# C)

izvjestaj = df_spojeno.groupby("status").agg(
    ukupna_zarada=("ukupno","sum"),
    broj_porudzbina=("porudzbina_id","count")
)
print(izvjestaj)

# D)

izvjestaj.to_csv("izvjestaj.csv", index=True, encoding="utf-8-sig", sep=";")

izvjestaj.to_excel("izvjestaj.xlsx", index=True, sheet_name="Izvjestaj_status")