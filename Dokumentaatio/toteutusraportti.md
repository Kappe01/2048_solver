# Toteutusraportti

### 2048 ratkoja

2048 ratkoja on toteutettu expectimax algoritmia käyttäen. Expectimaxin tietorakenteena toimii haku puu. 

### Miten toimii

Ratkoja luo itse puun jokaisesta mahdollisesta siirrosta (vasemmalle, oikealle, ylös tai alas) halutulla syvyydellä. Puun nodeille annetaan arvoksi jokin luku joka kertoo miten hyvä tilanne laudalla on. Kun kaikki nodet on luotu hakee algoritmi expectimaxin avulla noden korkeimmalla arvolla ja palauttaa siirron joka tapahtuisi ensimmäisenä. Tämän jälkeen ratkoja liikuttaa lautaa parhaan siirron mukaan jonka jälkeen ratkoja luo uudelleen nodet halutulla syvyydellä ja hakee parhaan siirron.

### O(n) toteutumat

Hakupuun nodet luodaan ajassa O(n^s) missä n on eri siirtojen lukumäärä (4) ja s on syvyys eli hakupuun lopputulos = O(4^s). Expectimxin pitäisi toimia samalla nopeudella. Tilavaativuudeltaan Hakupuun tekeminen on O(4 * s) missä s on syvyys ja sama on myös expectimaxissa.


### Työn puutteet ja parannukset

Tällähetkellä (viikko 6 loppupuoli) ratkoja ei vielä pysty ratkaisemaan peliä. Parannuksena minun pitää parantaa heurestiikkaa sillä siirron haku algoritmi näyttää ainakin toimivan oikein.

### Tekoälyn käyttö.
Tekoälyä on käytetty hieman bugien korjaamiseen mutta ei sen enempää.

### Lähteet 
[Expecimax, geek for geeks](https://www.geeksforgeeks.org/expectimax-algorithm-in-game-theory/)

