# 
Web-käyttöliittymä, joka purkaa APIsta haettuja kryptattuja lauseita. Lauseet on kryptattu Caesar-salakirjoitusjärjestelmällä. Lauseet näytetään jaoteltuina No bullshit ja bullshit –lauseisiin. Käännettävissä olevat no bullshit –lauseet näytetään suomeksi ja bullshit-lauseet, jotka eivät käänny selkokielisiksi, näytetään alkuperäismuodossaan.

# Ohjeet

1. Halutessasi luo virtuaaliympäristö 
```
conda create --name app_venv
conda activate app_venv
```
2. Kloonaa repository
3. Navigoi kloonattuun kansioon ja lataa tarvittavat python paketit:
```
pip install -r requirements.txt 
```
4. Käynistä sovellus:
```
python app.py
```
5. Avaa http://127.0.0.1:5000/ selaimessa

# Lista suomenkielisistä sanoista

kotus-sanalista_v1.xml sisältää Kotimaisten kielten keskuksen (Kotus) koostaman ja julkaiseman listan nykysuomen sanalistan. Sanalistan laajuus on 94 110 sanatietuetta. Lista on [ladattavissa](http://kaino.kotus.fi/sanat/nykysuomi/) Kotimaisten kielten keskuksen sivustoilta.

Sanalista on julkaistu lisensseillä GNU LGPL (Lesser General Public License), EUPL v.1.1 (Euroopan unionin yleinen lisenssi) ja CC Nimeä 3.0 Muokkaamaton.

Sovelluksessa listaa käytetään suomenkielisten sanojen tunnistamiseen
