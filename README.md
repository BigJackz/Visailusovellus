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

Sovelluksessa on mahdollista luoda yksittäisiä kysymyksiä sekä vastata satunnaisiin jo luotuoihin kysymyksiin. Kysymysten satunnaisuus tulee muuttumaan, mutta aluksi nyt vain näin, että sovellusta oli mukavampi testata. Sivun "/new" kenttä Topic ei tee vielä mitään.

Sovelluksen kaikki koodi on vielä tiedostossa app.py, josta se olisi tarkoitus refaktoroida jossain kohtaa.

Sovellus vaatii tällä hetkellä kolmea eri tietokantaa

questions: 
```
CREATE TABLE questions (id SERIAL PRIMARY KEY, question TEXT);
```
answers:
```
CREATE TABLE answers (id SERIAL PRIMARY KEY, question_id INTEGER REFERENCES questions, answer1 TEXT, answer2 TEXT, answer3, TEXT, answer4 TEXT);
```
correct:
```
CREATE TABLE correct (id SERIAL PRIMARY KEY, question_id INTEGER REFERENCES questions, answer TEXT);
```
Sovellukseen tulossa vielä kirjautuminen, sekä tietokanta, joka pitää yllä 10 kysymyksen visoja.

Sovelluksen testaus onnistuu lataamalla koodin, luomalla tietokannat, vaihtamalla .env tiedostoon omien tietokantojen osoitteen ja käynnistämällä terminalista komennolla: flask run

Sovellus käyttää, Flask, SQLAlchemy, getenv sekä random.

HUOM! En saanut kurssimateriaalin mukaista sql intjektion estämistä toimimaan, joten ymmärtääkseni sql injektio on vielä mahdollista tässä sovelluksessa.

