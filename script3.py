import pandas as pd

podaci = [
    {"kategorija": "Tehnika", "proizvod": "Telefon", "cijena": 800.0},
    {"kategorija": "Tehnika", "proizvod": "Laptop", "cijena": 1200.0},
    {"kategorija": "Tehnika", "proizvod": "Punjac", "cijena": 50.0},
    {"kategorija": "Odjeca", "proizvod": "Majica", "cijena": 30.0},
    {"kategorija": "Odjeca", "proizvod": "Majica", "cijena": 150.0},
    {"kategorija": "Odjeca", "proizvod": "Majica", "cijena": 70.0}
]

df = pd.DataFrame(podaci)
print("=== PODACI ===")
print(df)

izvjestaj = df.groupby("kategorija")["cijena"].agg(["sum","mean","max"])
print("\n=== IZVJESTAJ ===")
print(izvjestaj)