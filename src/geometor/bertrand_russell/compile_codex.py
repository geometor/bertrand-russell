"""Deterministic HTML-to-RST Book Codex compiler for Bertrand Russell's 1897 and 1903 treatises."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any

from geometor.bertrand_russell.commentary import (
    EFG_APPARATUS,
    POM_APPARATUS,
    ChapterApparatus,
)
from geometor.bertrand_russell.concordance import (
    apparatus_slug,
    get_repo_root,
    load_apparatus_registries,
    load_concordance,
)
from geometor.bertrand_russell.diagrams import generate_all_diagrams

POM_CHAPTER_SPECS: tuple[dict[str, Any], ...] = (
    {
        "stem": "preface",
        "html_id": "preface",
        "part_label": "Front Matter (1903 First Edition)",
        "heading": "PREFACE",
        "rubric": "London, December 1902 (pp. v–ix)",
        "toc_title": "Preface (1903)",
        "sec_range": None,
        "pages": "pp. v–ix",
    },
    {
        "stem": "ch-01-pure-math",
        "html_id": "chapter1",
        "part_label": "Part I — The Indefinables of Mathematics",
        "heading": "CHAPTER I",
        "rubric": "Definition of Pure Mathematics (§§ 1–10, pp. 3–9)",
        "toc_title": "Chapter I: Definition of Pure Mathematics (§§ 1–10)",
        "sec_range": (1, 10),
        "pages": "pp. 3–9",
    },
    {
        "stem": "ch-44-dimensions",
        "html_id": "chapter44",
        "part_label": "Part VI — Space",
        "heading": "CHAPTER XLIV",
        "rubric": "Dimensions and Complex Numbers (§§ 351–360, pp. 371–380)",
        "toc_title": "Chapter XLIV: Dimensions and Complex Numbers (§§ 351–360)",
        "sec_range": (351, 360),
        "pages": "pp. 371–380",
    },
    {
        "stem": "ch-45-projective",
        "html_id": "chapter45",
        "part_label": "Part VI — Space",
        "heading": "CHAPTER XLV",
        "rubric": "Projective Geometry (§§ 361–373, pp. 381–392)",
        "toc_title": "Chapter XLV: Projective Geometry (§§ 361–373)",
        "sec_range": (361, 373),
        "pages": "pp. 381–392",
    },
    {
        "stem": "ch-46-descriptive",
        "html_id": "chapter46",
        "part_label": "Part VI — Space",
        "heading": "CHAPTER XLVI",
        "rubric": "Descriptive Geometry (§§ 374–387, pp. 393–403)",
        "toc_title": "Chapter XLVI: Descriptive Geometry (§§ 374–387)",
        "sec_range": (374, 387),
        "pages": "pp. 393–403",
    },
    {
        "stem": "ch-47-metrical",
        "html_id": "chapter47",
        "part_label": "Part VI — Space",
        "heading": "CHAPTER XLVII",
        "rubric": "Metrical Geometry (§§ 388–404, pp. 404–418)",
        "toc_title": "Chapter XLVII: Metrical Geometry (§§ 388–404)",
        "sec_range": (388, 404),
        "pages": "pp. 404–418",
    },
    {
        "stem": "ch-48-relation",
        "html_id": "chapter48",
        "part_label": "Part VI — Space",
        "heading": "CHAPTER XLVIII",
        "rubric": "Relation of Metrical to Projective and Descriptive Geometry (§§ 405–411, pp. 419–428)",
        "toc_title": "Chapter XLVIII: Relation of Metrical to Projective and Descriptive Geometry (§§ 405–411)",
        "sec_range": (405, 411),
        "pages": "pp. 419–428",
    },
    {
        "stem": "ch-49-spaces",
        "html_id": "chapter49",
        "part_label": "Part VI — Space",
        "heading": "CHAPTER XLIX",
        "rubric": "Definitions of Various Spaces (§§ 412–415, pp. 429–436)",
        "toc_title": "Chapter XLIX: Definitions of Various Spaces (§§ 412–415)",
        "sec_range": (412, 415),
        "pages": "pp. 429–436",
    },
    {
        "stem": "ch-50-continuity",
        "html_id": "chapter50",
        "part_label": "Part VI — Space",
        "heading": "CHAPTER L",
        "rubric": "The Continuity of Space (§§ 416–422, pp. 437–444)",
        "toc_title": "Chapter L: The Continuity of Space (§§ 416–422)",
        "sec_range": (416, 422),
        "pages": "pp. 437–444",
    },
    {
        "stem": "ch-51-points",
        "html_id": "chapter51",
        "part_label": "Part VI — Space",
        "heading": "CHAPTER LI",
        "rubric": "Logical Arguments Against Points (§§ 423–431, pp. 445–453)",
        "toc_title": "Chapter LI: Logical Arguments Against Points (§§ 423–431)",
        "sec_range": (423, 431),
        "pages": "pp. 445–453",
    },
    {
        "stem": "ch-52-kant",
        "html_id": "chapter52",
        "part_label": "Part VI — Space",
        "heading": "CHAPTER LII",
        "rubric": "Kant's Theory of Space (§§ 432–436, pp. 454–461)",
        "toc_title": "Chapter LII: Kant's Theory of Space (§§ 432–436)",
        "sec_range": (432, 436),
        "pages": "pp. 454–461",
    },
)

POM_INCLUDED_SECTIONS: frozenset[int] = frozenset(
    list(range(1, 11)) + list(range(351, 437))
)
POM_INCLUDED_CHAPTERS: dict[int, str] = {
    1: "ch-01-pure-math",
    44: "ch-44-dimensions",
    45: "ch-45-projective",
    46: "ch-46-descriptive",
    47: "ch-47-metrical",
    48: "ch-48-relation",
    49: "ch-49-spaces",
    50: "ch-50-continuity",
    51: "ch-51-points",
    52: "ch-52-kant",
}

EFG_CHAPTER_SPECS: tuple[dict[str, Any], ...] = (
    {
        "stem": "preface",
        "heading": "PREFACE & DEDICATION",
        "rubric": "Haslemere, May 1897 — Dedicated to John McTaggart Ellis McTaggart",
        "toc_title": "Preface & Dedication (1897)",
        "sec_range": None,
        "pages": "pp. v–vi",
        "has_subheadings": False,
    },
    {
        "stem": "intro",
        "heading": "INTRODUCTION",
        "rubric": "Our Problem Defined by Its Relations to Logic, Psychology and Mathematics (§§ 1–9, pp. 1–6)",
        "toc_title": "Introduction: Our Problem Defined (§§ 1–9)",
        "sec_range": (1, 9),
        "pages": "pp. 1–6",
        "has_subheadings": False,
    },
    {
        "stem": "ch-01-metageometry",
        "heading": "CHAPTER I",
        "rubric": "A Short History of Metageometry (§§ 10–50, pp. 7–53)",
        "toc_title": "Chapter I: A Short History of Metageometry (§§ 10–50)",
        "sec_range": (10, 50),
        "pages": "pp. 7–53",
        "has_subheadings": True,
    },
    {
        "stem": "ch-02-critique",
        "heading": "CHAPTER II",
        "rubric": "Critical Account of Some Previous Philosophical Theories of Geometry (§§ 51–101, pp. 54–116)",
        "toc_title": "Chapter II: Critical Account of Previous Philosophical Theories (§§ 51–101)",
        "sec_range": (51, 101),
        "pages": "pp. 54–116",
        "has_subheadings": True,
    },
    {
        "stem": "ch-03a-projective",
        "heading": "CHAPTER III — SECTION A",
        "rubric": "The Axioms of Projective Geometry (§§ 102–140, pp. 117–147)",
        "toc_title": "Chapter III, Section A: The Axioms of Projective Geometry (§§ 102–140)",
        "sec_range": (102, 140),
        "pages": "pp. 117–147",
        "has_subheadings": False,
    },
    {
        "stem": "ch-03b-metrical",
        "heading": "CHAPTER III — SECTION B",
        "rubric": "The Axioms of Metrical Geometry (§§ 141–179, pp. 147–177)",
        "toc_title": "Chapter III, Section B: The Axioms of Metrical Geometry (§§ 141–179)",
        "sec_range": (141, 179),
        "pages": "pp. 147–177",
        "has_subheadings": True,
    },
    {
        "stem": "ch-04-consequences",
        "heading": "CHAPTER IV",
        "rubric": "Philosophical Consequences (§§ 180–209, pp. 178–201)",
        "toc_title": "Chapter IV: Philosophical Consequences (§§ 180–209)",
        "sec_range": (180, 209),
        "pages": "pp. 178–201",
        "has_subheadings": True,
    },
)

EFG_FIGURE_INFO: dict[str, tuple[str, str]] = {
    "imagep021.jpg": (
        "efg-fig-01-p021.svg",
        "Fig. 1 (p. 21, § 22) — Singly infinite pencil of geodesics $dx_i = \\lambda' d'x_i + \\lambda'' d''x_i$ forming a 2-manifold.",
    ),
    "imagep041.jpg": (
        "efg-fig-02-p041.svg",
        "Fig. 2 (p. 41, § 40) — Oriented circle in the two-dimensional elliptic plane.",
    ),
    "imagep099.jpg": (
        "efg-fig-03-p099.svg",
        "Fig. 3 (p. 99, § 91) — Lotze's definition of parallel straight lines $a\\alpha$ and $b\\beta$.",
    ),
    "imagep101.jpg": (
        "efg-fig-04-p101.svg",
        "Fig. 4 (p. 101, § 93) — Lotze's Sphereland great circles: poles $N, S$, equator $EW$, and meridian $NBS$.",
    ),
    "imagep106.jpg": (
        "efg-fig-05-p106.svg",
        "Fig. 5 (p. 106, § 95) — Concentric spheres and rays meeting at acute angle $O$ in Lotze's coordinate reconstruction.",
    ),
    "imagep123.jpg": (
        "efg-fig-06-p123.svg",
        "Fig. 6 (p. 123, § 111) — Central projection of collinear points $A, B, C, D$ from $O$ onto $A', B', C', D'$ with equal anharmonic ratio.",
    ),
    "imagep124.jpg": (
        "efg-fig-07-p124.svg",
        "Fig. 7 (p. 124, § 111) — Projective extension from four rays in one plane to a second plane via transversal $A''B''C''D''$.",
    ),
    "imagep125.jpg": (
        "efg-fig-08-p125.svg",
        "Fig. 8 (p. 125, § 113) — Von Staudt's Complete Quadrilateral Construction of the harmonic conjugate $C$ to $A$ with respect to $B, D$.",
    ),
    "imagep145.jpg": (
        "efg-fig-09-p145.svg",
        "Fig. 9 (p. 145, § 138 n. 144) — Projective construction of the plane from triad $O, P, Q$ via $p, q$ and $P', Q'$.",
    ),
}

GREEK_TO_TEX: dict[str, str] = {
    "α": r"\alpha",
    "β": r"\beta",
    "γ": r"\gamma",
    "δ": r"\delta",
    "ε": r"\varepsilon",
    "ζ": r"\zeta",
    "η": r"\eta",
    "θ": r"\theta",
    "λ": r"\lambda",
    "μ": r"\mu",
    "ν": r"\nu",
    "ξ": r"\xi",
    "π": r"\pi",
    "ρ": r"\rho",
    "σ": r"\sigma",
    "τ": r"\tau",
    "φ": r"\varphi",
    "ψ": r"\psi",
    "ω": r"\omega",
    "Σ": r"\sum",
    "Ω": r"\Omega",
    "∞": r"\infty",
}


def _rst_heading(title: str, char: str) -> str:
    clean = " ".join(title.splitlines()).strip()
    bar = char * max(len(clean), 4)
    return f"{clean}\n{bar}"


def _tex_clean_atom(raw: str) -> str:
    """Convert an HTML fragment inside a math fraction/sub/sup into clean LaTeX."""
    s = re.sub(r"</?(?:var|em|i|span)[^>]*>", "", raw)
    s = html.unescape(s)
    s = s.replace("\u00a0", " ").replace("\u202f", " ")
    s = s.replace("−", "-").replace("–", "-")
    s = s.replace("′′", "''").replace("″", "''").replace("′", "'")
    s = re.sub(r"\bsin\b", r"\\sin ", s)
    s = re.sub(r"\bcos\b", r"\\cos ", s)
    s = re.sub(r"\btan\b", r"\\tan ", s)
    s = re.sub(r"\blog\b", r"\\log ", s)
    for gr, tex in GREEK_TO_TEX.items():
        s = s.replace(gr, f"{tex} ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


_INLINE_TOKEN_RE = re.compile(
    r"(\*\*[^*\n]+?\*\*|\*(?!\*)[^*\n]+?\*(?!\*)|\$[^$\n]+?\$|:(?:ref|sup):`[^`\n]+`|\[#[A-Za-z0-9_]+\]_)"
)
_VALID_PREFIX_CHARS = frozenset(" \t\n-:/'\"<([{–—\u2018\u201c")
_NEEDS_SUFFIX_ESCAPE = frozenset("'’([*`$")


def _fix_inline_rst_boundaries(text: str) -> str:
    """Merge adjacent inline math spans and ensure Docutils start/end boundaries around inline markup."""
    # Merge touching $A'$$B'$ -> $A'B'$
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r"\$([^$\n]+)\$\$([^$\n]+)\$", r"$\1\2$", text)

    out: list[str] = []
    pos = 0
    for m in _INLINE_TOKEN_RE.finditer(text):
        start, end = m.span()
        tok = m.group(0)
        chunk_before = text[pos:start]
        out.append(chunk_before)

        if start > 0:
            prev_ch = text[start - 1]
            # Avoid double-escaping if already preceded by '\ '
            already_escaped = start >= 2 and text[start - 2 : start] == "\\ "
            if not already_escaped and prev_ch not in _VALID_PREFIX_CHARS:
                out.append("\\ ")

        out.append(tok)

        if end < len(text):
            next_ch = text[end]
            if (next_ch.isalnum() or next_ch in _NEEDS_SUFFIX_ESCAPE) and not text[end:].startswith("\\ "):
                out.append("\\ ")

        pos = end

    out.append(text[pos:])
    return "".join(out)


def _italic_wrap(m: re.Match[str]) -> str:
    inner = m.group(1)
    if not inner or not inner.strip():
        return inner
    lead = " " if inner[0].isspace() else ""
    trail = " " if inner[-1].isspace() else ""
    core = inner.strip()
    if core.startswith("$") and core.endswith("$"):
        return f"{lead}{core}{trail}"
    return f"{lead}*{core}*{trail}"


def _bold_wrap(m: re.Match[str]) -> str:
    inner = m.group(1)
    if not inner or not inner.strip():
        return inner
    lead = " " if inner[0].isspace() else ""
    trail = " " if inner[-1].isspace() else ""
    return f"{lead}**{inner.strip()}**{trail}"


# ---------------------------------------------------------------------------
# Codex I (1903 Principles of Mathematics) HTML -> RST
# ---------------------------------------------------------------------------

_POM_INLINE_TABLE_RE = re.compile(
    r'<span style="display:\s*inline-table[^"]*">'
    r'<span style="display:\s*table-row[^"]*"><span[^>]*>(.*?)</span></span>'
    r'<span style="display:\s*table-row[^"]*"><span[^>]*>(.*?)</span></span>'
    r"</span>",
    re.DOTALL,
)

_POM_DOUBLE_FRAC_RE = re.compile(
    r'<span style="position:\s*relative;">\s*'
    r'<span style="display:\s*inline-table[^"]*">'
    r'<span style="display:\s*table-row[^"]*"><span[^>]*>(.*?)</span></span>'
    r'<span style="display:\s*table-row[^"]*"><span[^>]*>(.*?)</span></span>'
    r"</span>\s*"
    r"<span[^>]*>∕</span>\s*"
    r'<span style="display:\s*inline-table[^"]*">'
    r'<span style="display:\s*table-row[^"]*"><span[^>]*>(.*?)</span></span>'
    r'<span style="display:\s*table-row[^"]*"><span[^>]*>(.*?)</span></span>'
    r"</span>\s*</span>",
    re.DOTALL,
)

_POM_CONVERSE_RE = re.compile(
    r'<span style="display:\s*inline-block;\s*position:\s*relative[^"]*">'
    r"<span[^>]*>˘</span><span><var>(.*?)</var></span></span>"
    r"(?:<sub>(.*?)</sub>)?(?:<sup>(.*?)</sup>)?",
    re.DOTALL,
)

_POM_VAR_SUBSUP_RE = re.compile(
    r"(?:<var>([^<]+)</var>|(\d+))"
    r"(?:<var>)?(?:<sub>(.*?)</sub>)?(?:</var>)?"
    r"(?:<sup>(.*?)</sup>)?",
    re.DOTALL,
)


def _convert_pom_inline(raw_html: str) -> str:
    """Convert inline HTML inside a 1903 PoM paragraph or footnote to clean RST."""
    s = raw_html

    # 1. Strip embedded page markers and HTML comments (page anchors are extracted beforehand)
    s = re.sub(r'<a\s+id="page[^"]+"\s*>(?:<!--[^>]*-->)?</a>', "", s)
    s = re.sub(r"<!--[\s\S]*?-->", "", s)

    # 2. Compound cross-ratio fractions and single inline-table fractions
    def _repl_double_frac(m: re.Match[str]) -> str:
        n1, d1, n2, d2 = (_tex_clean_atom(m.group(i)) for i in range(1, 5))
        return rf"$\frac{{{n1}}}{{{d1}}} / \frac{{{n2}}}{{{d2}}}$"

    def _repl_single_frac(m: re.Match[str]) -> str:
        n1, d1 = _tex_clean_atom(m.group(1)), _tex_clean_atom(m.group(2))
        return rf"$\frac{{{n1}}}{{{d1}}}$"

    s = _POM_DOUBLE_FRAC_RE.sub(_repl_double_frac, s)
    s = _POM_INLINE_TABLE_RE.sub(_repl_single_frac, s)

    # 3. Converse relation ˘R (with optional sub/sup)
    def _repl_converse(m: re.Match[str]) -> str:
        base = _tex_clean_atom(m.group(1))
        sub = _tex_clean_atom(m.group(2)) if m.group(2) else ""
        sup = _tex_clean_atom(m.group(3)) if m.group(3) else ""
        tex = rf"\breve{{{base}}}"
        if sub:
            tex += f"_{{{sub}}}"
        if sup:
            tex += f"^{{{sup}}}"
        return f"${tex}$"

    s = _POM_CONVERSE_RE.sub(_repl_converse, s)

    # 4. Variables/digits with subscripts or superscripts (e.g. A_0, A_n, R_1^{-x}, 2^{\alpha_0})
    # Handle nested 2<sup><var>α</var><sub>0</sub></sup> first
    s = re.sub(
        r"2<sup><var>α</var><sub>0</sub></sup>",
        r"$2^{\\alpha_0}$",
        s,
    )

    def _repl_varsubsup(m: re.Match[str]) -> str:
        var_part, num_part, sub_raw, sup_raw = m.group(1), m.group(2), m.group(3), m.group(4)
        if not sub_raw and not sup_raw:
            return m.group(0)
        base = _tex_clean_atom(var_part or num_part or "")
        tex = base
        if sub_raw:
            tex += f"_{{{_tex_clean_atom(sub_raw)}}}"
        if sup_raw:
            tex += f"^{{{_tex_clean_atom(sup_raw)}}}"
        return f"${tex}$"

    s = _POM_VAR_SUBSUP_RE.sub(_repl_varsubsup, s)

    # Any remaining bare <sub>...</sub> or <sup>...</sup>
    s = re.sub(r"<sub>(.*?)</sub>", lambda m: f"$_{{{_tex_clean_atom(m.group(1))}}}$", s)
    s = re.sub(r"<sup>(.*?)</sup>", lambda m: f"$^{{{_tex_clean_atom(m.group(1))}}}$", s)

    # 5. Consecutive <var>A</var><var>B</var> (and primes ′ / ′′) -> merged italic *AB* or $AB'$
    s = re.sub(r"</var><var>", "", s)
    s = re.sub(
        r"<var>([^<]+)</var>(′′|′|″)?",
        lambda m: f"${_tex_clean_atom(m.group(1))}{'′′' if m.group(2) in ('′′', '″') else ('′' if m.group(2) else '')}$".replace(
            "′", "'"
        )
        if m.group(2)
        else _italic_wrap(m),
        s,
    )

    # 6. Footnote markers: <a href="#fn408-1" id="fn408-1marker" >*</a>
    def _repl_fn_marker(m: re.Match[str]) -> str:
        fn_id = re.sub(r"[^A-Za-z0-9]+", "_", m.group(1))
        return f" [#pom_{fn_id}]_"

    s = re.sub(
        r'<a\s+href="#(fn[^"]+)"\s+id="[^"]*marker"[^>]*>.*?</a>',
        _repl_fn_marker,
        s,
        flags=re.DOTALL,
    )

    # 7. Section anchors at start of paragraph: <a id="sec389" ><strong>389.</strong></a>
    s = re.sub(
        r'<a\s+id="sec\d+"\s*>\s*<strong>(\d+\.)</strong>\s*</a>',
        r"**\1** ",
        s,
    )

    # 8. Internal cross-reference links <a href="#...">TEXT</a> (protected from tag stripping)
    ref_placeholders: list[str] = []

    def _store_ref(rst_ref: str) -> str:
        idx = len(ref_placeholders)
        ref_placeholders.append(rst_ref)
        return f"PHOTONREFTMP{idx}END"

    def _repl_link(m: re.Match[str]) -> str:
        href = m.group(1).strip()
        label = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        m_sec = re.match(r"^#sec(\d+)$", href)
        if m_sec:
            sec_num = int(m_sec.group(1))
            if sec_num in POM_INCLUDED_SECTIONS:
                return _store_ref(f":ref:`{label} <pom-{sec_num}>`")
            return label
        m_ch = re.match(r"^#chapter(\d+)$", href)
        if m_ch:
            ch_num = int(m_ch.group(1))
            if ch_num in POM_INCLUDED_CHAPTERS:
                return _store_ref(f":ref:`{label} <pom-{POM_INCLUDED_CHAPTERS[ch_num]}-en>`")
            return label
        return label

    s = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', _repl_link, s, flags=re.DOTALL)

    # 9. Small caps span, line breaks, strong, em
    s = re.sub(r'<span style="font-variant:\s*small-caps;">(.*?)</span>', lambda m: m.group(1).upper(), s)
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<strong>(.*?)</strong>", _bold_wrap, s, flags=re.DOTALL)
    s = re.sub(r"<em>(.*?)</em>", _italic_wrap, s, flags=re.DOTALL)
    s = re.sub(r"<[^>]+>", "", s)

    s = html.unescape(s)
    for idx, rst_ref in enumerate(ref_placeholders):
        s = s.replace(f"PHOTONREFTMP{idx}END", rst_ref)
    s = s.replace("\u202f", " ").replace("\u00a0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" *\n *", " ", s).strip()

    # Protect paragraph-leading parenthesized numerals (1), (2), etc. from Docutils list-state warnings
    s = re.sub(r"^\((\d+|[a-z]|[ivx]+)\)\s+", r"**(\1)** ", s)
    return _fix_inline_rst_boundaries(s)


def _compile_pom_chapter_en(
    spec: dict[str, Any],
    raw_chunk: str,
    toc_map: dict[str, dict[str, Any]],
) -> str:
    """Compile a single 1903 PoM chapter HTML slice into its verbatim `-en.rst` track."""
    stem = spec["stem"]
    lines: list[str] = [
        ":layout: book",
        "",
        f".. _pom-{stem}:",
        f".. _pom-{stem}-en:",
        "",
        _rst_heading(spec["heading"], "="),
        "",
        f".. rubric:: {spec['part_label']} — {spec['rubric']}",
        "",
    ]

    if spec["sec_range"] is not None:
        lines.extend(
            [
                ".. contents:: Analytical Section Outline",
                "   :local:",
                "   :depth: 2",
                "   :backlinks: none",
                "",
            ]
        )

    # Separate footnotes block (<div class="fnnote">Notes</div>...) from chapter body
    fn_split = raw_chunk.split('<div class="fnnote">Notes</div>', 1)
    body_html = fn_split[0]
    fn_html = fn_split[1] if len(fn_split) > 1 else ""

    # Remove chapter heading <h2>...</h2> and decorative <hr />
    body_html = re.sub(r"<h[12][^>]*>[\s\S]*?</h[12]>", "", body_html)

    emitted_pages: set[str] = set()
    token_re = re.compile(
        r'(<a\s+id="page([A-Za-z0-9]+)"[^>]*>(?:<!--[^>]*-->)?</a>|<p[^>]*>[\s\S]*?</p>|<table[^>]*>[\s\S]*?</table>)',
        re.DOTALL,
    )
    pending_pages: list[str] = []

    for m in token_re.finditer(body_html):
        tok = m.group(0)
        if m.group(2):
            pg = m.group(2)
            if pg not in emitted_pages:
                pending_pages.append(pg)
                emitted_pages.add(pg)
            continue

        if tok.startswith("<table"):
            rows = re.findall(r"<tr[^>]*>([\s\S]*?)</tr>", tok)
            block_lines: list[str] = []
            for row in rows:
                cells = [_convert_pom_inline(c) for c in re.findall(r"<td[^>]*>([\s\S]*?)</td>", row)]
                joined = " ".join(c for c in cells if c).strip()
                if joined:
                    block_lines.append(f"   | {joined}")
            if block_lines:
                lines.extend(block_lines)
                lines.append("")
            continue

        # Extract any inline <a id="page..."> inside this <p>
        for pg in re.findall(r'<a\s+id="page([A-Za-z0-9]+)"', tok):
            if pg not in emitted_pages:
                pending_pages.append(pg)
                emitted_pages.add(pg)

        # Check if this paragraph starts a numbered section <a id="secN">
        m_sec = re.search(r'<a\s+id="sec(\d+)"', tok)
        if m_sec:
            sec_num = m_sec.group(1)
            toc_entry = toc_map.get(sec_num, {})
            sec_title = toc_entry.get("title_text", f"Section {sec_num}")
            sec_page = toc_entry.get("page", "")
            lines.append(f".. _pom-{sec_num}:")
            lines.append("")
            lines.append(_rst_heading(f"§ {sec_num}. {sec_title}", "-"))
            lines.append("")
            if sec_page:
                lines.append(f".. folio:: §{sec_num}")
                lines.append(f"   :page: p. {sec_page}")
                lines.append("")

        for pg in pending_pages:
            lines.append(f".. _pom-p{pg}:")
            lines.append("")
        pending_pages.clear()

        is_center = 'class="noindent center"' in tok
        inner_p = re.sub(r"^<p[^>]*>|</p>$", "", tok.strip(), flags=re.DOTALL)
        para_rst = _convert_pom_inline(inner_p)
        if para_rst:
            if is_center:
                lines.append(f"   {para_rst}")
            else:
                lines.append(para_rst)
            lines.append("")

    # Parse footnotes for this chapter
    fn_items = re.findall(
        r'<div class="fn" id="(fn[^"]+)"\s*>[\s\S]*?<span class="fntext">([\s\S]*?)</span></div>',
        fn_html,
    )
    if fn_items:
        lines.append("----")
        lines.append("")
        lines.append(".. rubric:: Author's Footnotes (1903 Edition)")
        lines.append("")
        for raw_id, raw_fntext in fn_items:
            fn_id = re.sub(r"[^A-Za-z0-9]+", "_", raw_id)
            fn_rst = _convert_pom_inline(raw_fntext)
            lines.append(f".. [#pom_{fn_id}] {fn_rst}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Codex II (1897 An Essay on the Foundations of Geometry) HTML -> RST
# ---------------------------------------------------------------------------

_EFG_SQRT_RE = re.compile(r"√<span class=\"over\">(.*?)</span>")
_EFG_BLKSUM_RE = re.compile(
    r'<span class="blksum">\s*<span class="blka borbtm">(.*?)</span>\s*<span class="blka">(.*?)</span>\s*</span>',
    re.DOTALL,
)


def _convert_efg_math_em(m: re.Match[str]) -> str:
    """Convert an <em>...</em> block containing <sub> or <sup> into $...$ math."""
    inner = m.group(1)
    if "<sub" not in inner and "<sup" not in inner:
        return m.group(0)
    s = inner
    s = re.sub(r"<sub>(.*?)</sub>", lambda sm: f"_{{{_tex_clean_atom(sm.group(1))}}}", s, flags=re.DOTALL)
    s = re.sub(r"<sup>(.*?)</sup>", lambda sm: f"^{{{_tex_clean_atom(sm.group(1))}}}", s, flags=re.DOTALL)
    s = _tex_clean_atom(s)
    s = s.replace("...", r"\dots ")
    return f"${s}$"


def _convert_efg_inline(raw_html: str) -> str:
    """Convert inline HTML inside an 1897 EFG paragraph, heading, or footnote to clean RST."""
    s = raw_html

    # 1. Strip page-number spans (anchors extracted prior to inline conversion)
    s = re.sub(r'<span class="pagenum">[\s\S]*?</span>', "", s)

    # 2. Unwrap transcriber <ins class="corr">...</ins>
    s = re.sub(r"<ins[^>]*>(.*?)</ins>", r"\1", s, flags=re.DOTALL)

    # 3. French ordinal superscript II<sup>me</sup> before math sub/sup handling
    s = re.sub(r"<sup>\s*me\s*</sup>", r"\\ :sup:`me`", s)

    # 4. Large display parens/slashes & radicals & blksum fractions
    s = re.sub(r"<sub>\s*<sub>\s*<span class=\"xxl\">/</span>\s*</sub>\s*</sub>", " / ", s)
    s = re.sub(r"<sub>\s*<span class=\"xl\">([()/])</span>\s*</sub>", r"\1", s)
    s = re.sub(
        r'<span class="xxl">\)</span><sup>\s*<sup>\s*<sup>\s*<span class="xs">2</span>\s*</sup>\s*</sup>\s*</sup>',
        r")$^2$",
        s,
    )
    s = re.sub(r'<span class="xxl">([()])</span>', r"\1", s)
    s = _EFG_SQRT_RE.sub(lambda m: rf"$\sqrt{{{_tex_clean_atom(m.group(1))}}}$", s)
    s = _EFG_BLKSUM_RE.sub(
        lambda m: rf"$\frac{{{_tex_clean_atom(m.group(1))}}}{{{_tex_clean_atom(m.group(2))}}}$",
        s,
    )

    # 5. <em>...</em> containing nested <sub> or <sup> -> $...$
    s = re.sub(r"<em>([\s\S]*?)</em>", _convert_efg_math_em, s)

    # 6. Base variable/symbol followed immediately by <sub>/<sup> and optional prime ′
    s = re.sub(
        r"(?:<em>([^<]+)</em>|(Σ|∞))"
        r"(?:<sub>(.*?)</sub>)?"
        r"(?:<sup>(.*?)</sup>)?"
        r"(′′|′|″)?",
        lambda m: (
            m.group(0)
            if not (m.group(3) or m.group(4) or m.group(2))
            else (
                m.group(0)
                if (m.group(2) and not m.group(3) and not m.group(4))
                else "$"
                + _tex_clean_atom(m.group(1) or m.group(2) or "")
                + (f"_{{{_tex_clean_atom(m.group(3))}}}" if m.group(3) else "")
                + (f"^{{{_tex_clean_atom(m.group(4))}}}" if m.group(4) else "")
                + ("''" if m.group(5) in ("′′", "″") else ("'" if m.group(5) else ""))
                + "$"
            )
        ),
        s,
    )

    # Remaining bare <sub> / <sup>
    s = re.sub(r"<sub>(.*?)</sub>", lambda m: f"$_{{{_tex_clean_atom(m.group(1))}}}$", s, flags=re.DOTALL)
    s = re.sub(r"<sup>(.*?)</sup>", lambda m: f"$^{{{_tex_clean_atom(m.group(1))}}}$", s, flags=re.DOTALL)

    # 7. Footnote anchors in body: <a id="FNanchor_7_7"></a><a class="fnanchor pginternal" href="#Footnote_7_7">[7]</a>
    s = re.sub(r'<a\s+id="FNanchor_\d+_\d+"\s*></a>', "", s)
    s = re.sub(
        r'<a\s+class="fnanchor[^"]*"\s+href="#Footnote_(\d+)_\d+"[^>]*>\[\d+\]</a>',
        r" [#efg_fn\1]_",
        s,
    )
    # Strip footnote return-label inside footnote definition: <a id="Footnote_1_1"></a><a href="#FNanchor_1_1"...><span class="label">[1]</span></a>
    s = re.sub(r'<a\s+id="Footnote_\d+_\d+"\s*></a>', "", s)
    s = re.sub(
        r'<a\s+href="#FNanchor_\d+_\d+"[^>]*><span class="label">\[\d+\]</span></a>\s*',
        "",
        s,
    )

    # 8. Section number anchor at start of paragraph: <b>12.</b><a id="N12"></a>
    s = re.sub(r"<b>(\d+\.)</b>\s*<a\s+id=\"N\d+\"\s*></a>", r"**\1** ", s)
    s = re.sub(r"<a\s+id=\"[A-Za-z0-9_]+\"\s*></a>", "", s)

    # 9. Internal links <a href="#N135" class="pginternal">...</a> (protected from tag stripping)
    efg_refs: list[str] = []

    def _store_efg_ref(rst_ref: str) -> str:
        idx = len(efg_refs)
        efg_refs.append(rst_ref)
        return f"PHOTONEFGREF{idx}END"

    def _repl_efg_link(m: re.Match[str]) -> str:
        href = m.group(1).strip()
        label = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        label = re.sub(r"\s+", " ", label)
        m_sec = re.match(r"^#N(\d+)$", href)
        if m_sec:
            return _store_efg_ref(f":ref:`{label} <efg-{m_sec.group(1)}>`")
        return label

    s = re.sub(r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>', _repl_efg_link, s, flags=re.DOTALL)

    # 10. Formatting tags: hoist any footnote marker outside closing bold/italic tags first
    s = re.sub(
        r"(\s*\[#[A-Za-z0-9_]+\]_)([.,;:]?)</(b|strong|em|i|cite)>",
        r"\2</\3>\1",
        s,
    )
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<(?:b|strong)[^>]*>(.*?)</(?:b|strong)>", _bold_wrap, s, flags=re.DOTALL)
    s = re.sub(r"<(?:em|i|cite)[^>]*>(.*?)</(?:em|i|cite)>", _italic_wrap, s, flags=re.DOTALL)
    s = re.sub(r"<[^>]+>", "", s)

    s = html.unescape(s)
    for idx, rst_ref in enumerate(efg_refs):
        s = s.replace(f"PHOTONEFGREF{idx}END", rst_ref)
    s = s.replace("\u202f", " ").replace("\u00a0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" *\n *", " ", s).strip()
    s = re.sub(r"^\((\d+|[a-z]|[ivx]+)\)\s+", r"**(\1)** ", s)
    return _fix_inline_rst_boundaries(s)


def _render_efg_figure(img_src: str, indent: str = "") -> list[str]:
    """Render a vector SVG ``.. figure::`` block for one of the 9 geometric figures in EFG."""
    basename = Path(img_src).name
    if basename not in EFG_FIGURE_INFO:
        return []
    svg_name, caption = EFG_FIGURE_INFO[basename]
    return [
        f"{indent}.. figure:: /_static/diagrams/{svg_name}",
        f"{indent}   :align: center",
        f"{indent}   :alt: {svg_name}",
        "",
        f"{indent}   {caption}",
        "",
    ]


def _parse_efg_footnotes(full_html: str) -> dict[str, list[str]]:
    """Parse all numbered footnote divs in EFG into indented RST lines (preserving multi-paragraph & Fig. 9)."""
    footnotes: dict[str, list[str]] = {}
    div_tag_re = re.compile(r"</?div\b[^>]*>")
    for m_start in re.finditer(r'<div class="footnote">', full_html):
        pos = m_start.start()
        depth = 0
        end_pos = len(full_html)
        for m_div in div_tag_re.finditer(full_html, pos):
            if m_div.group(0).startswith("</div"):
                depth -= 1
                if depth == 0:
                    end_pos = m_div.end()
                    break
            else:
                depth += 1
        chunk = full_html[pos:end_pos]
        m_id = re.search(r'id="Footnote_(\d+)_\d+"', chunk)
        if not m_id:
            continue
        fn_num = m_id.group(1)

        block_re = re.compile(
            r'(<div class="fig(?:center|right)">\s*<img[^>]+src="([^"]+)"[^>]*>\s*</div>|<p[^>]*>[\s\S]*?</p>)',
            re.DOTALL,
        )
        fn_blocks: list[str] = []
        first_para = True
        for bm in block_re.finditer(chunk):
            if bm.group(2):
                fn_blocks.extend(_render_efg_figure(bm.group(2), indent="   "))
            else:
                inner_p = re.sub(r"^<p[^>]*>|</p>$", "", bm.group(1).strip(), flags=re.DOTALL)
                txt = _convert_efg_inline(inner_p)
                if not txt:
                    continue
                if first_para:
                    fn_blocks.append(f".. [#efg_fn{fn_num}] {txt}")
                    fn_blocks.append("")
                    first_para = False
                else:
                    fn_blocks.append(f"   {txt}")
                    fn_blocks.append("")
        if fn_blocks:
            footnotes[fn_num] = fn_blocks
    return footnotes


def _compile_efg_chapter_en(
    spec: dict[str, Any],
    body_html: str,
    toc_map: dict[str, dict[str, Any]],
    all_footnotes: dict[str, list[str]],
    emitted_pages: set[str],
) -> str:
    """Compile a single 1897 EFG chapter slice into its verbatim `-en.rst` track."""
    stem = spec["stem"]
    sec_char = "~" if spec["has_subheadings"] else "-"

    lines: list[str] = [
        ":layout: book",
        "",
        f".. _efg-{stem}:",
        f".. _efg-{stem}-en:",
        "",
        _rst_heading(spec["heading"], "="),
        "",
        f".. rubric:: {spec['rubric']}",
        "",
    ]

    if spec["sec_range"] is not None:
        lines.extend(
            [
                ".. contents:: Analytical Section Outline",
                "   :local:",
                "   :depth: 3",
                "   :backlinks: none",
                "",
            ]
        )

    # Strip any trailing <div class="footnotes"> section from body_html (we attach referenced footnotes cleanly)
    fn_div_idx = body_html.find('<div class="footnotes">')
    if fn_div_idx != -1:
        body_html = body_html[:fn_div_idx]

    # Remove top-level <h2> chapter headers and Chapter III Section A/B <h3> headers
    body_html = re.sub(r"<h2[^>]*>[\s\S]*?</h2>", "", body_html)
    body_html = re.sub(r'<h3><a id="S[AB]"></a>[\s\S]*?</h3>', "", body_html)

    referenced_fns: list[str] = []
    pending_pages: list[str] = []
    seen_subheading = False

    token_re = re.compile(
        r'(<div class="poetry-container">\s*<div class="poetry">([\s\S]*?)</div>\s*</div>'
        r'|<div class="fig(?:center|right)">\s*<img[^>]+src="([^"]+)"[^>]*>\s*</div>'
        r"|<h([34])[^>]*>([\s\S]*?)</h\4>"
        r"|<p[^>]*>[\s\S]*?</p>)",
        re.DOTALL,
    )

    for m in token_re.finditer(body_html):
        tok = m.group(0)

        # Record any footnotes referenced in this block
        for fn_num in re.findall(r'href="#Footnote_(\d+)_\d+"', tok):
            if fn_num not in referenced_fns:
                referenced_fns.append(fn_num)

        # Record any page anchors inside this block
        for raw_pg in re.findall(r'id="Page_([A-Za-z0-9]+)"', tok):
            if raw_pg not in emitted_pages:
                pending_pages.append(raw_pg)
                emitted_pages.add(raw_pg)

        # Case 1: Poetry block
        if m.group(2) is not None:
            verses = re.findall(r"<p[^>]*>([\s\S]*?)</p>", m.group(2))
            for v in verses:
                v_txt = _convert_efg_inline(v)
                if v_txt:
                    lines.append(f"   | {v_txt}")
            lines.append("")
            continue

        # Case 2: Geometric figure
        if m.group(3) is not None:
            lines.extend(_render_efg_figure(m.group(3)))
            continue

        # Case 3: Subheading <h3> or <h4> (e.g. First Period., Kant., I. The Axiom of Free Mobility., Conclusion.)
        if m.group(4) is not None:
            seen_subheading = True
            raw_h = m.group(5)
            # Check if heading itself contains a footnote anchor (e.g. L7331 Footnote 163!)
            h_fns = re.findall(r'href="#Footnote_(\d+)_\d+"', raw_h)
            raw_h_clean = re.sub(r'<a\s+id="FNanchor_\d+_\d+"\s*></a>', "", raw_h)
            raw_h_clean = re.sub(r'<a\s+class="fnanchor[^"]*"[^>]*>\[\d+\]</a>', "", raw_h_clean)
            raw_h_clean = re.sub(r"<[^>]+>", "", raw_h_clean)
            h_text = re.sub(r"\s+", " ", html.unescape(raw_h_clean)).strip()
            lines.append(_rst_heading(h_text, "-"))
            lines.append("")
            if h_fns:
                fn_refs = " ".join(f"[#efg_fn{n}]_" for n in h_fns)
                lines.append(f"* Section heading note: {fn_refs}")
                lines.append("")
            continue

        # Case 4: Paragraph <p>...</p>
        m_sec = re.search(r'<a\s+id="N(\d+)"', tok)
        if m_sec:
            if spec["has_subheadings"] and not seen_subheading:
                lines.append(_rst_heading("Preliminary", "-"))
                lines.append("")
                seen_subheading = True
            sec_num = m_sec.group(1)
            toc_entry = toc_map.get(sec_num, {})
            sec_title = toc_entry.get("title_text", f"Section {sec_num}")
            sec_page = toc_entry.get("page", "")
            lines.append(f".. _efg-{sec_num}:")
            lines.append("")
            lines.append(_rst_heading(f"§ {sec_num}. {sec_title}", sec_char))
            lines.append("")
            if sec_page:
                lines.append(f".. folio:: §{sec_num}")
                lines.append(f"   :page: p. {sec_page}")
                lines.append("")

        inner_p = re.sub(r"^<p[^>]*>|</p>$", "", tok.strip(), flags=re.DOTALL)
        para_rst = _convert_efg_inline(inner_p)
        if not para_rst:
            continue

        for pg in pending_pages:
            lines.append(f".. _efg-p{pg}:")
            lines.append("")
        pending_pages.clear()

        is_centered = any(cls in tok[:40] for cls in ('class="center"', 'class="noindent pad2"'))
        if is_centered:
            lines.append(f"   {para_rst}")
        else:
            lines.append(para_rst)
        lines.append("")

    # Also scan footnotes themselves for nested footnote references (none expected, safe check)
    if referenced_fns:
        lines.append("----")
        lines.append("")
        lines.append(".. rubric:: Author's Footnotes (1897 Edition)")
        lines.append("")
        for fn_num in referenced_fns:
            if fn_num in all_footnotes:
                lines.extend(all_footnotes[fn_num])

    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Companion Tracks (-summary.rst & -notes.rst) and Book Index Pages
# ---------------------------------------------------------------------------


def _compile_summary_track(
    prefix: str,
    spec: dict[str, Any],
    apparatus: ChapterApparatus,
) -> str:
    """Render `<stem>-summary.rst` for a chapter unit."""
    stem = spec["stem"]
    title = f"Summary — {spec['toc_title']}"
    lines: list[str] = [
        ":layout: book",
        "",
        f".. _{prefix}-{stem}-summary:",
        "",
        _rst_heading(title, "="),
        "",
        (f"*Primary Text:* :ref:`Read Verbatim Treatise Track ({spec['pages']}) <{prefix}-{stem}-en>` · "
        f"*Commentary:* :ref:`Critical Notes <{prefix}-{stem}-notes>`"),
        "",
        "Executive Summary",
        "-----------------",
        "",
        apparatus.executive_summary,
        "",
        "Argumentative Architecture",
        "--------------------------",
        "",
        ".. code-block:: text",
        "",
    ]
    for mline in apparatus.mermaid_flow.splitlines():
        lines.append(f"   {mline}")
    lines.extend(["", "Key Arguments & Theses", "----------------------", ""])
    for arg_title, arg_body in apparatus.key_arguments:
        lines.append(_rst_heading(arg_title, "~"))
        lines.append("")
        lines.append(arg_body)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _compile_notes_track(
    prefix: str,
    spec: dict[str, Any],
    apparatus: ChapterApparatus,
) -> str:
    """Render `<stem>-notes.rst` for a chapter unit."""
    stem = spec["stem"]
    title = f"Critical Notes — {spec['toc_title']}"
    lines: list[str] = [
        ":layout: book",
        "",
        f".. _{prefix}-{stem}-notes:",
        "",
        _rst_heading(title, "="),
        "",
        (f"*Primary Text:* :ref:`Read Verbatim Treatise Track ({spec['pages']}) <{prefix}-{stem}-en>` · "
        f"*Overview:* :ref:`Analytical Summary <{prefix}-{stem}-summary>` · "
        f"*Cross-Corpus Loci:* :ref:`Master Concordance <concordance>`"),
        "",
        "Historical & Cross-Corpus Commentary",
        "------------------------------------",
        "",
    ]
    for note_title, note_body in apparatus.critical_notes:
        lines.append(_rst_heading(note_title, "~"))
        lines.append("")
        lines.append(note_body)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _compile_pom_book_index() -> str:
    """Generate `docsrc/principles_of_mathematics/index.rst`."""
    lines: list[str] = [
        ":navigation: header",
        ":order: 1",
        ":layout: book",
        ":title: Principles of Mathematics (1903)",
        ":book_title: The Principles of Mathematics",
        ":book_subtitle: Vol. I — Preface, Part I (Ch. I), and Part VI: Space (1903)",
        ":author: Bertrand Russell, M.A.",
        ":series: First Edition (Excluding 1937 Second-Edition Introduction)",
        ":publisher: At the University Press",
        ":location: Cambridge",
        ":year: 1903",
        "",
        ".. _pom-index:",
        ".. _principles-of-mathematics-index:",
        "",
        "THE PRINCIPLES OF MATHEMATICS",
        "=============================",
        "",
        ".. rubric:: Vol. I — 1903 First Edition: Preface, Part I (Chapter I), and Part VI (*Space*, Chapters XLIV–LII)",
        "",
        ".. container:: title-page",
        "",
        "   | **THE PRINCIPLES OF MATHEMATICS**",
        "   | BY :person:`BERTRAND RUSSELL <russell>`, M.A.",
        "   | LATE FELLOW OF TRINITY COLLEGE, CAMBRIDGE",
        "   | VOL. I",
        "   | CAMBRIDGE: AT THE UNIVERSITY PRESS — 1903",
        "",
        "Editorial Scope & Public-Domain Provenance",
        "------------------------------------------",
        "",
        ("This Book Codex presents the **unabridged, verbatim 1903 Cambridge University Press first edition** "
        "of the foundational and geometrical portions of :cite:`*The Principles of Mathematics* <russell:1903>`: "
        "the **1903 Preface** (pp. v–ix), **Part I, Chapter I** (*Definition of Pure Mathematics*, §§ 1–10, pp. 3–9), "
        "and the complete **Part VI: Space** (**Chapters XLIV–LII**, §§ 351–436, pp. 371–461)—comprising **96 numbered "
        "sections** in full, including **Chapter XLVII (§§ 389–391, pp. 404–407)** where Russell formulates his "
        "celebrated critique of :person:`Euclid <euclid>`'s circle-intersection assumption (``I.1``) and method of "
        ":term:`superposition <superposition>` (``I.4``) directly answered by :person:`Fr. Petrus Hoenen, S.J. <hoenen>` "
        "in :cite:`*De Noetica Geometriae* <hoenen:1954>` (Caput IV) and cited by :person:`Sir Thomas L. Heath <heath>` "
        "in :cite:`*The Thirteen Books of Euclid's Elements* <euclid:elements:i-4>` (Vol. I, pp. 225–227, 249)."),
        "",
        ".. note::",
        "",
        ("   Russell's later Introduction to the 1937 George Allen & Unwin second edition remains under copyright "
        "   in several jurisdictions and is strictly **excluded** from this edition."),
        "",
        "----",
        "",
        "Analytical Table of Contents",
        "----------------------------",
        "",
    ]

    for spec in POM_CHAPTER_SPECS:
        stem = spec["stem"]
        lines.append(_rst_heading(spec["toc_title"], "~"))
        lines.append("")
        lines.append(f"*{spec['part_label']} · {spec['pages']}*")
        lines.append("")
        lines.append(
            f":ref:`English (1903) <pom-{stem}-en>` · "
            f":ref:`Summary <pom-{stem}-summary>` · "
            f":ref:`Notes <pom-{stem}-notes>`"
        )
        lines.append("")

    lines.extend(
        [
            ".. toctree::",
            "   :maxdepth: 2",
            "   :hidden:",
            "   :caption: 1903 Treatise (Verbatim)",
            "",
        ]
    )
    for spec in POM_CHAPTER_SPECS:
        s = spec["stem"]
        lines.append(f"   {s}/{s}-en")

    lines.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: Summaries & Critical Notes",
            "",
        ]
    )
    for spec in POM_CHAPTER_SPECS:
        s = spec["stem"]
        lines.append(f"   {s}/{s}-summary")
        lines.append(f"   {s}/{s}-notes")

    return "\n".join(lines) + "\n"


def _compile_efg_book_index() -> str:
    """Generate `docsrc/foundations_of_geometry/index.rst`."""
    lines: list[str] = [
        ":navigation: header",
        ":order: 2",
        ":layout: book",
        ":title: Foundations of Geometry (1897)",
        ":book_title: An Essay on the Foundations of Geometry",
        ":book_subtitle: Complete First Edition (§§ 1–209, 1897)",
        ":author: Bertrand A. W. Russell, M.A.",
        ":series: Fellowship Dissertation Expansion, Trinity College, Cambridge",
        ":publisher: At the University Press",
        ":location: Cambridge",
        ":year: 1897",
        "",
        ".. _efg-index:",
        ".. _foundations-of-geometry-index:",
        "",
        "AN ESSAY ON THE FOUNDATIONS OF GEOMETRY",
        "=======================================",
        "",
        ".. rubric:: Complete 1897 Cambridge University Press First Edition (Preface, Dedication, and §§ 1–209)",
        "",
        ".. container:: title-page",
        "",
        "   | **AN ESSAY ON THE FOUNDATIONS OF GEOMETRY**",
        "   | BY :person:`BERTRAND A. W. RUSSELL <russell>`, M.A.",
        "   | FELLOW OF TRINITY COLLEGE, CAMBRIDGE",
        "   | CAMBRIDGE: AT THE UNIVERSITY PRESS — 1897",
        "   | *To John McTaggart Ellis McTaggart, to whose discourse and friendship is owing the existence of this book.*",
        "",
        "Editorial Scope & Diagram Reconstructions",
        "-----------------------------------------",
        "",
        ("This Book Codex reproduces the **complete, unabridged 1897 Cambridge University Press first edition** "
        "of :cite:`*An Essay on the Foundations of Geometry* <russell:1897>` (xvi + 201 pp., **all 209 numbered "
        "sections §§ 1–209** and **all 171 authorial footnotes**), accompanied by **9 exact analytical vector SVG "
        "diagrams** newly reconstructed from Russell's geometric specifications—including :person:`von Staudt <staudt>`'s "
        ":term:`complete quadrilateral harmonic construction <quadrilateral-construction>` (Fig. 8, p. 125, :ref:`§ 113 <efg-113>`)."),
        "",
        "----",
        "",
        "Analytical Table of Contents",
        "----------------------------",
        "",
    ]

    for spec in EFG_CHAPTER_SPECS:
        stem = spec["stem"]
        lines.append(_rst_heading(spec["toc_title"], "~"))
        lines.append("")
        lines.append(f"*{spec['pages']}*")
        lines.append("")
        lines.append(
            f":ref:`English (1897) <efg-{stem}-en>` · "
            f":ref:`Summary <efg-{stem}-summary>` · "
            f":ref:`Notes <efg-{stem}-notes>`"
        )
        lines.append("")

    lines.extend(
        [
            ".. toctree::",
            "   :maxdepth: 2",
            "   :hidden:",
            "   :caption: 1897 Treatise (Verbatim)",
            "",
        ]
    )
    for spec in EFG_CHAPTER_SPECS:
        s = spec["stem"]
        lines.append(f"   {s}/{s}-en")

    lines.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: Summaries & Critical Notes",
            "",
        ]
    )
    for spec in EFG_CHAPTER_SPECS:
        s = spec["stem"]
        lines.append(f"   {s}/{s}-summary")
        lines.append(f"   {s}/{s}-notes")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Top-Level Apparatus Pages: Concordance, Bibliography, Persons, Glossary
# ---------------------------------------------------------------------------


def _compile_concordance_page(repo_root: Path) -> str:
    """Generate `docsrc/concordance.rst` linking Russell (1897 & 1903) to Hoenen, Heath's Euclid, and Pappus."""
    entries = load_concordance(repo_root)
    lines: list[str] = [
        ":navigation: header",
        ":order: 3",
        ":layout: book",
        ":title: Concordance",
        "",
        ".. _concordance:",
        "",
        "CROSS-CORPUS CONCORDANCE",
        "========================",
        "",
        ".. rubric:: Bidirectional Loci Across Russell (1897 & 1903), Hoenen (*De Noetica Geometriae*, 1954), Heath's *Euclid* (1908), and *Pappus*",
        "",
        ("This master concordance maps the foundational geometric arguments of :person:`Bertrand Russell <russell>` across "
        "his two Cambridge treatises—:cite:`*An Essay on the Foundations of Geometry* (1897) <russell:1897>` and "
        ":cite:`*The Principles of Mathematics* (1903) <russell:1903>`—directly to the classical and philosophical "
        "corpora in the **GEOMETOR** initiative: :person:`Fr. Petrus Hoenen, S.J. <hoenen>`'s Thomistic critique in "
        ":cite:`*De Noetica Geometriae* (1954) <hoenen:1954>`, :person:`Sir Thomas L. Heath <heath>`'s commentary on "
        ":cite:`*Euclid's Elements* (1908) <euclid:elements:i-4>`, and :person:`Pappus of Alexandria <pappus>`'s "
        "projective cross-ratio lemmas in :cite:`*Collection* Book VII <pappus:collection:vii>`."),
        "",
        ".. contents:: Thematic Loci",
        "   :local:",
        "   :depth: 2",
        "   :backlinks: none",
        "",
        "Summary Matrix",
        "--------------",
        "",
        ".. list-table:: Master Concordance of Geometric Foundations",
        "   :header-rows: 1",
        "   :widths: 28 22 22 28",
        "",
        "   * - Foundational Theme",
        "     - Russell *PoM* (1903)",
        "     - Russell *EFG* (1897)",
        "     - GEOMETOR Sister Corpora",
    ]

    for entry in entries:
        sec_1903 = ", ".join(f"§{s}" for s in entry.russell_1903.sections)
        sec_1897 = ", ".join(f"§{s}" for s in entry.russell_1897.sections)
        ext_summary = "; ".join(f"{e.corpus} ({e.locus})" for e in entry.external_loci)
        lines.extend(
            [
                f"   * - :ref:`{entry.theme} <conc-{entry.id}>`",
                f"     - :ref:`{sec_1903} <{entry.russell_1903.anchor}>` ({entry.russell_1903.pages})",
                f"     - :ref:`{sec_1897} <{entry.russell_1897.anchor}>` ({entry.russell_1897.pages})",
                f"     - {ext_summary}",
            ]
        )

    lines.extend(["", "----", "", "Detailed Analytical Concordance Entries", "---------------------------------------", ""])

    for idx, entry in enumerate(entries, start=1):
        lines.append(f".. _conc-{entry.id}:")
        lines.append("")
        lines.append(_rst_heading(f"{idx}. {entry.theme}", "~"))
        lines.append("")
        r03_links = ", ".join(f":ref:`§ {s} <pom-{s}>`" for s in entry.russell_1903.sections)
        r97_links = ", ".join(f":ref:`§ {s} <efg-{s}>`" for s in entry.russell_1897.sections)
        lines.append(
            f"* **1903 Principles of Mathematics:** {r03_links} ({entry.russell_1903.pages}) — "
            f":ref:`Chapter Unit <pom-{entry.russell_1903.chapter}-en>` · "
            f":ref:`Critical Notes <pom-{entry.russell_1903.chapter}-notes>`"
        )
        lines.append(
            f"* **1897 Foundations of Geometry:** {r97_links} ({entry.russell_1897.pages}) — "
            f":ref:`Chapter Unit <efg-{entry.russell_1897.chapter}-en>` · "
            f":ref:`Critical Notes <efg-{entry.russell_1897.chapter}-notes>`"
        )
        lines.append("")
        if entry.russell_1903.verbatim_excerpt:
            lines.append(".. pull-quote::")
            lines.append("")
            lines.append(f'   "{entry.russell_1903.verbatim_excerpt}"')
            lines.append(f"   — *The Principles of Mathematics* (1903), {entry.russell_1903.pages}")
            lines.append("")
        lines.append("**Cross-Corpus Relations:**")
        lines.append("")
        for ext in entry.external_loci:
            just_badge = ""
            if ext.corpus == "euclid-elements":
                first_id = ext.locus.split(",")[0].strip()
                just_badge = f" (:just:`{first_id}`)"
            lines.append(f"* **{ext.corpus}** — *{ext.work}*, ``{ext.locus}``{just_badge}: {ext.relation}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _compile_bibliography_page(citations: dict[str, dict[str, Any]]) -> str:
    """Generate `docsrc/bibliography.rst` with `#cite-<slug>` anchors matching `publish`."""
    lines: list[str] = [
        ":title: Systematic Bibliography & Cited Sources",
        ":layout: book",
        "",
        ".. _bibliography:",
        "",
        "Bibliography & Cited Sources",
        "============================",
        "",
        ".. rubric:: Primary Russell Editions, 19th-Century Geometrical Sources, and GEOMETOR Critical Apparatus",
        "",
        (f"This bibliography catalogues **{len(citations)} foundational treatises, memoirs, and critical editions** "
        "referenced across the 1897 and 1903 Book Codexes and cross-corpus notes. Every inline ``:cite:`` role "
        "links directly to its corresponding entry below."),
        "",
        "----",
        "",
    ]
    for key, info in citations.items():
        slug = apparatus_slug(key)
        title_line = f"{info['author']} — {info['work']} ({info['year']})"
        lines.extend(
            [
                f".. _cite-{slug}:",
                "",
                _rst_heading(title_line, "-"),
                "",
                f"* **Citation Key:** ``{key}``",
                f"* **Publication / Locus:** {info.get('locus', '')}",
                f"* **Context:** {info.get('note', '')}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _compile_persons_page(persons: dict[str, dict[str, Any]]) -> str:
    """Generate `docsrc/persons.rst` with `#person-<slug>` anchors matching `publish`."""
    lines: list[str] = [
        ":title: Biographical Register of Geometers & Philosophers",
        ":layout: book",
        "",
        ".. _persons:",
        "",
        "Biographical Register of Persons",
        "================================",
        "",
        ".. rubric:: Mathematicians, Logicians, and Philosophers of Space in Russell's Geometric Treatises",
        "",
        (f"This register profiles **{len(persons)} geometers, logicians, and philosophers** discussed across "
        ":cite:`*An Essay on the Foundations of Geometry* (1897) <russell:1897>`, "
        ":cite:`*The Principles of Mathematics* (1903) <russell:1903>`, and the GEOMETOR critical commentary. "
        "Every inline ``:person:`` reference resolves directly to its biographical entry here."),
        "",
        "----",
        "",
    ]
    for key in sorted(persons.keys(), key=lambda k: persons[k]["name"]):
        info = persons[key]
        slug = apparatus_slug(key)
        heading = f"{info['name']} ({info['dates']})"
        lines.extend(
            [
                f".. _person-{slug}:",
                "",
                _rst_heading(heading, "-"),
                "",
                f"*{info['role']}*",
                "",
                info["bio"],
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _compile_glossary_page(glossary: dict[str, dict[str, Any]]) -> str:
    """Generate `docsrc/glossary.rst` with `#term-<slug>` anchors matching `publish`."""
    lines: list[str] = [
        ":title: Technical Glossary of Geometric & Logical Terms",
        ":layout: book",
        "",
        ".. _glossary:",
        "",
        "Technical Glossary",
        "==================",
        "",
        ".. rubric:: Projective, Descriptive, Metrical, Logicist, and Scholastic Terminology",
        "",
        (f"This lexicon defines **{len(glossary)} technical concepts** central to Russell's 1897 and 1903 geometric "
        "treatises and their reception in Hoenen and Heath. Every inline ``:term:`` role links directly to its "
        "entry below."),
        "",
        "----",
        "",
    ]
    for key in sorted(glossary.keys(), key=lambda k: glossary[k]["headword"].lower()):
        info = glossary[key]
        slug = apparatus_slug(key)
        lines.extend(
            [
                f".. _term-{slug}:",
                "",
                _rst_heading(info["headword"], "-"),
                "",
                f"* **Tradition / Domain:** {info['language']}",
                f"* **Concise Formulation:** *{info['translation']}*",
                "",
                info["definition"],
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Master Build Entry Point
# ---------------------------------------------------------------------------


def compile_all(repo_root: Path | None = None) -> dict[str, int]:
    """Compile all SVG figures, Codex I (1903), Codex II (1897), and scholarly apparatus into ``docsrc/``."""
    root = repo_root or get_repo_root()
    sources_dir = root / "resources" / "bertrand_russell" / "sources"
    docsrc = root / "docsrc"

    # 1. Generate all 9 analytical SVG diagrams
    svg_paths = generate_all_diagrams(docsrc / "_static" / "diagrams")

    # 2. Compile Codex I: 1903 The Principles of Mathematics
    pom_html = (sources_dir / "pom_1903_extract.html").read_text(encoding="utf-8")
    pom_toc = json.loads((sources_dir / "pom_1903_toc.json").read_text(encoding="utf-8"))
    pom_license_idx = pom_html.index('http://creativecommons.org/publicdomain/mark/1.0/')
    pom_end_hr = pom_html.rfind("<hr />", 0, pom_license_idx)

    pom_starts: list[int] = []
    for spec in POM_CHAPTER_SPECS:
        marker = f'id="{spec["html_id"]}"'
        pos = pom_html.index(marker)
        h2_start = pom_html.rfind("<h2", 0, pos)
        pom_starts.append(h2_start)

    pom_root = docsrc / "principles_of_mathematics"
    pom_root.mkdir(parents=True, exist_ok=True)
    (pom_root / "index.rst").write_text(_compile_pom_book_index(), encoding="utf-8")

    pom_files_written = 1
    for i, spec in enumerate(POM_CHAPTER_SPECS):
        start_pos = pom_starts[i]
        end_pos = pom_starts[i + 1] if i + 1 < len(POM_CHAPTER_SPECS) else pom_end_hr
        raw_chunk = pom_html[start_pos:end_pos]
        # Trim any trailing <h1 id="part..."> header belonging to the next Part
        raw_chunk = re.sub(r'<hr\s*/>\s*<h1 id="part\d+"[\s\S]*$', "", raw_chunk)

        ch_dir = pom_root / spec["stem"]
        ch_dir.mkdir(parents=True, exist_ok=True)
        stem = spec["stem"]
        apparatus = POM_APPARATUS[stem]

        (ch_dir / f"{stem}-en.rst").write_text(
            _compile_pom_chapter_en(spec, raw_chunk, pom_toc), encoding="utf-8"
        )
        (ch_dir / f"{stem}-summary.rst").write_text(
            _compile_summary_track("pom", spec, apparatus), encoding="utf-8"
        )
        (ch_dir / f"{stem}-notes.rst").write_text(
            _compile_notes_track("pom", spec, apparatus), encoding="utf-8"
        )
        pom_files_written += 3

    # 3. Compile Codex II: 1897 An Essay on the Foundations of Geometry
    efg_html = (sources_dir / "efg_1897_pg52091.html").read_text(encoding="utf-8")
    efg_toc = json.loads((sources_dir / "efg_1897_toc.json").read_text(encoding="utf-8"))
    all_efg_footnotes = _parse_efg_footnotes(efg_html)

    idx_pref = efg_html.index("<h2>PREFACE.</h2>")
    idx_toc = efg_html.index('<h2> <a id="CONTENTS">')
    idx_intro = efg_html.index("<h2>INTRODUCTION.")
    idx_ch1 = efg_html.index('<h2><a id="CHAP_I">')
    idx_ch2 = efg_html.index('<h2><a id="CHAP_II">')
    idx_ch3a = efg_html.index('<h2><a id="CHAP_III">')
    idx_ch3b = efg_html.index('<h3><a id="SB">')
    idx_ch4 = efg_html.index('<h2><a id="CHAP_IV">')
    idx_colophon = efg_html.index('<hr class="chap pg-brk">', idx_ch4)

    efg_slices: dict[str, str] = {
        "preface": efg_html[idx_pref:idx_toc],
        "intro": efg_html[idx_intro:idx_ch1],
        "ch-01-metageometry": efg_html[idx_ch1:idx_ch2],
        "ch-02-critique": efg_html[idx_ch2:idx_ch3a],
        "ch-03a-projective": efg_html[idx_ch3a:idx_ch3b],
        "ch-03b-metrical": efg_html[idx_ch3b:idx_ch4],
        "ch-04-consequences": efg_html[idx_ch4:idx_colophon],
    }

    efg_root = docsrc / "foundations_of_geometry"
    efg_root.mkdir(parents=True, exist_ok=True)
    (efg_root / "index.rst").write_text(_compile_efg_book_index(), encoding="utf-8")

    emitted_efg_pages: set[str] = set()
    efg_files_written = 1
    for spec in EFG_CHAPTER_SPECS:
        stem = spec["stem"]
        ch_dir = efg_root / stem
        ch_dir.mkdir(parents=True, exist_ok=True)
        apparatus = EFG_APPARATUS[stem]

        (ch_dir / f"{stem}-en.rst").write_text(
            _compile_efg_chapter_en(
                spec, efg_slices[stem], efg_toc, all_efg_footnotes, emitted_efg_pages
            ),
            encoding="utf-8",
        )
        (ch_dir / f"{stem}-summary.rst").write_text(
            _compile_summary_track("efg", spec, apparatus), encoding="utf-8"
        )
        (ch_dir / f"{stem}-notes.rst").write_text(
            _compile_notes_track("efg", spec, apparatus), encoding="utf-8"
        )
        efg_files_written += 3

    # 4. Compile Top-Level Apparatus Pages
    registries = load_apparatus_registries(root)
    (docsrc / "concordance.rst").write_text(_compile_concordance_page(root), encoding="utf-8")
    (docsrc / "bibliography.rst").write_text(
        _compile_bibliography_page(registries["citations"]), encoding="utf-8"
    )
    (docsrc / "persons.rst").write_text(
        _compile_persons_page(registries["persons"]), encoding="utf-8"
    )
    (docsrc / "glossary.rst").write_text(
        _compile_glossary_page(registries["glossary"]), encoding="utf-8"
    )

    return {
        "svg_diagrams": len(svg_paths),
        "pom_rst_files": pom_files_written,
        "efg_rst_files": efg_files_written,
        "apparatus_rst_files": 4,
    }


def main() -> None:
    """CLI entry point to compile the Bertrand Russell Geometric Codex."""
    stats = compile_all()
    print(
        f"Compiled Bertrand Russell Codex: {stats['pom_rst_files']} PoM (1903) RST files, "
        f"{stats['efg_rst_files']} EFG (1897) RST files, {stats['svg_diagrams']} SVG diagrams, "
        f"and {stats['apparatus_rst_files']} apparatus pages."
    )


if __name__ == "__main__":
    main()
