# Vaatimusmäärittely dokumentti

## Laajempi kokonaisuus

Olen tutkiskellut ongelmaan "Miten tekoäly voisi ymmärtää narratiivien draaman kaaria" vuodesta 2016 alkaen. Kielimalleja, kuten BERT ja GPT-3, on käytetty laskennallisen luovuuden ongelmiin hyödyntäen kielimallien generatiivisia ominaisuuksia. Toisaalta tulokset vaikuttavat olevan epämielenkiintoisia ilman ihmisen tekemää "cherry-pick" prosessia, jonka vuoksi menestys siis perustuu hermeneuttiseen suhteeseen taiteilijan kanssa, eikä niinkään tilastolliseen luotettavuuteen. Isojen kielimallien kyky ymmärtää tekstin semanttista merkitystä on isosti kyseenalaistettu tutkimuksissa, joita on koottu esimerkiksi [tänne][1] ja [tänne][2]. Olen koostanut kahdeksan ammatillisessa käytössä olevan kirjoitusteorian pohjalta narratiivisen mallin, jonka pohjalta ainakin osittainen semanttinen ymmärrys voisi mahdollistua nimenomaan draaman kaaria analysoitaessa. Käytännössä ammattikirjoittajat ymmärtävät, että tekstin lisäksi on olemassa subteksti, joka määrittelee narratiivin luonnetta ja tämän rakenteen koneellinen löytäminen voi olla merkittävää.

Richard Walsh kirjoittaa [Narrating Complexity tutkimuskokoelmassa][3], että narratiivit muodostuvat käsitteistä, joilla on lokaali määrittely, mutta globaali vaikuttavuus. Monet fraktaalit menetelmät ovat menestyneet tämmöisissä rakenteissa. Esimerkiksi [tutkija ryhmä vuonna 2020][4] onnistui löytämään Nobelin kirjallisuuspalkinnon saaneesta kirjasta dramaattiset kohokohdat esiin käyttäen sentimentti sanastoja adaptiivisen fraktaalianalyysin (AFA) ja epälineaarisen filtteröinnin yhdistelmällä. Menetelmässä data ensiksi pilkotaan ikkunoihin, jonka jälkeen tarkkaillaan AFAn avulla sentimenttisanojen esiintyvyyttä. Tilastomatemaattisesti kyse on eräänlaisesta dynaamisesta liukuvasta keskiarvosta (normaalin staattisen välin liukuvan keskiarvon sijaan). Toisaalta kirja oli tarkoin valittu sopivaksi sentimentti sanaston puolesta. Tämä herättää jatkotutkimuskysymyksen sen suhteen, että voidaanko sanastoja yleistää.

## Tässä projektissa

Jotta tämmöisen semanttisen rakenteen hakumallin voisi yleistää, olen rakentanut viitekehyksen narratiivien semanttiseen mallintamiseen, joka perustuu kolmeen aiemmin mainitsemaani kirjoitusteoriaan. Näillä kaikilla teorioilla on vahva fraktaalinen luonne: ne perustuvat toistuviin rakenteisiin, jotka toistuvat eri skaaloissa, mutta saman muotoisina (eri sisällöllä). Nämä kirjoitusteoriat myös kuvaavat näiden elementtien sisältövaatimuksia tavoilla, joiden pohjalta on mahdollista rakentaa sanastoja. Yleistyvätkö nämä rakenteet hyvin käytännön kirjoihin on siis hyvä kysymys. Käytän siis ensin sentimentti sanastoja, jonka jälkeen yritän yleistää kirjoitusteorioiden erityispiirteisiin. Valitsemani kirjoitusteoriat ovat Mary Robinette Kowalin "MICE Quotient", Brandon Sandersonin "Promises, Progresses and Payoffs", sekä Chris Huntleyn "Dramatica". Olen jo aiemmin luonut hyvin toimivan käytettävyyden (kokonaisuus yhä vahvasti esijulkaisuvaiheessa; kesällä 2022 ehkä valmista) näiden menetelmien käyttämiseen annotoimisessa matalan kognitiivisen kuorman mukaan suunnitellen ja esitestannut kokonaisuutta The Great Gatsby ja Pride and Prejudice teosten kanssa (ne omaavat valmiit Dramatica kaaret ja ovat saatavissa Project Gutenbergissä).

Hakumallin lisäksi on mahdollista luoda myös uudenlainen kielimalli. Isommassa kuvassa on myös [osoitettu tutkimuksessa][11], että BERTin voi kouluttaa tunnistamaan sentimenttirakenteita suurin piirtein kappalejaon mittaisista tekstipätkistä. Jos siis olisi annotoitua dataa, voisi BERTin myös kouluttaa tunnistamaan näitä semanttisia narratiivien rakenteita. Ja tosiaan, [Walshin mukaan][3] narratiivien ymmärtämisessä on keskeistä se, että pystytään karoittamaan mikrotason tekstiä makrotason subtekstiksi. Tähän tarkoitukseen erityisesti sopisivat Dramatica teorian mikrotason rakenteet. Tämmöinen BERT olisi käytännössä Bellmannin yhtälö tekstin ja subtekstin välillä, joka voisi johtaa samanlaisiin mahdollisuuksien kasvuun narratiivisen älyntutkimuksessa, kuin johon yllettin kuvantunnistamisessa ImageNetin avulla. Jotta tämmöisen kielimallin rakentaminen olisi mahdollista, pitäisi siis kerätä annotoitua dataa. Valitettavasti kirjat omaavat harvakseen (sparse) tämmöisiä tapahtumia, joiden annotoimisesta olisi hyötyä. Tästä syystä kehitän tässä projektissa menetelmää (hakumalli), joka pystyisi kirjoitusteoriakehikkoni mukaan rakentamaan priorisoituja listoja kirjojen kappaleista, joissa isolla todennäköisyydellä olisi tietynlaisia semanttisia narratiivisesti merkittäviä tapahtumia.

## Ydintavoite (vertaisarvioijalle)

Idea on ottaa kirjoja tekstinä sisään, pilkkoa ne 500 sanan ikkunoiksi perustuen suurinpiirtein kappalejakoihin. Näistä olisi sitten ideana rakentaa priorisoitu lista käyttäen [tämän (Hu et. al. 2020) paperin][4] esittelemiä menetelmiä ja mahdollisesti kokeilla sentimentti sanastojen sijaan myös muita mahdollisia sanastoja, jotka perustuvat isommassa projektissa käyttämiini kirjoitusteorioihin.

## Tärkeitä teknisiä piirteitä

Teen tämän projektin Python-kielellä. Syötteenä toimivat Project Gutenbergista saatavat kirjat (tähän on jo skriptat) ja tuotoksena toimii priorisoitu lista kirjojen kappaleista (joka siis viedään jo kehityksen alla olevaan annotointityökaluun). Kappaleiden pituus ja täten ikkunan yhteiskoko on n. 500 sanaa perustuen BERTin teknisiin rajoituksiin. Prosessia ajetaan taustalla ja ainoastaan kerran tai korkeintaan harvoin, jonka vuoksi aikahaastavuus tai muistijälki eivät sinänsä ole ongelmia. Toisaalta AFA toimii parhaan käsitykseni mukaan O(n log n) nopeudella ja pienellä muistijäljellä, joten ongelmia ei tässäkään mielessä pitäisi syntyä.

## Kurssiin liittyviä lisätietoja

Kuulun TKT kandiohjelmaan ja toteutan projektin englanniksi. Pystyn vertaisarvioimaan hyvin Golangia ja Pythonia (muita osaamiani kieliä tuskin käytetään tällä kurssilla).

## Lähdeluettelo

1: What does it mean for AI to Understand: https://www.quantamagazine.org/what-does-it-mean-for-ai-to-understand-20211216/

2: Limitations of scaling up AI language models: https://venturebeat.com/2021/12/10/the-limitations-of-scaling-up-ai-language-models/

3: Narrating Complexity: https://www.academia.edu/39366860/Narrative_Theory_for_Complexity_Scientists

4: Dynamic evolution of sentiments in Never Let Me Go: Insights from multifractal theory and its implications for literary analysis: https://academic.oup.com/dsh/article/36/2/322/5856850

5: A tutorial introduction to adaptive fractal analysis: https://www.researchgate.net/publication/232236967_A_tutorial_introduction_to_adaptive_fractal_analysis

6: Fractal Analysis of Time-Series Data Sets: Methods and Challenges: https://www.intechopen.com/chapters/64463

7: Detrended Fluctuation Analysis and Adaptive Fractal Analysis of Stride Time Data in Parkinson's Disease: Stitching Together Short Gait Trials: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0085787

8: MICE quotient: https://www.youtube.com/watch?v=blehVIDyuXk

9: Promises, Progresses, Payoffs: https://www.youtube.com/watch?v=0cf-qdZ7GbA&list=PLSH_xM-KC3Zv-79sVZTTj-YA6IAqh8qeQ

10: Dramatica: https://dramatica.com/theory/book

11: Modeling Label Semantics for Predicting Emotional Reactions: https://arxiv.org/abs/2006.05489

[1]: https://www.quantamagazine.org/what-does-it-mean-for-ai-to-understand-20211216/

[2]: https://venturebeat.com/2021/12/10/the-limitations-of-scaling-up-ai-language-models/

[3]: https://www.academia.edu/39366860/Narrative_Theory_for_Complexity_Scientists

[4]: https://academic.oup.com/dsh/article/36/2/322/5856850

[5]: https://www.researchgate.net/publication/232236967_A_tutorial_introduction_to_adaptive_fractal_analysis

[6]: https://www.intechopen.com/chapters/64463

[7]: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0085787

[8]: https://www.youtube.com/watch?v=blehVIDyuXk

[9]: https://www.youtube.com/watch?v=0cf-qdZ7GbA&list=PLSH_xM-KC3Zv-79sVZTTj-YA6IAqh8qeQ

[10]: https://dramatica.com/theory/book

[11]: https://arxiv.org/abs/2006.05489

