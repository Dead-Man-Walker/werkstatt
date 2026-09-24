import math
from pathlib import Path
from graphlib import TopologicalSorter

# model mm: x right (0..780), y up (0..740), z depth (0 = back, 140 = front)
W, H, D, T = 780, 740, 140, 20
MID = 620                      # left face of centre divider
SH = [(240, 260), (480, 500)]  # shelves (y)
GROOVE_BACK, GROOVE_W, GROOVE_DEPTH, GLASS = 10, 5, 8, 4
CUT_Y = 370

S = 0.9
FX, FY = 370, 130                      # front view top-left
SX = 110                               # side view left
SEC_Y = FY + H * S + 95                # section top
CW, CH = 1720, 1100

LINE, DIM = "#1a1a1a", "#333"
WOOD, GLASSC, GLASSCUT = "#f6ecdf", "#e4ecf2", "#9fb3c4"
FONT = "font-family='Liberation Sans, Arial, sans-serif' font-size='15' fill='#1a1a1a'"

out = []
add = out.append


def fx(x): return FX + x * S
def fy(y): return FY + (H - y) * S


def line(x1, y1, x2, y2, w=0.7, c=DIM, dash=None):
    d = f" stroke-dasharray='{dash}'" if dash else ""
    add(f"<line x1='{x1:.2f}' y1='{y1:.2f}' x2='{x2:.2f}' y2='{y2:.2f}' stroke='{c}' stroke-width='{w}'{d}/>")


def rect(x, y, w, h, fill="none", sw=1.8, stroke=LINE, extra=""):
    add(f"<rect x='{x:.2f}' y='{y:.2f}' width='{w:.2f}' height='{h:.2f}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}' {extra}/>")


def arrow(x, y, ang):
    L, B = 10, 3.3
    ca, sa = math.cos(ang), math.sin(ang)
    p1 = (x - L * ca + B * sa, y - L * sa - B * ca)
    p2 = (x - L * ca - B * sa, y - L * sa + B * ca)
    add(f"<polygon points='{x:.2f},{y:.2f} {p1[0]:.2f},{p1[1]:.2f} {p2[0]:.2f},{p2[1]:.2f}' fill='{DIM}'/>")


def dot(x, y):
    add(f"<circle cx='{x:.2f}' cy='{y:.2f}' r='1.9' fill='{DIM}'/>")


def text(x, y, s, rot=False, anchor="middle"):
    if rot:
        add(f"<text x='{x:.2f}' y='{y:.2f}' {FONT} text-anchor='{anchor}' transform='rotate(-90 {x:.2f} {y:.2f})'>{s}</text>")
    else:
        add(f"<text x='{x:.2f}' y='{y:.2f}' {FONT} text-anchor='{anchor}'>{s}</text>")


def hchain(xs, labels, y_line, y_obj, ends="arrows"):
    """Horizontal dimension chain; xs screen coords, extension lines from y_obj."""
    up = y_line < y_obj
    g, o = (-3, 4) if up else (3, -4)
    for x in xs:
        line(x, y_obj + g, x, y_line - o if up else y_line + 4)
    small = [(b - a) < 26 for a, b in zip(xs, xs[1:])]
    lo, hi = xs[0] - (14 if small[0] else 0), xs[-1] + (14 if small[-1] else 0)
    line(lo, y_line, hi, y_line)
    for i, (a, b) in enumerate(zip(xs, xs[1:])):
        if small[i]:
            # tight span: outer arrows only at chain ends; inner boundaries use neighbour arrows or dots
            if i == 0:
                arrow(a, y_line, 0)
            if i == len(small) - 1:
                arrow(b, y_line, math.pi)
        else:
            arrow(a, y_line, math.pi)
            arrow(b, y_line, 0)
        text((a + b) / 2, y_line - 5, labels[i])
    for i in range(1, len(xs) - 1):
        if small[i - 1] and small[i]:
            dot(xs[i], y_line)


def vchain(ys, labels, x_line, x_obj, text_side=-1):
    """Vertical dimension chain; ys screen coords top->bottom."""
    left = x_line < x_obj
    for y in ys:
        if left:
            line(x_obj - 3, y, x_line - 4, y)
        else:
            line(x_obj + 3, y, x_line + 4, y)
    small = [(b - a) < 26 for a, b in zip(ys, ys[1:])]
    lo, hi = ys[0] - (14 if small[0] else 0), ys[-1] + (14 if small[-1] else 0)
    line(x_line, lo, x_line, hi)
    n = len(small)
    for i, (a, b) in enumerate(zip(ys, ys[1:])):
        if small[i]:
            # tight span: arrows from outside, or dot when shared with another tight span
            if i == 0:
                arrow(x_line, a, math.pi / 2)
            if i == n - 1:
                arrow(x_line, b, -math.pi / 2)
        else:
            arrow(x_line, a, -math.pi / 2)
            arrow(x_line, b, math.pi / 2)
        text(x_line - 5, (a + b) / 2, labels[i], rot=True)
    for i in range(1, len(ys) - 1):
        if small[i - 1] and small[i]:
            dot(x_line, ys[i])


add(f"<svg xmlns='http://www.w3.org/2000/svg' width='{CW}' height='{CH}' viewBox='0 0 {CW} {CH}'>")
add("<defs><pattern id='hatch' patternUnits='userSpaceOnUse' width='5' height='5' patternTransform='rotate(45)'>"
    f"<rect width='5' height='5' fill='{WOOD}'/><line x1='0' y1='0' x2='0' y2='5' stroke='#555' stroke-width='0.7'/></pattern></defs>")
add(f"<rect width='{CW}' height='{CH}' fill='#fff'/>")

# ---------------- front view ----------------
rect(fx(0), fy(H), W * S, H * S, fill=WOOD, sw=0)
rect(fx(T), fy(H - T), (MID - T) * S, (H - 2 * T) * S, fill=GLASSC, sw=0)
rect(fx(MID + T), fy(H - T), (W - MID - 2 * T) * S, (H - 2 * T) * S, fill="#fff", sw=0)
for y0, y1 in SH:
    rect(fx(MID + T), fy(y1), (W - MID - 2 * T) * S, T * S, fill=WOOD, sw=0)
# hidden glass edges inside the grooves
gi = T - GROOVE_DEPTH + 1
line(fx(gi), fy(H - gi), fx(MID + GROOVE_DEPTH - 1), fy(H - gi), 0.8, LINE, "6 3")
line(fx(gi), fy(gi), fx(MID + GROOVE_DEPTH - 1), fy(gi), 0.8, LINE, "6 3")
line(fx(gi), fy(H - gi), fx(gi), fy(gi), 0.8, LINE, "6 3")
line(fx(MID + GROOVE_DEPTH - 1), fy(H - gi), fx(MID + GROOVE_DEPTH - 1), fy(gi), 0.8, LINE, "6 3")
# glass symbol
for k in (0, 1):
    line(fx(180 + k * 30), fy(560 - k * 10), fx(300 + k * 30), fy(680 - k * 10), 0.6, "#8aa0b2")
    line(fx(330 + k * 30), fy(90 - k * 10), fx(450 + k * 30), fy(210 - k * 10), 0.6, "#8aa0b2")
# visible edges
rect(fx(0), fy(H), W * S, H * S, sw=1.8)
line(fx(0), fy(H - T), fx(W), fy(H - T), 1.8, LINE)
line(fx(0), fy(T), fx(W), fy(T), 1.8, LINE)
for x in (T, MID, MID + T, W - T):
    line(fx(x), fy(H - T), fx(x), fy(T), 1.8, LINE)
for y0, y1 in SH:
    for y in (y0, y1):
        line(fx(MID + T), fy(y), fx(W - T), fy(y), 1.8, LINE)

# section plane A-A
yc = fy(CUT_Y)
for xa, xb in ((fx(0) - 22, fx(0) - 7), (fx(W) + 7, fx(W) + 22)):
    line(xa, yc, xb, yc, 2.6, LINE)
    xm = xa if xa < fx(0) else xb
    line(xm, yc, xm, yc + 16, 0.8, LINE)
    arrow(xm, yc + 18, math.pi / 2)
    text(xm, yc + 36, "A")

# front view dimensions
top = fy(H)
hchain([fx(v) for v in (0, T, MID, MID + T, W - T, W)], ["20", "600", "20", "120", "20"], top - 30, top)
hchain([fx(v) for v in (0, MID + T, W)], ["640", "140"], top - 62, top)
hchain([fx(v) for v in (0, W)], ["780"], top - 94, top)
vchain([fy(v) for v in (H, H - T, T, 0)], ["20", "700", "20"], fx(0) - 46, fx(0))
vchain([fy(v) for v in (H, 0)], ["740"], fx(0) - 80, fx(0))
ys = [H, H - T, SH[1][1], SH[1][0], SH[0][1], SH[0][0], T, 0]
vchain([fy(v) for v in ys], ["20", "220", "20", "220", "20", "220", "20"], fx(W) + 58, fx(W))

# ---------------- right side view (first-angle: left of front view) ----------------
# viewed from +x: front (z=140) on the left, back (z=0) on the right
def sx(z): return SX + (D - z) * S


rect(sx(D), fy(H), D * S, H * S, fill=WOOD, sw=0)
for y0, y1 in SH:
    for y in (y0, y1):
        line(sx(D), fy(y), sx(0), fy(y), 0.9, LINE, "6 3")
for z in (GROOVE_BACK, GROOVE_BACK + GROOVE_W):
    line(sx(z), fy(H - T + GROOVE_DEPTH), sx(z), fy(T - GROOVE_DEPTH), 0.9, LINE, "6 3")
rect(sx(D), fy(H), D * S, H * S, sw=1.8)
line(sx(D), fy(H - T), sx(0), fy(H - T), 1.8, LINE)
line(sx(D), fy(T), sx(0), fy(T), 1.8, LINE)
hchain([sx(D), sx(0)], ["140"], fy(H) - 30, fy(H))
vchain([fy(v) for v in ys], ["20", "220", "20", "220", "20", "220", "20"], sx(D) - 34, sx(D))
vchain([fy(v) for v in (H, 0)], ["740"], sx(D) - 66, sx(D))

# ---------------- section A-A (first-angle: below front view) ----------------
# viewed from above: back (z=0) at top, next to the front view
def sz(z): return SEC_Y + z * S


rect(fx(0), sz(0), W * S, D * S, fill=WOOD, sw=0)
g0, g1 = GROOVE_BACK, GROOVE_BACK + GROOVE_W


def board_with_groove(x0, x1, groove_side):
    if groove_side == "right":
        gx = x1 - GROOVE_DEPTH
        pts = [(x0, 0), (x1, 0), (x1, g0), (gx, g0), (gx, g1), (x1, g1), (x1, D), (x0, D)]
    elif groove_side == "left":
        gx = x0 + GROOVE_DEPTH
        pts = [(x0, 0), (x1, 0), (x1, D), (x0, D), (x0, g1), (gx, g1), (gx, g0), (x0, g0)]
    else:
        pts = [(x0, 0), (x1, 0), (x1, D), (x0, D)]
    p = " ".join(f"{fx(x):.2f},{sz(z):.2f}" for x, z in pts)
    add(f"<polygon points='{p}' fill='url(#hatch)' stroke='{LINE}' stroke-width='1.8'/>")


board_with_groove(0, T, "right")
board_with_groove(MID, MID + T, "left")
board_with_groove(W - T, W, None)
# glass: 4 mm, front face on the groove's front flank (125 behind the front edge)
gx0, gx1 = T - GROOVE_DEPTH + 1, MID + GROOVE_DEPTH - 1
rect(fx(gx0), sz(g1 - GLASS), (gx1 - gx0) * S, GLASS * S, fill=GLASSCUT, sw=0.9)
rect(fx(0), sz(0), W * S, D * S, sw=1.8)
text(fx(W / 2), SEC_Y - 16, "A–A")

# section dimensions
xl = fx(0)
xd = xl - 32
for z in (0, D):
    line(xl - 3, sz(z), xd - 4, sz(z))
for z in (g0, g1):  # from the groove flanks inside the board
    line(fx(T - GROOVE_DEPTH), sz(z), xd - 4, sz(z))
line(xd, sz(0) - 16, xd, sz(D))
arrow(xd, sz(0), math.pi / 2)
dot(xd, sz(g0))
arrow(xd, sz(g1), -math.pi / 2)
arrow(xd, sz(D), math.pi / 2)
text(xd - 5, (sz(g1) + sz(D)) / 2, "(125)", rot=True)
# tight 10 / 5: numbers with short leaders
line(xd - 1, (sz(0) + sz(g0)) / 2, xd - 16, sz(0) - 10, 0.6)
text(xd - 18, sz(0) - 8, "10", anchor="end")
line(xd - 1, (sz(g0) + sz(g1)) / 2, xd - 16, sz(g1) + 12, 0.6)
text(xd - 18, sz(g1) + 18, "5", anchor="end")
vchain([sz(0), sz(D)], ["140"], xl - 72, xl)
hchain([fx(0), fx(T)], ["20"], sz(D) + 30, sz(D))

# ---------------- isometric (unscaled, no dimensions) ----------------
IS = 0.58
c30, s30 = math.cos(math.radians(30)), math.sin(math.radians(30))


def iso(x, y, z):
    return (x - z) * c30 * IS, -(y - (x + z) * s30) * IS


boxes = {
    "bottom": (0, W, 0, T, 0, D), "top": (0, W, H - T, H, 0, D),
    "left": (0, T, T, H - T, 0, D), "mid": (MID, MID + T, T, H - T, 0, D),
    "right": (W - T, W, T, H - T, 0, D),
    "s1": (MID + T, W - T, *SH[0], 0, D), "s2": (MID + T, W - T, *SH[1], 0, D),
    "glass": (T, MID, T, H - T, g1 - GLASS, g1),
}
pts = [iso(x, y, z) for b in boxes.values() for x in b[:2] for y in b[2:4] for z in b[4:]]
minx, maxx = min(p[0] for p in pts), max(p[0] for p in pts)
miny, maxy = min(p[1] for p in pts), max(p[1] for p in pts)
ox = 1195 - minx
oy = (FY + H * S / 2) - (miny + maxy) / 2


def P(x, y, z):
    a, b = iso(x, y, z)
    return f"{a + ox:.2f},{b + oy:.2f}"


def behind(a, b):
    # viewer at (+x,+y,+z): the box on the lower side of a separating axis is farther away
    for i in (0, 2, 4):
        if a[i + 1] <= b[i]:
            return True
        if b[i + 1] <= a[i]:
            return False
    return None


ts = TopologicalSorter({k: set() for k in boxes})
for ka, a in boxes.items():
    for kb, b in boxes.items():
        if ka != kb and behind(a, b) is True:
            ts.add(kb, ka)
for k in ts.static_order():
    x0, x1, y0, y1, z0, z1 = boxes[k]
    fill = GLASSC if k == "glass" else WOOD
    faces = [
        [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)],  # front
        [(x1, y0, z0), (x1, y0, z1), (x1, y1, z1), (x1, y1, z0)],  # right
        [(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)],  # top
    ]
    for f in faces:
        add(f"<polygon points='{' '.join(P(*v) for v in f)}' fill='{fill}' stroke='{LINE}' stroke-width='1.2' stroke-linejoin='round'/>")
    if k == "glass":
        for k2 in (0, 1):
            add(f"<line x1='{P(160 + k2*30, 420 - k2*10, z1).split(',')[0]}' y1='{P(160 + k2*30, 420 - k2*10, z1).split(',')[1]}' "
                f"x2='{P(300 + k2*30, 600 - k2*10, z1).split(',')[0]}' y2='{P(300 + k2*30, 600 - k2*10, z1).split(',')[1]}' stroke='#8aa0b2' stroke-width='0.6'/>")

# ISO first-angle projection symbol (pictogram only)
px, py = SX - 20, SEC_Y + 40
add(f"<polygon points='{px},{py-10} {px+40},{py-20} {px+40},{py+20} {px},{py+10}' fill='none' stroke='{LINE}' stroke-width='1.4'/>")
add(f"<circle cx='{px+80}' cy='{py}' r='20' fill='none' stroke='{LINE}' stroke-width='1.4'/>")
add(f"<circle cx='{px+80}' cy='{py}' r='10' fill='none' stroke='{LINE}' stroke-width='1.4'/>")
line(px - 6, py, px + 108, py, 0.5, LINE, "12 3 2 3")
line(px + 80, py - 26, px + 80, py + 26, 0.5, LINE, "12 3 2 3")

add("</svg>")
open(Path(__file__).with_name("ausgabe") / "spiegelregal_v1.svg", "w").write("\n".join(out))
print("ok", ox, oy, maxx - minx, maxy - miny)
