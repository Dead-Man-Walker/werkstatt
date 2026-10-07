import math
from pathlib import Path

# model mm: x along wall (post centre = 0), y up (0 = top of lower balcony floor), z off wall (0 = plaster)
STOREY = 2800                    # assumption: not measured yet
RISE_TARGET = 250                # cat step rise, Fachwissen (20-30 cm), not researched
N = round(STOREY / RISE_TARGET)  # boards; top board flush with upper floor
RISE = STOREY / N
PW, PD = 78, 98                  # post: 78 along wall, 98 deep
GAP = 20                         # stand-off post/plaster
FOOT = 50                        # post foot above lower floor
POST_TOP = STOREY + 100
B, T = 300, 22                   # board 300 x 300, OSB 22
OVER = 50                        # board reaches past far post face
WEB = 25                         # remaining web at back of post, notch from front
NOTCH_H = T + 2                  # clearance: wet OSB swells
SLOT_W, SLOT_D = PW + 1, WEB + 1   # board notch at back edge
PLATE_L, PLATE_W, TRIM, KERF = 2050, 625, 8, 3

Z0, Z1 = GAP, GAP + PD
LEVELS = [RISE * k for k in range(1, N + 1)]           # board top
ANCHORS = [(LEVELS[i] + LEVELS[i + 1]) / 2 for i in (0, 3, 6, 9) if i + 1 < N]


def board_x(k):  # odd k long side left, even right
    s = -1 if k % 2 else 1
    near = -s * (PW / 2 + OVER)
    return (min(near, near + s * B), max(near, near + s * B)), s


LINE, DIM, WOOD, OSB, WALL, CUT = "#1a1a1a", "#333", "#f3e3c8", "#e2c98f", "#d9d9d9", "#b5523b"
FONT = "font-family='Liberation Sans, Arial, sans-serif' fill='#1a1a1a'"
U = 4                            # SVG units per paper mm; sheet A3 landscape
CW, CH = 420 * U, 297 * U
M20, M10, M5 = U / 20, U / 10, U / 5
out = []
add = out.append


def line(x1, y1, x2, y2, w=0.7, c=DIM, dash=None):
    d = f" stroke-dasharray='{dash}'" if dash else ""
    add(f"<line x1='{x1:.2f}' y1='{y1:.2f}' x2='{x2:.2f}' y2='{y2:.2f}' stroke='{c}' stroke-width='{w}'{d}/>")


def rect(x, y, w, h, fill="none", sw=1.4, stroke=LINE, dash=None):
    d = f" stroke-dasharray='{dash}'" if dash else ""
    add(f"<rect x='{x:.2f}' y='{y:.2f}' width='{w:.2f}' height='{h:.2f}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}'{d}/>")


def text(x, y, s, size=14, anchor="middle", rot=False, bold=False):
    tr = f" transform='rotate(-90 {x:.2f} {y:.2f})'" if rot else ""
    b = " font-weight='bold'" if bold else ""
    add(f"<text x='{x:.2f}' y='{y:.2f}' {FONT} font-size='{size}' text-anchor='{anchor}'{b}{tr}>{s}</text>")


def arrow(x, y, ang):
    L, W = 8, 2.8
    ca, sa = math.cos(ang), math.sin(ang)
    p1 = (x - L * ca + W * sa, y - L * sa - W * ca)
    p2 = (x - L * ca - W * sa, y - L * sa + W * ca)
    add(f"<polygon points='{x:.2f},{y:.2f} {p1[0]:.2f},{p1[1]:.2f} {p2[0]:.2f},{p2[1]:.2f}' fill='{DIM}'/>")


def hdim(x1, x2, y, label, ext_from=None, size=12):
    if ext_from is not None:
        line(x1, ext_from, x1, y + 3, 0.5)
        line(x2, ext_from, x2, y + 3, 0.5)
    line(x1, y, x2, y)
    arrow(x1, y, math.pi)
    arrow(x2, y, 0)
    text((x1 + x2) / 2, y - 4, label, size)


def vdim(y1, y2, x, label, ext_from=None, size=12):
    if ext_from is not None:
        line(ext_from, y1, x - 3, y1, 0.5)
        line(ext_from, y2, x - 3, y2, 0.5)
    line(x, y1, x, y2)
    arrow(x, y1, -math.pi / 2)
    arrow(x, y2, math.pi / 2)
    text(x - 5, (y1 + y2) / 2, label, size, rot=True)


# ---- 1 Wandansicht ----
S1, AX, AY = M20, 190, 110
def ax(x): return AX + x * S1
def ay(y): return AY + (POST_TOP + 60 - y) * S1

text(ax(0), AY - 40, "1  Wandansicht  M 1:20", 17, bold=True)
rect(ax(-420), ay(POST_TOP + 60), 840 * S1, (POST_TOP + 60) * S1, WALL, 0)
for yy, l1, l2 in ((0, "OK Boden unten", "±0"), (STOREY, "OK Boden oben", f"+{STOREY} (Annahme)")):
    line(ax(-420), ay(yy), ax(420), ay(yy), 1.6, LINE)
    text(ax(-430), ay(yy) - 14, l1, 11, "end")
    text(ax(-430), ay(yy) - 1, l2, 11, "end")
rect(ax(-PW / 2), ay(POST_TOP), PW * S1, (POST_TOP - FOOT) * S1, WOOD)
for k, top in enumerate(LEVELS, 1):
    (xa, xb), s = board_x(k)
    rect(ax(xa), ay(top), (xb - xa) * S1, T * S1, OSB, 1.1)
for a in ANCHORS:
    add(f"<circle cx='{ax(0):.2f}' cy='{ay(a):.2f}' r='3' fill='none' stroke='{CUT}' stroke-width='1.4'/>")
vdim(ay(LEVELS[1]), ay(LEVELS[0]), ax(270), f"{RISE:.0f}", ext_from=ax(215))
vdim(ay(STOREY), ay(0), ax(400), f"{STOREY} = {N} × {RISE:.1f}", ext_from=ax(230))
vdim(ay(FOOT), ay(0), ax(-150), "50", ext_from=ax(-PW / 2), size=10)
text(ax(60), ay(STOREY) + 34, "Kantholz 78×98", 11, "start")
text(ax(60), ay(STOREY) + 47, f"L = {POST_TOP - FOOT}", 11, "start")
text(ax(-430), ay(-50) + 22, "○ Wandanker M10 A4 zwischen den Aussparungen", 11, "start")
text(ax(-430), ay(-50) + 37, f"{N} Stufen, wechselnd links/rechts; oberste = Ausstieg Geländerlücke", 11, "start")

# ---- 2 Seitenansicht ----
S2, BX = M20, 470
def bx(z): return BX + z * S2
text(bx(150), AY - 40, "2  Seitenansicht  M 1:20", 17, bold=True)
rect(bx(-80), ay(POST_TOP + 60), 80 * S2, (POST_TOP + 60) * S2, WALL, 0)
line(bx(0), ay(POST_TOP + 60), bx(0), ay(-40), 1.4, LINE)
text(bx(-40), ay(-40) + 16, "Fassade", 11)
rect(bx(Z0), ay(POST_TOP), PD * S2, (POST_TOP - FOOT) * S2, WOOD)
for top in LEVELS:
    rect(bx(Z0), ay(top), B * S2, T * S2, OSB, 1.1)
for a in ANCHORS:
    line(bx(-40), ay(a), bx(Z1), ay(a), 1.3, CUT)
hdim(bx(Z0), bx(Z0 + B), ay(LEVELS[-1]) - 22, "300", ext_from=ay(LEVELS[-1]))
hdim(bx(0), bx(Z0), ay(LEVELS[-1]) - 44, "20", size=10)
text(bx(Z1) + 30, ay(ANCHORS[0]) + 4, "M10 A4, Injektionsmörtel,", 10, "start")
text(bx(Z1) + 30, ay(ANCHORS[0]) + 17, "Distanzhülse 20, Hutmutter", 10, "start")

# ---- 3 Draufsicht Knoten (linke Stufe) ----
S3, CX, CZ = M5, 700, 150
def cx(x): return CX + (x + 230) * S3
def cz(z): return CZ + z * S3
text(cx(-60), CZ - 50, "3  Draufsicht Knoten (Stufe nach links)  M 1:5", 17, bold=True)
rect(cx(-230), cz(-30), 360 * S3, 30 * S3, WALL, 0)
line(cx(-230), cz(0), cx(130), cz(0), 1.4, LINE)
text(cx(110), cz(-10), "Fassade", 11, "end")
(xa, xb), s = board_x(1)
add(f"<path d='M{cx(xa):.2f},{cz(Z0):.2f} H{cx(-SLOT_W / 2):.2f} V{cz(Z0 + SLOT_D):.2f} H{cx(SLOT_W / 2):.2f} V{cz(Z0):.2f} H{cx(xb):.2f} V{cz(Z0 + B):.2f} H{cx(xa):.2f} Z' fill='{OSB}' stroke='{LINE}' stroke-width='1.4'/>")
rect(cx(-PW / 2), cz(Z0), PW * S3, WEB * S3, WOOD, 1.4)
rect(cx(-PW / 2), cz(Z0), PW * S3, PD * S3, "none", 1, LINE, "5 3")
scr = (0, Z0 + WEB + (PD - WEB) / 2)
add(f"<circle cx='{cx(scr[0]):.2f}' cy='{cz(scr[1]):.2f}' r='4' fill='none' stroke='{CUT}' stroke-width='1.6'/>")
hdim(cx(xa), cx(xb), cz(Z0 + B) + 28, "300", ext_from=cz(Z0 + B))
hdim(cx(PW / 2), cx(xb), cz(Z0 + B) + 52, "50", ext_from=cz(Z0 + B), size=10)
hdim(cx(-PW / 2), cx(PW / 2), cz(Z0 + B) + 76, "78", ext_from=cz(Z0 + PD), size=10)
vdim(cz(Z0), cz(Z0 + B), cx(xb) + 30, "300", ext_from=cx(xb))
vdim(cz(Z0), cz(Z1), cx(xa) - 18, "98", ext_from=cx(xa))
vdim(cz(Z0), cz(Z0 + WEB), cx(xb) + 12, "25", ext_from=cx(PW / 2), size=10)
text(cx(-110), cz(Z0 + 200), "OSB 300×300×22", 12)
text(cx(-110), cz(Z0 + 216), f"Kerbe {SLOT_W}×{SLOT_D} an Hinterkante", 12)
text(cx(scr[0]) - 30, cz(scr[1]) + 70, "○ Schraube A4 5×60", 11, "end")
line(cx(scr[0]) - 28, cz(scr[1]) + 62, cx(scr[0]), cz(scr[1]) + 6, 0.6)
text(cx(-60), cz(Z0 + B) + 104, f"Steg {WEB} hinten bleibt stehen, Brett von vorn auf den Steg schieben", 11)

# ---- 4 Aussparung Seitenansicht ----
S4, DX, DY = M5, 1180, 150
def dx(z): return DX + z * S4
def dy(y): return DY + (120 - y) * S4
text(dx(150), CZ - 50, "4  Aussparung (Seitenansicht)  M 1:5", 17, bold=True)
rect(dx(-20), dy(120), 20 * S4, 240 * S4, WALL, 0)
line(dx(0), dy(120), dx(0), dy(-120), 1.4, LINE)
add(f"<path d='M{dx(Z0):.2f},{dy(120):.2f} H{dx(Z1):.2f} V{dy(NOTCH_H / 2):.2f} H{dx(Z0 + WEB):.2f} V{dy(-NOTCH_H / 2):.2f} H{dx(Z1):.2f} V{dy(-120):.2f} H{dx(Z0):.2f} Z' fill='{WOOD}' stroke='{LINE}' stroke-width='1.4'/>")
line(dx(Z1), dy(NOTCH_H / 2), dx(Z1), dy(-NOTCH_H / 2), 1, LINE, "4 3")
for yy in (NOTCH_H / 2, -NOTCH_H / 2):
    line(dx(Z0 + WEB) + 2, dy(yy), dx(Z1) - 2, dy(yy), 3, CUT)
hdim(dx(0), dx(Z0), dy(120) - 12, f"{GAP}", size=10)
hdim(dx(Z0), dx(Z0 + WEB), dy(120) - 30, f"{WEB}", ext_from=dy(120), size=10)
hdim(dx(Z0 + WEB), dx(Z1), dy(120) - 30, f"{PD - WEB}", ext_from=dy(120), size=10)
vdim(dy(NOTCH_H / 2), dy(-NOTCH_H / 2), dx(Z1) + 26, f"{NOTCH_H}", ext_from=dx(Z1), size=10)
text(dx(-10), dy(-120) + 16, "Fassade", 11)
text(dx(170), dy(80), "Kantholz, Aussparung von vorn,", 12, "start")
text(dx(170), dy(64), f"volle Breite {PW}, Tiefe {PD - WEB}", 12, "start")
text(dx(170), dy(40), f"{NOTCH_H} hoch = 22 + 2 Luft", 12, "start")
text(dx(170), dy(16), "(OSB quillt bei Nässe)", 12, "start")
text(dx(170), dy(-14), "rot: Hirnholzflächen –", 12, "start")
text(dx(170), dy(-30), "+ Brettkerbe: 2× versiegeln", 12, "start")
text(dx(170), dy(-54), "alle Aussparungen gleich", 12, "start")

# ---- 5 Zuschnitt ----
S5, EX, EY = M10, 700, 720
def ex(x): return EX + x * S5
def ey(y): return EY + y * S5
text(ex(PLATE_L / 2), EY - 40, "5  Zuschnitt OSB-3 2050 × 625 × 22 (Nut + Feder abschneiden)  M 1:10", 17, bold=True)
rect(ex(0), ey(0), PLATE_L * S5, PLATE_W * S5, "#f7f0dd", 1.2)
for yy in (TRIM, PLATE_W - TRIM):
    line(ex(0), ey(yy), ex(PLATE_L), ey(yy), 0.8, CUT, "6 3")
n = 0
for r in range(2):
    for c in range(6):
        x0, y0 = TRIM + c * (B + KERF), TRIM + r * (B + KERF)
        if x0 + B > PLATE_L or y0 + B > PLATE_W - TRIM:
            continue
        n += 1
        fill = OSB if n <= N else "#ffffff"
        rect(ex(x0), ey(y0), B * S5, B * S5, fill, 1.1)
        text(ex(x0 + B / 2), ey(y0 + B / 2) + 5, str(n) if n <= N else "Reserve", 13)
hdim(ex(0), ex(PLATE_L), ey(PLATE_W) + 24, "2050", ext_from=ey(PLATE_W))
vdim(ey(0), ey(PLATE_W), ex(0) - 18, "625", ext_from=ex(0))
text(ex(0), ey(PLATE_W) + 52, f"{n} Bretter 300×300 aus einer Platte ({N} nötig); Längsfasern quer zur Wand; Schnittfuge {KERF}, Randschnitt {TRIM} je Seite (Annahme)", 12, "start")

# ---- Annahmen ----
notes = [
    "Annahmen / Festlegungen:",
    f"• Geschosshöhe {STOREY} nicht gemessen → Stufenzahl/Steigung neu rechnen",
    f"• Steigung ≈ 250 (Fachwissen 20–30 cm, nicht recherchiert) = Höhe zwischen zwei aufeinanderfolgenden Stufen",
    "• festgelegt: Brett ragt 50 über die gegenüberliegende Kantholzseite; Start Boden unterer Balkon",
    "• alle Aussparungs- und Schlitzflächen vor Montage 2× mit Hirnholzsiegel/Epoxid streichen",
]
for i, s_ in enumerate(notes):
    text(700, 1050 + i * 18, s_, 12, "start", bold=(i == 0))

text(CW - 30, CH - 24, "A3 quer, Druck 100 % (ohne Anpassen) · Maße in mm", 12, "end")
line(30, CH - 50, 30 + 100 * U, CH - 50, 1.2, LINE)
for i in range(11):
    line(30 + i * 10 * U, CH - 54, 30 + i * 10 * U, CH - 46, 0.8, LINE)
text(30, CH - 28, "Prüfstrecke 100 mm auf Papier", 11, "start")

svg = (f"<svg xmlns='http://www.w3.org/2000/svg' width='420mm' height='297mm' viewBox='0 0 {CW} {CH}'>"
       f"<rect width='{CW}' height='{CH}' fill='#ffffff'/>" + "".join(out) + "</svg>")
p = Path(__file__).parent / "ausgabe" / "katzentreppe_v3.svg"
p.parent.mkdir(exist_ok=True)
p.write_text(svg, encoding="utf-8")
print(p, f"N={N} RISE={RISE:.1f} ANCHORS={[round(a) for a in ANCHORS]} web%={WEB / PD * 100:.0f}")
