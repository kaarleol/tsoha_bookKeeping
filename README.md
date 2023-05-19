# tsoha_bookKeeping
Harjoitustyö kurssille Tsoha.
Samankaltaisia sovelluksi on varmasti olemassa jo useampia mutta kehitämpä nyt oman versioni, lähinnä omaan käyttöön.

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
