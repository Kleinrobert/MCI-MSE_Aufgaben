# Beschreibung der Anwendungsfälle

## UML-Diagramm

![](UML_UseCase_Ergometer.svg)

## Tabellen


### UC 2.0. - Auswertung der Leistungsdaten


|                                |                                                                                                                                                                               | Beispiel                                                                                                                                         |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Name und Identifikationsnummer |                                                                                                   UC 2.0. - Auswertung der Leistungsdaten                                                                                                                |
| Beschreibung                   |                                                                                                                | Die Diagnostiker:in führt das Programm aus, welche alle neuen Daten zu Leistungstests einliest und nacheinander aufbereitet. Die Diagnostiker:in kann alle Tests bewerten und dann abspeichern   |
| Beteiligte Akteure             |                                                                                                       | Diagnostiker:in                                                                                                                    |
| Status                         |                                                                                                              | In Arbeit                                                                                                                                        |
| Verwendete Anwendungsfälle     |                                                                                    | UC 2.1, UC 2.2, UC 2.3, UC 2.4, UC 2.6, UC 2.6                                                                                                          |
| Auslöser                       |                                                                                                   | Nachbereitung einer Leistungsdiagnose durch Diagnostiker:in                                                                                           |
| Vorbedingungen                 |                                                                                           | Daten sind vollständig vorhanden (UC 1.0)                                                                                                                                            |
| Invarianten                    |  | Originial-Aufzeichnung bleiben vorhanden, bis verarbeitete Daten gespeichert werden                                                                        |
| Nachbedingung/Ergebnis         |                                                                                                   | Grafiken und Auswertungen sind gespeichert. Eingangsordner ist leer.                                                                    |
| Standardablauf                 |                                     | Alle Leistungsstufen werden nacheinander durchlaufen. Überprüfung, ob Widerstandswerte eingehalten. Daten werden gespeichert.                     |
| Alternative Ablaufschritte     |                                           | Diagnostiker:in erkennt Abbruchgrund und gibt diesen ein. Eingabe wird dokumentiert und mit Daten gespeichert.                                                                         |
| Hinweise                       |            | keine                                                                                                                                            |
| Änderungsgeschichte            |                                                                                                                                                    | 0.01; 19.03.2022.; Robert Klein und Nikon Muigg                                                                                                                  |
|                                |                                                                                                                                                                                         |                                                                                                                                                  |


