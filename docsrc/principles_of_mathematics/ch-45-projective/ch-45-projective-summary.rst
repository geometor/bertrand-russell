:layout: book

.. _pom-ch-45-projective-summary:

Summary — Chapter XLV: Projective Geometry (§§ 361–373)
=======================================================

*Primary Text:* :ref:`Read Verbatim Treatise Track (pp. 381–392) <pom-ch-45-projective-en>` · *Commentary:* :ref:`Critical Notes <pom-ch-45-projective-notes>`

Executive Summary
-----------------

Chapter XLV (*Projective Geometry*, §§361–373, pp. 381–392) establishes the pure qualitative architecture of projective three-space without appeal to betweenness, segments, or metrical distance. Following :person:`Karl Georg Christian von Staudt <staudt>` (:cite:`1847 <staudt:1847>`) and :person:`Mario Pieri <pieri>` (:cite:`1898 <pieri:1898>`), :person:`Russell <russell>` defines lines and planes as classes of points determined by symmetric incidence relations, constructs :term:`harmonic ranges <harmonic-range>` via the :term:`complete quadrilateral <quadrilateral-construction>` (§365), derives cyclic order via :person:`Vailati <vailati>`'s :term:`separation of couples <separation-of-couples>` and :term:`involutions <involution>` (§§366–367), assigns rational and real projective coordinates through :term:`Möbius nets <moebius-net>` (§§368–371), and culminates in :term:`projective duality <duality>` (§373).

Argumentative Architecture
--------------------------

.. code-block:: text

   flowchart TD
       A["§§361–364 Threefold Division & Pieri Incidence"] --> B["§365 Von Staudt Quadrilateral Harmonic Range"]
       B --> C["§§366–367 Involutions & Separation of Couples"]
       C --> D["§§368–371 Möbius Nets & Projective Coordinates"]
       D --> E["§§372–373 Anharmonic Ratio & Principle of Duality"]

Key Arguments & Theses
----------------------

§§361–362: Projective, Descriptive, and Metrical Geometry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Russell classifies modern foundational research into three autonomous tiers: projective (closed lines, incidence only), descriptive (open serial lines, betweenness), and metrical (quantitative congruence of stretches and angles).

§365: Von Staudt's Complete Quadrilateral Construction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given collinear points $a, b, c$, their harmonic fourth $d$ is constructed solely by joining and intersecting lines in three-space; Desargues's theorem guarantees uniqueness independent of the auxiliary plane and projection centers.

§§367–371: Projective Generation of Order and Coordinates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Harmonic separation generates Vailati's four-term cyclic order on every projective line, enabling :person:`Möbius <moebius>`'s harmonic net to map points bijectively to real coordinates and define :term:`anharmonic ratio <anharmonic-ratio>` non-metrically.
