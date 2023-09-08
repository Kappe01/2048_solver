## Määrittelydokumentti

### 2048 pelin ratkoja pythonilla

Projektin tarkoituksena on tehdä tekoäly joka pystyy ratkaisemaan 2048 pelin. Ohjelmointi kielenä toimii python ja dokumentaation kielenä Suomi. Kuulun TKT opinto-ohjelmaan

### Tietorakenteet ja algoritmit

- Minmax algoritmi 
- Expectimax algoritmi
- Hakupuu tietorakenne

Vaikka algoritmit toimivat samalla perjaatteella on niitä minun mielestä hyvä tarkastella sillä minmax toimii pienimmällä riskillä ja on todennäköisesti varmempi tapa ratkaista peli ja expectimax on sitten todennäköisesti parempi tapa jos haluaa päästä pelissä yli 2048. Molemmat algoritmit käyttävät tietorakenteenaan haku puuta.

### O analyysit

Expectimax algoritmin aikavaatimus on O(n^m) missä n on "oksien määrä" ja m on haun syvyys. Tilavaativuus on O(n*m). 

Minmax algoritmin aikavaativuus sekä tilavaatimus ovat samat expectimaxin kanssa.

### Input ja output

Tekoäly saa syötteenä aloitus kentän ja lopputulos on toivottavasti ratkaistu peli.

### GUI

Graafinen käyttöliittymä toteutetaan pygamella.

### Lähteet
[MinMax](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)

[Expectimax](https://www.geeksforgeeks.org/expectimax-algorithm-in-game-theory/)

[2048](https://2048game.com/)

