import pandas as pd
import numpy as np

podaci = [
    {"porudzbina_id": 1, "kupac": " andrija ", "kategorija": "Tehnika", "cijena": 1200.0},
    {"porudzbina_id": 2, "kupac": "Milica", "kategorija": "Odjeca", "cijena": np.nan},
    {"porudzbina_id": 3, "kupac": "andrija", "kategorija": "Tehnika", "cijena": 1200.0},
    {"porudzbina_id": 4, "kupac": "STEFAN", "kategorija": "Knjige", "cijena": -300.0},
    {"porudzbina_id": 5, "kupac": "Milica", "kategorija": "Odjeca", "cijena": 2500.0}
]

df = pd.DataFrame(podaci)
print("=== PODACI ===")
print(df)

df["kupac"] = df["kupac"].str.strip()
df["kupac"] = df["kupac"].str.title()

df["cijena"] = df["cijena"].fillna(1000.0)
df = df[df["cijena"] >= 0]

df = df.drop_duplicates(subset=["kupac","kategorija","cijena"],keep="first")

print("\n=== OCISCENI PODACI ===")
print(df)

# groupby
izvjestaj = df.groupby("kupac")["cijena"].agg(["sum","count"])
print("\n=== IZVJESTAJ ===")
print(izvjestaj)