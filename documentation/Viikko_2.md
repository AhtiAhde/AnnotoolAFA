# Viikko 2

Pohdin tätä testaus puolta... ei ole ihan helppo homma Python + Flask + Alchemy kombolla tehdä luotettavaa testiympäristöä projektille jossa tietokannan vahinko deletoiminen joskus jatkossa olisi isoin paha; en myöskään halua tehdä tätä niin että unohdan jonkun epäoptimin ratkaisun jonnekin syvälle ja sitten joskus itse väsyneenä tai joku apulainen tekee sen taikatempun, että tuotannossa ajetaan yksikkötestejä vahingossa ja huomataan että TearDown prosessi tuhosi tietokannat (no toki backupit pitää olla olemassa jne.).

Optimaalinen tietokannan Mockaus olisi in-memory tietokanta, joka on olemassa ainoastaan testien ajan. PostgreSQL:ssä ei näemmä tämmöistä ole ja koska joitakin transaktioita pitää suorittaa multirow insertteinä, sekä Flaskin SQLAlchemy on vähän susi niin en voi käyttää ORMia pelkästään. Kun en voi käyttää ORMia niin en voi käyttää testeissä SQLiteä tai MySQL:ää, jossa in-memory testaus onnistuu...

Postgresissa tyypillisesti testikanta tehdään eri userille ja tietokannalle, mutta se miten tämä on joskus aiemmin tehty eivät nyt toimikaan tässä setupissa jonka olen luonut.

Ilmeisesti paras tapa kuintekin olisi kirjoittaa homma (se toinen softa johon tämä perustuu) hieman uusiksi siten, että userilla olisi default schema, josta hän hakee (ALTER ROLE your_user IN DATABASE your_db SET search_path TO your_schema;); tätä ilmeisesti SQL Alchemykin tukee natiivisti. Eli olisi tuo annotool schema ja sitten tuo unittest schema, jossa tietokantojen taulut truncatoitaisiin aina testi session aluksi ja testien välillä mahdollisesti. Jatkan tämän selvittelyä ensi viikolla ja keskityn oikeisiin ongelmiin.

