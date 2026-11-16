# GEOMETOR • bertrand-russell

**Foundational Treatises on Geometry by Bertrand Russell (1872–1970)** — Dual Multi-Track Book Codex, Analytical SVG Reconstructions, and Cross-Corpus Philosophical Concordance for the **GEOMETOR** Initiative.

> **Note**: This repository (`geometor/bertrand-russell`, Python package `geometor.bertrand_russell`) studies the mathematical and philosophical works of **Bertrand Russell (1872–1970)** cited in `geometor/hoenen` (*De Noetica Geometriae*, 1954) and Sir Thomas L. Heath's `geometor/euclid` (*The Thirteen Books of Euclid's Elements*, 1908). It is completely distinct from Walter Russell (`walter-russell`).

---

## Primary Codices

### 1. *The Principles of Mathematics* (1903, 1st Edition — Cambridge University Press)

Located in `docsrc/principles_of_mathematics/`, strictly faithful to the **public-domain 1903 first edition** (omitting the copyrighted 1937 second-edition introduction). Structured across **11 canonical chapter containers** (`preface`, `ch_01`, `ch_44`..`ch_52`) with visual `.. collection::` galleries, synchronized companion track pills (`English` · `Summary` · `Notes`), and atomic section pages covering **all 96 numbered sections** and **all 103 authorial footnotes**:

| Chapter | Canonical ID | Title & Topic | Sections | Pages |
| :--- | :--- | :--- | :--- | :--- |
| `preface` | Preface | Preface (dated December 1902) | — | pp. v–ix |
| `ch_01` | Ch. I | Part I, Ch. I — *Definition of Pure Mathematics* | §§ 1–10 | pp. 3–9 |
| `ch_44` | Ch. XLIV | Part VI (*Space*), Ch. XLIV — *Dimensions and Complex Numbers* | §§ 351–360 | pp. 371–380 |
| `ch_45` | Ch. XLV | Ch. XLV — *Projective Geometry* | §§ 361–373 | pp. 381–392 |
| `ch_46` | Ch. XLVI | Ch. XLVI — *Descriptive Geometry* | §§ 374–387 | pp. 393–403 |
| `ch_47` | Ch. XLVII | Ch. XLVII — *Metrical Geometry* (Euclid `I.1` & `I.4` critique, §§ 388–391, 392–399, 400–404) | §§ 388–404 | pp. 404–418 |
| `ch_48` | Ch. XLVIII | Ch. XLVIII — *Relation of Metrical to Projective and Descriptive Geometry* | §§ 405–411 | pp. 419–428 |
| `ch_49` | Ch. XLIX | Ch. XLIX — *Definitions of Various Spaces* | §§ 412–415 | pp. 429–436 |
| `ch_50` | Ch. L | Ch. L — *The Continuity of Space* | §§ 416–422 | pp. 437–444 |
| `ch_51` | Ch. LI | Ch. LI — *Logical Arguments Against Points* | §§ 423–431 | pp. 445–453 |
| `ch_52` | Ch. LII | Ch. LII — *Kant's Theory of Space* | §§ 432–436 | pp. 454–461 |

### 2. *An Essay on the Foundations of Geometry* (1897 — Cambridge University Press)

Located in `docsrc/foundations_of_geometry/` (from Project Gutenberg `#52091`), presenting the **complete, unabridged 1897 treatise** across **6 canonical chapter containers** (`preface`, `introduction`, `ch_01`, `ch_02`, `ch_03`, `ch_04`), with visual `.. collection::` galleries, 27 atomic section pages with companion tracks (`English` · `Summary` · `Notes`) covering **all 209 numbered sections (`§§ 1–209`)**, all **171 author's footnotes**, and **9 analytical SVG vector diagrams** (`efg-fig-01-p021.svg` through `efg-fig-09-p145.svg`):

| Chapter | Canonical ID | Title & Topic | Sections | Pages | Figures |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `preface` | Preface | Dedication (to J. McT. E. McTaggart) & Preface | — | pp. v–ix | — |
| `introduction` | Intro | Introduction — *Our Problem Defined* | §§ 1–9 | pp. 1–6 | — |
| `ch_01` | Cap. I | Ch. I — *A Short History of Metageometry* | §§ 10–50 | pp. 7–53 | Figs. 1–2 |
| `ch_02` | Cap. II | Ch. II — *Critical Account of Previous Philosophical Theories* | §§ 51–101 | pp. 54–116 | Figs. 3–5 |
| `ch_03` | Cap. III | Ch. III — *The Axioms of Geometry* (Sec. A: Projective, Sec. B: Metrical) | §§ 102–179 | pp. 117–177 | Figs. 6–9 |
| `ch_04` | Cap. IV | Ch. IV — *Philosophical Consequences* | §§ 180–209 | pp. 178–201 | — |

---

## Cross-Corpus Apparatus

- **`docsrc/concordance.rst`** (`resources/bertrand_russell/concordance.json`): 10 bidirectional analytical loci linking Russell (1897 & 1903) to:
  - **Petrus Hoenen, S.J.**, *De Noetica Geometriae* (1954) (`geometor/hoenen`): Caput III §2.6.B (continuum & points), Caput IV §§2–3 nn. 3–5, 8–10 (Euclid `I.4` superposition, rigid bodies, thermometer paradox, congruence postulate), Caput IV §4 n. 16 (direction & angle), Caput IV §7 n. 28 (Euclid `I.1` circle intersection), and Caput V §§3–4 (formal implication vs. intuitive abstraction).
  - **Sir Thomas L. Heath**, *The Thirteen Books of Euclid's Elements* (1908) (`geometor/euclid`): Vol. I commentary on Common Notion 4 (pp. 225–227), Prop. `I.1` (pp. 242–243), and Prop. `I.4` (p. 249).
  - **Pappus of Alexandria**, *Collection* Book VII Props. 129–145 (`geometor/pappus`): Cross-ratio invariance, Desargues configuration, and von Staudt's complete quadrilateral construction of the harmonic fourth.
- **Interactive Hover Apparatus**: `resources/{citations,persons,glossary}.json` compiled into `docsrc/{bibliography,persons,glossary}.rst` for `photon-platform/publish` `:cite:`, `:person:`, and `:term:` roles.

---

## Repository Structure & Commands

```text
bertrand-russell/
├── pyproject.toml                     # Package metadata (geometor-bertrand-russell, Python >=3.13)
├── resources/
│   ├── citations.json                 # 24 bibliographic entries (:cite:)
│   ├── persons.json                   # 38 prosopographical entries (:person:)
│   ├── glossary.json                  # 25 technical terms (:term:)
│   └── bertrand_russell/
│       ├── sources/                   # SHA-256 verified verbatim 1897 & 1903 primary archives
│       ├── sources_manifest.json
│       └── concordance.json           # 10 cross-corpus concordance entries
├── src/geometor/bertrand_russell/
│   ├── __init__.py
│   ├── concordance.py                 # Manifest checksum verifier & concordance query API
│   ├── diagrams.py                    # Exact SVG generator for all 9 1897 geometric figures
│   ├── commentary.py                  # Structured summaries & critical notes for all 18 chapter units
│   └── compile_codex.py               # Deterministic HTML-to-RST Book Codex compiler CLI
├── docsrc/                            # Sphinx Book Codex source (built via photon-platform/publish)
└── tests/
    └── test_codex.py                  # Source checksum, section completeness, verbatim, SVG & role tests
```

### Regenerate Codices, Run Tests, and Build Docs

```bash
# Recompile all 60 codex & apparatus RST files and 9 SVG figures from archived sources
PYTHONPATH=src python3 -m geometor.bertrand_russell.compile_codex

# Lint and run verification suite
ruff check src tests
pytest

# Build HTML Book Codex into docs/
publish build
```
