CREATE TABLE ARTIKLI(
SIFRA SERIAL PRIMARY KEY,
NAZIV VARCHAR(40),
KOLICINA INTEGER,
CENA FLOAT);

INSERT INTO ARTIKLI (NAZIV,KOLICINA,CENA) VALUES ('Lasko pivo',150,77.99);
INSERT INTO ARTIKLI (NAZIV,KOLICINA,CENA) VALUES ('LAV Premium pivo',280,69.99);
INSERT INTO ARTIKLI (NAZIV,KOLICINA,CENA) VALUES ('Nektar pivo',75,87.99);
INSERT INTO ARTIKLI (NAZIV,KOLICINA,CENA) VALUES ('Niksicko pivo',34,71.99);
INSERT INTO ARTIKLI (NAZIV,KOLICINA,CENA) VALUES ('Dzin BEEFEATER',64,1399);
INSERT INTO ARTIKLI (NAZIV,KOLICINA,CENA) VALUES ('Dzin GORDONS',88,1299);
INSERT INTO ARTIKLI (NAZIV,KOLICINA,CENA) VALUES ('Dzin LORDSON',740,589.99);
INSERT INTO ARTIKLI (NAZIV,KOLICINA,CENA) VALUES ('Viski BALLANTINES',4,2050);
INSERT INTO ARTIKLI (NAZIV,KOLICINA,CENA) VALUES ('Viski JAMESON',45,2399);
INSERT INTO ARTIKLI (NAZIV,KOLICINA,CENA) VALUES ('Viski FOUR ROSES',456,2459);

SELECT * FROM ARTIKLI WHERE