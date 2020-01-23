# RailNL

In de case RailNL is het de bedoeling dat je binnen een gegeven tijdsframe een aantal trajecten
uitzet. Een traject is een route van sporen en stations waarover treinen heen en weer rijden.
Hierbij moet gelden dat een traject niet langer mag zijn dan het opgegeven tijdsframe.

## Aan de slag
### Vereisten

In requirements.txt staan alle benodigde packages om het programma succesvol te runnen. Deze zijn
gemakkelijk te installeren via pip door middel van de volgende instructies:

```
pip install -r requirements.txt
```

### Gebruik
In main.py regel 49 kan je specificaties invullen, namelijk:
- **CONNECTIONS_FILE:** Pad naar het bestand met de verschillende connecties.
- **COORDINATES_FILE:** Pad naar het bestand met de coordinaten van een station.
- **BEST_SCHEDULE_FILE:** Pad naar het bestand waar de beste oplossing is opgeslagen van alle runs
ooit uitgevoerd.
- **N:** Het aantal runs.
- **MIN_180 / MIN_120:** Het maximale aantal minuten van een traject.
- **IMPROVE:** Het wel of niet gebruiken van het optimalisatie algoritme
(zie [/code/algorithms/README.md](/code/algorithms/README.md)).
- **DEPTH:** Het aantal lagen waarop het Depth First algoritme wordt toegepast.
- **EXCLUSION:** De naam van de stad die wordt weggelaten.
- **A t/m E:** De heuristiek die wordt toegepast
(zie [/code/algorithms/README.md](/code/algorithms/README.md)).

Run het programma door aan te roepen:

```
python main.py
```

Het beste resultaat van Holland / Nederland wordt gevisualiseerd door de volgende code in main.py
toe te voegen:

```
visualisation(load(BEST_SCHEDULE_FILE))
```

### Structuur

Hieronder volgt wat in iedere map te vinden is.

- **/code:** bevat alle code van dit project.
  - **../algorithms:** bevat de code voor de algoritmes.
  - **../classes:** bevat de code voor de benodigde classes.
  - **../input:** bevat de code voor het inlezen van de benodigde data.
  - **../output:** bevat code om de output te genereren en visualiseren.
- **/data:** bevat de gegevens van connecties en stations.
- **/presentation:** bevat de eindpresentatie.
- **/results:** bevat de output bestanden van de resultaten.

## Auteurs
- Amber Remmelzwaal
- Ilse de Langen
- Stefan van den Berg
