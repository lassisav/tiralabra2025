# Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit
## Lassi Savolainen, fil.yo tietojenkäsittelytieteen kandiohjelmassa, 2025
### Määrittelydokumentti


#### Harjoitustyön ydin

Harjoitustyössä vertaillaan [konveksin verhon](https://en.wikipedia.org/wiki/Convex_hull) selvittämiseen käytettäviä [algoritmeja](https://en.wikipedia.org/wiki/Convex_hull_algorithms)

#### Työssä käytettävät ohjelmointikielet

Harjoitustyö toteutetaan Pythonilla.

#### Työssä käytettävät algoritmit ja tietorakenteet.

Harjoitustyössä vertaillaan ainakin seuraavia konveksin verhon selvittämisen algoritmeja:

- [Gift wrapping](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm)
- [Graham scan](https://en.wikipedia.org/wiki/Graham_scan)
- [Quickhull](https://en.wikipedia.org/wiki/Quickhull)

Ajan salliessa vertailuun voidaan lisätä muitakin algoritmeja.

#### Työssä ratkaistava ongelma

Työssä demonstroidaan eri algortimien vahvuuksia ja heikkouksia erikokoisilla syötteillä.

Ajan salliessa työssä voidaan vertailla algoritemja myöskin erityisillä syötteillä, jotka ovat tietynlaisille algoritmeille vaikeampia kuin toisille.

#### Työssä käytettävien algoritmien aika- ja tilavaativuudet

Merkiten, että *n* pisteen joukosta löydetään *h* pistettä sisältävä koveksi verho.

- [Gift wrapping](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm)
    - Aikavaativuus O(*n^2^*)
    - Tilavaativuus O(*n*)
- [Graham scan](https://en.wikipedia.org/wiki/Graham_scan)
    - Aikavaativuus O(*n* log *n*)
    - Tilavaativuus O(*n*)
- [Quickhull](https://en.wikipedia.org/wiki/Quickhull)
    - Aikavaativuus O(*n* log *n*)
    - Tilavaativuus O(*n*)

### Muut merkittävät asiat


#### Kurssisuoritus

Kurssi suoritetaan tieojenkäsittelytieteen kandiohjelmassa suomen kielellä.

#### Vertaisarviointikielet

Voin vertaisarvioida ainakin seuraavia kieliä käyttäviä projekteja:

 - Python
 - Java
 - JavaScript