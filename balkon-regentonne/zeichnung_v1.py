from html import escape
from pathlib import Path

OUT = Path(__file__).parent / 'ausgabe'
OUT.mkdir(exist_ok=True)
C = {'ink': '#18343b', 'muted': '#587079', 'blue': '#087eaf', 'water': '#ccebf7', 'orange': '#c06622', 'green': '#127a63'}


def text(x, y, value, size=19, color='ink', weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{C.get(color, color)}" font-weight="{weight}">{escape(value)}</text>'


def line(x1, y1, x2, y2, color='blue', dash=False, width=4, arrow=False):
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{C.get(color, color)}" stroke-width="{width}"' + (' stroke-dasharray="8 6"' if dash else '') + (' marker-end="url(#arrow)"' if arrow else '') + '/>'


def path(d, color='blue', dash=False, arrow=False):
    return f'<path d="{d}" fill="none" stroke="{C.get(color, color)}" stroke-width="5" stroke-linejoin="round"' + (' stroke-dasharray="8 6"' if dash else '') + (' marker-end="url(#arrow)"' if arrow else '') + '/>'


def rect(x, y, w, h, fill, stroke='none', radius=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{C.get(fill, fill)}" stroke="{C.get(stroke, stroke)}" stroke-width="3"/>'


def tank(x=380, top=155, bottom=355, level=210, width=145, label=True):
    return ''.join([
        rect(x, top, width, bottom-top, '#fff', 'ink', 9),
        rect(x+3, level, width-6, bottom-level-3, 'water'),
        line(x+3, level, x+width-3, level, width=2),
        line(x+width, bottom-28, x+width+28, bottom-28, 'green'),
        text(x+width+35, bottom-21, 'Hahn', 17, 'green') if label else '',
        line(x, bottom+8, x+width, bottom+8, 'muted', width=2),
    ])


def downpipe(y=210):
    return ''.join([
        rect(150, 105, 38, 265, '#e9eef0', 'muted'),
        rect(140, y-15, 58, 30, '#93aab1', 'ink', 4),
        line(169, 110 if y > 160 else 155, 169, y-28 if y > 160 else 200, 'blue', arrow=True),
        line(169, y+28, 169, 355, 'muted', arrow=False),
        text(38, 131, 'Fallrohr', 17, 'muted'),
        text(85, 397, 'Restregen weiter im Fallrohr', 17, 'muted'),
    ])


def overflow(x=525, y=185):
    return path(f'M{x},{y} H690 V355', 'orange', dash=True) + text(555, 278, 'Notüberlauf', 17, 'orange')


def card(letter, title, subtitle, drawing, notes, recommended=False):
    s = rect(0, 0, 790, 475, '#ffffff', '#d4e0e3', 15)
    s += rect(22, 20, 42, 40, 'green' if recommended else 'ink', radius=8)
    s += text(34, 49, letter, 25, '#fff', 700)
    s += text(79, 45, title, 25, weight=700)
    s += text(25, 78, subtitle, 18, 'green' if recommended else 'muted')
    s += drawing
    for i, note in enumerate(notes):
        s += text(25, 429+i*25, note, 18)
    return s


cards = []
a = downpipe(210) + tank(level=210)
a += line(198, 210, 380, 210) + line(210, 210, 650, 210, dash=True, width=2)
a += text(240, 190, 'hS = hmax', 20, 'blue', 700)
a += text(400, 140, 'belüfteter Tank', 17, 'muted')
a += overflow()
cards.append(card('A', 'Direktanschluss', 'Einfacher Referenzfall · feste maximale Füllhöhe', a,
                  ['Tankwechsel: Sammlerhöhe muss zum neuen Pegel passen.', 'Ein tieferer Tankstutzen allein ändert daran nichts.']))

b = downpipe(120) + tank(top=200, level=245)
b += path('M198,120 H330 V220 H410')
b += rect(401, 215, 18, 18, 'green', radius=3)
b += line(420, 224, 449, 244, 'green', width=3)
b += '<circle cx="461" cy="245" r="12" fill="#127a63"/>'
b += text(220, 148, 'hS höher als Ventil', 18, 'blue')
b += text(378, 181, 'Schwimmerventil', 18, 'green', 700)
b += overflow(y=220)
b += line(365, 260, 365, 341, 'muted', dash=True, width=2)
cards.append(card('B', 'Hoher Sammler + Schwimmer', 'Bevorzugte Richtung · wenn genügend Höhe verfügbar ist', b,
                  ['Ventil/Schlauch an Tank anpassen; Fallrohr bleibt gleich.', 'Nur Ventil für sehr geringen Zulaufdruck; Modell noch offen.'], True))

c = downpipe(120) + tank(top=190, level=240)
c += path('M198,120 H350 V215 H400', arrow=True)
c += path('M525,240 H685 V355', 'orange', arrow=True)
c += path('M525,210 H735 V355', 'orange', dash=True)
c += text(640, 196, 'Notweg', 17, 'orange')
c += text(215, 150, 'offener Einlauf', 18, 'blue')
c += text(548, 228, 'Betriebsüberlauf', 17, 'orange')
c += text(552, 275, 'läuft bei voll', 17, 'orange')
c += text(552, 300, 'zum Ablauf', 17, 'orange')
cards.append(card('C', 'Hoher Sammler + Überlauf', 'Passiv und höhenflexibel · kein Füllventil', c,
                  ['Zulauf stoppt bei vollem Tank nicht; Ablauf läuft im Regen.', 'Sicherer Betriebs- und zusätzlicher Notweg erforderlich.']))

d = downpipe(210) + tank(level=210)
d += line(198, 210, 380, 210)
d += rect(130, 120, 78, 235, 'none', 'green', 7)
d += text(218, 145, 'tauschbare', 18, 'green') + text(218, 170, 'Rohrstücke', 18, 'green')
d += line(116, 160, 116, 280, 'green', width=3)
d += '<path d="M108,170 L116,158 L124,170 M108,270 L116,282 L124,270" fill="none" stroke="#127a63" stroke-width="3"/>'
d += line(210, 210, 650, 210, dash=True, width=2) + overflow()
cards.append(card('D', 'Sammlerhöhe später ändern', 'Passiv · Umbau statt zusätzlicher Regelung', d,
                  ['Bei Tankwechsel Rohrstücke ober-/unterhalb anpassen.', 'Keine freie Schiebemontage: sichere Steckungen/Schellen.']))

e = downpipe(185) + tank(top=140, level=210)
e += rect(230, 260, 100, 90, '#fff', 'ink', 6)
e += rect(234, 305, 92, 40, 'water')
e += path('M198,185 H250 V260', arrow=True)
e += '<circle cx="280" cy="325" r="14" fill="#127a63"/>'
e += path('M293,325 H352 V120 H405 V155', arrow=True)
e += text(212, 376, 'Pumpe + Pegelsteuerung', 17, 'green')
e += path('M230,285 H210 V355', 'orange', dash=True)
e += overflow(y=175)
cards.append(card('E', 'Zwischenbehälter + Pumpe', 'Für Tankhöhen oberhalb des möglichen Sammlerpegels', e,
                  ['Zwei sichere Überläufe; Tank-voll und Trockenlauf regeln.', 'Strom, zusätzlicher Platz und Wartung erforderlich.']))

f = tank(x=90, top=115, level=175, width=140, label=False)
f += path('M230,150 H600 V320', 'orange', arrow=True)
f += text(285, 137, 'Überlauf: dauerhaftes Gefälle', 18, 'orange', 700)
f += text(285, 176, 'unterhalb der Überlaufhöhe anschließen', 17)
f += rect(575, 325, 150, 30, '#eef3f3', 'muted', 5)
f += text(580, 380, 'gesicherter Ablauf', 17, 'muted')
f += path('M90,340 H58 V375 H545 V350', 'green')
f += text(270, 315, 'tiefer Ablass + Absperrhahn', 18, 'green')
f += text(270, 340, 'Schlauch nur zum Entleeren öffnen', 17, 'green')
f += text(270, 220, 'Alternativ: Rückführung ins Fallrohr.', 17)
f += text(270, 245, 'Anschluss und Rückstau gesondert prüfen.', 17)
f += text(270, 270, 'Kein Ablauf über die Balkonkante.', 17, 'orange')
cards.append(card('F', 'Abfluss bei allen Varianten', 'Überlauf, Wasserentnahme und Winterablass getrennt', f,
                  ['Notüberlauf ohne Absperrung; Leistung am Zulauf auslegen.', 'Kein Anschlussmaß vor Bestandsaufnahme festlegen.']))

defs = '''<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#087eaf"/></marker></defs>'''


def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="DejaVu Sans, sans-serif">{defs}{body}</svg>'


body = rect(0, 0, 1680, 1715, '#f1f6f6')
body += text(40, 55, 'Balkon-Regentonne · fünf Anschlusskonzepte', 36, weight=700)
body += text(40, 89, 'Planungsstand v1 · 22.10.2026 · schematisch, nicht maßstäblich · keine Montagezeichnung', 20, 'muted')
for i, item in enumerate(cards):
    x, y = 40 + (i % 2)*810, 120 + (i//2)*495
    body += f'<g transform="translate({x},{y})">{item}</g>'
    (OUT / f'konzept_{chr(97+i)}_v1.svg').write_text(svg(790, 475, item), encoding='utf-8')
body += text(40, 1618, 'hS: wirksamer Sammlerpegel · hmax: maximaler Tankpegel · gestrichelt orange: Notweg', 17, 'muted')
body += text(40, 1648, 'Blau: Zulauf/Wasserpegel    Orange: Überlauf/Notweg    Grün: Ventil, Anpassung oder Entleerung', 20)
body += text(40, 1678, 'Vor Auswahl: Balkonlast, Stellfläche, Fallrohr, Sammleridentität und sicheren Ablauf klären.', 21, 'orange', 700)
(OUT / 'konzepte_v1.svg').write_text(svg(1680, 1715, body), encoding='utf-8')
print(OUT / 'konzepte_v1.svg')

models = [
    ('Slim Stone Decor', '350 l · Wandtank', 60, 39, 184, '368,5 kg', 'T1'),
    ('Slim Stone Decor', '500 l · Wandtank', 75, 51, 184, '525 kg', 'T2'),
    ('GARANTIA Säule', '500 l · rund', 73, 73, 193, '525 kg', 'T3'),
    ('GARANTIA Color 2in1', '350 l · rund', 62, 62, 150, '365 kg*', 'T4'),
]
s = rect(0, 0, 1680, 1030, '#f1f6f6')
s += text(40, 55, 'Schmale Tanks · Größenvergleich', 36, weight=700)
s += text(40, 90, 'Schematische Außenhüllen laut Hersteller · Ansichten mit gleichem Maßstab · Stand 22.10.2026', 20, 'muted')
scale = 1.6
for i, (name, title, w, depth, height, mass, source) in enumerate(models):
    left = 40 + i*405
    center = left + 192
    s += rect(left, 120, 385, 790, '#fff', '#d4e0e3', 12)
    s += text(left+20, 158, name, 23, weight=700)
    s += text(left+20, 189, title, 21, 'blue')
    x = center-w*scale/2
    y = 550-height*scale
    s += rect(x, y, w*scale, height*scale, 'water', 'ink', 6)
    s += line(left+40, 550, left+345, 550, 'muted', width=2)
    s += text(left+20, 594, f'{w} × {depth} × {height} cm', 23, weight=700)
    s += text(left+20, 622, 'Breite × Tiefe × Höhe', 18, 'muted')
    s += text(left+20, 656, f'Wasser + Leertank: {mass}', 19)
    plan_y = 770
    if i < 2:
        s += rect(center-w*scale/2, plan_y-depth*scale/2, w*scale, depth*scale, 'water', 'ink', 4)
    else:
        s += f'<circle cx="{center}" cy="{plan_y}" r="{w*scale/2}" fill="{C["water"]}" stroke="{C["ink"]}" stroke-width="3"/>'
    s += text(left+20, 870, f'Draufsicht · Quelle {source}', 18, 'muted')
s += text(40, 949, 'Hüllmaße: Armaturen, Wandabstand, Schläuche und Zugang zusätzlich einplanen.', 22)
s += text(40, 981, '* Ohne Pflanzsubstrat/Zubehör. Runde Grundrisse beanspruchen ein quadratisches Stellfenster.', 19, 'muted')
s += text(40, 1012, 'Kleine Stellfläche konzentriert die Last. Darstellung ersetzt keine Prüfung der Balkontragfähigkeit.', 20, 'orange', 700)
(OUT / 'tankformen_v1.svg').write_text(svg(1680, 1030, s), encoding='utf-8')
