# Viikko 2

Pohdin tätä testaus puolta... ei ole ihan helppo homma Python + Flask + Alchemy kombolla tehdä luotettavaa testiympäristöä projektille jossa tietokannan vahinko deletoiminen joskus jatkossa olisi isoin paha; en myöskään halua tehdä tätä niin että unohdan jonkun epäoptimin ratkaisun jonnekin syvälle ja sitten joskus itse väsyneenä tai joku apulainen tekee sen taikatempun, että tuotannossa ajetaan yksikkötestejä vahingossa ja huomataan että TearDown prosessi tuhosi tietokannat (no toki backupit pitää olla olemassa jne.).

Optimaalinen tietokannan Mockaus olisi in-memory tietokanta, joka on olemassa ainoastaan testien ajan. PostgreSQL:ssä ei näemmä tämmöistä ole ja koska joitakin transaktioita pitää suorittaa multirow insertteinä, sekä Flaskin SQLAlchemy on vähän susi niin en voi käyttää ORMia pelkästään. Kun en voi käyttää ORMia niin en voi käyttää testeissä SQLiteä tai MySQL:ää, jossa in-memory testaus onnistuu...

Postgresissa tyypillisesti testikanta tehdään eri userille ja tietokannalle, mutta se miten tämä on joskus aiemmin tehty eivät nyt toimikaan tässä setupissa jonka olen luonut.

Ilmeisesti paras tapa kuintekin olisi kirjoittaa homma (se toinen softa johon tämä perustuu) hieman uusiksi siten, että userilla olisi default schema, josta hän hakee (ALTER ROLE your_user IN DATABASE your_db SET search_path TO your_schema;); tätä ilmeisesti SQL Alchemykin tukee natiivisti. Eli olisi tuo annotool schema ja sitten tuo unittest schema, jossa tietokantojen taulut truncatoitaisiin aina testi session aluksi ja testien välillä mahdollisesti. Jatkan tämän selvittelyä ensi viikolla ja keskityn oikeisiin ongelmiin.

Koitan keskittää projektin oleellisen koodin Book_Analytics luokkaan ja testailen sitten sitä testeillä. Teksti korpuksien dataa ja ominaisuuksia tutkiskelen notebookeissa, joista sitten siirrän toimivat ideat Book_Analytics luokkaan.

Aloittelen tässä sen tutkimuspaperin soveltamista The Great Gatsby kirjaan. Kokeilen ensin, että 1) pystyykö sentimentti sanasto poimimaan merkittäviä kohtia teoksesta ollenkaan, 2) onko laadullisesti eroa ovatko ikkunat täysin samanmittaisia, vai toimiiko myös kappalejako perustainen analyysi jotenkin normalisoituna, 3) saanko menetelmän osumaan annotoituihin testi kappaleisiin tai ylipäätään indikoiko menetelmä hyviä annotoitavia kappaleita millään sanastolla.

## Paperin toteutusta

### Non-linear Adaptive Filtering

Aineiston jakaminen ikkunoihin on helppoa ja tehty. Seuraavaksi pitäisi ymmärtää paperin kohta 2.1. syvällisemmin.

#### Kernel Adaptive Filetring

#### Adaptive Filtering

#### Transfer function in discrete time system

#### Decscribing Function

Wiki: Describing function; Nonlinear control

https://en.wikipedia.org/wiki/Describing_function

Wiki: "It is based on quasi-linearization, which is the approximation of the non-linear system under investigation by a linear time-invariant (LTI) transfer function that depends on the amplitude of the input waveform"

Diskreetissä systeemissä siis ne ikkunat luovat amplitude of the input wave form, perustuen codewordsien esiintyvyyteen / windowin sanojen määrä.

Wiki: "By definition, a transfer function of a true LTI system cannot depend on the amplitude of the input function because an LTI system is linear. Thus, this dependence on amplitude generates a family of linear systems that are combined in an attempt to capture salient features of the non-linear system behavior."

Eli periaateessa kai tässä "describing function" on se Non-linear Adaptive Filteringin ja Adaptive Fractal Analysisin yhdistelmä?

Deadband input: tilanne jossa windowissa on nolla codewordia.

Wiki: "As the linear system's output amplitude decays, the nonlinearity may move into a different continuous region. This switching from one continuous region to another can generate periodic oscillations. The describing function method attempts to predict characteristics of those oscillations (e.g., their fundamental frequency) by assuming that the slow system acts like a low-pass or bandpass filter that concentrates all energy around a single frequency. Even if the output waveform has several modes, the method can still provide intuition about properties like frequency and possibly amplitude; in this case, the describing function method can be thought of as describing the sliding mode of the feedback system."

Tämä vaikuttaa hyvinkin paperin lopputulokselta, jossa on amplitudia normalisoimalla päästy todentamaan dramaattisten eventtien vaihtelua; frequency on ehkä liian säännöllinen sana kuvaamaan mitä tapahtuu, mutta melko säännöllisesti toistuvia state transitioita ainakin on havaittavissa ja vieläpä selvästi.

#### Transfer funktioita ei ole olemassa useille epälineaarisille yhtälöille

Super positio propertyä ei ole olemassa epälineaarisille systeemeile. Additive state decomposition voidaan määritellä epälineaarisille systeemeille (tämä yhtälö näyttää hieman samalta kuin non-linear adaptive filteringin yhtälö); lineaarisissa systeemeissä inputit ja outputit ikään kuin summautuvat, epälineaarisissa eivät. Epälineaarisia systeemejä voidaan kuitenkin yrittää kuvata, esimerkiksi ottamalla globaali keskiarvo syötteeksi, jonka avulla voidaan laskea transfer funktio. Fraktaaleissa menetelmissä ei ehkä oteta globaalia keskiarvoa, vaan jokin liukuvakeskiarvo, jonka jälkeen liukuvan keskiarvon alueella oleville ikkunoille voidaan laskea transfer functionin arvo.

#### Non-linear systems

Wikipediasta:
"Typically, the behavior of a nonlinear system is described in mathematics by a nonlinear system of equations, which is a set of simultaneous equations in which the unknowns (or the unknown functions in the case of differential equations) appear as variables of a polynomial of degree higher than one or in the argument of a function which is not a polynomial of degree one. In other words, in a nonlinear system of equations, the equation(s) to be solved cannot be written as a linear combination of the unknown variables or functions that appear in them. Systems can be defined as nonlinear, regardless of whether known linear functions appear in the equations. In particular, a differential equation is linear if it is linear in terms of the unknown function and its derivatives, even if nonlinear in terms of the other variables appearing in it."

Tämä näyttäisi liittyvän paperin kohtaan "Then, for each segment, we fit a polynomial of order D. Note that D=0 means a piece-wise constant, and D=1 a linear fit."