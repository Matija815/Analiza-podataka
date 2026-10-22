import pandas as pd;
import numpy as np;

np.random.seed(42);
# Ucitavanje podataka
podaci = {
    "Datum_Transakcije": [
        "2026-05-01",
        "2026-05-02",
        "2026-05-03",
        "2026-05-04",
        "2026-05-05",
        "2026-05-06",
        "2026-05-07",
        "2026-05-08",
        "2026-05-09",
        "2026-05-10",
    ],
    "Grad_Kupca": [
        "  Beograd ",
        "novi sad",
        "BEOGRAD",
        " Niš",
        "Novi Sad ",
        "Beograd",
        "Niš ",
        "Subotica",
        "BEOGRAD",
        "Novi Sad",
    ],
    "Naziv_Artikla": [
        "Laptop",
        "Miš",
        " Tastatura ",
        "Monitor",
        "Laptop",
        "Miš",
        "Monitor",
        "Tastatura",
        "Laptop",
        "Miš",
    ],
    "Iznos_EUR": [
        1200.50,
        np.nan,
        450.00,
        300.00,
        np.nan,
        25.00,
        320.00,
        80.00,
        1150.00,
        30.00,
    ],  # Namjerni NaN-ovi!
    "Radnik_ID": [101, 102, 103, 101, 104, 102, 105, 103, 101, 104],
}

df_podaci = pd.DataFrame(podaci);

radnici = {
    "Radnik_ID": [101,102,103,104,105],
    "Ime_radnika": ["Damjan K.","Dimitrije M.","Slavko S.","Vladan V.","Matija S."],
    "Sektor": ["Prodaja","Logistika","Prodaja","Podrska","Logistika"]
}
df_radnici = pd.DataFrame(radnici);

# Sredjivanje podataka 
