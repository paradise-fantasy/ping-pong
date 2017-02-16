# ping-pong
Sick app for bordtennisbord
- [Kort om arkitektur](#kort-om-arkitektur)
- [Utvikling](#development)
  - [API](#api)
  - [Game](#game)
  - [Screen](#screen)
  - [Portal](#portal)

# Kort om arkitektur
![Basic Deployment Architecture](https://s3-eu-west-1.amazonaws.com/ping-pong.komstek.no/assets/Basic+Deployment+Architecture.png)

## Komponentene
Applikasjonen består av en mengde komponenter:
- DB (MySQL)
- API (Django)
- Game (Python med Flask-socketIO ++)
- Portal (React)
- Web (React)
- Nginx (for reverse proxy)

__API__: Laget i Django, avhenger av __DB__, MySQL-databasen.

__Game__: Selve "spill-logikken". Tar input fra kortleser og knapper, kommuniserer events gjennom en websocket (Flask-socketIO) til klienten (i utgangspunktet kun screen). Når en rangert kamp er over poster den match-data til __API__.

__Portal__: En nettside for oversikt over "ligaen", brukes også for registering av nye brukere. Kommuniserer kun med __API__.

__Screen__: En nettside som viser spillets gang, skal i utgangspunktet kun vises ett sted (på skjermen ved bordtennisbordet). Kommuniserer med __API__ og __Game__.

Under utvikling trenger man ikke kjøre alle komponentene i applikasjonen, men man må ha alle avhengigheter kjørende. For eksempel må både __API__ og __Game__ kjøre for å kunne utvikle på __Screen__.

## Docker
I deployment kjører vi alt i Docker. Dette har en rekke fordeler:
- Enklere å porte applikasjonen til nye enheter
- Bedre oversikt over prosjektet som helhet
- Enklere å utvikle på egen maskin (når bildene først er bygget)

..og noen ulemper:
- Man må sette seg inn i deployment-rutiner for å få gjort endringer i prod.
- Vanskelig å lage bilder som fungerer på både RPi og egen maskin

Bruk av Docker står forklart i egen seksjon.. etter hvert

# Development

## API
__Referanser__:
- https://docs.docker.com/compose/django/
- https://docs.djangoproject.com
- http://www.django-rest-framework.org/

For å utvikle på APIet anbefales det å bruke Docker. Ettersom APIet avhenger av en MySQL-database, og vi ikke ønsker å utvikle på produksjonsdatabasen, er det bedre å hoste en egen lokalt. Dette gjøres enkelt med `docker-compose`.

```
docker-compose build api
docker-compose run api
```

Docker spinner automatisk opp et MySQL-bilde som APIet kan snakke med, og deretter bildet til APIet. Filene i `/api` er mountet i API-bildet, så endringer i koden skal vanligvis oppdages og oppdateres i bildet automatisk. APIet kjører på `localhost:8000`.

### Hensyn ved første kjøring (migrasjoner)
Ved første kjøring krever APIet at man utfører "migrasjoner". Migrasjoner utfører MySQL-spørringer for at databasen skal gjenspeile Django-modellene. For å kjøre migrasjoner kan man kjøre:

```
docker-compose run api python manage.py migrate
```

### Installering av nye biblioteker
Dersom man trenger nye pip-biblioteker i APIet må man legge avhengigheten inn i `requirements.txt`, og deretter bygge bildet på nytt med `docker-compose build api`.

### Lage/endre modeller - Nye migrasjoner
Dersom man endrer eller lager nye modeller i Django må man lage og kjøre migrasjoner på databasen. Dette gjøres på følgende måte:

```
docker-compose run api python manage.py makemigrations
docker-compose run api python manage.py migrate
```


## Game
For å utvikle på Game er det greiest å kjøre i et virtuelt miljø, enten på Rasberry Pi eller på egen maskin. Game avhenger av __API__ for å kunne poste matcher, men denne avhengiheten er sjelden noe man trenger å tenke på.

### Virtuelt miljø
Den enkleste måten å utvikle på er ved å bruke et virtuelt miljø (virtual environment). Installér `virtualenv` som beskrevet [her](https://virtualenv.pypa.io) (`virtualenvwrapper` anbefales også) og lag et nytt environment. Du kan deretter installere avhengigheter med:

```
pip install -r requirements.txt
```

__Merk__: Utvikling i virtuelt miljø, uansett om det er på RPi eller på egen maskin, er ingen garanti for at koden kommer til å kjøre i Docker-bildet. Det er lurt å jevnlig teste at koden kjører på det nye bildet.

### Ekte og Simulert Hardware
For å gjøre det mulig å utvikle både på RPi og egen maskin, har vi laget en abstraksjon av "hardware" som heter "simulated hardware". Den simulerte hardwaren leser keyboard-input og lager events basert på kommandoer. For å aktivere simulert hardware må man sette environment variabelen `USE_SIMULATED_HARDWARE=True`.

### Kjøring av Game
For å kjøre programmet kjører man `main.py`:

```bash
python main.py
# eller, for å kjøre med simulert hardware
USE_SIMULATED_HARDWARE=True python main.py
```

### Installering av nye biblioteker
Dersom man installerer nye pip-biblioteker i Game må man legge avhengigheten inn i `requirements.txt`. Dersom man jobber i et virtuelt milø uten overflødige biblioteker installert, kan man bruke `pip freeze > requirements.txt` for å oppdatere avhengighetene.


## Screen
__Referanser__:
- https://github.com/facebookincubator/create-react-app
- http://socket.io/

For å utvikle på Screen må __API__ og __Game__ kjøre enten lokalt eller i produksjon. Du bør ha en forholdsvis ny versjon av `node`, helst `7.4.0` eller høyere.

### Installasjon
Installér først `create-react-app` globalt, deretter prosjektets avhengigheter.

```
npm install -g create-react-app
npm install
```

__Note:__ Pass på å kjøre `npm install` i riktig mappe, altså `/web`.

### Kjøring
For å kjøre en dev-server med hot-reload kan du bruke `npm start`.

### Environment variabler
Vi bruker environment variabler for å spesifisere endepunktene til __API__ og __Game__. Disse må være spesifisert i en fil kalt `.env` - den er ignorert av git, så man må lage den selv. Avhengig av hvilke adresser de to endepunktene har kan `.env` for eksempel se ut som dette:

```
REACT_APP_SOCKET_HOST=localhost
REACT_APP_SOCKET_PORT=5000
REACT_APP_API_HOST=localhost
REACT_APP_API_PORT=8000
```

_Mer om dette kan du lese her: [create-react-app docs: .env](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#adding-custom-environment-variables)_


## Portal
__Referanser__:
- https://github.com/facebookincubator/create-react-app

For å utvikle på Portal må __API__ kjøre enten lokalt eller i produksjon. Du bør ha en forholdsvis ny versjon av `node`, helst `7.4.0` eller høyere.

### Installasjon
Installér først `create-react-app` globalt, deretter prosjektets avhengigheter.

```
npm install -g create-react-app
npm install
```

__Note:__ Pass på å kjøre `npm install` i riktig mappe, altså `/portal`.

### Kjøring
For å kjøre en dev-server med hot-reload kan du bruke `npm start`.

### Environment variabler
Vi bruker environment variabler for å spesifisere endepunktene til __API__. Disse må være spesifisert i en fil kalt `.env` - den er ignorert av git, så man må lage den selv. Avhengig av hvilke adresser de to endepunktene har kan `.env` for eksempel se ut som dette:

```
REACT_APP_API_HOST=localhost
REACT_APP_API_PORT=8000
```

_Mer om dette kan du lese her: [create-react-app docs: .env](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#adding-custom-environment-variables)_
