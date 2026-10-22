import pandas as pd
import numpy as np  

np.random.seed(42)

# 1. NumPy: Generisanje matrica ocjena (5 radnika, 4 kvartala) iz opsega [50, 100]
ocjene_matrix = np.random.randint(50,101,size=(5,4)) 

# 2. Pandas: Pravljenje DataFrame-a
radnici = ["Damjan","Vladan","Slavko","Matija","Dimitrije"]
kvartali = ["Q1","Q2","Q3","Q4"]

df = pd.DataFrame(ocjene_matrix,index=radnici,columns=kvartali)

print("=== POCETNI DATAFRAME ===")
print(df)

# A. Prosjecna ocjena po radniku (Pandas mean po osi 1)
df["Prosjek"] = df[kvartali].mean(axis=1)

# B. Koristimo np.where za kategorizaciju (Vektorski IF-ELSE)
# Ako je prosjek >= 80 -> "Bonus", inace -> "Bez bonusa"
df["Bonus_Status"] = np.where(df["Prosjek"] >= 80, "Bonus", "Bez bonusa")

# C. Koristimo np.select za vise uslova (Vektorski IF-ELIF-ELSE)
uslovi = [
    df["Prosjek"] >= 90,
    (df["Prosjek"] >= 75) & (df["Prosjek"] < 90),
    df["Prosjek"] < 75
]
kategorije = ["Odlican","Vrlodobar","Potrebno poboljsanje"]
df["Kategorija"] = np.select(uslovi,kategorije,default="Nije definisano")

print("\n=== NAKON DODAVANJA VEKTORSKIH KOLONA ===")
print(df)

# Dodajemo namerno nekoliko NaN vrijednosti  pomocu np.nan
df_prljavo = df[kvartali].copy()
df_prljavo.iloc[0, 1] = np.nan # Damjan Q2
df_prljavo.iloc[3, 3] = np.nan # Matija Q4

print("\n=== PODACI SA MISSING VALUE (NaN) ===")
print(df_prljavo)

# 1. Popunjavanje NaN vrijednosti medijanom tog kvartala (Pandas fillna + median)
df_cisto = df_prljavo.fillna(df_prljavo.median())

print("\n=== POPUNJENI PODACI (MEDIJANA) ===")
print(df_cisto)

# 2. Min-Max Normalizacija u opseg [0, 1] pomoću NumPy operacija
# Formula: (X - X_min) / (X_max - X_min)

x = df_cisto.values # Vraća čisti NumPy ndarray iz DataFrame-a
x_norm = (x - np.min(x)) / (np.max(x) - np.min(x))

df_normalizovano = pd.DataFrame(x_norm, index = df_cisto.index, columns = df_cisto.columns)

print("\n=== NORMALIZOVANI PODACI [0, 1] ===")
print(df_normalizovano.round(2))

# ZADATAK
suma_po_kvartalu = df_cisto[kvartali].sum(axis=0)
print("=== UKUPNA SUMA BODOVA PO KVARTALIMA ===")
print(suma_po_kvartalu)

df_cisto["Q4_Skok"] = np.where(df_cisto["Q4"] > df_cisto["Q1"], True, False)
print("\n=== NAKON DODAVANJA Q4_Skok ===")
print(df_cisto)