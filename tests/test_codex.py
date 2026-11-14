"""Verification suite for geometor.bertrand_russell Dual Book Codex & Concordance."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

from geometor.bertrand_russell import (
    __version__,
    apparatus_slug,
    find_concordance_by_corpus,
    find_concordance_by_section,
    load_apparatus_registries,
    load_concordance,
    load_sources_manifest,
    verify_source_checksums,
)
from geometor.bertrand_russell.commentary import EFG_APPARATUS, POM_APPARATUS
from geometor.bertrand_russell.compile_codex import EFG_CHAPTER_SPECS, POM_CHAPTER_SPECS
from geometor.bertrand_russell.diagrams import DIAGRAM_SPECS

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCSRC = REPO_ROOT / "docsrc"


def _strip_rst_inline_markup(text: str) -> str:
    """Normalize compiled RST text to plain prose for verbatim substring comparison."""
    s = text
    s = re.sub(r":(?:ref|cite|person|term):`([^`<]+?)\s*<[^>]+>`", r"\1", s)
    s = re.sub(r"\s*\[#[A-Za-z0-9_]+\]_", "", s)
    s = s.replace(r"\ ", "")
    s = s.replace("**", "").replace("*", "").replace("$", "")
    return re.sub(r"\s+", " ", s).strip()


def test_package_version_and_source_checksums() -> None:
    """All archived 1897 and 1903 primary source files match SHA-256 checksums and byte counts."""
    assert __version__ == "0.1.1"
    manifest = load_sources_manifest(REPO_ROOT)
    assert len(manifest.get("works", [])) == 2
    verification = verify_source_checksums(REPO_ROOT)
    assert len(verification) == 5
    assert all(ok for _path, ok in verification), f"Checksum mismatch: {verification}"


def test_pom_1903_codex_completeness_and_public_domain_scope() -> None:
    """Codex I covers all 11 multi-track units, all 96 sections, and omits the 1937 introduction."""
    pom_dir = DOCSRC / "principles_of_mathematics"
    assert (pom_dir / "index.rst").is_file()
    assert len(POM_CHAPTER_SPECS) == 11
    assert len(POM_APPARATUS) == 11

    en_texts: list[str] = []
    for spec in POM_CHAPTER_SPECS:
        stem = spec["stem"]
        unit_dir = pom_dir / stem
        for track in ("en", "summary", "notes"):
            track_path = unit_dir / f"{stem}-{track}.rst"
            assert track_path.is_file(), f"Missing PoM track file: {track_path}"
        en_content = (unit_dir / f"{stem}-en.rst").read_text(encoding="utf-8")
        assert ".. code-block:: python" not in en_content
        assert "Introduction to the Second Edition" not in en_content
        assert "1937" not in en_content
        en_texts.append(en_content)

    combined_en = "\n".join(en_texts)
    expected_sections = list(range(1, 11)) + list(range(351, 437))
    assert len(expected_sections) == 96
    for sec in expected_sections:
        matches = re.findall(rf"^\.\. _pom-{sec}:$", combined_en, flags=re.MULTILINE)
        assert len(matches) == 1, f"Expected unique anchor .. _pom-{sec}:, got {len(matches)}"

    ch47_en = (pom_dir / "ch-47-metrical" / "ch-47-metrical-en.rst").read_text(encoding="utf-8")
    for page_num in (404, 405, 406, 407):
        assert f".. _pom-p{page_num}:" in ch47_en


def test_efg_1897_codex_completeness_and_footnotes() -> None:
    """Codex II covers all 7 multi-track units, all 209 sections, and balanced footnotes."""
    efg_dir = DOCSRC / "foundations_of_geometry"
    assert (efg_dir / "index.rst").is_file()
    assert len(EFG_CHAPTER_SPECS) == 7
    assert len(EFG_APPARATUS) == 7

    en_texts: list[str] = []
    total_fn_defs = 0
    for spec in EFG_CHAPTER_SPECS:
        stem = spec["stem"]
        unit_dir = efg_dir / stem
        for track in ("en", "summary", "notes"):
            track_path = unit_dir / f"{stem}-{track}.rst"
            assert track_path.is_file(), f"Missing EFG track file: {track_path}"
        en_content = (unit_dir / f"{stem}-en.rst").read_text(encoding="utf-8")
        assert ".. code-block:: python" not in en_content
        en_texts.append(en_content)

        fn_refs = set(re.findall(r"\[#(efg_fn\d+)\]_", en_content))
        fn_defs = set(re.findall(r"^\.\. \[#(efg_fn\d+)\]", en_content, flags=re.MULTILINE))
        assert fn_refs == fn_defs, f"Footnote mismatch in {stem}: diff={fn_refs ^ fn_defs}"
        total_fn_defs += len(fn_defs)

    assert total_fn_defs >= 170

    combined_en = "\n".join(en_texts)
    for sec in range(1, 210):
        matches = re.findall(rf"^\.\. _efg-{sec}:$", combined_en, flags=re.MULTILINE)
        assert len(matches) == 1, f"Expected unique anchor .. _efg-{sec}:, got {len(matches)}"


def test_verbatim_passages_and_concordance_excerpts() -> None:
    """Canonical passages in both codices and all concordance 1903 excerpts match verbatim."""
    pom_ch1 = _strip_rst_inline_markup(
        (DOCSRC / "principles_of_mathematics" / "ch-01-pure-math" / "ch-01-pure-math-en.rst").read_text(
            encoding="utf-8"
        )
    )
    assert "Pure Mathematics is the class of all propositions of the form" in pom_ch1

    pom_ch47 = _strip_rst_inline_markup(
        (DOCSRC / "principles_of_mathematics" / "ch-47-metrical" / "ch-47-metrical-en.rst").read_text(
            encoding="utf-8"
        )
    )
    for phrase in (
        "There is no evidence whatever that the circles which we are told to construct intersect",
        "strikes every intelligent child as a juggle",
        "can no more change its position than the leopard can change his spots",
        "column of mercury in a thermometer",
        "most fatally vicious circle if we attempt to define metrical properties by rigidity",
        "This is, in fact, the exact assumption which is concealed in the method of superposition.",
    ):
        assert phrase in pom_ch47, f"Missing canonical PoM Ch. XLVII phrase: {phrase}"

    efg_ch3a = _strip_rst_inline_markup(
        (DOCSRC / "foundations_of_geometry" / "ch-03a-projective" / "ch-03a-projective-en.rst").read_text(
            encoding="utf-8"
        )
    )
    assert "Given any three points A, B, D in one straight line, the quadrilateral construction" in efg_ch3a

    efg_ch3b = _strip_rst_inline_markup(
        (DOCSRC / "foundations_of_geometry" / "ch-03b-metrical" / "ch-03b-metrical-en.rst").read_text(
            encoding="utf-8"
        )
    )
    assert "Spatial magnitudes can be moved from place to place without distortion" in efg_ch3b

    entries = load_concordance(REPO_ROOT)
    assert len(entries) == 10
    for entry in entries:
        stem = entry.russell_1903.chapter
        chapter_rst = (DOCSRC / "principles_of_mathematics" / stem / f"{stem}-en.rst").read_text(
            encoding="utf-8"
        )
        normalized_chapter = _strip_rst_inline_markup(chapter_rst)
        normalized_excerpt = re.sub(r"\s+", " ", entry.russell_1903.verbatim_excerpt).strip()
        assert normalized_excerpt in normalized_chapter, (
            f"Concordance excerpt for {entry.id} not found verbatim in {stem}-en.rst"
        )


def test_svg_diagrams_well_formed_and_embedded() -> None:
    """All 9 analytical SVG diagrams parse as valid XML/SVG and are embedded in Codex II."""
    diag_dir = DOCSRC / "_static" / "diagrams"
    assert len(DIAGRAM_SPECS) == 9

    efg_all_rst = "\n".join(
        p.read_text(encoding="utf-8")
        for p in sorted((DOCSRC / "foundations_of_geometry").rglob("*-en.rst"))
    )

    for svg_name, _builder_fn in DIAGRAM_SPECS.values():
        svg_path = diag_dir / svg_name
        assert svg_path.is_file(), f"Missing diagram SVG: {svg_path}"
        raw_svg = svg_path.read_text(encoding="utf-8")
        assert len(raw_svg) > 400
        root = ET.fromstring(raw_svg)
        assert root.tag.endswith("svg")
        assert root.attrib.get("viewBox")
        assert f"/_static/diagrams/{svg_name}" in efg_all_rst, f"SVG {svg_name} not referenced in EFG"


def test_concordance_queries_and_apparatus_role_integrity() -> None:
    """All :cite:, :person:, :term:, and :ref: roles across docsrc/ resolve without orphans."""
    hoenen_entries = find_concordance_by_corpus("geometor/hoenen", REPO_ROOT)
    euclid_entries = find_concordance_by_corpus("geometor/euclid", REPO_ROOT)
    pappus_entries = find_concordance_by_corpus("geometor/pappus", REPO_ROOT)
    assert len(hoenen_entries) >= 6
    assert len(euclid_entries) >= 2
    assert len(pappus_entries) >= 1

    sec390_entries = find_concordance_by_section("1903", "390", REPO_ROOT)
    assert len(sec390_entries) >= 2

    regs = load_apparatus_registries(REPO_ROOT)
    citations = regs["citations"]
    persons = regs["persons"]
    glossary = regs["glossary"]

    bib_rst = (DOCSRC / "bibliography.rst").read_text(encoding="utf-8")
    pers_rst = (DOCSRC / "persons.rst").read_text(encoding="utf-8")
    glos_rst = (DOCSRC / "glossary.rst").read_text(encoding="utf-8")

    all_rst_files = [
        p for p in sorted(DOCSRC.rglob("*.rst")) if "modules/api/" not in p.as_posix()
    ]
    assert len(all_rst_files) >= 65

    defined_labels: set[str] = set()
    for rst_file in all_rst_files:
        txt = rst_file.read_text(encoding="utf-8")
        for lbl in re.findall(r"^\.\. _([A-Za-z0-9_.-]+):$", txt, flags=re.MULTILINE):
            defined_labels.add(lbl.lower())

    role_re = re.compile(r":(cite|person|term|ref):`([^`]+)`")
    for rst_file in all_rst_files:
        txt = rst_file.read_text(encoding="utf-8")
        for role, body in role_re.findall(txt):
            m_target = re.search(r"<([^>]+)>\s*$", body)
            target = m_target.group(1).strip() if m_target else body.strip()
            if role == "cite":
                assert target in citations, f"Unregistered :cite: `{target}` in {rst_file}"
                assert f".. _cite-{apparatus_slug(target)}:" in bib_rst
            elif role == "person":
                assert target in persons, f"Unregistered :person: `{target}` in {rst_file}"
                assert f".. _person-{apparatus_slug(target)}:" in pers_rst
            elif role == "term":
                assert target in glossary, f"Unregistered :term: `{target}` in {rst_file}"
                assert f".. _term-{apparatus_slug(target)}:" in glos_rst
            elif role == "ref":
                assert target.lower() in defined_labels, (
                    f"Unresolved :ref: `{target}` in {rst_file}"
                )
