# Gegenprobe v1 · 2026-10-22

## Bezug

- Original: `../../anforderung.md`; Herstellerquellen laut `../../konzept_v1.md`.
- Planungsstand; kein laufender Tankaufbau vorhanden. Physische Gegenprobe am Balkon mangels Anlage/Maßen nicht möglich, daher keine Montage-/Betriebsfreigabe.

## Ausgeführt · Quelllinks

- `python /home/kev/.agents/skills/research/scripts/linkcheck.py scratchpad/research/E1.md scratchpad/research/E2.md --roh scratchpad/research/roh/check` · 19 PASS, 1 FAIL: falsche GARANTIA-Domain beim Frostkatalog, HTTP 404. Vollständige Tabellen-/Fehlerausgabe im Toolprotokoll; keine pauschale Aussage, alle Links seien bestätigt.
- Frostverweis in `E2.md` auf bereits gelesene Hersteller-FAQ korrigiert.
- `python /home/kev/.agents/skills/research/scripts/linkcheck.py scratchpad/research/E2.md --roh scratchpad/research/roh/check-final` · 12/12 Links HTTP 200. Zusammen mit acht gültigen E1-Links 20 bestätigte aktuelle Ziel-URLs; HTTP 200 ist ein Erreichbarkeitsbeleg, keine Inhaltsabnahme.
- Eigene Webparser-Abrufe: SAREI-Baureihendatenblatt und Produktseite, Mankenberg-Ventilauslegung, 4rain-Slim-350-Maßskizze, Slim-Stone-500-Maßskizze, Säulentank-500-Maßskizze gelesen. Slim-350-Referenz diente zunächst der Formprüfung; finale Grafik nutzt die separat durch Recherche/QM gelesene Stone-Decor-350-Variante.
- Wiederabrufe der beiden SAREI-Portal-PDFs im Webparser gescheitert, Linkcheck per HTTP hingegen erfolgreich. Color-2in1-Wiederabruf im Webparser Timeout, HTTP-Abruf erfolgreich. Inhalt dieser Quellen zunächst gelesen aus Recherchebericht; unabhängige Stichprobe separat in `qm-v1.md`.

## Ausgeführt · Sichtprüfung mit Iteration

Belege: `../../ausgabe/konzepte_v1-render1.png` (Erstrender), `../../ausgabe/konzepte_v1.png` (aktuell), `../../ausgabe/tankformen_v1.png` (aktuell). PNGs aus SVG mit `rsvg-convert`; tatsächliche Bilder mit `view_image` angesehen.

| Gegen Originalanforderung | Erstrender | Nach sichtbarer Iteration |
|---|---|---|
| Fünf Konzepte grafisch erkennbar, unterschiedliche Tankhöhen berücksichtigt | PASS | PASS |
| Überlauf/Entnahme/Ablass getrennt dargestellt | FAIL: Beschriftungen überlagert | PASS: Beschriftungen verschoben, zusätzlicher C-Notweg ergänzt |
| Fließrichtung hoher Sammler nachvollziehbar | FAIL: kurzer Pfeil zeigte aufwärts | PASS: Pfeil nach unten versetzt |
| Beschriftungen lesbar | FAIL: Fallrohrtext berührte Untertitel | PASS: seitlich angeordnet |
| Vier Tankhüllen mit konsistentem Maßstab, 350/500 l, schmal/hoch | PASS | PASS; exakte Modellbezeichnung T1 nach Quellenabgleich angepasst |
| Grenzen zu Last, Ablauf, Sammleridentität und Montage klar | PASS | PASS |

Unabhängige Schlussprüfung: `qm-v1.md`. Prüferbericht ist für Hauptagent gelesen; selbst ausgeführte Nachprüfungen bleiben getrennt.

## Änderungsprotokoll

- 2026-10-22 · ausgeführt: `apply_patch` ergänzt projektlokale `.gitignore` für rohe HTML-/Linkcheck-Downloads; verhindert die Versionierung auch von als `.html` gespeicherten PDF-Rohantworten. Rohdateien bleiben lokal im Scratchpad.
