# Algorithms

Hieronder volgt wat in ieder bestand te vinden is.

## Heuristic
In de Heuristic class zijn verschillende functies te vinden die de heuristiek 
vastleggen. Bij het maken van een instantie is een city_function en een 
connection_function vereist. Een city function is een van de eerste drie 
functies, die bepalen in welke stad het algoritme begint met trajecten 
aanleggen. Een connection_function is een van de volgende drie functies,
die specificeren op welke manier connecties worden aangelegd. In run worden,
afhankelijk van de gekozen heuristiek, trajecten gemaakt en toegevoegd aan 
de lijnvoering. 

## Optimize
In optimize wordt een Depth First algoritme uitgevoerd op een gegeven
lijnvoering. Hierbij wordt geprobeerd een gegenereerde oplossing te verbeteren. 
Dit kan door zowel trajecten samen te voegen, of trajecten weg te laten uit de 
lijnvoering. Dit algoritme wordt alleen uitgevoerd als de variabele 'IMPROVE' in 
main.py op TRUE staat. 