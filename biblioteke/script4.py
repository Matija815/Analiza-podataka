import pandas as pd  
import numpy as np 

np.random.seed(42)

datumi_tekst = [
    "2026-01-01",
    "2026-01-02",
    "2026-01-03",
    "2026-01-04",
    "2026-01-05",
    "2026-01-06",
    "2026-01-07",
    "2026-01-08",
    "2026-01-09",
    "2026-01-10",
]

prodaja = np.random.randint(100,500,size=10)
df_prodaja = pd.DataFrame({
    "Datum_Tekst": datumi_tekst,
    "Prodaja_EUR": prodaja
})

# Konverzija u pravi datetime objekat
df_prodaja["Datum"] = pd.to_datetime(df_prodaja["Datum_Tekst"])

# Izvlacenje informacija iz datuma
df_prodaja["Dan_U_Nedelji"] = df_prodaja["Datum"].dt.day_name()

# Kumulativna suma (rastuci zbir iz dana u dan)
df_prodaja["Kumulativna_Prodaja"] = df_prodaja["Prodaja_EUR"].cumsum()

print("\n=== PREGLED PRODAJE SA VREMENSKIM FUNKCIJAMA ===")

print(df_prodaja[["Datum","Dan_U_Nedelji","Prodaja_EUR","Kumulativna_Prodaja"]])
# Ako bismo stampali print(df_prodaja),stampali bi i kolonu Datum_Tekst,ovako sa dva puta [] zagradama,
# koje su unutrasnje zagrade,predstavljaju obicnu Python listu imena kolona koje zelimo da izvucemo tj. u ovom slucaju
# Datum i Prodaja_EUR.

# ZADATAK
# Racuna pokretni prosjek za posljednja 3 dana
df_prodaja["Pokretni_Prosjek_3D"] = (
    df_prodaja["Prodaja_EUR"].rolling(window=3).mean()
)
print("\n=== SA POKRETNIM PROSJEKOM ===")
print(df_prodaja[["Datum","Prodaja_EUR","Pokretni_Prosjek_3D","Kumulativna_Prodaja"]].round(2))

# Filtriranje samo vikenda pomocu .isin()
vikend_dani = ["Saturday","Sunday"]

df_vikend = df_prodaja[df_prodaja["Dan_U_Nedelji"].isin(vikend_dani)]
print("\n=== PRODAJA TOKOM VIKENDA ===")
print(df_vikend)
# isin() prolazi kroz kolonu Dan_U_Nedelji red po red i vraca True za svaki red gdje je vrijednost
# Saturday ili Sunday.Pandas kada se zavrsi prolazak izvuce samo one gdje je True vrijednost.