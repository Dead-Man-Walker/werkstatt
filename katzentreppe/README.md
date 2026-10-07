# katzentreppe

Hohe Katzentreppe zwischen zwei Balkonen, dauerhaft bewittert. Plattformen OSB-3, Stütze Fichtenkantholz.

## Stand (2026-10-07)

| Fassung | Inhalt | Status |
|---|---|---|
| v1 | Materialwahl, Holzschutzkonzept, Zeichnung `zeichnung_v1.py` (Wandansicht, Seite, Knoten, Aussparung, Zuschnitt), Bildschirmmaßstab | verworfen |
| v2 | wie v1, maßstäblich auf A3 quer: Ansichten M 1:20, Knoten M 1:5, Zuschnitt M 1:10, Prüfstrecke 100 mm | aktuell |

## Material (Produktseiten abgerufen 2026-10-07)

| Teil | Produkt | Daten laut OBI |
|---|---|---|
| Plattform | OSB-3 Verlegeplatte 22 mm N+F, OBI 5799762 | 2050 × 625 × 22 mm, E1, „Trocken- und Feuchtbereich" (= Nutzungsklasse 2, nicht für Bewitterung) |
| Stütze | Kantholz Fichte/Tanne sägerau, OBI 4726428 | 98 × 78 × 3000 mm, Güteklasse 1/2, nicht imprägniert, 10,8 kg |

## Entscheidungen

| Punkt | Entscheidung | Grund |
|---|---|---|
| Plattformmaterial | OSB-3 22 mm | User-Vorgabe; Empfehlung war Lärche/Douglasie-Rost. Erwartete Standzeit bewittert ~2–4 J. (Fachwissen, nicht recherchiert) |
| Geometrie | Balkone ein Stockwerk übereinander, leicht versetzt | User-Angabe 2026-10-07 |
| Befestigung | Fassade, gedübelt; Mauerwerk/Beton verputzt → Edelstahl-Schwerlastdübel/Injektionsanker, Bohrlöcher abdichten | User-Angabe 2026-10-07 |
| Ausstieg oben | durch Lücke im oberen Geländer, auf Höhe oberer Boden | User-Angabe 2026-10-07 |
| Standort | außerhalb des oberen Balkons, im Versatz → voll bewittert | User-Angabe 2026-10-07 |
| Konstruktion | wie Vorlagenbild: Kantholz an Fassade, Bretter 300×300 wechselnd links/rechts | User 2026-10-07 |
| Steckverbindung | Kantholz seitlich ausgespart über volle Tiefe 98, 24 hoch (22 + 2 Luft gegen Quellen), Steg 25 bleibt; Brett mit Schlitz 26×99 von hinten, von vorn aufgeschoben; tauschbar | User-Vorgabe 2–3 cm Steg, Ausführung Vorschlag |
| Kantholzlage | 78 an Wand, 98 tief → Steg 25×98 = 32 % Querschnitt | mehr Steg, tiefere Brettauflage |
| Überlappung | Brett ragt 50 über gegenüberliegende Kantholzseite | User bestätigt 2026-10-07 |
| Startpunkt | Boden unterer Balkon, Durchgang unteres Geländer | User 2026-10-07 |
| Hirnholzschutz | alle Aussparungs- und Schlitzflächen vor Montage 2× Hirnholzsiegel/Epoxid | Befund: Steg 32 % Querschnitt, untere Schulter = nach oben zeigendes Hirnholz; User wählt Versiegeln, kein Gefälle, Steg bleibt 25 |
| Steigung | 11 × 254,5 bei Geschoss 2800 (Annahme); oberste Stufe bündig oberer Boden | ~25 cm Fachwissen (20–30), keine Quelle gefunden |
| Fixierung | je Brett 1 Senkkopfschraube A4 5×60 senkrecht in Aussparungsboden, vorgebohrt | Vorschlag |
| Wandabstand 20 | Hinterlüftung: Spalt trocknet ab, keine Fäulnis an verdeckter Rückseite, Putz bleibt trocken | Fachwissen, nicht recherchiert |
| Wandbefestigung | 4 × M10 A4 Injektionsanker mittig zwischen Aussparungen, Distanzhülse 20; Fuß 50 über Boden, nichts auf Balkonboden | Vorschlag |
| Stützenmaterial | Fichte/Tanne unimprägniert | User-Vorgabe; Empfehlung war Lärche/Douglasie oder Stahlrohr. Dauerhaftigkeitsklasse 4, Fäulnis zuerst am Fuß |

## Holzschutzkonzept (für gewähltes Material)

- OSB: alle Kanten und Nut/Feder vor Montage rundum versiegeln (Kantenschutz/Epoxid oder 2× deckender Lack), Fläche allseitig beschichten, auch Unterseite. Oberseite rutschfest (Quarzsand einstreuen oder Gummimatte mit Ablauf). 2–3 % Gefälle, Abstand zur Stütze, keine Wassernester. Jährliche Sichtkontrolle Kanten; aufgequollen = tauschen.
- Fichte: Fuß in Pfostenträger, ≥ 2 cm über Grund; Kopf abdecken; Hirnholz versiegeln; deckende Farbe (Grundierung + 2×). Seitliche Aussteifung an Balkon/Fassade.
- Verbindungsmittel: Edelstahl A2/A4.
- Katzenkontakt: keine Biozide auf Laufflächen; Beschichtung speichelecht (DIN EN 71-3).

## Offene Punkte

- Maße: Versatz in cm, Breite der Geländerlücke oben.
- Geschosshöhe (OK Boden unten → OK Boden oben) messen; > ~2,95 m: 3-m-Kantholz zu kurz.
- Aussparungen jährlich auf Fäulnis prüfen (Steg 25 = 32 % Querschnitt).
- Statik/Kippsicherheit der 3-m-Stütze (Knicklänge, Wind).
- Zustimmung Vermieter/WEG/Nachbar (Orientierung, keine Rechtsberatung).

## Reproduktion

Voraussetzungen: `python3` (nur Standardbibliothek), `rsvg-convert`, Schrift Liberation Sans. PNG per `.gitignore` ausgeschlossen.

```bash
cd ~/werkstatt/katzentreppe
python3 zeichnung_v2.py            # schreibt ausgabe/katzentreppe_v2.svg (A3 quer, 420×297 mm), druckt N, Steigung, Ankerhöhen
rsvg-convert ausgabe/katzentreppe_v2.svg -d 96 -o ausgabe/katzentreppe_v2.png
```

Druck: 100 %, ohne „An Seite anpassen"; Prüfstrecke unten links muss 100 mm messen. Geprüft per Pixelmessung (Blatt, Prüfstrecke, Brett M 1:5, Platte M 1:10, Kantholz M 1:20). Alle Maße aus Konstanten am Skriptanfang (`STOREY`, `RISE_TARGET`, `OVER`, `WEB` …).
