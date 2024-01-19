## Määrittelydokumentti

Jatkan ensimmäisen periodin epäonnistunutta expectimax algoritmiä.

### 2048 pelin ratkoja pythonilla

Projektin tarkoituksena on tehdä tekoäly joka pystyy ratkaisemaan 2048 pelin. Ohjelmointi kielenä toimii python ja dokumentaation kielenä Suomi. Kuulun TKT opinto-ohjelmaan

### Tietorakenteet ja algoritmit

- Expectimax algoritmi
- Hakupuu tietorakenne

Expectimax perustuu samaan perjaatteeseen kuin minmax algoritmi mutta expectimaxin etu tulee siinä että se osaa huomioida pelin epäsäännöllisyyden (ei tiedetä tuleeko 2 vai 4 ja mihin kohtaan)
Expectimax algoritmit käyttävät tietorakenteenaan haku puuta.

### O analyysit

Expectimax algoritmin aikavaatimus on O(n^m) missä n on "oksien määrä" ja m on haun syvyys. Tilavaativuus on O(n*m). 

### Input ja output

Tekoäly saa syötteenä aloitus kentän ja lopputulos on toivottavasti ratkaistu peli.

### GUI

Graafinen käyttöliittymä toteutetaan pygamella.

### Lähteet

[Expectimax](https://www.geeksforgeeks.org/expectimax-algorithm-in-game-theory/)

[2048](https://2048game.com/)

