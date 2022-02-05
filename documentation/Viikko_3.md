# Viikko 3

Compound arvo sentimentti analyysissä näyttää tuottavan signaalin amplitudiksi kelpaavan kuvaajan, seuraavaksi pitäisi siis sitten alkaa sovittamaan ikkunoihin polynomeja ja suorittaa niille Hurstin eksponenttiin perustuva tasoitus soveltamalla epälineaarista adaptiivista filteröintiä ja adaptiivista fraktaali analyysiä.

Lisäsin pydocsit, niiden tarkistajan, lintterin ja code coveragen, sekä aliotin kirjoittamaan testaus dokumenttia.

Intervallisumma kokeilu tuottikin yllättävän hyviä tuloksia; se muistuttaa hieman epälineaarisen adaptiivisen filtteröinnin ja adaptiivisen fraktaali analyysin yhdistelmän perusideaa, jossa havaitaan Hurstin eksponentin muutokset dynaamisesti tasatuissa aikaikkunoissa. Seuraavaksi voisi rakentaa lisää esimerkkejä ja katsoa golden rank henkisesti (eli haluttujen asioiden etäisyys listan kärjestä) miten ne osuvat virhemarginaaliin, jossa satunnaisvalintaa pidetään baselinenä.