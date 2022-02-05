# Testaaminen

Tässä projektissa testattavaa koodia on melko vähän, suhteessa algoritmin viilaamisen vaatimaan työmäärään. Projektissa on kaksi pääasiallista testialustaa, testattava koodi moduulissa `modules/book_analytics.py`, joka omaa yksikkötestit kansiossa `tests/`, sekä `jupyter notebook`issa oleva data tieteellisempi testaus (tämän tarkistaminen on vertaisarvioijalle vapaaehtoista ja kirjoitan tärkeimmät löydökset tähän dokumenttiin).

Tällä hetkellä projektissa on myös muuta koodia, joiden alkuperä on "isäntä projektista" (annotaatio työkalu). Näitä ei ole tarkoitus testata tässä projektissa ainakaan heti alkuun.

## Yksikkötestit, lintterit ja testikattavuus

Kannattaa ensin luoda `README.md` dokumentissa mainittu `virtualenv` ja ajaa riippuvuuksien asennus.

Docstyle testit voi ajaa:
```
pydocstyle modules/book_analytics.py
```

Yksikkö testit voi ajaa:
```
python -m pytest tests/
```

Lintterin voi ajaa:
```
pylint modules/book_analytics.py
```

Testi kattavuus raportin saa ajamalla:
```
coverage run -m pytest tests/
coverage report
```

![Code coverage](Coverage.png?raw=true "Code coverage")

## Data tiede testaus

Aja Jupyter Notebook ja käynnistä `notebooks/Analytics.ipynb` notebookki:
```
jupyter notebook
```

Esimerkiksi tässä on yksi sentimentti analyysi, jolle pitäisi saada kuvaaja, jonka mukaan kappalejako 184 on draamallisesti tylsää sisältöä (tällä hetkellä algoritmi ei siis vielä toimi oikein):

![Compound](Compound.png?raw=true "Compound")

Toisaalta taas kappalejako 394 käynnistää MICE quotientin Inquiry draaman kaaren (tällä hetkellä sekään ei ihmeemmin näy kuvaajassa merkityksellisesti):

![MICE 1](MICE_ex_1.png?raw=true "Mice 1")

### Ensimmäiset lupaukset

Lisäsin sentimentti intervallin, joka on hieman samantapainen suure kuin tutkimuspaperissa käytetty menetelmä, mutta paljon yksinkertaisempi ja yhtäkkiä tulokset alkoivatkin näyttämään lupaavilta.

Tylsällä kohdalla on korkea intervalli summa, eli ambivalenssia on ilmeisesti paljon:

![Boring with More data](Boring_second.png?raw=true "Boring with More Data")

Ja mielenkiintoisella on matala intervalli summa, eli sentimentti on selkeästi keskittynyt:

![MICE with More data](MICE_ex_1_second.png?raw=true "MICE with More Data")
