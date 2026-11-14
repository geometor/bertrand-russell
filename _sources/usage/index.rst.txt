:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: A Guide to the Interactive Features of the Bertrand Russell Digital Critical Edition

This digital critical edition of **Bertrand Russell's** foundational treatises on geometry—*An Essay on the Foundations of Geometry* (1897) and *The Principles of Mathematics* (1903)—is built upon the **GEOMETOR** publishing platform. It unites unabridged historical texts, reconstructed vector figures, and an extensive scholarly apparatus into an interconnected research environment.

----

1. Synchronized Reading Tracks
==============================

Every chapter unit in both Book Codices is arranged across synchronized reading tracks accessible from the reader header bar:

* **English (Verbatim Source)**: The complete, authentic primary text—the unabridged 1897 Cambridge University Press first edition (Preface, Introduction, and §§ 1–209 with all 171 authorial footnotes) and the 1903 Cambridge first edition (Preface, Part I Ch. I, and Part VI *Space*, §§ 351–436).
* **Summary Track**: Analytical breakdowns providing section-by-section summaries, key deductive milestones, and philosophical lemmas.
* **Notes Track**: Scholarly commentary detailing Russell's engagements with :person:`Kant <kant>`, :person:`Riemann <riemann>`, :person:`Helmholtz <helmholtz>`, :person:`Klein <klein>`, :person:`von Staudt <staudt>`, :person:`Peano <peano>`, and :person:`Cantor <cantor>`, with explicit cross-corpus concordance to :person:`Fr. Petrus Hoenen, S.J. <hoenen>`'s Thomistic critique in :cite:`*De Noetica Geometriae* <hoenen:1954>` and :person:`Sir Thomas L. Heath <heath>`'s commentary in :cite:`*The Thirteen Books of Euclid's Elements* <euclid:elements:i-4>`.

Readers can toggle between tracks while preserving their reading position across corresponding chapters.

----

2. Primary-Source Folio Milestones
==================================

Marginal milestone markers and section headers correspond directly to primary physical witnesses and archived digital sources:

* **Numbered Sections (§§ 1–209 and §§ 351–436)**: Every section is anchored with a permanent reference target (e.g., ``.. _efg-113:`` or ``.. _pom-390:``) allowing stable deep linking across the GEOMETOR ecosystem.
* **Original Pagination**: Marginal indicators (e.g. ``[p. 405]``) mark original 1897 and 1903 Cambridge page boundaries.
* **Folio Links**: Folio milestones link directly to the verified source archives preserved under ``resources/bertrand_russell/sources/``.

----

3. Analytical Diagrams & Geometric Figures
==========================================

The 1897 *Essay* features **9 exact analytical vector SVG diagrams** newly reconstructed according to Russell's mathematical specifications:

* **Harmonic Constructions**: Analytical figures including :person:`von Staudt <staudt>`'s complete quadrilateral construction (:ref:`EFG § 113 <efg-113>`, Fig. 8, p. 125), illustrating projective invariance and harmonic separation without metrical assumptions.
* **Metageometrical Models**: Reconstructions of Beltrami's pseudosphere, Cayley-Klein projective metrics, and non-Euclidean pencils of parallels.
* **Vector Quality & Dark Mode**: Diagrams are rendered in scalable vector graphics (SVG) with high-contrast styling optimized for both Light and Dark reading modes.

----

4. Full-Text Search with Term Highlighting
==========================================

The edition features an instant, client-side search index covering both treatises and all apparatus files:

* Enter search terms into the documentation search field in the navigation bar or press ``/`` to focus.
* Results display matching sections and chapter tracks.
* Selecting a result navigates to the target passage with query terms dynamically highlighted via URL highlight parameters (``?highlight=...``).

----

5. Facets, Categories & Collection Views
========================================

The research log, thematic loci, and essays are indexed using structured metadata:

* **Log Collections**: Chronological entries in the :doc:`Log </log/index>` document archival verification, source transcription, and apparatus milestones.
* **Collection Toggles**: Collection pages support interactive view switching between **Cards**, **Banners**, and compact **List** layouts.

----

6. Interactive Tooltips & Apparatus Lookups
===========================================

Rich cross-references are integrated throughout all texts:

* **Person References (``:person:``)**: Hovering over or clicking a person link (such as :person:`Bertrand Russell <russell>`, :person:`Fr. Petrus Hoenen <hoenen>`, or :person:`Sir Thomas L. Heath <heath>`) displays their biographical summary and links to their entry in the :doc:`Biographical Register </persons>`.
* **Citation References (``:cite:``)**: Citation links resolve directly to full bibliographic data and contextual commentary in the :doc:`Systematic Bibliography </bibliography>`.
* **Term References (``:term:``)**: Technical terminology (such as :term:`free mobility <free-mobility>`, :term:`betweenness <betweenness>`, or :term:`superposition <superposition>`) links directly to definitions in the :doc:`Technical Glossary </glossary>`.
* **Concordance Links**: Deep links connect Russell's passages directly to external loci in ``geometor/hoenen``, ``geometor/euclid``, and ``geometor/pappus``.

----

7. Python API & Research Tooling
================================

The underlying Python package ``geometor.bertrand_russell`` provides a structured API for programmatic research and concordance analysis:

.. code-block:: python

   from geometor.bertrand_russell import (
       load_concordance,
       find_concordance_by_corpus,
       find_concordance_by_section,
       load_apparatus_registries,
   )

   # 1. Query concordance entries connecting Russell to Hoenen's Thomistic critique
   hoenen_loci = find_concordance_by_corpus("hoenen")
   for entry in hoenen_loci:
       print(f"[{entry.id}] {entry.theme}")
       print(f"  PoM (1903): §§ {', '.join(entry.russell_1903.sections)}")
       print(f"  EFG (1897): §§ {', '.join(entry.russell_1897.sections)}")

   # 2. Find loci discussing Euclid's superposition axiom (PoM § 390)
   sec390_entries = find_concordance_by_section("1903", 390)
   for entry in sec390_entries:
       print(f"Theme: {entry.theme}")
       for ext in entry.external_loci:
           print(f"  -> {ext.corpus}: {ext.work} ({ext.locus})")

   # 3. Access biographical and bibliographic registries
   registries = load_apparatus_registries()
   print(f"Indexed Persons: {len(registries['persons'])}")
   print(f"Indexed Citations: {len(registries['citations'])}")
   print(f"Glossary Terms: {len(registries['glossary'])}")
