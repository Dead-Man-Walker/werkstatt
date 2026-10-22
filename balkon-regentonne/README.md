# Balkon-Regentonne

300–500 l Regenwasser auf kleinem Balkon; vorhandenen Fallrohrsammler verwenden, Anschluss für unterschiedliche Tankhöhen entwickeln.

## Stand (2026-10-22)

| Fassung | Inhalt | Status |
|---|---|---|
| v1 | [Konzeptvergleich](konzept_v1.md), fünf Anschlussvarianten, vier Tankformen und [Grafiken](ausgabe/konzepte_v1.svg); unabhängig auf Planungsebene geprüft | aktuell für Grundkonzepte; Produktstand siehe Ergänzung |
| Produktstand v1 | [rloao G 1″ DN25](produkt_rloao_v1.md), belegte Angebotsdaten und offene Ventilmaße | Ventildaten aktuell; Anschlusskette durch v2 ersetzt |
| Anschluss v2 | [GARDENA 7251-20 und 7142-20](anschluss_v2.md), endgültige Produktauswahl, Anschlusskette mit STOUCLA-Hahn IG/IG und Schlauchempfehlung mit Ausschlussgründen | aktuell; Anschlüsse ausgewählt, Schlauchprodukt empfohlen, Montage offen |

## Entscheidungen

| Punkt | Entscheidung | Grund |
|---|---|---|
| Arbeitsort | `~/werkstatt/balkon-regentonne` | Werkstattprojekt |
| Speicher | 300–500 l, schmal/hoch bevorzugt; Modell offen | Nutzervorgabe |
| Bestand | Regenwassersammler Amazon-ASIN B00UFJLVHW gekauft | Nutzervorgabe; Ausführung noch zu verifizieren |
| Planungsrichtung | Hoher Sammler + mechanisches Schwimmerventil; rloao ASIN B0GWQM88ZH als Produktkandidat dokumentiert | Unterschiedliche Tankhöhen ohne erneuten Fallrohrumbau; Durchlass und Niederdruckeignung offen |
| Absperrhahn | STOUCLA ASIN B0D7Q67728, 1″ IG/IG gewählt | Nutzerentscheidung; Gewindenorm und freier Durchlass noch offen |
| Hahnseitige Tülle | GARDENA 7251-20, ASIN B0001E3ZDO, G 1″ AG × 25-mm-Schlauch | Endgültige Nutzerfestlegung 22.10.2026; Dichtsitz am Hahn noch abgleichen |
| Ventilseitige Verschraubung | GARDENA 7142-20, ASIN B0001E3YQW, G 1″ IG × 25-mm-Schlauch, Tülle + Überwurfmutter | Endgültige Nutzerfestlegung 22.10.2026; Dichtfläche am Schwimmerventil noch abgleichen |
| Schlauchgröße | 25 mm Innen-Ø; Produkt und Länge offen | Folgt aus beiden ausgewählten GARDENA-Anschlüssen; ersetzt früheren 32-mm-Vorschlag |
| Schlauchempfehlung | Gewebeverstärkter, innen glatter, UV-beständiger Gartenschlauch als Meterware; Beispiel GARDENA Comfort FLEX 18057-22 | Kurze Leitung durch Schwerkraft; Empfehlung dokumentiert, keine endgültige Produktwahl |

## Offene Punkte

- Stellfläche, Fallrohrmaterial/-durchmesser, verfügbare Höhen, gesicherter Ablauf, zulässige Balkonlast.
- Sammler vermutlich SAREI DN100, EAN 4260036893847; Händler bestätigt 1″ AG für diese EAN, ASIN-Verknüpfung und Gewinde-/Dichtgeometrie am Bestand prüfen.
- rloao: tatsächliche Ventilöffnung, Niederdruckbetrieb, nutzbarer Gewindestutzen, Einbauraum und Einbauanleitung; Kauf nicht bestätigt.
- Gewindenorm des STOUCLA-Hahns, konkrete Dichtpaarungen der ausgewählten GARDENA-Anschlüsse und freie Tüllen-/Ventilbohrungen prüfen; keine Zusage eines vollen 25-mm-Durchlasses.
- Schlauchprodukt/-länge, Schellengröße, tankabhängige Halterung, Einbauzugang und unabhängigen Tanknotüberlauf bestimmen.
- Tankwahl und Anschlusskonzept; keine Montagefreigabe erteilt.
- Unbeantwortete Maß-/Ablaufrückfrage bleibt Grundlage für eine spätere Ausführungsplanung.

## Prüfung

- Ausgeführt: Originalanforderung mit Dokumentation und gerenderten Grafiken abgeglichen; sichtbare Korrektur nach erstem Render. [Gegenprobe](scratchpad/research/pruefung-v1.md).
- Gelesen: [Unabhängige Sol-QM](scratchpad/research/qm-v1.md) bewertet Konzepte/Grafiken auf Planungsebene PASS; Herstellermaße und Sammlerprinzip live stichprobenartig bestätigt. Keine Bestätigung von Balkontragfähigkeit, konkretem Ventil oder Montage.

## Reproduktion

- Voraussetzungen: Python 3 (Stdlib); optional `rsvg-convert` für PNG-Vorschauen. Arbeitsverzeichnis `/home/kev/werkstatt/balkon-regentonne`.
- `python zeichnung_v1.py` erzeugt versionierbare SVGs in `ausgabe/`: Übersicht `konzepte_v1.svg`, Einzelgrafiken `konzept_a_v1.svg` bis `konzept_f_v1.svg`, Tankvergleich `tankformen_v1.svg`.
- `rsvg-convert -o ausgabe/konzepte_v1.png ausgabe/konzepte_v1.svg`
- `rsvg-convert -o ausgabe/tankformen_v1.png ausgabe/tankformen_v1.svg`
- `python /home/kev/.agents/skills/research/scripts/linkcheck.py scratchpad/research/E1.md scratchpad/research/E2.md --roh scratchpad/research/roh/check` prüft Quelllinks erneut; zusätzliche Skillinstallation erforderlich, gehört nicht zur Grafikreproduktion.
- PNGs/PDF-Downloads sind lokal vorhanden oder reproduzierbar und gemäß `../.gitignore` nicht versioniert. Quellen und Prüfvermerke stehen im Konzept und unter `scratchpad/research/`.

## Änderungsprotokoll

- 2026-10-22 · ausgeführt: Projekt mit `apply_patch` angelegt: `README.md`, `anforderung.md`, `scratchpad/research/status.md`; `../index.md` ergänzt.
- 2026-10-22 · ausgeführt: `konzept_v1.md`, `zeichnung_v1.py`, `scratchpad/research/E1.md`, `scratchpad/research/E2.md` und Abrufprotokolle angelegt; mit `python zeichnung_v1.py` SVGs erzeugt und mit `rsvg-convert` PNGs gerendert. Erste sichtbare Iteration: Rohrbeschriftungen, Fließrichtung und überlagerte Abflussbeschriftungen korrigiert.
- 2026-10-22 · ausgeführt: `.gitignore` und `scratchpad/research/pruefung-v1.md` angelegt; rohen HTML-/Linkcheck-Download vom Versionieren ausgeschlossen. Mit `apply_patch` T1-Modellbezeichnung und C-Notweg in `zeichnung_v1.py` ergänzt sowie falschen Frost-Quellenlink in `scratchpad/research/E2.md` korrigiert; SVG/PNG neu erzeugt.
- 2026-10-22 · ausgeführt: `scratchpad/research/qm-v1.md` angelegt; `scratchpad/research/status.md`, `README.md` und `../index.md` auf geprüften Planungsstand v1 aktualisiert. Keine Beschaffung, Montage, Commits oder Synchronisation ausgeführt.
- 2026-10-22 · ausgeführt: Mit `apply_patch` `produkt_rloao_v1.md` angelegt; `README.md` und `../index.md` um Produktstand und Anschlussvorschlag ergänzt. Angebotsdaten aus Chrome dokumentiert; Sitzmaß, Niederdruckbetrieb, Dichtung und Tankmontage ausdrücklich offen.
- 2026-10-22 · ausgeführt: Mit `apply_patch` `anschluss_v2.md` angelegt; `README.md`, `anforderung.md` und `../index.md` auf die endgültig gewählten GARDENA-Artikel 7251-20/7142-20 und 25-mm-Schlauchzuordnung aktualisiert. `produkt_rloao_v1.md` und `konzept_v1.md` um Verweis auf aktuellen Anschlussstand ergänzt; frühere Fassungen bleiben erhalten. STOUCLA-Hahn IG/IG berücksichtigt; keine Bestellung oder Montage ausgeführt.
- 2026-10-22 · ausgeführt: Mit `apply_patch` `anschluss_v2.md` um Schlauchempfehlung, GARDENA Comfort FLEX 18057-22 als Kandidat, Suchbegriff, ungünstige Schlaucharten und geeignete Saugschlauch-Alternative ergänzt; `README.md` und `../index.md` entsprechend aktualisiert. Schlauchprodukt und Länge bleiben offen.
