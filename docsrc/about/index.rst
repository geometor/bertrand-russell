:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor.bertrand_russell`` establishes a verified, public-domain digital critical edition of **Bertrand Russell's** two foundational Cambridge treatises on geometry: *An Essay on the Foundations of Geometry* (1897) and *The Principles of Mathematics* (1903, First Edition: Preface, Part I Ch. I, and Part VI *Space*). Reconstructed from primary Cambridge University Press impressions, this edition recovers the historical progression of Russell's spatial thought from his neo-Kantian fellowship dissertation to the relational logic of the logicist thesis.

The edition reconstructs the complete unabridged 1897 dissertation—including all 209 numbered sections, 171 author's footnotes, and 9 calibrated vector figures—alongside all 96 numbered sections of the 1903 spatial foundations (Chapters XLIV–LII, §§ 351–436). It provides a complete, machine-addressable semantic representation of Russell's famous critique of Euclid in Chapter XLVII (§§ 389–391), including the circle-intersection dilemma in Proposition I.1, the illegitimacy of triangle superposition in Proposition I.4, and the formalization of projective, descriptive, and metrical geometry via the relational logic of Peano, Cantor, and Pieri.

Within the **GEOMETOR** canon, Russell's treatises serve as the primary logicist and metageometrical interlocutor for three sister projects:

1. **Epistemology of Geometry (`geometor/hoenen`)**: Supplying the exact 1903 text and surrounding relational continuum chapters answered point-by-point by :person:`Fr. Petrus Hoenen, S.J. <hoenen>` in *De Noetica Geometriae* (1954), Caput III–V.
2. **Classical Euclidean Foundations (`geometor/euclid` & `geometor/elements`)**: Providing the structural context for :person:`Sir Thomas L. Heath <heath>`'s engagement with Russell's critique of circle intersection in ``I.1``, triangle :term:`superposition <superposition>` in ``I.4``, and implicit order axioms.
3. **Synthetic Projective Geometry (`geometor/pappus`)**: Tracing the modern axiomatization of :person:`Pappus of Alexandria <pappus>`'s cross-ratio invariance and :person:`Karl Georg Christian von Staudt <staudt>`'s :term:`quadrilateral construction <quadrilateral-construction>` from Russell's 1897 circularity critique to his 1903 :person:`Pieri <pieri>`-inspired deductive synthesis.

The GEOMETOR Mission
--------------------

The **GEOMETOR** initiative, founded by **phi ARCHITECT**, is dedicated to a three-fold synthesis of classical geometry, exact symbolic computation, and modern knowledge architecture:

* **Extracting Historical Semantic Knowledge**: Moving beyond passive page scans and static OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises. We elevate running prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs where every enunciation, proof step, and historical cross-reference is individually referenceable.
* **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (via ``SymPy``) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic number fields rather than lossy floating-point approximations. Every geometric theorem is treated as an exact algebraic truth verifiable through computational modeling.
* **Repurposing Knowledge Across Mediums**: Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (via ``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

This critical edition derives from original nineteenth- and early-twentieth-century primary print impressions:

* **Foundations of Geometry (1897)**: Bertrand Russell, *An Essay on the Foundations of Geometry*. Cambridge: At the University Press, 1897. Collation verified against the original Cambridge print copy and high-resolution scans.
* **Principles of Mathematics (1903)**: Bertrand Russell, *The Principles of Mathematics*, Vol. I. Cambridge: At the University Press, 1903. This edition strictly reproduces the first edition text of 1903, deliberately omitting the copyrighted 1937 second-edition introduction.

The texts have been collated, proofread, and encoded into semantic reStructuredText following the GEOMETOR Digital Scriptorium methodology, with full citation integration, cross-corpus concordance, and analytical vector figures.

Contextual and Biographical Essays:

* :ref:`Bertrand Russell (1872–1970): From Trinity Fellowship to Logicism <about-bertrand-russell>`
* :ref:`Philosophical Turn (1897 → 1903): Form of Externality vs. Logic of Relations <about-evolution-1897-1903>`
* :ref:`The Russell–Hoenen–Heath Dialogue on Euclid, Motion, and Spatial Intuition <about-hoenen-dialogue>`

.. toctree::
   :maxdepth: 1
   :hidden:

   bertrand-russell
   evolution-1897-1903
   hoenen-dialogue
