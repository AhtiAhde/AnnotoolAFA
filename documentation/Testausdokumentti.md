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

Tylsällä kohdalla (184) on korkea intervalli summa, eli ambivalenssia on ilmeisesti paljon:

![Boring with More data](Boring_second.png?raw=true "Boring with More Data")

Ja mielenkiintoisella kohdalla (394) on matala intervalli summa, eli sentimentti on selkeästi keskittynyt:

![MICE with More data](MICE_ex_1_second.png?raw=true "MICE with More Data")

Tein myös Golden Rank metriikan, jossa draaman kannalta oleellinen kohta (394) sijoittuu jo top 20%:iin.

### Non-Linear Adaptive Filtering kokeilu

Tein alustavan version Non-Linear Adaptive Filteringing algoritmistä (NAF). Sen voi nähdä `jupyter notebook`ista, mutta laitan koodin varmuuden vuoksi tänne myös (en vielä aio laittaa sitä osaksi koodia, koska haluan ensin tehdä seuraavatkin vaiheet):

```
def do_segmentation(n, timeline):
    segment_timeline = []
    filtered_timeline = []
    print(dramatic_sents, boring_sents)
    # We will implement this algorithm as one run, which means that we will
    # cumulate the values to the
    segment_index = -1
    for l in range(len(timeline)):
        if l in dramatic_sents:
            dramatic_seg = segment_index
            print("Dramatic segment: ", segment_index, len(filtered_timeline))
        if l in boring_sents:
            boring_seg = segment_index
            print("Boring segment: ", segment_index, len(filtered_timeline))
        # print(l, filtered_timeline, segment_timeline, segment_index)
        if (l + n) == len(timeline):
            break
        if l % n == 0:
            segment_timeline.append([])
            segment_index += 1
        if l % n == 1 and l > 2*n:
            w1 = 1 - ( ( ( l % n + 1 ) - 1 ) / n) # + 1 for avoiding 0 index
            w2 = 1 - w1
            yc = w1*timeline[l + n] + w2*timeline[l]
            segment_timeline[segment_index - 2].append(yc)
            filtered_timeline.append(sum(segment_timeline[segment_index - 2]) / len(segment_timeline[segment_index - 2]))
            # print("Here")
        # iterate through the 2n+1 part after n has been covered
        if l >= n:
            w1 = 1 - ( ( ( l % n + 1 ) - 1 ) / n) # + 1 for avoiding 0 index
            w2 = 1 - w1
            yc = w1*timeline[l + n] + w2*timeline[l]
            segment_timeline[segment_index - 1].append(yc)
        w1 = 1 - ( ( ( l % n + 1 ) - 1 ) / n) # + 1 for avoiding 0 index
        w2 = 1 - w1
        yc = w1*timeline[l + n] + w2*timeline[l]
        segment_timeline[segment_index].append(yc)

    fig, axs = plt.subplots(2, 1, constrained_layout=True)
    fig.set_size_inches(18.5, 10.5)
    fig.suptitle('Dramatic and Boring should be local minima and maxima (n=' + str(n) + ')', fontsize=16)
    index = dramatic_seg
    axs[0].plot(range(index - 10, index - 10 + len(filtered_timeline[index - 10: index + 10])), filtered_timeline[index - 10: index + 10], label="NAF")
    axs[0].set_title('Dramatic (at ' + str(index) + ')')

    index = boring_seg
    axs[1].plot(range(index - 10, index - 10 + len(filtered_timeline[index - 10: index + 10])), filtered_timeline[index - 10: index + 10], label="NAF")
    axs[1].set_title('Boring (at ' + str(index) + ')')

    plt.show()
```

Myös NAF kokeilu näyttäisi tuottavan tuloksia. Tässä menetelmässä tarinan sentimentti jaetaan segmentteihin, joiden pituus on `2n+1`. Hypoteesini on, että kun `n` on lähellä kappalejakojen keskimääräistä lauseiden määrää, NAF tuottaa parhaan tuloksen mikrotason ilmiöiden löytämiselle. Vastaavasti makrotason ilmiöt (kuten Vonneguthin draamankaaret) varmaan löytyvät lukujen keskimääräisen lausemäärän mukaan. Tämä hypoteesi näyttää pätevän, koska `n=10` tuntuisi olevan lähellä virkkeiden / lauseiden keskimääräistä määrää ja `n=10` näyttäisi tuottavan parhaan tuloksen tässä pientestissä.

Tässä hieman kuvia:

![n=5](n_5.png?raw=true "n=5")

![n=10](n_10.png?raw=true "n=10")

![n=20](n_20.png?raw=true "n=20")

![n=40](n_40.png?raw=true "n=40")

![n=70](n_70.png?raw=true "n=40")

Toinen ajatus on siinä, että lauseet ylipäätään eivät ehkä muodosta optimia tapaa analysoida fiktion sentimenttiä, koska lauseiden pituudella on tyylillisiä merkityksiä enemmän kuin dramaattisia merkityksiä. Kappalejako on pienin yksikkö, joka sisältää koherentisti dramaattisia elementtejä. Jostain syystä tutkimuspaperissa lauseet oli kuitenkin valittu menetelmän ytimeksi; todennäköisesti siksi, että dialogin ja kappalejaon siivoaminen olisi tärkeää, jotta yhtä dialogi riviä ei tulkita kappalejaoksi, kuten monet algoritmit tekevät. Paras mikrotason analyysi saattaisi siis syntyä arvolla `n=1`, jos käytettäisiin kappalejakoja lauseiden sijaan ja dialogit konkatenoitaisiin kappalejaoiksi jonkin pituus jaon mukaan.

Kun lisäsin datapisteitä, näyttää siltä, että kyseessä saattaa myös olla vain sattuma; useammalla dramaattisella kohdalla ei näytä syntyvän samalla tavalla tuloksia. Adaptiivinen Fraktaali Analyysi tuskin pelastaa tilannetta, toki `n=40` näyttää hieman siltä, että Hurstin eksponentilla käsittelyn jälkeen tulos voisi muuttu suotuisammaksi. Periaatteessa toimivan datapisteen suhteen kyse on MICE Inquiryn kysymyskohdasta ja voisi kokeilla jos muut samanlaiset pisteet jäisivät haaviin tai jos muiden MICE kohtien alkupisteet jäisivät haaviin; tämä olisi myös tärkeä indikaattori Promises datapisteille Sandersonin teoriassa.
