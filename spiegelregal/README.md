# Spiegelregal

Wandhängendes Spiegelregal aus Holz, 780 × 740 × 140 mm: Spiegel links, schmales Regal rechts. Fertigungszeichnung als maßstäbliches SVG/PNG, per Skript konstruiert. Anforderung: [anforderung.md](anforderung.md). Materialrecherche: [material.md](material.md). Oberfläche (Beize, Bad): [oberflaeche.md](oberflaeche.md).

## Stand (2026-10-08)

Aktuell: **v4**, `ausgabe/spiegelregal_v4.svg`.

| Fassung | Inhalt | Status |
|---|---|---|
| v1 | Prompt umgesetzt: offenes Regal, zwei feste Böden, drei Fächer à 220 | abgenommen |
| v2 | Lochreihen Ø5 im 32er-Raster, verstellbarer Boden, Kasten mit Tür oben, Push-to-open | verworfen |
| v3 | Feste Böden wie v1, Tür im mittleren Fach, Knauf links | abgenommen |
| v4 | wie v3, Spiegel statt Nut in Falz von hinten 20 × 8 mit kurzen Halteleisten, Detail Z 4:1 | aktuell |

Herkunft: 2026-09-24 aus `~/downloads` übernommen (Originale nach Byte-Vergleich per `rm` entfernt), Skripte aus dem Sitzungs-Scratchpad. ChatGPT-Entwurf danach auf Wunsch gelöscht.

Ausgangspunkt war ein Entwurf per Bildgenerator (ChatGPT, verworfen, nicht aufbewahrt). Nicht maßstäblich: Regal ca. 53 % zu breit; Spiegel in der Isometrie nur ca. 45–60 mm statt 125 mm zurückversetzt; Seiten statt Ober-/Unterbrett durchlaufend.

## Entscheidungen

| Punkt | Entscheidung | Grund |
|---|---|---|
| Brettverbindung | Ober-/Unterbrett 780 durchlaufend, Seiten, Mittelsteg, rechtes Brett 700 dazwischen | Vorgabe Prompt |
| Projektion | Methode 1 (DIN), Symbol unten links | DIN-Anmutung verlangt; Symbol verhindert Fehllesen der Spiegellage |
| Tiefenlage Spiegel | Horizontalschnitt A–A statt Draufsicht | Oberbrett verdeckt von oben alles |
| Seitenansicht | ab v2 Vertikalschnitt B–B durch die Regalspalte | zeigt Tür, Knauf, Fächer ohne verdeckte Kanten |
| Nut/Spiegel (bis v3) | Nut 10 von hinten, 5 breit, 8 tief; Spiegel 4 mm, 614 × 714, Vorderfläche 125 hinter Vorderkante | Prompt; ab v4 ersetzt |
| Falz/Spiegel (v4) | Falz von hinten 20 tief × 8; Spiegel 4 mm, 612 × 712 (2 mm Luft rundum), Vorderfläche 120 hinter Vorderkante; je Falzseite 2 Halteleisten 8 × 14 × 80, schräg verschraubt 3 × 20, Puffer 2 mm; unten Verglasungsklötze 2 mm | Spiegel nach Oberfläche einsetzbar und tauschbar, Silberkante nicht in geschlossener Nut; AGC-Vorgaben nur teilweise erfüllt (siehe belassene Risiken) (User 2026-10-08: Falz 20 × 8, kurze Leistenstücke); Leistenmaß/Schraube Einschätzung |
| Tür (v3) | einliegend, 116 × 216, Fuge 2, 20 mm, 2 Topfscharniere Ø35 rechts mit Zuhaltefeder | bündige Front; öffnet vom Spiegel weg |
| Knauf (v3) | Ø25, ca. 25 vorstehend, 25 von linker Türkante, mittig (108 \| 108) | Kaufteil, nur Bohrposition bemaßt |
| Bewusst belassene Risiken (v4, User 2026-10-08) | Glas liegt direkt auf der Falzschulter (AGC verlangt Abstandhalter); Fichte-Leiste 8 mm mit Schraube 3 × 20 schräg (Spalt-/Durchschlagrisiko, Spitze ~3 mm unter Außenfläche); keine Hinterlüftung, Rahmen bündig an der Wand | Alternativen geprüft und abgewählt: Vorlegeband + Falz 22, Hartholzleiste 3 × 16, Wandpuffer/Lüftungskerben |
| Rückwand | keine, auch nicht hinter der Tür | Prompt; zweite Nut im Mittelsteg ließe nur 4–6 mm Steg |
| Eckverbindung | Holzdübel 8 × 40, 3 je Stoß (10 Stöße), Mitte 30/70/110 von Hinterkante; Bohrtiefe Fläche 12 / Hirnholz 30 (bei 18 mm: 10/32); verleimen in zwei Etappen: rechte Spalte (Mittelsteg, Böden, rechte Seite), dann Rest; Spiegel erst nach Aushärtung der Oberfläche (v4) | bis v3: Nut 10–15 von hinten hätte mittiges Hirnholzloch angeschnitten; v4: Falz z 0–20, Dübel ab z 26, 6 mm Steg; ohne Rückwand trägt nur die Ecke die Winkelsteifigkeit; Weißleim-offene Zeit ~10 min |

Maßketten im Prompt teils doppelt verlangt (740/220/20 in Vorderansicht und Schnitt B–B, 140 in A–A und B–B): so übernommen. `(125)` (v3) bzw. `(120)` (v4) als Hilfsmaß geklammert, übrige überbestimmte Ketten nicht.

## Offene Punkte

- Einsatzort Bad, Oberfläche Beize matt (2026-10-08): Fichte gesetzt; Beize und Deckschicht (Tendenz Klarlack) offen bis Probestück; Leim D3 statt Weißleim. Details: [oberflaeche.md](oberflaeche.md).

- Material/Brettdicke: 20 mm nur aus sägerauem Schalbrett + Hobeln; gehobelte Ware 18/19 mm → Maßkette anpassen (Außenmaß oder Spiegelöffnung halten), Optionen und Preise in [material.md](material.md).
- Konkreter Knauf (Maße, Befestigung von vorn/hinten).
- Topfposition (21,5 von Kante, 50 von oben/unten) nur gezeichnet, abhängig vom Scharnierhersteller.
- Falz im Ober-/Unterbrett gestoppt x 12–628 (sonst offene Kerbe am Hirnholz außen und in der Regalspalte); Ecken ausstemmen.
- Keine Rückwand → Winkelsteifigkeit allein über Eckverbindungen.

## Reproduktion

Voraussetzungen: `python3` (nur Standardbibliothek), `rsvg-convert` (librsvg), Schrift Liberation Sans.

Binärdateien sind per `.gitignore` ausgeschlossen: PNGs in `ausgabe/` nach Checkout neu erzeugen.

```bash
cd ~/werkstatt/spiegelregal
python3 zeichnung_v4.py                                   # schreibt ausgabe/spiegelregal_v4.svg
rsvg-convert -z 2 ausgabe/spiegelregal_v4.svg -o ausgabe/spiegelregal_v4.png
```

Maßstab im SVG 0,9 px/mm, PNG ×2 = 1,8 px/mm. Alle Geometrie aus den Konstanten am Skriptanfang; Prüfung durch Pixelmessung der Kantenpositionen im PNG.
