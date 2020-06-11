# Ertragswerte
Das Python-Script „ertragswert.py“ berechnet schnell den Ertragswert einer Immobilie.

Die Ausgangswerte werden direkt ins Script eingegeben.
Ausgegeben wird neben dem Ertragswert auch das Vielfache des Rohertrags – ein Wert mit dem vor allem Makler z.B. den Wert eines Mietwohnhauses überschlägig schätzen.

# Monte-Carlo-Simulation
Bei der Berechnung des Ertragswertes besteht immer das Problem, dass die Ausgangswerte nicht exakt bestimmt werden können, sondern mehr oder weniger sicher *geschätzt* werden müssen. Die Ausgangswerte bewegen sich also in einer gewissen Schätzungs-Bandbreite.
Das Python-Script „ertragswert_mc.py“ erlaubt daher die Eingabe eines Minimum- und eines Maximum-Wertes für die zur Berechnung des Ertragswertes benötigten Ausgangswerte.

Aus diesen Werten erstellt das Script jeweils 10.000 normalverteilte Zufallszahlen innerhalb der Bandbreite und berechnet damit 10.000 normalverteilte Ertragswerte und stellt die Ergebnisse in einem Histogramm dar.

# Liegenschaftszinssatz finden

