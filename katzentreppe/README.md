# katzentreppe

Hohe Katzentreppe zwischen zwei Balkonen, dauerhaft bewittert. Plattformen OSB-3, Stütze Fichtenkantholz.

## Stand (2026-10-07)

| Fassung | Inhalt | Status |
|---|---|---|
| v1 | Materialwahl, Holzschutzkonzept, Zeichnung `zeichnung_v1.py` (Wandansicht, Seite, Knoten, Aussparung, Zuschnitt), Bildschirmmaßstab | verworfen |
| v2 | wie v1, maßstäblich auf A3 quer: Ansichten M 1:20, Knoten M 1:5, Zuschnitt M 1:10, Prüfstrecke 100 mm | verworfen |
| v3 | wie v2, Aussparung von vorn statt seitlich; Detail 4 als Seitenansicht | aktuell |

## Material (Produktseiten abgerufen 2026-10-07)

| Teil | Produkt | Daten laut OBI | Preis (abgerufen 2026-10-07, ohne Marktwahl) |
|---|---|---|---|
| Plattform | [OSB-3 Verlegeplatte 22 mm N+F, OBI 5799762](https://www.obi.de/p/5799762/osb-3-verlegeplatte-22-mm-mit-nut-und-feder-205-cm-x-62-5-cm) | 2050 × 625 × 22 mm, E1, „Trocken- und Feuchtbereich" (= Nutzungsklasse 2, nicht für Bewitterung) | 15,48 € |
| Stütze | [Kantholz Fichte/Tanne sägerau, OBI 4726428](https://www.obi.de/p/4726428/kantholz-fichte-tanne-saegerau-98-mm-x-78-mm-x-3000-mm) | 98 × 78 × 3000 mm, Güteklasse 1/2, nicht imprägniert, 10,8 kg | 22,17 € |

Vollständige Stückliste: [material.md](material.md).

## Entscheidungen

| Punkt | Entscheidung | Grund |
|---|---|---|
| Plattformmaterial | OSB-3 22 mm | User-Vorgabe; Empfehlung war Lärche/Douglasie-Rost. Erwartete Standzeit bewittert ~2–4 J. (Fachwissen, nicht recherchiert) |
| Geometrie | Balkone ein Stockwerk übereinander, leicht versetzt | User-Angabe 2026-10-07 |
| Befestigung | Fassade, gedübelt; Mauerwerk/Beton verputzt → Edelstahl-Schwerlastdübel/Injektionsanker, Bohrlöcher abdichten | User-Angabe 2026-10-07 |
| Ausstieg oben | durch Lücke im oberen Geländer, auf Höhe oberer Boden | User-Angabe 2026-10-07 |
| Standort | außerhalb des oberen Balkons, im Versatz → voll bewittert | User-Angabe 2026-10-07 |
| Konstruktion | wie Vorlagenbild: Kantholz an Fassade, Bretter 300×300 wechselnd links/rechts | User 2026-10-07 |
| Steckverbindung | Kantholz von vorn ausgespart, volle Breite 78, Tiefe 73, 24 hoch (22 + 2 Luft gegen Quellen), Steg 25 hinten bleibt; Brett mit Kerbe 79×26 an Hinterkante, von vorn aufgeschoben; alle Aussparungen gleich, tauschbar | User 2026-10-07 (v3); ersetzt seitliche Aussparung v2: Hebel zur Seite 78 statt 53, Brett kaum geschwächt, einfacher zu fertigen; Preis: 25 % statt 32 % Restquerschnitt, Auflage nach vorn 73 statt 98 |
| Kantholzlage | 78 an Wand, 98 tief → Steg 78×25 = 25 % Querschnitt | Auflage nach vorn 73; gedreht (98 an Wand) nur 53 Auflage bei 222 Überstand |
| Überlappung | Brett ragt 50 über gegenüberliegende Kantholzseite | User bestätigt 2026-10-07 |
| Startpunkt | Boden unterer Balkon, Durchgang unteres Geländer | User 2026-10-07 |
| Hirnholzschutz | alle Aussparungs- und Schlitzflächen vor Montage 2× Hirnholzsiegel/Epoxid | Befund: Steg 25–32 % Querschnitt, untere Schulter = nach oben zeigendes Hirnholz; User wählt Versiegeln, kein Gefälle, Steg bleibt 25 |
| Steigung | 11 × 254,5 bei Geschoss 2800 (Annahme); oberste Stufe bündig oberer Boden | ~25 cm Fachwissen (20–30), keine Quelle gefunden |
| Fixierung | je Brett 1 Senkkopfschraube A4 5×60 senkrecht in Aussparungsboden, vorgebohrt | Vorschlag |
| Wandabstand 20 | Hinterlüftung: Spalt trocknet ab, keine Fäulnis an verdeckter Rückseite, Putz bleibt trocken | Fachwissen, nicht recherchiert |
| Wandbefestigung | 4 × M10 A4 Injektionsanker mittig zwischen Aussparungen, Distanzhülse 20; Fuß 50 über Boden, nichts auf Balkonboden | Vorschlag |
| Stützenmaterial | Fichte/Tanne unimprägniert | User-Vorgabe; Empfehlung war Lärche/Douglasie oder Stahlrohr. Dauerhaftigkeitsklasse 4, Fäulnis zuerst am Fuß |

## Holzschutzkonzept (für gewähltes Material, Stand v3)

- OSB: Nut und Feder abschneiden; alle Schnittkanten und Kerbe 79×26 vor Montage 2× Kantenschutz/Epoxid; Fläche allseitig deckend beschichten (Grundierung + 2×, auch Unterseite), Quarzsand in letzte Schicht oben gegen Rutschen. Krallen beschädigen die Schicht → jährlich nachbessern; aufgequollenes Brett tauschen (Reserve-Brett, Steckverbindung lösbar). Brett liegt waagerecht, kein Gefälle (Entscheidung: nur Versiegeln).
- Fichte: hängt an Fassade, 20 mm Wandabstand (Hinterlüftung), Fuß 50 über Balkonboden, kein Bodenkontakt; Hirnholz an Fuß, Kopf und allen Aussparungsflächen 2× Hirnholzsiegel/Epoxid; Kopf zusätzlich mit Blechkappe; Fläche deckende Farbe (Grundierung + 2×). Aussteifung über 4 Wandanker.
- Verbindungsmittel: Edelstahl A4.
- Katzenkontakt: keine Biozide; Beschichtungen speichelecht (DIN EN 71-3).

## Offene Punkte

- Maße: Versatz in cm, Breite der Geländerlücke oben.
- Geschosshöhe (OK Boden unten → OK Boden oben) messen; > ~2,95 m: 3-m-Kantholz zu kurz.
- Aussparungen jährlich auf Fäulnis prüfen (Steg 25 = 25 % Querschnitt).
- Statik/Kippsicherheit der 3-m-Stütze (Knicklänge, Wind).
- Zustimmung Vermieter/WEG/Nachbar (Orientierung, keine Rechtsberatung).

## Reproduktion

Voraussetzungen: `python3` (nur Standardbibliothek), `rsvg-convert`, Schrift Liberation Sans. PNG per `.gitignore` ausgeschlossen.

```bash
cd ~/werkstatt/katzentreppe
python3 zeichnung_v3.py            # schreibt ausgabe/katzentreppe_v3.svg (A3 quer, 420×297 mm), druckt N, Steigung, Ankerhöhen
rsvg-convert ausgabe/katzentreppe_v3.svg -d 96 -o ausgabe/katzentreppe_v3.png
```

Druck: 100 %, ohne „An Seite anpassen"; Prüfstrecke unten links muss 100 mm messen. Geprüft per Pixelmessung (Blatt, Prüfstrecke, Brett M 1:5, Platte M 1:10, Kantholz M 1:20). Alle Maße aus Konstanten am Skriptanfang (`STOREY`, `RISE_TARGET`, `OVER`, `WEB` …).
