CREATE SCHEMA IF NOT EXISTS bioskopi;
USE bioskopi;

CREATE TABLE adresa (
	adresa_id INT PRIMARY KEY,
    ulica VARCHAR(20),
    broj INT,
    grad VARCHAR(30),
    drzava VARCHAR(30)
);

CREATE TABLE bioskop (
	bioskop_id INT PRIMARY KEY,
    adresa_id INT,
    FOREIGN KEY (adresa_id) REFERENCES Adresa(adresa_id)
);

CREATE TABLE uloga (
	uloga_id INT PRIMARY KEY,
    naziv VARCHAR(50)
);

CREATE TABLE zaposleni (
	zaposleni_id INT PRIMARY KEY,
	ime VARCHAR(30),
    prezime VARCHAR(30),
    adresa_id INT,
    uloga_id INT,
    bioskop_id INT,
    FOREIGN KEY (adresa_id) REFERENCES Adresa(adresa_id),
	FOREIGN KEY (uloga_id) REFERENCES Uloga(uloga_id),
	FOREIGN KEY (bioskop_id) REFERENCES Bioskop(bioskop_id)
);

ALTER TABLE zaposleni
ADD plata DECIMAL(10,2);

CREATE TABLE prostorija (
	prostorija_id INT PRIMARY KEY,
    bioskop_id INT,
    tip_ekrana ENUM('IMAX','2D','3D'),
    FOREIGN KEY (bioskop_id) REFERENCES bioskop(bioskop_id)
);

CREATE TABLE tip_sjedista (
	tip_sjedista_id INT PRIMARY KEY,
    naziv VARCHAR(40)
);

CREATE TABLE sjediste (
	sjediste_id INT PRIMARY KEY,
    broj INT,
    prostorija_id INT,
    tip_sjedista_id INT,
    FOREIGN KEY (prostorija_id) REFERENCES prostorija(prostorija_id),
    FOREIGN KEY (tip_sjedista_id) REFERENCES tip_sjedista(tip_sjedista_id)
);

CREATE TABLE film (
	film_id INT PRIMARY KEY,
    naziv VARCHAR(30),
    trajanje INT,
    godina_proizvodnje INT
);

CREATE TABLE projekcija (
	projekcija_id INT PRIMARY KEY,
	prostorija_id INT,
    film_id INT,
    datum_projekcije DATE,
    vrijeme_pocetka TIME,
    FOREIGN KEY (prostorija_id) REFERENCES prostorija(prostorija_id),
    FOREIGN KEY (film_id) REFERENCES film(film_id)
);

CREATE TABLE korisnik (
	korisnik_id INT PRIMARY KEY,
    ime VARCHAR(30)
);

CREATE TABLE kupovina (
	kupovina_id INT PRIMARY KEY,
    korisnik_id INT,
    FOREIGN KEY (korisnik_id) REFERENCES korisnik(korisnik_id)
);

CREATE TABLE karta (
	karta_id INT PRIMARY KEY,
    kupovina_id INT,
    sjediste_id INT,
    projekcija_id INT,
    FOREIGN KEY (kupovina_id) REFERENCES kupovina(kupovina_id),
    FOREIGN KEY (sjediste_id) REFERENCES sjediste(sjediste_id),
    FOREIGN KEY (projekcija_id) REFERENCES projekcija(projekcija_id)
);

INSERT INTO adresa VALUES
(1,'Nemanjina',10,'Beograd','Srbija'),
(2,'Knez Mihailova',25,'Beograd','Srbija'),
(3,'Bulevar Revolucije',15,'Novi Sad','Srbija'),
(4,'Marsala Tita',8,'Nis','Srbija'),
(5,'Cara Dusana',12,'Kragujevac','Srbija');

INSERT INTO bioskop VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,1),
(7,2),
(8,3);

INSERT INTO uloga VALUES
(1,'Salterski radnik'),
(2,'Kontroler ulaznica'),
(3,'Menadzer'),
(4,'Tehnicar');

INSERT INTO zaposleni VALUES
(1,'Marko','Markovic',1,1,1,65000),
(2,'Jelena','Jovanovic',2,2,1,70000),
(3,'Nikola','Nikolic',3,3,2,95000),
(4,'Ana','Petrovic',4,1,2,68000),
(5,'Stefan','Ilic',5,4,3,85000),
(6,'Srdjan','Cabrilo',1,1,1,65000),
(7,'Dimitrije','Skrivan',2,2,1,70000),
(8,'Bojan','Ijacic',3,3,2,95000),
(9,'Djordje','Bojanic',4,1,2,68000),
(10,'Marko','Sukovic',5,4,3,85000);

INSERT INTO prostorija VALUES
(1,1,'IMAX'),
(2,1,'3D'),
(3,2,'2D'),
(4,3,'IMAX'),
(5,3,'3D'),
(6,2,'IMAX'),
(7,2,'2D');

INSERT INTO tip_sjedista VALUES
(1,'Obicno'),
(2,'Luksuzno'),
(3,'VIP');

INSERT INTO sjediste VALUES
(1,1,1,1),
(2,2,1,1),
(3,3,1,2),
(4,4,1,3),

(5,1,2,1),
(6,2,2,2),
(7,3,2,3),

(8,1,3,1),
(9,2,3,1),
(10,3,3,2),

(11,1,4,1),
(12,2,4,2),
(13,3,4,3);

INSERT INTO film VALUES
(1,'Avatar 2',192,2022),
(2,'Inception',148,2010),
(3,'Titanic',194,1997),
(4,'Oppenheimer',180,2023),
(5,'Interstellar',169,2014);

INSERT INTO projekcija VALUES
(1,1,1,'2025-07-01','18:00:00'),
(2,1,2,'2025-07-01','21:00:00'),
(3,2,3,'2025-07-02','19:00:00'),
(4,3,4,'2025-07-02','20:00:00'),
(5,4,5,'2025-07-03','18:30:00');

INSERT INTO korisnik VALUES
(1,'Milan'),
(2,'Petar'),
(3,'Sara'),
(4,'Ivana'),
(5,'Luka');

INSERT INTO kupovina VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,1);

INSERT INTO karta VALUES
(1,1,1,1),
(2,1,2,1),

(3,2,3,1),

(4,3,4,2),

(5,4,5,3),
(6,4,6,3),

(7,5,7,4),

(8,6,8,1),
(9,6,9,1),
(10,6,10,1);

SELECT * FROM film
WHERE godina_proizvodnje < 2020;

SELECT p.projekcija_id,COUNT(DISTINCT k.kupovina_id) AS broj_rezervacija
FROM projekcija p
JOIN karta k ON p.projekcija_id = k.projekcija_id
JOIN kupovina kp ON k.kupovina_id = kp.kupovina_id
GROUP BY p.projekcija_id
HAVING COUNT(DISTINCT k.kupovina_id) > 3;

SELECT u.naziv,AVG(z.plata) AS prosjecna_plata
FROM zaposleni z
JOIN uloga u ON z.uloga_id = u.uloga_id
GROUP BY naziv;

SELECT f.naziv,COUNT(k.karta_id) AS broj_rezervisanih_sjedista
FROM film f
JOIN projekcija p ON f.film_id = p.film_id
JOIN karta k ON p.projekcija_id = k.projekcija_id
GROUP BY f.film_id,f.naziv
ORDER BY broj_rezervisanih_sjedista DESC
LIMIT 1;

SELECT DISTINCT b.bioskop_id
FROM bioskop b
JOIN prostorija p ON b.bioskop_id = p.bioskop_id
WHERE p.tip_ekrana ='IMAX';

SELECT p.prostorija_id
FROM prostorija p
JOIN sjediste s ON p.prostorija_id = s.prostorija_id
GROUP BY p.prostorija_id
HAVING COUNT(DISTINCT s.tip_sjedista_id) >= 3;

DELIMITER //

CREATE PROCEDURE dobaviProjekcijuFilma (
	IN p_naziv VARCHAR(30),
    IN p_datum DATE
)
BEGIN
SELECT p.projekcija_id,f.naziv,p.datum_projekcije,p.vrijeme_pocetka,p.prostorija_id
FROM projekcija p
JOIN film f ON p.film_id = f.film_id
WHERE f.naziv = p_naziv AND datum_projekcije = p_datum;

END //

DELIMITER ;

CALL dobaviProjekcijuFilma('Avatar 2','2025-07-01');

DELIMITER //

CREATE TRIGGER DaLiJeprojekcijaProsla
BEFORE INSERT ON karta
FOR EACH ROW
BEGIN
	DECLARE vrijeme_proj DATETIME;
    SELECT TIMESTAMP(datum_projekcije, vrijeme_pocetka)
    INTO vrijeme_proj
    FROM projekcija
    WHERE projekcija_id = NEW.projekcija_id;

    IF vrijeme_proj < NOW() THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Projekcija je vec prosla';
    END IF;
END //

DELIMITER ;