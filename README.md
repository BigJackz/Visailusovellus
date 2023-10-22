# Visailusovellus

## Visailusovellus

Sovelluksen perusidea on, että sivulta löytyy kysymyksiä erinäisillä aiheilla.

Sovellu sisältää yksittäisiä kysymyksiä, joissa on 1 oikea vastaus ja 3 väärää.

Käyttäjä voi luoda tunnuksen, kirjautua sisään sekä ulos.

Kirjautumisen jälkeen käyttäjä voi luoda sivulle uusia kysymyksiä vastauksineen, sekä vastata sivulta jo löytyviin kysymyksiin.

Käyttäjä voi vastata joko satunnaiseen kysymykseen, etsiä kysymyksiä liittyen haettuun aiheeseen tai selata kaikki lisättyjä kysymyksiä ja valita niistä mihin vastaa.

Sovelluksen ulkoasu jäi hieman köyhäksi.

------------------------------------------------------------------------------

## Käynnistysohje

Kloonaa reposotirio omalle koneellesi
```
git clone git@github.com:BigJackz/Visailusovellus.git
```
Siirry sitten sovelluksen juurikansioon
```
cd Visailusovellus
```
Luo .env tiedosto ja lisää sinne tietokannan paikallinen osoite sekä salainen avain
```
DATABASE_URL=<tietokannan_paikallinen_osoite>
SECRET_KEY=<salainen_avain>
```
Aktivoi virtuaaliympäristö ja asenna riippuvuudet (requirements.txt saattaa sisältää liikaa riippuvuuksia, käytin kurssimateriaalin tyyliä luoda requirements.txt)
```
python3 -m venv venv
source venv/bin/activate
pip install flask-sqlalchemy
pip install python-dotenv
pip install psycopg2 tai pip install psycopg2-binary
```
Luo tietokannat tiedostosta schema.sql (sisältää tietokannat nimeltä, questions, answers, correct)
```
psql < schema.sql
```
Jonka jälkeen voi sovelluksen käynnistää komennolla
```
flask run
```
