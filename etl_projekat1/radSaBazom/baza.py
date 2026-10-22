import pandas as pd
from sqlalchemy import create_engine 
from sqlalchemy.exc import OperationalError,SQLAlchemyError,IntegrityError

# Konekcija na MySQL Workbench bazu podataka
USER ="root"
PASSWORD ="Singidunum"
HOST ="localhost"
PORT ="3306"
DB_NAME ="hotel"

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

try:
    print("Pokusavam ovezivanje sa MySQL bazom...")
    # Kreiranje SQLAlchemy engine
    engine = create_engine(DATABASE_URL)
    
    with engine.connect() as connection:
        print("Uspjesno povezivanje na bazu!")
        # Priprema podataka po tabelama u pandasu

        df_gosti = pd.DataFrame({
        "gost_id": [1,2],
        "gost_ime": ["Petar P.","Milica M."],
        "gost_grad": ["Nis","Kragujevac"]
        })

        df_hoteli = pd.DataFrame({
        "hotel_id": [1,2],
        "hotel_ime": ["Hotel Moskva","Hotel Park"],
        "hotel_grad": ["Beograd","Novi Sad"]
        })

        df_rezervacije = pd.DataFrame({
        "rezervacija_id": [101,102],
        "gost_id": [1,2],
        "hotel_id": [1,2]
        })

        df_rezervacije_sobe = pd.DataFrame({
        "rezervacija_sobe": [1,2,3],
        "rezervacija_id": [101,101,102],
        "soba_broj": [201,202,105],
        "cijena_sobe": [8000.0,10000.0,6000.0]
        })

        # Upisivanje u MySQL bazu
        print("Slanje podataka u MySQL bazu...")
        try:
            df_gosti.to_sql("gosti",con=engine,if_exists="append",index=False)
            print("\nGosti uspijesno upisani.")
        except (IntegrityError,pd.errors.DatabaseError):
            print("-> [INFO] Gosti vec postoje u bazi! (preskacem upis)")
        try:
            df_hoteli.to_sql("hoteli",con=engine,if_exists="append",index=False)
            print("\nHoteli uspijesno upisani.")
        except (IntegrityError,pd.errors.DatabaseError):
            print("-> [INFO] Hoteli vec postoje u bazi! (preskacem upis)")
        try:
            df_rezervacije.to_sql("rezervacije",con=engine,if_exists="append",index=False)
            print("\nRezervacije uspijesno upisane.")
        except (IntegrityError,pd.errors.DatabaseError):
            print("\n -> [INFO] Rezervacije vec postoje u bazi! (preskacem upis)")
        try:
            df_rezervacije_sobe.to_sql("rezervacije_sobe",con=engine,if_exists="append",index=False)
            print("\nRezervacije sobe uspijesno upisane.")
        except (IntegrityError,pd.errors.DatabaseError):
            print("\n -> [INFO] Rezervacije soba su vec upisane u bazi! (preskacem upis)")
        # Citanje i JOIN preko sql upita nazad u pandas

        sql_upit="""
        SELECT
            r.rezervacija_id,
            g.gost_ime,
            h.hotel_ime,
            rs.soba_broj,
            rs.cijena_sobe
        FROM rezervacije r
        JOIN gosti g ON r.gost_id = g.gost_id
        JOIN hoteli h ON r.hotel_id = h.hotel_id
        JOIN rezervacije_sobe rs ON r.rezervacija_id = rs.rezervacija_id
        """

        df_izvjestaj = pd.read_sql(sql_upit, con=engine)

        print("=== IZVJESTAJ IZ MYSQL BAZE ===")
        print(df_izvjestaj)
        
except OperationalError as e:
    # Ova greska hvata: pogresnu lozinku/user,nepostojecu bazu ili ugasen MySQL server
    print("\n[GRESKA U KONEKCIJI] Nije moguce pristupiti bazi.")
    print("Provjeri: lozinku,korisnicko ime,da li baza postoji i da li je MySQL server ugasen.")
    print(f"Detalji greske: {e.orig}") # e.orig daje tacan mysql error kod

except SQLAlchemyError as e:
    # Opsta greska za sve ostale SQLAlchemy error probleme
    print(f"\n[SQLAlchemy GRESKA] Doslo je do opste greske pri radu sa bazom.")

except Exception as e:
    # Hvata sve neocekivane python greske
    print(f"\n[NEOCEKIVANA GRESKA] {e}")
