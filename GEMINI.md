# GEMINI.md — `geometor/bertrand-russell`

## 1. Purpose & Scope

`geometor/bertrand-russell` (`geometor.bertrand_russell`) is the authoritative **GEOMETOR** primary-source archive, multi-track Book Codex (`:layout: book`), analytical SVG diagram engine, and cross-corpus concordance for the foundational geometric treatises of **Bertrand Russell (1872–1970)**:

1. **Codex I — *The Principles of Mathematics* (1903, 1st ed., Cambridge University Press)**:
   - Verbatim 1903 Preface (pp. v–ix), Part I Chapter I (*Definition of Pure Mathematics*, §§ 1–10, pp. 3–9), and Part VI (*Space*, Chapters XLIV–LII, §§ 351–436, pp. 371–461) — **96 numbered sections** across 11 3-track chapter units (`-en.rst`, `-summary.rst`, `-notes.rst`).
   - Preserves exact page-break anchors (`.. _pom-p404:` through `.. _pom-p407:`, etc.) and section anchors (`.. _pom-1:` .. `.. _pom-436:`), including the locus classicus in **Chapter XLVII (§§ 389–391, pp. 404–407)** on Euclid `I.1` circle intersection, `I.4` superposition, the mercury thermometer paradox, and the three-part congruence postulate.
   - **Public-Domain Constraint**: Strictly excludes Russell's 1937 George Allen & Unwin second-edition introduction.
2. **Codex II — *An Essay on the Foundations of Geometry* (1897, 1st ed., Cambridge University Press)**:
   - Unabridged treatise (Preface, Introduction, Chapters I–IV, **§§ 1–209**, pp. 1–201) with all **171 author's footnotes** and **9 analytical vector SVG diagrams** across 7 3-track chapter units (`-en.rst`, `-summary.rst`, `-notes.rst`).

> **Strict Authorial Isolation**: Never confuse **Bertrand Russell (1872–1970)** (`geometor/bertrand-russell`) with Walter Russell (`walter-russell`).

---

## 2. Key Python Modules (`src/geometor/bertrand_russell/`)

- `concordance.py`: Dataclasses (`SourceRecord`, `RussellLocus`, `ExternalTarget`, `ConcordanceEntry`), SHA-256 primary-source integrity verifier (`verify_source_checksums()`), cross-corpus concordance search/lookup helpers (`find_entries_by_section()`, `find_entries_by_corpus()`), and JSON registry loaders.
- `diagrams.py`: Pure-Python exact analytical SVG generator (`generate_all_diagrams()`) producing all 9 geometric figures from the 1897 *Essay* (`docsrc/_static/diagrams/efg-fig-01-p021.svg` .. `efg-fig-09-p145.svg`), including spherical antipodal poles, Beltrami's pseudospherical mapping, Helmholtz's non-rigid linear transformation, von Staudt's complete quadrilateral construction of the harmonic fourth, and Footnote 144's planar Desargues failure configuration.
- `commentary.py`: Structured scholarly apparatus (`POM_APPARATUS` and `EFG_APPARATUS`) supplying executive summaries, ASCII/Mermaid argumentative flowcharts, key theses, and cross-corpus critical notes for all 18 chapter units.
- `compile_codex.py`: Deterministic compiler (`compile_all()`, CLI `geometor-bertrand-russell`) transforming the archived HTML sources and JSON registries into 60 Book Codex RST documents and 9 SVG figures without mutating primary prose.

---

## 3. Editorial & Technical Invariants

1. **Verbatim Primary Tracks (`*-en.rst`)**:
   - Historical prose in `<stem>-en.rst` must remain 100% verbatim to the 1897 and 1903 Cambridge University Press first editions.
   - Never embed modern Python code blocks (`.. code-block:: python`) inside historical `-en.rst` treatise tracks; modern formalizations, diagrams of argument structure, and commentary belong strictly in `-summary.rst`, `-notes.rst`, `concordance.rst`, and `about/*.rst`.
2. **Sphinx & `photon-platform/publish` Conventions**:
   - `global_conf.py` enforces fixed RST heading underline levels: `=` (H1), `-` (H2), `~` (H3), `^` (H4). Never skip a heading level.
   - Top-level `docsrc/{bibliography,persons,glossary}.rst` paired with `resources/{citations,persons,glossary}.json` power `:cite:`, `:person:`, and `:term:` hover-card links across both Book Codices.
3. **Verification Gate**:
   - Every change must pass `ruff check src tests`, `pytest`, and `publish build` with zero warnings and zero errors.
