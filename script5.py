import pandas as pd

prodaja = [
    {"prodaja_id": 1, "proizvod_id": 10, "kolicina": 2},
    {"prodaja_id": 2, "proizvod_id": 20, "kolicina": 1},
    {"prodaja_id": 3, "proizvod_id": 10, "kolicina": 5},
    {"prodaja_id": 4, "proizvod_id": 20, "kolicina": 3}
]
df_prodaja = pd.DataFrame(prodaja)

proizvodi = [
    {"id_proizvoda": 10, "naziv": "Tastatura", "cijena": 50.0},
    {"id_proizvoda": 20, "naziv": "Mis", "cijena": 25.0}
]
df_proizvodi = pd.DataFrame(proizvodi)

df_spojeno = pd.merge(df_prodaja,df_proizvodi,left_on="proizvod_id",right_on="id_proizvoda",how="inner")

df_spojeno["ukupno"] = df_spojeno["kolicina"] * df_spojeno["cijena"]

df_spojeno = df_spojeno.drop(columns=["id_proizvoda"])

izvjestaj = df_spojeno.groupby("naziv").agg(
    ukupna_zarada=("ukupno","sum"),
    ukupno_prodato_komada=("kolicina","sum"),
    prosjecna_kolicina=("kolicina","mean")
)
print("=== ZBIRNI IZVJESTAJ PO PROIZVODU ===")
print(izvjestaj)