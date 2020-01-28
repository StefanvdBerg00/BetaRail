# Algorithms

Hieronder volgt wat in ieder bestand te vinden is.

## Heuristic
In de Heuristic class zijn verschillende functies te vinden die de heuristiek
vastleggen. Bij het maken van een instantie is een city_function en een
connection_function vereist. Een city function is een van de eerste drie
functies, die bepalen in welke stad het algoritme begint met trajecten
aanleggen: een random stad, de stad met de minste connecties, of de stad met
de meeste connecties. Een connection_function is een van de volgende drie functies,
die specificeren op welke manier connecties worden aangelegd. Overlay_connections
bepaalt door middel van een kansverdeling waar het traject wordt aangelegd.
Verbindingen die al in een ander traject worden bereden, hebben een kleinere kans
dan verbindingen die nog niet bereden zijn. Least_connections zorgt dat het
traject wordt vervolgd naar de stad die de minste connecties heeft.
General_connections returnt alle connecties van de huidige stad, waar later
een random connectie uit wordt gekozen. In run worden, afhankelijk van de
gekozen city_function en connection_function, trajecten gemaakt en toegevoegd
aan de lijnvoering. In main.py kunnen vijf van deze verschillende heuristieken
worden toegepast (A t/m E), die verschillende combinaties van city_functions en
connection_function aanroepen.

## Optimize
In optimize wordt een Depth First algoritme uitgevoerd op een gegeven
lijnvoering. Hierbij wordt geprobeerd een gegenereerde oplossing te verbeteren.
Dit kan door zowel trajecten samen te voegen, of trajecten weg te laten uit de
lijnvoering. Dit algoritme wordt alleen uitgevoerd als de variabele 'IMPROVE' in
main.py op TRUE staat. Het algoritme werkt als volgt:  
Eerst wordt vanuit een bepaalde stad gekeken naar alle mogelijkheden om
trajecten aan elkaar te verbinden. Elke mogelijkheid wordt gerepresenteerd
door een Node. In run wordt via het Depth First algoritme voor elke Node berekend
of deze de doelfunctie zal verhogen. Nadat alle trajecten zijn langsgelopen wordt 
er gekeken naar de beste verbetering. Bij deze verbetering wordt een keuze gemaakt 
tussen het samenvoegen van de trajecten of het verwijderen van het traject waaruit 
depth first werd uitgevoerd. Als laatst, als er geen verbeteringen meer mogelijk 
zijn, wordt er gekeken of het eventueel weglaten van een traject de doelfunctie verhoogd.

## Datastructuur
![Datastructuur](https://github.com/StefanvdBerg00/BetaRail/blob/master/images/datastructureAlgorithms.PNG) *Datastructuur van de algoritmes*
