# Visailusovellus

## Visailusovellus

Sovelluksen perusidea on, että sivulta löytyy visoja erinäisillä aiheilla, joita voi etsiä hakusanoilla.

Jokainen visa sisältää jonkin määrän kysymyksiä (mahdollisesti 10), sekä jokaiseen kysymykseen 4 vastausta, joista 1 on oikea ja 3 väärää vastausta.

Käyttäjä voi luoda tunnuksen, kirjautua sisään sekä ulos.

Käyttäjä voi luoda sivulle uuden visan vastauksineen, sekä pelata sivulta jo löytyviä visoja.

Sivulta löytyy tilastot, joissa näkyy eniten täydellisesti suoritettuja visoja omaava käyttäjä sekä määrä siitä, montako visaa on suorittanut täydellisesti, mahdollisesti myös mitkä visat.

Täydellisesti suoritettu visa on sellainen, jossa henkilö ei vastaa kertaakaan väärin.

Mahdollinen haluatko miljonääriksi muoto, jossa tulisi monta visaa putkeen ja yhdellä väärällä vastauksella tippuu pois. (jos jää aikaa toteuttaa)

------------------------------------------------------------------------------

## Nykytilanne

Sovelluksessa on mahdollista luoda yksittäisiä kysymyksiä sekä vastata satunnaisiin jo luotuoihin kysymyksiin. Kysymysten satunnaisuus tulee muuttumaan, mutta aluksi nyt vain näin, että sovellusta oli mukavampi testata.

Sovellus vaatii tällä hetkellä kolmea eri tietokantaa, questions, answers sekä correct. Lisää tulossa myöhemmin viimeistään sovelluksen viimeiseen versioon.

Sovelluksen koodi refaktoroitu useampaan tiedostoon.

Sovellukseen tulossa vielä kirjautuminen, sekä tietokanta, joka pitää yllä 10 kysymyksen visoja.

Sovelluksessa on mahdollista tarkastella kaikkia lisättyjä kysymyksiä, joista tulevaisuudessa pitäisi voida valita mihin aikoo vastata.

Sovelluksen sivujen navigointia parannettu.

Sovellus jäi ominaisuuksiltaan vielä puutteelliseksi ajan puutteen takia.

HUOM! En saanut kurssimateriaalin mukaista sql injektion estämistä toimimaan, joten ymmärtääkseni sql injektio on vielä mahdollista tässä sovelluksessa.

## Käynnistysohje

Kloonaa reposotirio omalle koneellesi
```
git clone git@github.com:BigJackz/Visailusovellus.git
```
Siirry sitten sovelluksen juurikansioon
```
cd Visailusovellus
```
Luo .env tiedosto ja lisää sinne tietokannan paikallinen osoite
```
DATABASE_URL=<tietokannan_paikallinen_osoite>
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
