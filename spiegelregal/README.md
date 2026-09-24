# Spiegelregal

Wandhängendes Spiegelregal aus Holz, 780 × 740 × 140 mm: Spiegel links, schmales Regal rechts. Fertigungszeichnung als maßstäbliches SVG/PNG, per Skript konstruiert. Anforderung: [anforderung.md](anforderung.md).

## Stand (2026-09-24)

Aktuell: **v3**, `ausgabe/spiegelregal_v3.svg`.

| Fassung | Inhalt | Status |
|---|---|---|
| v1 | Prompt umgesetzt: offenes Regal, zwei feste Böden, drei Fächer à 220 | abgenommen |
| v2 | Lochreihen Ø5 im 32er-Raster, verstellbarer Boden, Kasten mit Tür oben, Push-to-open | verworfen |
| v3 | Feste Böden wie v1, Tür im mittleren Fach, Knauf links | aktuell |

Herkunft: 2026-09-24 aus `~/downloads` übernommen (Originale nach Byte-Vergleich per `rm` entfernt), Skripte aus dem Sitzungs-Scratchpad. ChatGPT-Entwurf danach auf Wunsch gelöscht.

Ausgangspunkt war ein Entwurf per Bildgenerator (ChatGPT, verworfen, nicht aufbewahrt). Nicht maßstäblich: Regal ca. 53 % zu breit; Spiegel in der Isometrie nur ca. 45–60 mm statt 125 mm zurückversetzt; Seiten statt Ober-/Unterbrett durchlaufend.

## Entscheidungen

| Punkt | Entscheidung | Grund |
|---|---|---|
| Brettverbindung | Ober-/Unterbrett 780 durchlaufend, Seiten, Mittelsteg, rechtes Brett 700 dazwischen | Vorgabe Prompt |
| Projektion | Methode 1 (DIN), Symbol unten links | DIN-Anmutung verlangt; Symbol verhindert Fehllesen der Spiegellage |
| Tiefenlage Spiegel | Horizontalschnitt A–A statt Draufsicht | Oberbrett verdeckt von oben alles |
| Seitenansicht | ab v2 Vertikalschnitt B–B durch die Regalspalte | zeigt Tür, Knauf, Fächer ohne verdeckte Kanten |
| Nut/Spiegel | Nut 10 von hinten, 5 breit, 8 tief; Spiegel 4 mm, 614 × 714, Vorderfläche 125 hinter Vorderkante | Prompt; Nuttiefe/Glasdicke gewählt, nur gezeichnet, nicht bemaßt |
| Tür (v3) | einliegend, 116 × 216, Fuge 2, 20 mm, 2 Topfscharniere Ø35 rechts mit Zuhaltefeder | bündige Front; öffnet vom Spiegel weg |
| Knauf (v3) | Ø25, ca. 25 vorstehend, 25 von linker Türkante, mittig (108 \| 108) | Kaufteil, nur Bohrposition bemaßt |
| Rückwand | keine, auch nicht hinter der Tür | Prompt; zweite Nut im Mittelsteg ließe nur 4–6 mm Steg |

Maßketten im Prompt teils doppelt verlangt (740/220/20 in Vorderansicht und Schnitt B–B, 140 in A–A und B–B): so übernommen. `(125)` als Hilfsmaß geklammert, übrige überbestimmte Ketten nicht.

## Offene Punkte

- Konkreter Knauf (Maße, Befestigung von vorn/hinten).
- Topfposition (21,5 von Kante, 50 von oben/unten) nur gezeichnet, abhängig vom Scharnierhersteller.
- Spiegel liegt in umlaufend geschlossener Nut → beim Verleimen einzusetzen, ohne Zerlegen nicht tauschbar. Alternative: ein Rahmenbrett nur verschrauben oder Falz von hinten mit Halteleisten.
- Keine Rückwand → Winkelsteifigkeit allein über Eckverbindungen.

## Reproduktion

Voraussetzungen: `python3` (nur Standardbibliothek), `rsvg-convert` (librsvg), Schrift Liberation Sans.

Binärdateien sind per `.gitignore` ausgeschlossen: PNGs in `ausgabe/` nach Checkout neu erzeugen.

```bash
cd ~/werkstatt/spiegelregal
python3 zeichnung_v3.py                                   # schreibt ausgabe/spiegelregal_v3.svg
rsvg-convert -z 2 ausgabe/spiegelregal_v3.svg -o ausgabe/spiegelregal_v3.png
```

Maßstab im SVG 0,9 px/mm, PNG ×2 = 1,8 px/mm. Alle Geometrie aus den Konstanten am Skriptanfang; Prüfung durch Pixelmessung der Kantenpositionen im PNG.
