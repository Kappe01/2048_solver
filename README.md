# 2048_solver

## Dokumentaatio
[Määrittelydokumentti](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/maarittelydokumentti.md)

### Viikkoraportit
[Viikko 1](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/viikkoraportti_1.md)
[Viikko 2](https://github.com/Kappe01/2048_solver/blob/main/Dokumentaatio/viikkoraportti_2.md)

## Asennus

1. Asenna riippuvuudet komennolla:
```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet:
```bash
poetry run invoke build
```

3. Käynnistä sovellus:
```bash
poetry run invoke start
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

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tarkistukset koodin laadusta voi suorittaa komennolla:

```bash
poetry run invoke lint
```


