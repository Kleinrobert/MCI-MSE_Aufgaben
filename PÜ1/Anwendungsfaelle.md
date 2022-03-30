# Beschreibung der Anwendungsfälle

## UML-Diagramm

![](UML_UseCase_Ergometer.svg)

## Tabellen


### UC 2.5. - Visualisierung der Daten 


|                | Beispiel                                                                                                                                                  | |                                                                                                                                       
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Name und Identifikationsnummer |                                                                                                   UC 2.5. - Visualisierung der Daten                                                                                                                |
| Beschreibung                   |                                                                                                                Die Software wandelt die erhaltenen Daten um in eine graphische Lösung oder gibt die Werte als Zahlen aus.|
| Beteiligte Akteure             |                                                                                                        Diagnostiker:in                                                                                                                    |
| Status                         |                                                                                                               In Arbeit                                                                                                                                        |
| Verwendete Anwendungsfälle     |                                                                                    UC 2.1, UC 2.2, UC 2.3, UC 2.4, UC 2.6 *keine -YS*                                                                                                          |
| Auslöser                       |                                                                                                    Nachbereitung einer Leistungsdiagnose durch Diagnostiker:in                                                                                           |
| Vorbedingungen                 |                                                                                            Daten sind vollständig vorhanden (UC 1.0) *Alle weiteren Schritte die für die Visualisierung notwendig sind sollten voher bearbeitet sein (Daten einlesen, vorverarbeiten, kein Abbruch, etc. -YS*                                                                                                                                            |
| Invarianten                    |   Visualisierung (Graphik) bleibt vorhanden, bis verarbeitete Daten gespeichert werden.                                                                        |
| Nachbedingung/Ergebnis         |                                                                                                    Grafiken und Daten wurden in der gewünschten Form ausgegeben und dargestellt. Eingangsordner ist leer.                                                                    |
| Standardablauf                 |                                      Alle Leistungsstufen werden nacheinander durchlaufen. Überprüfung, ob Widerstandswerte eingehalten. Visualisierung der Daten. Daten werden gespeichert. *Speichern ist nicht mehr Teil von UC 2.6 -YS*                    |
| Alternative Ablaufschritte     |                                            Diagnostiker:in erkennt Abbruchgrund und gibt diesen ein. Eingabe wird dokumentiert und mit Daten gespeichert. Erneuter Durchlauf.                                                                       |
| Hinweise                       |             keine                                                                                                                                            |
| Änderungsgeschichte            |                                                                                                                                                     0.01; 19.03.2022.; Robert Klein und Nikon Muigg                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                       


