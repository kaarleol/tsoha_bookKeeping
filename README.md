# tsoha_bookKeeping
Harjoitustyö kurssille Tsoha.
Samankaltaisia sovelluksi on varmasti olemassa jo useampia mutta kehitämpä nyt oman versioni, lähinnä omaan käyttöön.


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

**Create the database in psql:**

Go back to the source file (tsoha_bookKeeping)

$ psql -d database_name < schema.sql

**Or open the psql and paste the contents of schema.sql**

**Start the app:**

Go back to the source file (tsoha_bookKeeping)

$ flask run

***Suunnitelma sovellukselle***


**Toiminnallisuuksia**


Tarkoituksena on luoda sovellus johon voi lisätä kirjoja, elokuvia ja TV-ohjelmia joita on lukenut/katsonut ja joita tahtoo tulevaisuudessa lukea/katsoa.
Lisäksi sovelluksessa olisi mahdollista arvostella luettuja/katsottuja kirjoja/elokuvia.

Käyttäjä voisi hakea omat suosikkikirjansa yms. tai suunnitella mitä aikoo seuraavaksi lukea/katsoa.

Alkuun sovelluksen on määrä mahdollistaa näiden tietojen näyttäminen vain käyttäjälle itselleen, mutta jos aikaa jää, on mahdollista, että sovelluksessa voisi nähdä myös muiden arvostelemia kirjoja yms. ja hakea suosituimmat kirjat yms.

**Toteutussuunnitelma**

Taulut: Käyttäjät, luetut/katsotut kirjat/showt, luettavat/katsottavat kirjat/showt, arvostelut

Käyttäjät: Nimi, salasana, automaattinen UID

Luetut/katsotut kirjat/showt: Nimi, tyyppi (kirja, elokuva, sarja, tms.), päivämäärä, ID (joko yksityinen id käyttäjälle tai kirjalle oma ID joka kaikilla käytössä tai molemmat)

Luettavat/katsottavat kirjat/showt: Nimi, tyyppi (kirja, elokuva, sarja, tms.), ID (joko yksityinen id käyttäjälle tai kirjalle oma ID joka kaikilla käytössä tai molemmat)

Arvostelut: käyttäjä ID, kirja ID, arvosana, kuvaus, päivämäärä

**Jos aikaa jää**

Parannuksia interaktioihin käyttäjien välillä, esim kaveritiedot, päätös onko omat listat muiden nähtävissä, ehkä jotkut kirjasuositukset, haku erilaisille kirjoille ja niiden arvosteluille jne jne jne.
