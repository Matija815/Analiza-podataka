import pandas as pd

prodaja = [
    {"prodaja_id": 1, "proizvod_id": 10, "kolicina": 2},
    {"prodaja_id": 2, "proizvod_id": 20, "kolicina": 1},
    {"prodaja_id": 3, "proizvod_id": 30, "kolicina": 5}
]
df_prodaja = pd.DataFrame(prodaja)
print("=== PRODAJA ===")
print(df_prodaja)

proizvodi = [
    {"id_proizvoda": 10, "naziv": "Tastatura", "cijena": 50.0},
    {"id_proizvoda": 20, "naziv": "Mis", "cijena": 25.0},
    {"id_proizvoda": 30, "naziv": "Monitor", "cijena": 200.0}
]
df_proizvodi = pd.DataFrame(proizvodi)
print("=== PROIZVODI ===")
print(df_proizvodi)

# Spajanje tabela
df_inner = pd.merge(df_prodaja,df_proizvodi,left_on="proizvod_id",right_on="id_proizvoda",how="inner")
print(df_inner)

# Uklanjanje duplikata
df_inner = df_inner.drop(columns=["id_proizvoda"])

df_inner["ukupno"] = df_inner["kolicina"] * df_inner["cijena"]

print("=== FINALNA TABELA ===")
print(df_inner)


# ZADATAK 2
ponuda = [
    {"ponuda_id": 1, "auto_id": 10, "kolicina": 2},
    {"ponuda_id": 2, "auto_id": 20, "kolicina": 1},
    {"ponuda_id": 3, "auto_id": 30, "kolicina": 4},
    {"ponuda_id": 4, "auto_id": 40, "kolicina": 1}
]

df_ponuda = pd.DataFrame(ponuda)

auta = [
    {"auto_id": 10, "naziv": "Audi Q3", "cijena": 43000.0},
    {"auto_id": 20, "naziv": "Passat VII", "cijena": 30000.0},
    {"auto_id": 30, "naziv": "Renault Clio", "cijena": 18500.0},
    {"auto_id": 50, "naziv": "Golf VIII GTI", "cijena": 40000.0}
]

df_auta = pd.DataFrame(auta)

print("\n=== POCETNE TABELE ===")
print("\n-- PONUDA --","\n", df_ponuda)
print("\n-- AUTA --","\n", df_auta)

# INNER JOIN
df_inner_join = pd.merge(df_ponuda,df_auta,on="auto_id",how="inner")
print("\n INNER JOIN TABELA")
print(df_inner_join)

# LEFT JOIN
df_left = pd.merge(df_ponuda,df_auta,on="auto_id",how="left")
print("==================================")
print("\n LEFT JOIN TABELA")
print(df_left)

# RIGHT JOIN 
df_right = pd.merge(df_ponuda,df_auta,on="auto_id",how="right")
print("RIGHT JOIN TABELA")
print(df_right)

# OUTER JOIN
df_outer = pd.merge(df_ponuda,df_auta,on="auto_id",how="outer")
print("OUTER TABELA")
print(df_outer)

"""  pd.merge(
    left_dataframe,    # Leva tabela
    right_dataframe,   # Desna tabela
    on='zajednicka_kolona', # Po kojoj koloni spajamo (mora postojati u obe)
    how='inner'        # Tip spajanja: 'inner', 'left', 'right' ili 'outer'
)"""