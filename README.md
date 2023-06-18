# tsoha_bookKeeping
Harjoitustyö kurssille Tsoha.
Samankaltaisia sovelluksi on varmasti olemassa jo useampia mutta kehitämpä nyt oman versioni, lähinnä omaan käyttöön.


***Sovelluksen tämänhetkinen tila***

Sovelluksessa voi rekisteröityä, kirjautua sisään, kirjautua ulos, lisätä julkisia kirjoja, merkata julkisia kirjoja itselle luetuksi ja arvostella niitä, merkata kirjoja suosikeiksi ja lisätä kirjoja lukulistalle. Lisäksi sovelluksessa voi poistaa kirjoja, arvosteluja, suosikkeja ja merkintöjä lukulistalla.

Sovelluksessa on viisi taulua: käyttäjät, kirjat, arvostelut, suosikit ja lukulista.

***Suunnitelmia tulevaisuuteen***
Sovellukseen on tarkoitus tulevaisuudessa tehdä mahdollisuus muokata omia arvosteluja, parantaa filteröintiä, esim omat parhaat arvostelut näkyviin, kirjat listattu aakkosjärjestyksessä yms. Lisäksi toiveenani olisi tehdä jonkinlainen hakutoiminto kirjoille.

Lisäksi tarkoitus on parantaa sovelluksen turvallisuutta kurssimateriaalin luvun 4 mukaiseksi.

Lisäksi sovelluksen napit yms. ovat melko sotkuisia joten varmaan siistin niitä.

On mahdollista että sovellukseen lisätään myös tuki elokuville, sarjoille yms. mutta se tulisi käytännössä olemaan vain oma kenttänsä kirjataulussa, esim. "viihdemuoto" tms.

***HOW TO OPEN***: 

**Clone the repository:**

$ git clone https://github.com/kaarleol/tsoha_bookKeeping

**Create virtual environment:**
Linux:

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r ./requirements.txt

**Create .env file to the source folder and fill in the database URL & secret key**

DATABASE_URL=<database_address>

SECRET_KEY=<secret_key>

**Example of .env -file:**

DATABASE_URL=postgresql+psycopg2://postgres:12345678@localhost/postgres

SECRET_KEY=12345678901234567890

**Note: SECRET_KEY NEEDS TO BE SET FOR LOGIN TO WORK**

**Create the database in psql:**

Go back to the source file (tsoha_bookKeeping)

$ psql -d database_name < schema.sql

**Or open the psql and paste the contents of schema.sql**

**Start the app:**

Go back to the source file (tsoha_bookKeeping)

$ flask run
