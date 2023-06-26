# tsoha_bookKeeping
Harjoitustyö kurssille Tsoha.
Samankaltaisia sovelluksi on varmasti olemassa jo useampia mutta kehitämpä nyt oman versioni, lähinnä omaan käyttöön.


***Sovelluksen tämänhetkinen tila***

Sovellus on avattavissa vain paikallisesti.

Sovelluksessa voi rekisteröityä, kirjautua sisään, kirjautua ulos, lisätä julkisia kirjoja, merkata julkisia kirjoja itselle luetuksi ja arvostella niitä, merkata kirjoja suosikeiksi ja lisätä kirjoja lukulistalle. Lisäksi sovelluksessa voi poistaa kirjoja, arvosteluja, suosikkeja ja merkintöjä lukulistalla. Lisäksi sovelluksessa voi muokata itse lisäämiään kirjoja ja arvosteluja. Sovelluksessa on nyt myös hakutoiminto kirjoille ja kirjailijoille.

Sovelluksessa on viisi taulua: käyttäjät, kirjat, arvostelut, suosikit ja lukulista.


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
