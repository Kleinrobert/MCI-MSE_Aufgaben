## Project background

### Purpose of project
Das Ziel des Projektes ist es eine Software zur Leistungsdiagnostik, basierend auf einem Ergometer, zu erstellen.


### Scope of project
Die Software soll herausfinden ob die Messungen gültig sind. Jede Messung einer Person zuordnen und die erfolgreichen Messungen in einem Ordner speichern sowie die ungültigen in einem anderen Ordner speichern.

### Other background information

Die die abgeschlossenen Tests werden vom Ergometer als separate Dateien (Zeitreihe mit Leistung und Herzrate) gespeichert.

## Perspectives

### Who will use the system?

Das System wird vom Diagnostiker benutzt. 


### Who can provide input about the system?

Der Proband:in und der Softwareentwickler.


## Project Objectives
Ziel ist es eine fehlerfreie Software für das Ergometer zu erstellen.

### Known business rules

Das System sollte auf einer Low-Code-Lösung basieren

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies


Die power_data gibt die Watt Leistung zu jeder Sekunde des Tests an, der 180 Sekunden lang andauert.
Die Datei subjet_ gibt Details über die Testperson. Hier wird die Nummer der Testperson, die Testleistung, das Geburtstjahr und die Länge des Tests angegeben.
Die ecg_data_subject gibt die EKG Daten für die jeweilige Testperson an. Die Messung wird pro Sekunde 1000 mal durchgeführt, wodurch man dann 180.000 Messwerte zur Verfügung hat.

### Design and implementation constraints

In einer Erweiterung könnte das Design verbessert werden.  

## Risks

Risiken können vor allem durch falsche Daten entstehen. So kann beispielsweise bei einer falschen Ausgabe von Pulswerten der Sportler überfordert werden und so auch überlastet werden. Außerdem kann durch falsche oder ungenaue Daten die wirkliche Leistungsstärke der Proband:in nicht genau bestimmt werden.


## Known future enhancements

Dass die Diagnostiker durch das Interface durch den Leistungstest geführt werden.
Und dass sobald Risiken für den Sportler auftreten können das System das erkennt und abbricht.

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues


