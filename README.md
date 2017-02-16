# ping-pong
Sick app for bordtennisbord
- [Kort om arkitektur](#kort-om-arkitektur)
- [Utvikling](#development)
  - [API](#api)

# Kort om arkitektur
![Basic Deployment Architecture](https://s3-eu-west-1.amazonaws.com/ping-pong.komstek.no/assets/Basic+Deployment+Architecture.png)

## Komponentene
Applikasjonen består av en mengde komponenter:
- Database (MySQL)
- API (Django)
- Game (Python med Flask-socketIO ++)
- Portal (React)
- Web (React)
- Nginx (for reverse proxy)

__API__: Laget i Django, bruker MySQL som database

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

# Med Docker
Prøver å fase inn docker. For å kjøre prosjektet med docker må du ha installert "docker" og "docker-compose" (tror begge er inkludert i docker engine). Deretter må du kjøre følgende (fra roten av prosjektet):

```bash
docker-compose build # Bygger bildene for api og web
docker-compose run api python manage.py migrate # Om du får feilmelding, prøv på nytt
docker-compose up # Starter opp prosjektet
```

`docker-compose build` bygger api-bildet ved hjelp av `Dockerfile` i /api.

`docker-compose run api python manage.py migrate` kjører alle "migrasjoner" for databasen, dvs at Django gjør om "modellene" våre til tables i MySQL-databasen. Ettersom du mest sannsynlig ikke alt har databasebildet vil den først laste dette ned (hypriot/rpi-mysql).

`docker-compose up` starter opp prosjektet og bør gjøre tjenesten tilgjengelig på `http://localhost:8000`.

# Uten Docker

## API
__NB: Krever MySQL__

Installér pip-moduler fra `requirements.txt`

Sett riktige innstillinger for database i `main/settings.py`. Man må sette riktige parametere under `DATABASES`.

Start API-et med:

```
python manage.py runserver 0.0.0.0:8000
```

## Game
Installér pip-moduler fra `requirements.txt`.
Kjør med:

```
python main.py
```

## Web
Prosjektet er laget med [create-react-app](https://github.com/facebookincubator/create-react-app), kan være du må installere det (globalt) først med `npm install -g create-react-app`.
Det du uansett MÅ gjøre for installasjon er:

```
npm install
```

For å starte dev-server kan du kjøre:

```
npm start
```
