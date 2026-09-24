# Material: günstigste Bretter

Recherche 2026-09-24, Basis v3. Preise aus abgerufenen Produktseiten (Sonnet-Subagenten, Abrufweg je Domain nach `~/wissen/shop-produktdaten-abrufwege.md`). Hornbach: Onlinepreis Markt Bornheim/Pfalz; OBI, Hagebau, toom, Globus: ohne Marktwahl, regional abweichend möglich.

## Bedarf

Teile à 140 tief: 2 × 780 (Ober-/Unterbrett), 3 × 700 (Seiten, Mittelsteg), 2 × 120 (Böden), 1 × 216 (Tür 116 breit) = 4116 mm + Schnittfugen (3 mm). 2 × 2000 reicht nicht → 3 Stück à 2000 oder 2 à 2500.

## Optionen, Projektsumme

| # | Option | Schnittplan | Summe | Oberfläche/Dicke | Werkzeug | Prüfvermerk |
|---|---|---|---|---|---|---|
| 1 | [OBI Schalbrett 23×140×3000](https://www.obi.de/p/2290443/schalbrett-fichte-tanne-saegerau-23-mm-x-140-mm-x-3000-mm) 7,47 € (kammergetrocknet) + [23×140×2000](https://www.obi.de/p/8003055/schalbrett-fichte-tanne-saegerau-140-mm-x-23-mm-x-2000-mm) 4,98 € | 3000: 780+780+700+700 · 2000: 700+120+120+216 | 12,45 € | sägerau 23 → gehobelt ~20 × ~136 (geschätzt) | Dickenhobel | abgerufen (curl, JSON-LD); nur Marktabholung |
| 2 | Schalbrett 23×140×2000: OBI 4,98 · [Globus](https://www.globus-baumarkt.de/p/schalbrett-nadelholz-saegerau-200-cm-140-x-23-mm-0780050101/) 4,98 (kammergetrocknet, Click & Collect) · [Hornbach](https://www.hornbach.de/p/konsta-schalbrett-fichte-2000-x-140-x-23-mm/1000084/) 5,15 | 3 Stück | 14,94–15,45 € | sägerau | Dickenhobel | abgerufen |
| 3 | [OBI Rettenmeier 19×144×1000](https://www.obi.de/p/2947513/rettenmeier-brett-fichte-tanne-gehobelt-19-mm-x-144-mm-x-1000-mm) 3,49 € | 5 Stück, je ein langes Teil; kurze Teile aus Resten | 17,45 € | gehobelt, 19 mm | Säge | abgerufen; online bestellbar |
| 4 | [Hornbach Glattkantbrett 18×140×2500](https://www.hornbach.de/p/konsta-glattkantbrett-fichte-gehobelt-2500-x-140-x-18-mm/1022055/) 9,15 € | 780+780+700 · 700+700+216+120+120 | 18,30 € | gehobelt, gefast, 18 mm | Säge | abgerufen (WebFetch) |
| 5 | Glattkantbrett 18×140×2000: [Globus](https://www.globus-baumarkt.de/p/glattkantbrett-fichte-tanne-200-x-14-cm-18-mm-4-seitig-gehobelt-0780200382/) 6,59 (kammergetrocknet) · [toom](https://toom.de/p/glattkantbrett-gehobelt-2000-x-140-x-18-mm/7200124) 6,98 (techn. getrocknet) · [Hagebau](https://www.hagebau.de/p/glattkantbrett-gehobelt-kanten-gefast-bxl-14-x-200-cm-anP7000203257/) 6,98 | 3 Stück | 19,77–20,94 € | gehobelt, 18 mm | Säge | abgerufen; nur Marktabholung |
| 6 | [Hornbach Leimholzplatte Fichte B/C 18×600×2000](https://www.hornbach.de/p/leimholzplatte-fichte-b-c-2000-x-600-x-18-mm/5065821/) 31,95 € | 4 Streifen à 140 (3 Längsschnitte) | 31,95 € + Zuschnitt | 2-seitig glatt, am formstabilsten | Säge oder Zuschnittservice | abgerufen; Zuschnitt OBI 0,99 €/Schnitt ([Quelle](https://www.obi.de/beratung-und-planung/zuschnitt-service/holzzuschnitt)), Hornbach/Hagebau kein Preis online |

Weitere Leimholz-Preise (je lfm Streifen): Hagebau 18×600×2000 44,99 € (5,62), toom 18×600×1200 32,49 € (6,77), OBI 18×600×1200 33,11 € (6,90).

## Verworfen

| Option | Grund |
|---|---|
| [Hornbach N+F Kiefer 121](https://www.hornbach.de/p/nut-und-federbrett-kiefer-roh-b-sortierung-2000-x-121-x-23-mm/5115937/) | Deckbreite 111, zu schmal; Nutlage passt nicht zur Spiegelnut |
| [OBI Rauspund 19×146](https://www.obi.de/p/2641355/rauspund-fichte-tanne-nut-und-feder-19-mm-x-146-mm-x-2000-mm) | nur 5er-Paket 24,80 €; ohne Nut/Feder vermutlich < 140 (nicht gemessen) |
| Online-Holzhandel (Speckmann, Vogt, Holzhandel Deutschland) | Spedition 159–349 € |
| Sägewerk | ab ~3 m³, roh, frisch (qualitativ) |
| Europaletten | ~1,2 m, Nägel, Zustand schwankend (qualitativ) |
| Bauhaus | nicht geprüft, nur per Browser-Tool abrufbar |

## Folgen für die Konstruktion

- 20 mm nicht fertig gehobelt erhältlich. Bei 18/19 mm: entweder Außenmaße 780 × 740 halten (Spiegelöffnung ~604 × 704 bei 18) oder Öffnung 600 × 700 halten (Möbel kleiner) → Entscheidung offen, ggf. Zeichnung v4.
- Topfscharnier Ø35: Tür ≥ 16 mm, 18 mm geht.
- Trocknung nur bei OBI-Schalbrett 3000, Globus, toom deklariert; Hornbach nirgends.
- Baumarkt-Glattkant im Markt auf Verzug und Äste an der Hinterkante (Spiegelnut) aussuchen.

## Empfehlung

Ohne Dickenhobel: Option 3 (19 mm, 17,45 €), Ausweichen auf Option 4. Mit Dickenhobel: Option 1 (12,45 €), 20 mm bleiben, Zeichnung unverändert. Maximale Formstabilität: Option 6.
