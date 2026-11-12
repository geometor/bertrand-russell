:layout: book

.. _pom-ch-01-pure-math-summary:

Summary — Chapter I: Definition of Pure Mathematics (§§ 1–10)
=============================================================

*Primary Text:* :ref:`Read Verbatim Treatise Track (pp. 3–9) <pom-ch-01-pure-math-en>` · *Commentary:* :ref:`Critical Notes <pom-ch-01-pure-math-notes>`

Executive Summary
-----------------

Chapter I (*Definition of Pure Mathematics*, §§1–10, pp. 3–9) opens :cite:`*The Principles of Mathematics* <russell:1903>` with arguably the most famous sentence in twentieth-century philosophy of mathematics, defining pure mathematics as the class of all :term:`formal implications <formal-implication>` ``p implies q`` containing only unrestricted variables and :term:`logical constants <logical-constant>`. Geometry is thereby split cleanly into two distinct enterprises: *pure geometry*, which proves strictly logical implications of the form 'if $S$ is a Euclidean (or hyperbolic) space, then $S$ possesses property $P$', and *applied geometry*, an empirical branch of physics asking whether actual perceptual space instantiates $S$.

Argumentative Architecture
--------------------------

.. code-block:: text

   flowchart TD
       A["§1 Formal Implication: p(x) → q(x)"] --> B["§§3–4 Refutation of Kantian Intuition via Peano"]
       B --> C["§5 Pure vs. Applied Geometry"]
       C --> D["§§6–8 Unrestricted Variables & Relation-Types"]
       D --> E["§§9–10 Identity of Pure Mathematics and Symbolic Logic"]

Key Arguments & Theses
----------------------

§§1–4: The Logicist Thesis and Refutation of Kant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pure mathematics employs only :term:`logical constants <logical-constant>` (implication, membership, *such that*, relation, truth) and twenty logical premisses. Traditional syllogistic could not capture mathematical deduction—giving :person:`Kant <kant>` apparent grounds for invoking *a priori* intuition—but :person:`Peano <peano>`'s relational logic removes that need.

§5 & §9: Hypothetico-Deductive Status of Euclidean Geometry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The axioms of :person:`Euclid <euclid>` do not follow from logic alone; what follows from logic is the conditional implication from Euclidean axioms to Euclidean theorems. Euclidean and non-Euclidean geometries are therefore equally true in pure mathematics.

§§6–8: Unrestricted Variables and Relation-Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apparent constants such as parameters $(a, b, c)$ in $ax + by + c = 0$ or the underlying point-set itself are variables; pure plane geometry studies any class of entities bearing relations of the Euclidean plane type, such as ordered pairs of real numbers.
