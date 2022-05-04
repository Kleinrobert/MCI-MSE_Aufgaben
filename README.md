# FinalProject 

## Lernziele des Projektes
In diesem Abschlussprojekt sollen sie bereits gelernte Fähigkeiten auf einen neuen Anwendungsfall anwenden. Dabei sind vor allem folgende Unterpunkte gemeint:
* Objektorientierung
* Algorithmen
* Daten einlesen
* Zeitreihen auswerten
* Darstellung von Daten 

Zusätzlich zu Ihren bereits erlernten Fähigkeiten sollen Sie in diesem Projekt ersten Kontakt mit **Dash** machen, welches eine interaktive Dashboardstruktur in Python bereitstellt. Dabei sollen Sie die grobe Struktur eines solchen Programmes verstehen und bereits entwickelte Interaktionen auf Ihre Problemstellung anpassen können. Außerdem soll das Projekt Ihnen eine Möglichkeit bieten, die **Dash** Oberfläche nach Ihren Vorstellungen und Wünschen zu designen. 

## Github Repo

In diesem Github Repository wird auf das Entwickeln von Dashboards mit Dash eingegangen. Dafür werden verschiedene Beispiele
gestellt ([Example Dashboards](ExampleDashboard)), die einige wichtige Funktionen
und Komponenten von Dash aufzeigen sollen. Zusätzlich wird ein "Gerüst" für das Abschlussprojekt der Programmierübung 2 gestellt, welches im Ordner [Project Files](ProjectFiles)
zu finden ist.

Im Ordner [Project Files](ProjectFiles) finden sich zusätzlich Daten unter **input_data**, in welchem sich drei *.csv* Files befinden. Diese Daten stehen für drei Datensätze von drei unterschiedlichen Patienten. Das *dash* Dashboard ist in [dashboard.py](ProjectFiles/dashboard.py) zu finden. Die Datei [utilities.py](ProjectFiles/cardiopulmonary_bypass.py) enthält Hilfsfunktionen, die nicht unmittelbar der Darstellung dienen sondern Werte im Hintergrund berechnen. Diese sollen z.B. dazu dienen, einen Probanden anlegen zu können und eine Analyse-Klasse zu erstellen. 



## Aufgaben: HLM

Als finales Projekt soll die Herz-Lungen-Maschine (HLM) behandelt werden. Diese ist für komplizierte Herz-Operationen essenziell, während denen sie viele verschiedene Vitalparameter beobachten und regeln kann. Nutzer ist dabei in erster Linie der Anästhesie, der die Operation begleitet und über Medikamente die Vitalparameter des Patienten einstellt. Für das folgende Projekt werden Datensätze der folgenden drei Parametern über einen Zeitraum von 481 Sekunden bereitgestellt.
1) SpO2 (%)
2) Blood Flow (ml/s)
3) Blood Temperature (°C)

## Aufgabe 1: lineare Interpolation (10%)

Wenn Sie die Daten im Dashboard betrachten, fallen Ihnen diverse Lücken auf. Interpolieren Sie diese Lücken über die in Pandas integrierte [**interpolate**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html) Funktion. Zusätzliche Informationen zum Thema Interpolation sind unter folgendem [Link](https://de.wikipedia.org/wiki/Interpolation_(Mathematik)) zu finden.

## Aufgabe 2: Datenverarbeitung (30%)
Die Analyse-Klasse sollte **mindestens** folgende Methoden zur Datenverarbeitung enthalten, wobei diese das Minimum und Maximum direkt im Graphen angezeigt werden sollen:
* Minimum
* Maximum 

Folgende Funktionen sollen in einem vierten Plot (```fig3``` im Code) auf den Blood Flow anwendbar sein: 
* Cumulative Moving Average mit Sliding Window (n=...)
* Simple Moving Average mit Sliding Window (n=...)

Hilfe unter [diesem Link](https://www.geeksforgeeks.org/how-to-calculate-moving-average-in-a-pandas-dataframe/)

(weitere Methoden zur Analyse von Zeitreihen werden als Bonuspunkte bewertet, sind aber nicht für eine volle Punktzahl des Abschlussprojektes nötig)

Als Input soll bei allen Methoden ein *pandas* Dataframe genutzt werden. Die Methode *Simple/Cumulative Moving Average* soll zusätzlich einen integer Wert entgegennehmen, welcher dann 
für die Berechnung herangezogen werden soll. Weitere Informationen zum *Moving Average* können sie unter diesem [Link](https://de.wikipedia.org/wiki/Gleitender_Mittelwert) finden. 

## Aufgabe 3: Blood Flow Alarm (30%)

In dieser Aufgabe soll besonders auf den *Blood Flow* in Abbildung 4 eingegangen werden. Dabei sollen die vorherigen Algorithmen verwendet werden, um einen Alarm bei Fehlfunktion auszulösen (Dies soll in diesem Beispiel nicht live passieren). Alle Ausgaben sollen direkt in Abbildung 4 (fig3 im Code) stattfinden.


1) Berechnen Sie den Mittelwert des Blood Flows (Ausgabe des Wertes über ein Label im Plot)
2) Berechnen Sie und zeigen Sie die 15% Intervalle um den berechneten Mittelwert im Graphen an 
3) Nutzen Sie den *Simple Moving Average*, um Ausreißer zu eliminieren und Warnungen auszugeben, wenn mehr als 3 Sekunden die +-15% Grenze über/-unterschritten wurde. Die Warnung soll auf einem Textfeld im Dashboard ausgegeben werden. Dabei sollen sie anzeigen, wie viele Sekunden von den 480 Sekunden der Grenzwert über-/unterschritten wurde.  
4) Wie haben Sie dafür ihre *Simple Moving Average* Funktion ausgelegt und warum? (n=?) Antwort als Kommentare am Ende des Codes

## Aufgabe 4: Moving Average (10%)
Der *Moving Average* kann vor allem dafür verwendet werden, Daten zu glätten bzw. Ausreißer zu identifizieren. Zusätzliche Aufgabe zum *Moving Average*, welche in der Datei [utilities.py](ProjectFiles/cardiopulmonary_bypass.py) als Kommentare in kurzer Form bzw. in Stichpunkten zu der Funktion hinzugefügt werden sollen:
1) Für welche Signale ist der *Simple Moving Average* im Allgemeinen sinnvoll?  Wofür ist er ungeeignet?
2) Testen Sie ihre Methode für n = 5,10,15,40. Was können Sie beobachten?

## Aufgabe 5: Design (20%)
Verwenden Sie die bereits bestehenden HTML Elemente in Dash und nutzen Sie die Dokumentation oder weitere Online-Quellen, um die Darstellungsform der App zu ändern / verbessern. Sie können davon ausgehen, dass der Bildschirm mit dem Dashboard an der Herz-Lungen-Maschine angebracht ist und nicht in der Hand gehalten wird. Mögliche Veränderungen können sein:
* Ausrichtung
* Layout Typen
* Farben
* Interaktionen
* Animationen
* neue HTML Elemente (wird als Bonuspunkte berechnet)

## Bonuspunkte:
Bonuspunkte können für besondere Leistungen vergeben werden wie zum Beispiel:
* neue HTML Elemente
* besondere Darstellungen / Graphen
* tolles Design
* zusätzliche Algorithmen
* **Zusatzinformationen in einer Tabelle** -> dafür ist eine Test Tabelle im Dashboard hinterlegt. Mögliche Informationen in der Tabelle könnten sein:
  * Minimum
  * Maximum
  * Anzahl der interpolierten Werte
  



# Dokumentation
Hilfe gibt es unter folgenden Links in der Dokumentation von Dash und plotly, sowie in folgenden Youtube Channels:

* [Dash Core Components](https://dash.plotly.com/dash-core-components)
* [Dash HTML Components](https://dash.plotly.com/dash-html-components)
* [Plotly Line Charts](https://plotly.com/python/line-charts/)

* [Youtube](https://www.youtube.com/c/CharmingData/playlists)


