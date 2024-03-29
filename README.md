# 2048_solver

## Dokumentaatio
[Määrittelydokumentti](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/maarittelydokumentti.md)

[Testausdokumentti](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/testaus_dokementti.md)

[Toteutusdokumennti](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/toteutusraportti.md)

[Käyttöohje](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/kayttoohje.md)
### Viikkoraportit
[Viikko 1](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/viikkoraportti_1.md)

[Viikko 2](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/viikkoraportti_2.md)

[Viikko 3](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/viikkoraportti_3.md)

[Viikko 4](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/viikkoraportti_4.md)

[Viikko 5](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/viikkoraportti_5.md)

[Viikko 6](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/viikkoraportti_6.md)
## Asennus

1. Asenna riippuvuudet komennolla:
```bash
poetry install
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```
![Testikattavuus](./Dokumentaatio/Kuvat/coverage_viikko3.png)

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tarkistukset koodin laadusta voi suorittaa komennolla:

```bash
poetry run invoke lint
```


