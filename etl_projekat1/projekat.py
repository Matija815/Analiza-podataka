import pandas as pd  
import numpy as np

raw_transakcije = [
    {"transakcija_id": 101, "kupac_id": 1, "proizvod_id": 10, "kolicina": 3, "datum": "2026-01-01 10:00:00"},
    {"transakcija_id": 102, "kupac_id": 2, "proizvod_id": 20, "kolicina": np.nan, "datum": "2026-01-02 11:30:00"},
    {"transakcija_id": 103, "kupac_id": 1, "proizvod_id": 20, "kolicina": 2, "datum": "2026-01-03 15:45:00"},
    {"transakcija_id": 104, "kupac_id": 3, "proizvod_id": 10, "kolicina": 5, "datum": "2026-01-04 09:15:00"},
    {"transakcija_id": 105, "kupac_id": 2, "proizvod_id": 30, "kolicina": 1, "datum": "2026-01-05 14:20:00"}
]

raw_kupci = [
    {"id_kupca": 1, "ime": "ana ", "grad": " beograd "},
    {"id_kupca": 2, "ime": "marko", "grad": "novi sad"},
    {"id_kupca": 3, "ime": "IVANA", "grad": "BEOGRAD"}
]

raw_proizvodi = [
    {"id_proizvoda": 10, "naziv": "Tastatura", "cijena": 50.0},
    {"id_proizvoda": 20, "naziv": "Miš", "cijena": 25.0},
    {"id_proizvoda": 30, "naziv": "Monitor", "cijena": 200.0}
]

df_transakcije = pd.DataFrame(raw_transakcije)
df_kupci = pd.DataFrame(raw_kupci)
df_proizvodi = pd.DataFrame(raw_proizvodi)

# ZADATAK 1

df_transakcije["kolicina"] = df_transakcije["kolicina"].fillna(1.0)
df_kupci["ime"] = df_kupci["ime"].str.strip()
df_kupci["ime"] = df_kupci["ime"].str.title()
df_kupci["grad"] = df_kupci["grad"].str.strip()
df_kupci["grad"] = df_kupci["grad"].str.title()
df_transakcije["datum"] = pd.to_datetime(df_transakcije["datum"])
df_transakcije.dtypes
# Ako je datum u formatu %d/%m/%Y
print(df_transakcije)
print("\n==============================\n")

# ZADATAK 2

df_spajanje = pd.merge(df_transakcije,df_kupci,left_on="kupac_id",right_on="id_kupca",how="inner")
df_spajanje = df_spajanje.drop(columns=["id_kupca"])
df_spajanje_2 = pd.merge(df_spajanje,df_proizvodi,left_on="proizvod_id",right_on="id_proizvoda",how="inner")
df_spajanje_2 = df_spajanje_2.drop(columns=["id_proizvoda"])

# ZADATAK 3

df_spajanje_2["ukupno"] = df_spajanje_2["kolicina"] * df_spajanje_2["cijena"]

uslovi = [
    df_spajanje_2["ukupno"] >= 200,
    (df_spajanje_2["ukupno"] >= 100) & (df_spajanje_2["ukupno"] < 200),
    df_spajanje_2["ukupno"] < 100
]

vrijednosti = ["Visoka","Srednja","Niska"]
df_spajanje_2["kategorija_potrosnje"] = np.select(uslovi,vrijednosti,default="Niska")

# ZADATAK 4

df_spajanje_2 = df_spajanje_2.sort_values(by="datum",ascending=True)

df_spajanje_2["kumulativni_prihod"] = df_spajanje_2["ukupno"].cumsum()

# ZADATAK 5

izvjestaj = df_spajanje_2.groupby("grad").agg(
    ukupna_zarada=("ukupno","sum"),
    prosjecna_kolicina=("kolicina","mean"),
    broj_transakcija=("transakcija_id","count")
)

print(df_spajanje_2)
print("\n === IZVJESTAJ ===")
print(izvjestaj)

izvjestaj.to_csv("izvjestaj_prodaje.csv",index=True,encoding="utf-8-sig",sep=";")
izvjestaj.to_excel("izvjestaj_prodaje.xlsx",index=True,sheet_name="Izvjestaj_prodaje")