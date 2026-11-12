"""Exact vector SVG reconstructions of the 9 geometric figures in Russell's 1897 treatise."""

from __future__ import annotations

from pathlib import Path

from geometor.bertrand_russell.concordance import get_repo_root

Point = tuple[float, float]


def _intersect(p1: Point, p2: Point, p3: Point, p4: Point) -> Point:
    """Compute exact intersection of lines (p1, p2) and (p3, p4)."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denom) < 1e-12:
        raise ValueError("Parallel lines do not intersect uniquely.")
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    return (px, py)


def _svg_wrap(width: int, height: int, title: str, body: str) -> str:
    """Wrap SVG elements in a clean, accessible classical-serif figure template."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="{title}">
  <title>{title}</title>
  <style>
    .bg {{ fill: #fcfaf5; stroke: #d8d0c0; stroke-width: 1; rx: 4; }}
    .primary {{ stroke: #1c2430; stroke-width: 1.75; fill: none; stroke-linecap: round; }}
    .aux {{ stroke: #526071; stroke-width: 1.15; stroke-dasharray: 4 3; fill: none; }}
    .accent {{ stroke: #8b3a2b; stroke-width: 1.85; fill: none; }}
    .pt {{ fill: #1c2430; }}
    .pt-accent {{ fill: #8b3a2b; }}
    .lbl {{ font-family: "Libertinus Serif", "STIX Two Text", Georgia, serif; font-size: 14px; font-style: italic; fill: #1c2430; }}
    .lbl-rom {{ font-family: "Libertinus Serif", "STIX Two Text", Georgia, serif; font-size: 13px; fill: #1c2430; }}
  </style>
  <rect class="bg" x="1" y="1" width="{width - 2}" height="{height - 2}" rx="4" />
{body}
</svg>
"""


def _dot(p: Point, label: str = "", dx: float = 6, dy: float = -6, accent: bool = False) -> str:
    cls = "pt-accent" if accent else "pt"
    out = f'  <circle class="{cls}" cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="3.2" />\n'
    if label:
        out += f'  <text class="lbl" x="{p[0] + dx:.2f}" y="{p[1] + dy:.2f}">{label}</text>\n'
    return out


def _line(p1: Point, p2: Point, cls: str = "primary") -> str:
    return f'  <line class="{cls}" x1="{p1[0]:.2f}" y1="{p1[1]:.2f}" x2="{p2[0]:.2f}" y2="{p2[1]:.2f}" />\n'


def _fig_01_p021() -> str:
    """§22 (p. 21): Geodesic surface Pencil dx_i = lambda' d'x_i + lambda'' d''x_i."""
    body = (
        '  <path class="primary" d="M 38 148 Q 125 112 228 36" />\n'
        '  <path class="primary" d="M 38 148 Q 138 138 246 126" />\n'
        '  <path class="aux" d="M 38 148 Q 130 120 236 66" />\n'
        '  <path class="aux" d="M 38 148 Q 134 129 242 96" />\n'
        '  <path class="accent" d="M 228 36 Q 244 80 246 126" />\n'
        + _dot((38, 148), "O", -16, 6)
        + '  <text class="lbl" x="190" y="34">d′x</text>\n'
        + '  <text class="lbl" x="206" y="144">d″x</text>\n'
        + '  <text class="lbl" x="245" y="76">dx</text>\n'
    )
    return _svg_wrap(280, 175, "Riemannian bundle of geodesics forming a 2-manifold (p. 21)", body)


def _fig_02_p041() -> str:
    """§40 (p. 41): Small oriented circle with arrow in the elliptic plane."""
    body = (
        '  <circle class="primary" cx="90" cy="80" r="42" />\n'
        '  <path class="accent" d="M 90 38 A 42 42 0 0 1 132 80" />\n'
        '  <polygon class="pt-accent" points="132,84 126,72 138,73" />\n'
        + _dot((90, 80))
    )
    return _svg_wrap(180, 160, "Oriented circle with directional arrow on the elliptic plane (p. 41)", body)


def _fig_03_p099() -> str:
    """§91 (p. 99): Lotze's definition of parallel lines a-alpha, b-beta."""
    a, alpha = (60.0, 52.0), (275.0, 52.0)
    b, beta = (85.0, 128.0), (300.0, 128.0)
    body = (
        _line((25, 52), (335, 52), "primary")
        + _line((25, 128), (335, 128), "primary")
        + _line(a, b, "aux")
        + _line(alpha, beta, "aux")
        + _dot(a, "a", -6, -10)
        + _dot(alpha, "α", -4, -10)
        + _dot(b, "b", -6, 18)
        + _dot(beta, "β", -4, 18)
    )
    return _svg_wrap(360, 175, "Lotze's definition of parallel straight lines aα and bβ (p. 99)", body)


def _fig_04_p101() -> str:
    """§93 (p. 101): Lotze's Sphereland meridian NBS and equator EW."""
    cx, cy, r = 115.0, 105.0, 72.0
    body = (
        f'  <circle class="primary" cx="{cx}" cy="{cy}" r="{r}" />\n'
        f'  <ellipse class="aux" cx="{cx}" cy="{cy}" rx="{r}" ry="22" />\n'
        f'  <path class="accent" d="M {cx} {cy - r} A 38 {r} 0 0 0 {cx} {cy + r}" />\n'
        f'  <path class="aux" d="M {cx} {cy - r} A 38 {r} 0 0 1 {cx} {cy + r}" />\n'
        + _dot((cx, cy - r), "N", -5, -8)
        + _dot((cx, cy + r), "S", -5, 18)
        + _dot((cx - r, cy), "E", -17, 5)
        + _dot((cx + r, cy), "W", 7, 5)
        + _dot((82.0, 74.0), "B", -16, -4, accent=True)
        + _dot((81.0, 134.0), "a", -15, 10)
    )
    return _svg_wrap(230, 210, "Sphereland globe with poles N, S, equator EW, and meridian NBS (p. 101)", body)


def _fig_05_p106() -> str:
    """§94 (p. 106): Lotze's orthogonal axes OX, OY, OZ and equidistant locus."""
    o = (190.0, 125.0)
    mx_neg, mx_pos = (95.0, 125.0), (285.0, 125.0)
    y_pt = (190.0, 48.0)
    z_pt = (122.0, 178.0)
    body = (
        _line((45, 125), (335, 125), "primary")
        + _line((190, 22), (190, 192), "primary")
        + _line(o, z_pt, "accent")
        + _line(mx_neg, y_pt, "aux")
        + _line(mx_pos, y_pt, "aux")
        + _dot(o, "O", 6, 16)
        + _dot(mx_neg, "−mx", -18, 18)
        + _dot(mx_pos, "+mx", -10, 18)
        + _dot(y_pt, "y", 8, 4)
        + '  <text class="lbl" x="338" y="129">X</text>\n'
        + '  <text class="lbl" x="196" y="28">Y</text>\n'
        + '  <text class="lbl" x="106" y="186">Z</text>\n'
    )
    return _svg_wrap(375, 210, "Orthogonal axes OX, OY, OZ in Lotze's dimension argument (p. 106)", body)


def _fig_06_p123() -> str:
    """§111 (p. 123): Projective invariance of anharmonic ratio across three transversals."""
    center = (195.0, 26.0)
    r_ends = [(45.0, 200.0), (138.0, 200.0), (242.0, 200.0), (345.0, 200.0)]
    t1_a, t1_b = (35.0, 92.0), (355.0, 78.0)
    t2_a, t2_b = (30.0, 142.0), (360.0, 152.0)
    t3_a, t3_b = (25.0, 190.0), (365.0, 182.0)

    pts1 = [_intersect(center, r, t1_a, t1_b) for r in r_ends]
    pts2 = [_intersect(center, r, t2_a, t2_b) for r in r_ends]
    pts3 = [_intersect(center, r, t3_a, t3_b) for r in r_ends]

    body = ""
    for r in r_ends:
        body += _line(center, r, "aux")
    body += _line(t1_a, t1_b, "primary")
    body += _line(t2_a, t2_b, "accent")
    body += _line(t3_a, t3_b, "primary")
    body += _dot(center, "O", 6, -4)
    for pt, nm in zip(pts1, ("a", "b", "c", "d"), strict=True):
        body += _dot(pt, nm, -3, -8)
    for pt, nm in zip(pts2, ("a′", "b′", "c′", "d′"), strict=True):
        body += _dot(pt, nm, 4, -7, accent=True)
    for pt, nm in zip(pts3, ("a″", "b″", "c″", "d″"), strict=True):
        body += _dot(pt, nm, 3, 16)
    return _svg_wrap(390, 220, "Projective invariance of anharmonic ratio across transversals (p. 123)", body)


def _fig_07_p124() -> str:
    """§113 (p. 124): Collinear harmonic range (a, b, c, d) with (ab/bc) = (ad/dc)."""
    # Exact harmonic coordinates: a=60, b=150, c=204, d=330 => ab=90, bc=54 (5/3), ad=270, dc=126?
    # Let a=0, b=6, c=10, d=30 => ab=6, bc=4 (6/4=3/2); ad=30, dc=20 (30/20=3/2)! Exact!
    # Scale by 9.5, offset 48: a=48, b=105, c=143, d=333
    a, b, c, d = (48.0, 62.0), (105.0, 62.0), (143.0, 62.0), (333.0, 62.0)
    body = (
        _line((24, 62), (356, 62), "primary")
        + _dot(a, "a", -4, -12)
        + _dot(b, "b", -4, -12, accent=True)
        + _dot(c, "c", -4, -12)
        + _dot(d, "d", -4, -12, accent=True)
    )
    return _svg_wrap(380, 105, "Harmonic range of four collinear points a, b, c, d (p. 124)", body)


def _fig_08_p125() -> str:
    """§113 (p. 125): Von Staudt's Complete Quadrilateral Construction of Harmonic Fourth Point C."""
    # Base line y = 195: A, B, D given; O external vertex
    a = (42.0, 195.0)
    b = (158.0, 195.0)
    d = (348.0, 195.0)
    o = (224.0, 28.0)

    # Transversal through A cutting OD in P and OB in Q
    trans_dir = (340.0, 88.0)
    p = _intersect(a, trans_dir, o, d)
    q = _intersect(a, trans_dir, o, b)

    # Diagonals DQ and BP meet in R
    r = _intersect(d, q, b, p)

    # OR meets ABD in harmonic conjugate C!
    c = _intersect(o, r, a, d)

    # Proof lines: OA meets DRQ in T; AR meets OD in S
    t = _intersect(o, a, d, q)
    s = _intersect(a, r, o, d)

    body = (
        _line((22, 195), (368, 195), "primary")
        + _line(o, b, "primary")
        + _line(o, d, "primary")
        + _line(a, p, "primary")
        + _line(d, q, "primary")
        + _line(b, p, "primary")
        + _line(o, c, "accent")
        + _line(o, a, "aux")
        + _line(a, s, "aux")
        + _dot(a, "A", -12, 18)
        + _dot(b, "B", -5, 18)
        + _dot(c, "C", -5, 18, accent=True)
        + _dot(d, "D", 4, 18)
        + _dot(o, "O", 4, -6)
        + _dot(p, "P", 8, -2)
        + _dot(q, "Q", -16, -5)
        + _dot(r, "R", 2, -9, accent=True)
        + _dot(s, "S", 8, 4)
        + _dot(t, "T", -16, -4)
    )
    return _svg_wrap(
        395,
        232,
        "Von Staudt's Complete Quadrilateral Construction of harmonic fourth C to A with respect to B, D (p. 125)",
        body,
    )


def _fig_09_p145() -> str:
    """§138 n. 144 (p. 145): Projective construction of the plane from triad O, P, Q."""
    o = (165.0, 30.0)
    p = (62.0, 182.0)
    q = (278.0, 182.0)
    # p, q along OP, OQ
    p_sm = (103.2, 121.2)
    q_sm = (232.8, 121.2)
    # P', Q' on line PQ when rays turn about O
    p_pr = (118.0, 182.0)
    q_pr = (224.0, 182.0)

    body = (
        _line(o, p, "primary")
        + _line(o, q, "primary")
        + _line((36, 182), (304, 182), "primary")
        + _line(p_sm, q_sm, "accent")
        + _line(o, p_pr, "aux")
        + _line(o, q_pr, "aux")
        + _dot(o, "O", 5, -6)
        + _dot(p, "P", -14, 17)
        + _dot(q, "Q", 6, 17)
        + _dot(p_sm, "p", -16, -2, accent=True)
        + _dot(q_sm, "q", 8, -2, accent=True)
        + _dot(p_pr, "P′", -6, 17)
        + _dot(q_pr, "Q′", -4, 17)
    )
    return _svg_wrap(340, 218, "Projective construction of the plane OPQ via p, q and P′, Q′ (p. 145)", body)


DIAGRAM_SPECS: dict[str, tuple[str, object]] = {
    "imagep021.jpg": ("efg-fig-01-p021.svg", _fig_01_p021),
    "imagep041.jpg": ("efg-fig-02-p041.svg", _fig_02_p041),
    "imagep099.jpg": ("efg-fig-03-p099.svg", _fig_03_p099),
    "imagep101.jpg": ("efg-fig-04-p101.svg", _fig_04_p101),
    "imagep106.jpg": ("efg-fig-05-p106.svg", _fig_05_p106),
    "imagep123.jpg": ("efg-fig-06-p123.svg", _fig_06_p123),
    "imagep124.jpg": ("efg-fig-07-p124.svg", _fig_07_p124),
    "imagep125.jpg": ("efg-fig-08-p125.svg", _fig_08_p125),
    "imagep145.jpg": ("efg-fig-09-p145.svg", _fig_09_p145),
}


def generate_all_diagrams(output_dir: Path | None = None) -> list[Path]:
    """Generate all 9 vector SVG diagrams into ``docsrc/_static/diagrams/``."""
    target_dir = output_dir or (get_repo_root() / "docsrc" / "_static" / "diagrams")
    target_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for (svg_name, builder_fn) in DIAGRAM_SPECS.values():
        svg_path = target_dir / svg_name
        svg_content = builder_fn()  # type: ignore[operator]
        svg_path.write_text(svg_content, encoding="utf-8")
        written.append(svg_path)
    return written
