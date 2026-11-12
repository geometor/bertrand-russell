"""Scholarly analytical summaries and critical commentary notes for the 1897 and 1903 treatises."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ChapterApparatus:
    """Analytical summary and critical notes for a single Book Codex chapter unit."""

    executive_summary: str
    mermaid_flow: str
    key_arguments: tuple[tuple[str, str], ...]
    critical_notes: tuple[tuple[str, str], ...]


POM_APPARATUS: dict[str, ChapterApparatus] = {
    "preface": ChapterApparatus(
        executive_summary=(
            "In the December 1902 Preface to :cite:`*The Principles of Mathematics* <russell:1903>`, "
            ":person:`Bertrand Russell <russell>` announces his decisive break from the neo-Kantian and "
            "neo-Hegelian framework of his 1897 :cite:`*Essay on the Foundations of Geometry* <russell:1897>`. "
            "Guided by :person:`G. E. Moore <moore>`'s analytic realism, :person:`Giuseppe Peano <peano>`'s "
            "symbolic logic, :person:`Georg Cantor <cantor>`'s transfinite arithmetic, and "
            ":person:`Gottlob Frege <frege>`'s foundational works, Russell formulates the twin pillars of "
            "logicism: (1) that all pure mathematics—including Euclidean and non-Euclidean geometry—derives "
            "solely from a small set of logical constants without appeal to spatial intuition, and (2) that "
            "mathematical existence-theorems are secured constructively through the principle of abstraction."
        ),
        mermaid_flow=(
            'flowchart LR\n'
            '    A["1903 Preface"] --> B["Realism over Idealism (G. E. Moore)"]\n'
            '    A --> C["Symbolic Logic (Peano & Frege)"]\n'
            '    A --> D["Existence-Theorems via Principle of Abstraction"]\n'
            '    A --> E["Candor on Russell\'s Class Contradiction (Ch. X)"]'
        ),
        key_arguments=(
            (
                "Philosophical Realism of Propositions",
                ("Against psychologism and Kantian idealism, Russell holds that what is true or false—a "
                "*proposition*—is non-mental, objective, and composed of mind-independent terms and relations."),
            ),
            (
                "Intellectual Debt to Peano, Frege, and Whitehead",
                ("Russell credits :person:`Peano <peano>`'s symbolic notation for separating distinct logical "
                "relations previously conflated by ordinary grammar (membership vs. inclusion), acknowledges "
                "independent convergence with :person:`Frege <frege>`, and highlights ongoing collaboration "
                "with :person:`A. N. Whitehead <whitehead>` toward Volume II (realized in 1910–1913 as "
                ":cite:`*Principia Mathematica* <whitehead-russell:1910>`)."),
            ),
            (
                "Constructive Existence-Theorems",
                ("Defining cardinals, ordinals, complex numbers, and geometric ideal elements as logical classes "
                "via equivalence relations eliminates unproved postulates and guarantees non-emptiness whenever "
                "the underlying relation is instantiated."),
            ),
        ),
        critical_notes=(
            (
                "Exclusion of the 1937 Second-Edition Introduction",
                ("This codex reproduces strictly the public-domain 1903 Cambridge University Press first edition "
                "(pp. v–ix), omitting Russell's later 1937 George Allen & Unwin retrospective introduction."),
            ),
            (
                "Contrast with the 1897 Preface",
                ("Compare :ref:`1897 Preface <efg-preface-en>`, where Russell acknowledged obligations to "
                "F. H. Bradley, Sigwart, and Bosanquet; by December 1902, Bradleyan monism is replaced by "
                ":person:`Moore <moore>`'s pluralism and external relations."),
            ),
        ),
    ),
    "ch-01-pure-math": ChapterApparatus(
        executive_summary=(
            "Chapter I (*Definition of Pure Mathematics*, §§1–10, pp. 3–9) opens :cite:`*The Principles of "
            "Mathematics* <russell:1903>` with arguably the most famous sentence in twentieth-century "
            "philosophy of mathematics, defining pure mathematics as the class of all :term:`formal implications <formal-implication>` "
            "``p implies q`` containing only unrestricted variables and :term:`logical constants <logical-constant>`. "
            "Geometry is thereby split cleanly into two distinct enterprises: *pure geometry*, which proves "
            "strictly logical implications of the form 'if $S$ is a Euclidean (or hyperbolic) space, then $S$ "
            "possesses property $P$', and *applied geometry*, an empirical branch of physics asking whether "
            "actual perceptual space instantiates $S$."
        ),
        mermaid_flow=(
            'flowchart TD\n'
            '    A["§1 Formal Implication: p(x) → q(x)"] --> B["§§3–4 Refutation of Kantian Intuition via Peano"]\n'
            '    B --> C["§5 Pure vs. Applied Geometry"]\n'
            '    C --> D["§§6–8 Unrestricted Variables & Relation-Types"]\n'
            '    D --> E["§§9–10 Identity of Pure Mathematics and Symbolic Logic"]'
        ),
        key_arguments=(
            (
                "§§1–4: The Logicist Thesis and Refutation of Kant",
                ("Pure mathematics employs only :term:`logical constants <logical-constant>` (implication, "
                "membership, *such that*, relation, truth) and twenty logical premisses. Traditional syllogistic "
                "could not capture mathematical deduction—giving :person:`Kant <kant>` apparent grounds for "
                "invoking *a priori* intuition—but :person:`Peano <peano>`'s relational logic removes that need."),
            ),
            (
                "§5 & §9: Hypothetico-Deductive Status of Euclidean Geometry",
                ("The axioms of :person:`Euclid <euclid>` do not follow from logic alone; what follows from logic "
                "is the conditional implication from Euclidean axioms to Euclidean theorems. Euclidean and "
                "non-Euclidean geometries are therefore equally true in pure mathematics."),
            ),
            (
                "§§6–8: Unrestricted Variables and Relation-Types",
                ("Apparent constants such as parameters $(a, b, c)$ in $ax + by + c = 0$ or the underlying point-set "
                "itself are variables; pure plane geometry studies any class of entities bearing relations of "
                "the Euclidean plane type, such as ordered pairs of real numbers."),
            ),
        ),
        critical_notes=(
            (
                "Dialogue with Hoenen (Caput V: On Axiomatics)",
                ("In :cite:`*De Noetica Geometriae* <hoenen:1954>` (Caput V, §3.2.A n. 8 & §4.2.B), "
                ":person:`Fr. Peter Hoenen, S.J. <hoenen>` confronts Russell's §4 claim directly. Citing "
                ":person:`G. H. Hardy <hardy>` (:cite:`*Mind* 1929 <hardy:1929>`) and dissecting "
                ":cite:`*Principia Mathematica* <whitehead-russell:1910>` ``*2.01``, Hoenen argues that "
                "substituting tokens into a :term:`propositional function <propositional-function>` already "
                "presupposes spatial intuition of linear symbol order and equiformity."),
            ),
            (
                "Leibniz's Anticipation (§5)",
                ("Russell notes that :person:`Leibniz <leibniz>` sought to prove Euclidean axioms logically, "
                "failing only because he lacked asymmetric relational logic and assumed Euclidean space "
                "categorically necessary."),
            ),
        ),
    ),
    "ch-44-dimensions": ChapterApparatus(
        executive_summary=(
            "Opening Part VI (*Space*), Chapter XLIV (*Dimensions and Complex Numbers*, §§351–360, pp. 371–380) "
            "recasts the concept of spatial dimension into pure relation-arithmetic. Reviewing the rise of "
            "non-Euclidean geometry (§353), :person:`Russell <russell>` defines geometry as the theory of "
            "multiple series of two or more dimensions (§352) and demonstrates against :person:`Cantor <cantor>`'s "
            "bijection paradox ($2^{\\alpha_0}$) that dimensionality belongs not to the cardinal point-set, "
            "but to the nested hierarchy of generating serial relations (§§354–356). Sections 357–360 apply "
            "this definition to universal algebra and $n$-tuple complex numbers, proving Stolz's theorem that "
            "ordinary two-term complex numbers ($x + iy$) are the maximal extension preserving the field laws."
        ),
        mermaid_flow=(
            'flowchart LR\n'
            '    A["§§351–353 Non-Euclidean Revolution"] --> B["§§354–356 Logical Definition of n Dimensions"]\n'
            '    B --> C["Cantor Cardinality vs. Relational Dimension"]\n'
            '    C --> D["§§357–360 Universal Algebra & Complex Numbers"]'
        ),
        key_arguments=(
            (
                "§§351–353: Retrospect on Non-Euclidean Geometry",
                ("Summarizing :person:`Gauss <gauss>`, :person:`Lobachevsky <lobatchewsky>`, :person:`Bolyai <bolyai>`, "
                ":person:`Riemann <riemann>`, :person:`Beltrami <beltrami>`, and :person:`Cayley <cayley>`–:person:`Klein <klein>`, "
                "Russell shows how metageometry forced the separation of pure relational geometry from physical space."),
            ),
            (
                "§§354–356: Purely Logical Definition of $n$ Dimensions",
                ("An $n$-dimensional series is defined inductively through $n$ transitive asymmetrical relations "
                "mapping terms through nested classes of series, resolving Cantor's discovery that a line and "
                "a plane have the same cardinal number of points."),
            ),
            (
                "§§357–360: Complex Numbers as Ordered Couples of Reals",
                ("Drawing on :person:`Whitehead <whitehead>`'s :cite:`*Universal Algebra* <whitehead:1898>`, "
                "Russell rejects formalist 'uninterpretable symbols' and defines complex numbers explicitly as "
                "one-dimensional series of real-number couples."),
            ),
        ),
        critical_notes=(
            (
                "Contrast with 1897 EFG §§18–19 & §94",
                ("In :ref:`1897 Ch. II §94 <efg-94>`, Russell used orders of infinity ($\\infty^2$) informally "
                "against :person:`Lotze <lotze>`; by 1903 (§355), having mastered :person:`Cantor <cantor>`'s "
                "proof that $(2^{\\alpha_0})^2 = 2^{\\alpha_0}$, he relocates dimensionality strictly in the "
                "ordinal structure of generating relations."),
            ),
        ),
    ),
    "ch-45-projective": ChapterApparatus(
        executive_summary=(
            "Chapter XLV (*Projective Geometry*, §§361–373, pp. 381–392) establishes the pure qualitative "
            "architecture of projective three-space without appeal to betweenness, segments, or metrical "
            "distance. Following :person:`Karl Georg Christian von Staudt <staudt>` (:cite:`1847 <staudt:1847>`) "
            "and :person:`Mario Pieri <pieri>` (:cite:`1898 <pieri:1898>`), :person:`Russell <russell>` defines "
            "lines and planes as classes of points determined by symmetric incidence relations, constructs "
            ":term:`harmonic ranges <harmonic-range>` via the :term:`complete quadrilateral <quadrilateral-construction>` (§365), "
            "derives cyclic order via :person:`Vailati <vailati>`'s :term:`separation of couples <separation-of-couples>` "
            "and :term:`involutions <involution>` (§§366–367), assigns rational and real projective coordinates "
            "through :term:`Möbius nets <moebius-net>` (§§368–371), and culminates in :term:`projective duality <duality>` (§373)."
        ),
        mermaid_flow=(
            'flowchart TD\n'
            '    A["§§361–364 Threefold Division & Pieri Incidence"] --> B["§365 Von Staudt Quadrilateral Harmonic Range"]\n'
            '    B --> C["§§366–367 Involutions & Separation of Couples"]\n'
            '    C --> D["§§368–371 Möbius Nets & Projective Coordinates"]\n'
            '    D --> E["§§372–373 Anharmonic Ratio & Principle of Duality"]'
        ),
        key_arguments=(
            (
                "§§361–362: Projective, Descriptive, and Metrical Geometry",
                ("Russell classifies modern foundational research into three autonomous tiers: projective "
                "(closed lines, incidence only), descriptive (open serial lines, betweenness), and metrical "
                "(quantitative congruence of stretches and angles)."),
            ),
            (
                "§365: Von Staudt's Complete Quadrilateral Construction",
                ("Given collinear points $a, b, c$, their harmonic fourth $d$ is constructed solely by joining "
                "and intersecting lines in three-space; Desargues's theorem guarantees uniqueness independent "
                "of the auxiliary plane and projection centers."),
            ),
            (
                "§§367–371: Projective Generation of Order and Coordinates",
                ("Harmonic separation generates Vailati's four-term cyclic order on every projective line, "
                "enabling :person:`Möbius <moebius>`'s harmonic net to map points bijectively to real coordinates "
                "and define :term:`anharmonic ratio <anharmonic-ratio>` non-metrically."),
            ),
        ),
        critical_notes=(
            (
                "Cross-Link to GEOMETOR Pappus Corpus",
                ("Russell's §§365–373 provide the modern logicist culmination of the projective tradition "
                "originating in :person:`Pappus of Alexandria <pappus>` (:cite:`*Collection* Book VII <pappus:collection:vii>`, "
                "modeled in ``geometor/pappus``), where cross-ratio invariance and the four-line harmonic fourth "
                "were first proved metrically before :person:`von Staudt <staudt>` purified them of length."),
            ),
            (
                "Refinement of 1897 EFG §§111–121",
                ("In :ref:`1897 Ch. III Sec. A <efg-113>`, Russell had not yet discovered :person:`Pieri <pieri>`'s "
                "1898 proof deriving cyclic order purely from harmonic conjugates without assuming open segments."),
            ),
        ),
    ),
    "ch-46-descriptive": ChapterApparatus(
        executive_summary=(
            "Chapter XLVI (*Descriptive Geometry*, §§374–387, pp. 393–403) examines spaces in which two points "
            "determine an *open* serial line rather than a closed projective circuit—the common ordinal "
            "substrate of Euclidean and hyperbolic geometry prior to congruence. Synthesizing "
            ":person:`Moritz Pasch <pasch>` (:cite:`1882 <pasch:1882>`) and :person:`Giuseppe Peano <peano>` "
            "(:cite:`1889/1894 <peano:1889>`), :person:`Russell <russell>` axiomatizes :term:`betweenness <betweenness>`, "
            "proves planar intersection properties via Pasch's transversal axiom (§380), and demonstrates how "
            "adjoining :term:`ideal points, lines, and planes <ideal-elements>` defined as logical classes "
            "(sheaves of lines) embeds every descriptive three-space into a projective space (§§383–387)."
        ),
        mermaid_flow=(
            'flowchart LR\n'
            '    A["§§374–378 Pasch–Peano Betweenness & Serial Rays"] --> B["§§379–382 Segments, Pasch Planar Axiom & Solid Space"]\n'
            '    B --> C["§§383–386 Ideal Points, Lines & Planes as Logical Sheaves"]\n'
            '    C --> D["§387 Equivalence with Punctured Projective Space"]'
        ),
        key_arguments=(
            (
                "§§375–378: Pasch–Peano Betweenness vs. Serial Relations",
                ("Lines may be generated either from Peano's primitive open segment $ab$ ($c \\in ab$) or from "
                "a class $K$ of transitive asymmetrical ray-relations $R$ with converse $\\breve{R}$."),
            ),
            (
                "§380: Pasch's Axiom and the Descriptive Plane",
                ("A plane cannot be defined merely as lines joining $A$ to points of $BC$, because parallels "
                "or hyperbolic ultra-parallels leave gaps; Pasch's triangle-transversal postulates close the plane."),
            ),
            (
                "§§383–387: Logical Construction of Ideal Elements",
                ("Instead of feigning non-existent 'points at infinity', Pasch and Russell define an *ideal point* "
                "as the class (sheaf) of coplanar ray-pairs satisfying three-plane concurrence—securing the "
                "existence-theorem purely logically."),
            ),
        ),
        critical_notes=(
            (
                "Relation to Hilbert's Axiom Group II (1899)",
                ("Russell compares :person:`Peano <peano>`'s axioms with :person:`David Hilbert <hilbert>`'s "
                ":cite:`*Grundlagen der Geometrie* <hilbert:1899>` Group II (*Axiome der Anordnung*), noting "
                "that Peano's symbolic rigor anticipated Hilbert's planar separation postulates by a decade."),
            ),
        ),
    ),
    "ch-47-metrical": ChapterApparatus(
        executive_summary=(
            "Chapter XLVII (*Metrical Geometry*, §§388–404, pp. 404–418) is the celebrated locus classicus "
            "cited by both :person:`Fr. Peter Hoenen, S.J. <hoenen>` (:cite:`*De Noetica Geometriae*, Caput IV <hoenen:1954>`) "
            "and :person:`Sir Thomas L. Heath <heath>` (:cite:`*Euclid* Vol. I, pp. 227, 249 <euclid:elements:i-4>`). "
            "In **§§389–391 (pp. 404–407)**, :person:`Russell <russell>` delivers his incisive critique of "
            ":person:`Euclid <euclid>`'s tacit appeals to spatial intuition in Prop. ``I.1`` (two-circle intersection) "
            "and of the method of :term:`superposition <superposition>` in Prop. ``I.4`` ('strikes every intelligent "
            "child as a juggle'), exposing the logical circularity of defining spatial congruence through rigid "
            "material bodies (the thermometer by the window and fire) and formulating the exact three-step "
            "congruence postulate required to replace motion. Sections 392–404 then build metrical geometry "
            "rigorously from :term:`stretches <stretch>`, :term:`magnitude of divisibility <magnitude-of-divisibility>`, "
            "and angles defined as stretches of rays."
        ),
        mermaid_flow=(
            'flowchart TD\n'
            '    A["§389 (pp. 404–405): Critique of Euclid I.1 Circle Intersection"] --> B["§390 (pp. 405–406): Refutation of Superposition & Rigid Bodies (Euclid I.4)"]\n'
            '    B --> C["§391 (pp. 406–407): Axiomatic Reconstruction of I.4, I.8, I.16, I.26"]\n'
            '    C --> D["§§392–399: Distance vs. Stretch & Magnitude of Divisibility"]\n'
            '    D --> E["§§400–404: Angle as Stretch of Rays, Area, Volume & Chirality"]'
        ),
        key_arguments=(
            (
                "§389 (pp. 404–405): Critique of Euclid I.1 and Implicit Intuition",
                ("Russell shows that ``I.1`` assumes without proof that two coplanar circles whose centers lie "
                "on each other's circumference intersect, and ``I.4``, ``I.7``, ``I.16`` rely on unaxiomatized "
                "planar order (*inside/outside*) and betweenness."),
            ),
            (
                "§390 (pp. 405–406): Why Superposition Fails Logically",
                ("First, spatial points are immutable positions ('can no more change its position than the leopard "
                "can change his spots'). Second, moving material triangles requires *rigidity*, whose very "
                "definition presupposes prior spatial equality—illustrated by setting up $\\triangle ABC$ by "
                "the window and $\\triangle DEF$ by the fire, where a heated thermometer changes equally with "
                "the triangles."),
            ),
            (
                "§391 (pp. 406–407): The Congruence Postulate Replacing Superposition",
                ("Following :person:`Hilbert <hilbert>`, Russell states the exact triangle-determination and "
                "SAS congruence axioms needed to validate ``I.4``, ``I.8``, and ``I.26`` without motion, while "
                "noting that ``I.16`` fails in spherical/elliptic space unless open serial order holds."),
            ),
            (
                "§§396–402: Magnitude of Divisibility and Angle as Stretch of Rays",
                ("Distances are derived from the :term:`magnitude of divisibility <magnitude-of-divisibility>` "
                "of generating serial relations rather than point-set cardinality ($2^{\\alpha_0}$); angles "
                "must be defined as stretches of rays rather than unbounded planar sectors (§402), because in "
                "hyperbolic space a proper sub-sector could otherwise exceed the whole."),
            ),
        ),
        critical_notes=(
            (
                "Hoenen's Direct Rebuttal in De Noetica Geometriae (Caput IV, §§2–3 & §7)",
                ("This chapter is the primary Russellian text engaged in ``geometor/hoenen``:\n\n"
                "1. **Caput IV, §2, nn. 3–5 (pp. 107–111)** quotes :ref:`§390 (pp. 405–406) <pom-390>` verbatim "
                "('strikes every intelligent child as a juggle... leopard can change its spots') and replies "
                "that Russell mistakes fictitious empty receptacle-space (*spatium imaginarium*) for real "
                "extended being (*ens extensum*), of which continuous mobility and homogeneous site-individuation "
                "(:term:`materia intelligibilis <materia-intelligibilis>`) are essential *propria*.\n"
                "2. **Caput IV, §3 (pp. 111–116)** applauds Russell's thermometer refutation of Poincaré/Helmholtz "
                "physical rigidity, then converts Russell's :ref:`§391 <pom-391>` congruence postulate into an "
                "intuitive static demonstration from the homogeneity of extension.\n"
                "3. **Caput IV, §7, n. 28 (pp. 139–142)** quotes :ref:`§389 (p. 404) <pom-389>` on ``I.1`` "
                "circle intersection, arguing that while formal *scientia* must list continuity explicitly, "
                "architectonic *intellectus principiorum* legitimately grasps circle-intersection from planar "
                "continuity."),
            ),
            (
                "Heath's Commentary on Euclid Book I (C.N. 4 & Prop. 4)",
                ("In ``geometor/euclid``, :person:`Sir Thomas L. Heath <heath>` (:cite:`Vol. I, p. 227 & p. 249 <euclid:elements:i-4>`) "
                "cites :ref:`PoM p. 405 (§§389–390) <pom-p405>` and Russell's :cite:`1902 *Britannica* article <russell:1902:britannica>` "
                "when concluding that Euclid used superposition reluctantly and that modern axiomatics rightly "
                "postulates ``I.4`` with Hilbert."),
            ),
        ),
    ),
    "ch-48-relation": ChapterApparatus(
        executive_summary=(
            "Chapter XLVIII (*Relation of Metrical to Projective and Descriptive Geometry*, §§405–411, pp. 419–428) "
            "examines the :person:`Cayley <cayley>`–:person:`Klein <klein>` projective theory of distance and "
            "reverses Russell's own 1897 assessment. Whereas in 1897 Russell dismissed projective metrics as "
            "'merely technical' because true distance seemed philosophically quantitative, in 1903 he shows "
            "that on pure logicist principles *any* two relations satisfying the axioms of distance are "
            "mathematically indistinguishable: defining distance via logarithmic functions of :term:`anharmonic ratios <anharmonic-ratio>` "
            "with respect to :term:`the Absolute <the-absolute>` (§§407–409) provides a completely rigorous "
            "deduction of metrical properties inside projective or descriptive space."
        ),
        mermaid_flow=(
            'flowchart LR\n'
            '    A["§§405–406 Logical Parity of Intrinsic & Projective Distance"] --> B["§§407–408 Anharmonic Ratio & Cayley–Klein Absolute"]\n'
            '    B --> C["§409 Real vs. Imaginary Absolute (Hyperbolic, Elliptic, Euclidean)"]\n'
            '    C --> D["§§410–411 Projective Distance in Descriptive Space"]'
        ),
        key_arguments=(
            (
                "§§405–407: Why Projective Distance Is Logically Legitimate",
                ("Once pure geometry deals only with formal properties of relations, a relation constructed "
                "from projective cross-ratios that obeys every axiom of distance *is* a valid distance relation."),
            ),
            (
                "§§408–409: Classification of Spaces via the Absolute Quadric",
                ("An imaginary non-degenerate quadric yields elliptic space; the interior of a real quadric "
                "yields hyperbolic space; a degenerate imaginary conic in an ideal plane yields Euclidean space."),
            ),
        ),
        critical_notes=(
            (
                "Connection to Rational & Projective Trigonometry (Wildberger)",
                ("Russell's §407 observation that rational algebraic functions of cross-ratios characterize "
                "collinear order and quadric polarity prior to transcendental logarithms directly anticipates "
                "modern algebraic/projective metrical formulations (cf. N. J. Wildberger's *Divine Proportions* "
                "and *Universal Hyperbolic Geometry*)."),
            ),
            (
                "Explicit Self-Correction of 1897 EFG §§37 & 42",
                ("Compare :ref:`EFG §37 <efg-37>`, where Russell argued projective coordinates could convey no "
                "genuinely metrical truth; in §406–407 Russell explains why logicism dissolves that objection."),
            ),
        ),
    ),
    "ch-49-spaces": ChapterApparatus(
        executive_summary=(
            "Chapter XLIX (*Definitions of Various Spaces*, §§412–415, pp. 429–436) demonstrates the culminating "
            "power of the logicist method in geometry: instead of treating 'Points', 'Lines', and 'Axioms' as "
            "unproved primitive postulates about actual space, :person:`Russell <russell>` turns every geometry "
            "into an explicit nominal *definition* of a class of relational structures—defining **projective spaces** "
            "(§413), **Euclidean spaces** via Peano–Whitehead directed magnitudes/vectors (§414), and "
            "**Clifford's locally flat finite spaces** (§415), and proving existence-theorems for each from "
            "the arithmetic continuum of real numbers."
        ),
        mermaid_flow=(
            'flowchart TD\n'
            '    A["§412 Axioms Transformed into Class-Definitions + Arithmetic Existence Proofs"] --> B["§413 Logical Definition of Projective 3-Space"]\n'
            '    B --> C["§414 Logical Definition of Euclidean Space via Vectors"]\n'
            '    C --> D["§415 Logical Definition of Clifford\'s Finite Flat Spaces"]'
        ),
        key_arguments=(
            (
                "§412: Elimination of Geometric Axioms in Pure Mathematics",
                ("In pure geometry there are no geometric axioms—only the nominal definition of a class of spaces "
                "(e.g. 'Euclidean spaces') together with an arithmetic existence proof built from ordered "
                "triples of real numbers, demonstrating consistency once for all."),
            ),
            (
                "§414: Vectorial Definition of Euclidean Space",
                ("Euclidean $n$-space is compactly defined as the field of a group of everywhere-defined bijective "
                "directed magnitudes (vectors) forming an $n$-dimensional real inner-product space."),
            ),
            (
                "§415: Clifford's Spaces and Klein's Space-Form Problem",
                ("Examining :person:`Clifford <clifford>`'s cylindrical/flat manifolds of finite extent where "
                "angle-sum equals $\\pi$ everywhere yet straight lines close, Russell highlights the distinction "
                "between local and global topological axioms."),
            ),
        ),
        critical_notes=(
            (
                "Relative Consistency via Arithmetic Models",
                ("Russell's §412 existence proofs parallel :person:`Hilbert <hilbert>`'s analytic models in "
                ":cite:`*Grundlagen der Geometrie* <hilbert:1899>`, grounding consistency in Cantor–Dedekind "
                "real-number segments established in Part V of *PoM*."),
            ),
        ),
    ),
    "ch-50-continuity": ChapterApparatus(
        executive_summary=(
            "Chapter L (*The Continuity of Space*, §§416–422, pp. 437–444) integrates :person:`Cantor <cantor>`'s "
            "ordinal continuity (Part V) into projective and metrical geometry. :person:`Russell <russell>` "
            "formulates projective continuity via Dedekind's axiom on harmonic quadrants (§416), metrical "
            "continuity via Archimedes and Dedekind cuts (§417), notes that continuity suffices to prove "
            ":person:`Euclid <euclid>`'s circle-intersection existence theorems though Hilbert showed a weaker "
            "algebraic field suffices (§418), critiques empirical geometry (§420), and concludes against "
            "monistic tradition that continuous space is literally an infinite aggregate of points (§422)."
        ),
        mermaid_flow=(
            'flowchart LR\n'
            '    A["§§416–417 Projective & Metrical Continuity"] --> B["§§418–419 Circle Intersection & Hilbert\'s Surd Sub-Space"]\n'
            '    B --> C["§§420–421 Empirical Premisses Need Not Assume Continuity"]\n'
            '    C --> D["§422 Space as Cantor Aggregate of 2^α₀ Points"]'
        ),
        key_arguments=(
            (
                "§§418–419: Circle Postulate vs. Full Continuity",
                ("Continuity implies the intersection of lines and circles assumed tacitly in Euclid ``I.1``, "
                "yet :person:`Hilbert <hilbert>` proved that Euclidean compass-and-straightedge constructions "
                "require only a countable quadratic-surd subfield (`GEOMETOR`'s exact algebraic domain!)."),
            ),
            (
                "§420: Critique of Approximate Empirical Geometry",
                ("Anticipating Hoenen's problem of exactitude from the opposite direction, Russell remarks that "
                "sense-perception yields only finite margins of error, whereas pure geometry treats exact "
                "hypothetical spaces."),
            ),
            (
                "§422: Space as an Infinite Aggregate of Points",
                ("Rejecting the Aristotelian–Kantian dictum that points are mere limits of division, Russell "
                "insists that Cantor's set theory rehabilitates space as a literal class of $2^{\\alpha_0}$ "
                "indivisible points."),
            ),
        ),
        critical_notes=(
            (
                "Resonance with GEOMETOR's Exact Quadratic-Surd Engine & Hoenen Caput III",
                ("Section 418 directly highlights why ``geometor/model`` can represent all classical ruler-and-compass "
                "constructions in exact symbolic algebra without floating-point reals. Meanwhile, §422 is the "
                "exact Cantorian thesis challenged by :person:`Hoenen <hoenen>` in :cite:`*De Noetica Geometriae* Caput III, §2.6.B <hoenen:1954>`."),
            ),
        ),
    ),
    "ch-51-points": ChapterApparatus(
        executive_summary=(
            "Chapter LI (*Logical Arguments Against Points*, §§423–431, pp. 445–453) confronts the classical "
            "metaphysical controversy between **absolute** (substantival) and **relational** theories of space. "
            "Reversing the relational conclusion of his 1897 *Essay* (Ch. IV), :person:`Russell <russell>` "
            "dissects :person:`Lotze <lotze>`'s monadistic critique of empty space (§§424–428) and "
            ":person:`Leibniz <leibniz>`'s identity of indiscernibles (§429), arguing that relationalism covertly "
            "presupposes irreducible asymmetric spatial relations whose terms can only be absolute, unextended "
            "points differing immediately without qualitative adjectives."
        ),
        mermaid_flow=(
            'flowchart TD\n'
            '    A["§423 Absolute vs. Relative Position"] --> B["§§424–428 Refutation of Lotze\'s Four Objections to Empty Space"]\n'
            '    B --> C["§§429–430 Critique of Leibniz\'s Identity of Indiscernibles"]\n'
            '    C --> D["§431 Defense of Absolute Points of Space"]'
        ),
        key_arguments=(
            (
                "§§424–428: Dissection of Lotze's Metaphysik",
                ("Against Lotze's claim that empty points have neither 'being' nor 'validity' and dissolve into "
                "relations, Russell applies Moore's distinction between timeless *being* (subsistence of all "
                "logical entities) and spatio-temporal *existence*."),
            ),
            (
                "§§429–431: Failure of Pure Material Relationalism",
                ("Because spatial relations are complex and continuous while material particles may be sparse or "
                "absent from unoccupied positions, geometry requires points themselves—differing numerically "
                "prior to concepts—as the ultimate terms of spatial relations."),
            ),
        ),
        critical_notes=(
            (
                "Complete Reversal of 1897 EFG Chapter IV (§§196–208)",
                ("In :ref:`1897 Ch. IV <efg-198>`, Russell held that empty space is a 'bare possibility of "
                "relations' leading to the antinomy of the point unless anchored in unextended material atoms; "
                "in 1903 (§428 n.), he explicitly repudiates that Hegelian antinomy."),
            ),
        ),
    ),
    "ch-52-kant": ChapterApparatus(
        executive_summary=(
            "Concluding Part VI, Chapter LII (*Kant's Theory of Space*, §§432–436, pp. 454–461) delivers "
            ":person:`Russell <russell>`'s definitive logicist critique of :person:`Immanuel Kant <kant>`'s "
            ":cite:`*Transcendental Aesthetic* <kant:1787:krv>` and *First/Second Mathematical Antinomies*. "
            "Russell shows that Cantor's transfinite continuum dissolves Kant's antinomies (§433), that modern "
            "relational logic Deduces all pure geometry without spatial construction in intuition (§434), that "
            "incongruent counterparts (left and right hands) arise purely from three-dimensional ordinal sense "
            "(§435), and summarizes the complete reduction of pure geometry to the logic of serial relations (§436)."
        ),
        mermaid_flow=(
            'flowchart LR\n'
            '    A["§§432–433 Dissolution of Kant\'s Mathematical Antinomies via Cantor"] --> B["§434 Symbolic Deduction vs. Kantian Diagrammatic Intuition"]\n'
            '    B --> C["§435 Left & Right Hands Reduced to 3D Ordinal Sense"]\n'
            '    C --> D["§436 Grand Summary of Part VI: Space"]'
        ),
        key_arguments=(
            (
                "§§433–434: Refutation of both Transcendental Dialectic and Aesthetic",
                ("Kant's antinomies rest on confusing infinite wholes with endless temporal synthesis; and "
                ":person:`Pieri <pieri>`, :person:`Peano <peano>`, and :person:`Hilbert <hilbert>` prove that "
                "rigorous geometric proofs never inspect spatial figures, using them merely as psychological mnemonics."),
            ),
            (
                "§435: Incongruent Counterparts Without Pure Intuition",
                ("Kant's argument from right and left hands (1768/1783) needs no non-conceptual intuition, being "
                "fully captured by difference of sense among ordered triads of rays in three dimensions (cf. §404)."),
            ),
            (
                "§436: Summary of Part VI",
                ("Pure geometry studies logically defined classes of multi-dimensional series whose existence "
                "is guaranteed by real arithmetic; whether actual physical space is Euclidean, hyperbolic, or "
                "elliptic belongs wholly to empirical science."),
            ),
        ),
        critical_notes=(
            (
                "The Three-Cornered Debate: Kant, Russell, and Hoenen",
                ("Russell (§434) and :person:`Hoenen <hoenen>` (:cite:`*De Noetica Geometriae*, Caput I–II & IV <hoenen:1954>`) "
                "both reject Kant's subjective *a priori* form of sensibility, yet diverge sharply on what "
                "replaces it: Russell banishes intuition completely from pure mathematics into hypothetico-deductive "
                "logicism, whereas Hoenen rehabilitates *objective* Aristotelian-Thomistic intellective intuition "
                "abstracted from sensory phantasms (*resolutio ad sensum*) to ground the truth of first principles."),
            ),
        ),
    ),
}


EFG_APPARATUS: dict[str, ChapterApparatus] = {
    "preface": ChapterApparatus(
        executive_summary=(
            "Written at Haslemere in May 1897 and dedicated to Cambridge idealist John McTaggart Ellis McTaggart, "
            "the Preface to :cite:`*An Essay on the Foundations of Geometry* <russell:1897>` introduces "
            ":person:`Bertrand Russell <russell>`'s revised 1895 Trinity College Fellowship dissertation. "
            "Russell credits :person:`Felix Klein <klein>`'s lectures on non-Euclidean geometry for the "
            "three-period historical framework of Chapter I, F. H. Bradley, Sigwart, and Bosanquet in logic, "
            "and :person:`A. N. Whitehead <whitehead>` for awakening him to the decisive philosophical "
            "primacy of :term:`projective geometry <projective-geometry>`."
        ),
        mermaid_flow=(
            'flowchart LR\n'
            '    A["1895 Trinity Fellowship Dissertation"] --> B["Klein: Three Periods of Metageometry"]\n'
            '    A --> C["Bradley & McTaggart: Epistemological Logic"]\n'
            '    A --> D["Whitehead: Philosophical Primacy of Projective Geometry"]'
        ),
        key_arguments=(
            (
                "Synthesis of Klein's Mathematics and Post-Kantian Epistemology",
                ("Russell bridges Continental differential/projective geometry—hitherto largely ignored by "
                "British philosophers—with critical epistemology."),
            ),
            (
                "Whitehead's Catalyst",
                ("Whitehead's insight that projective geometry captures the qualitative structure common to "
                "Euclidean and non-Euclidean spaces becomes the linchpin of Chapter III, Section A."),
            ),
        ),
        critical_notes=(
            (
                "Textual Provenance",
                ("Transcribed verbatim from the 1897 Cambridge University Press first edition via Project "
                "Gutenberg ``#52091``."),
            ),
        ),
    ),
    "intro": ChapterApparatus(
        executive_summary=(
            "The Introduction (*Our Problem Defined by Its Relations to Logic, Psychology and Mathematics*, "
            "§§1–9, pp. 1–6) severs :person:`Kant <kant>`'s identification of the *a priori* with the "
            "psychologically *subjective*. :person:`Russell <russell>` defines a postulate as logically "
            "**a priori** if and only if without it experience of the science's subject-matter would be "
            "impossible (§§3–5), and outlines his central thesis (§9): :term:`projective geometry <projective-geometry>` "
            "and the general axioms of :term:`free mobility <free-mobility>`, manifold continuity, and "
            "multiple dimensions are *a priori* conditions of any :term:`form of externality <form-of-externality>`, "
            "whereas the specific Euclidean zero-curvature value and exact triad of dimensions are empirical."
        ),
        mermaid_flow=(
            'flowchart TD\n'
            '    A["§§1–4 Severing Logical A Priori from Psychological Subjectivity"] --> B["§§5–8 Hypothetical Necessity & Transcendental Ground"]\n'
            '    B --> C["§9 Program: Projective & General Metrical Axioms A Priori; Space-Constant Empirical"]'
        ),
        key_arguments=(
            (
                "§§1–5: Epistemology Freed from Empirical Psychology",
                ("Whether space perception is innate or learned belongs to psychology; epistemology asks purely "
                "logically what axioms are presupposed in the possibility of experiencing outer diversity."),
            ),
            (
                "§9: Partition of Geometric Axioms",
                ("Axioms shared by Euclidean, hyperbolic, and spherical/elliptic spaces are *a priori*; "
                "axioms distinguishing Euclid (zero space-constant and $n = 3$) are empirical."),
            ),
        ),
        critical_notes=(
            (
                "From 1897 Transcendental Apriority to 1903 Logicist Apriority",
                ("Compare :ref:`EFG §5 <efg-5>` with :ref:`PoM §10 (1903) <pom-10>`: in 1897 apriority means "
                "'presupposed in possible sensory experience of externality'; in 1903 apriority means "
                "'derivable from pure logical constants alone'."),
            ),
        ),
    ),
    "ch-01-metageometry": ChapterApparatus(
        executive_summary=(
            "Chapter I (*A Short History of Metageometry*, §§10–50, pp. 7–53) presents a masterly historical "
            "and mathematical analysis of nineteenth-century :term:`Metageometry <metageometry>` across three "
            "periods (following :person:`Klein <klein>`): **First Period** (§§12–15: :person:`Gauss <gauss>`, "
            ":person:`Lobachevsky <lobatchewsky>`, :person:`János Bolyai <bolyai>`), establishing synthetic "
            "consistency without the parallel postulate; **Second Period** (§§16–29: :person:`Riemann <riemann>`, "
            ":person:`Helmholtz <helmholtz>`, :person:`Beltrami <beltrami>`), analyzing space as a quantitative "
            ":term:`manifold <manifold>` of constant :term:`measure of curvature <measure-of-curvature>`; and "
            "**Third Period** (§§30–45: :person:`Cayley <cayley>`, :person:`Klein <klein>`, :person:`Sophus Lie <lie>`), "
            "subordinating metrical geometry to projective invariance relative to :term:`the Absolute <the-absolute>`."
        ),
        mermaid_flow=(
            'flowchart LR\n'
            '    A["First Period (§§12–15): Gauss, Lobachevsky, Bolyai"] --> B["Second Period (§§16–29): Riemann, Helmholtz, Beltrami"]\n'
            '    B --> C["Third Period (§§30–45): Cayley, Klein, Sophus Lie"]\n'
            '    C --> D["§§46–50: Three Essential Axioms Retained Across All Periods"]'
        ),
        key_arguments=(
            (
                "§§17–26: Riemann's Curvature and Helmholtz's Free Mobility",
                ("Riemann's geodesic 2-pencils (Fig. 1, p. 21) show that figures move without distortion if and "
                "only if Gaussian curvature $k$ is constant everywhere."),
            ),
            (
                "§§30–43: Cayley–Klein Projective Metrics and Imaginaries",
                ("Russell praises von Staudt's purely projective cross-ratio (§36) and Beltrami–Ball models "
                "(§§38–39), examines non-orientability of the elliptic plane (Fig. 2, p. 41), and argues in "
                "1897 that Cayley's reduction of distance and imaginary loci is technically valid but "
                "philosophically conventional (a verdict he reverses in :ref:`PoM Ch. XLVIII <pom-406>`)."),
            ),
            (
                "§45: Sophus Lie's Group-Theoretic Resolution",
                ("Lie's continuous transformation groups prove Helmholtz's separate axiom of Monodromy superfluous "
                "in three dimensions."),
            ),
        ),
        critical_notes=(
            (
                "Figures 1 & 2 Reconstructed in Vector SVG",
                ("This chapter includes exact vector reconstructions of Russell's 1897 p. 21 Riemannian geodesic "
                "bundle (``efg-fig-01-p021.svg``) and p. 41 elliptic-plane oriented circle (``efg-fig-02-p041.svg``)."),
            ),
        ),
    ),
    "ch-02-critique": ChapterApparatus(
        executive_summary=(
            "Chapter II (*Critical Account of Some Previous Philosophical Theories of Geometry*, §§51–101, "
            "pp. 54–116) subjects six major philosophers and scientist-philosophers to sustained mathematical "
            "and logical scrutiny: :person:`Kant <kant>` (§§51–58), :person:`Riemann <riemann>` (§§59–65), "
            ":person:`Helmholtz <helmholtz>` (§§66–73), :person:`Erdmann <erdmann>` (§§74–84), "
            ":person:`Lotze <lotze>` (§§85–96), and Delbœuf plus French conventionalists (§§97–101). Particularly "
            "notable are §§69–73, refuting Helmholtz's claim that pure geometry depends on physical rigid bodies, "
            "and §§90–95, exposing the mathematical fallacies in Lotze's attacks on parallels, spherical 2-space, "
            "and higher dimensions."
        ),
        mermaid_flow=(
            'flowchart TD\n'
            '    A["§§51–58 Kant: Externality A Priori, Euclid Not"] --> B["§§59–65 Riemann: Quantitative Bias"]\n'
            '    B --> C["§§66–73 Helmholtz: Rigid-Body Fallacy Refuted"]\n'
            '    C --> D["§§74–84 Erdmann & §§85–96 Lotze\'s Mathematical Errors"]\n'
            '    D --> E["§§97–101 Delbœuf, Poincaré & Summary"]'
        ),
        key_arguments=(
            (
                "§§53–58: Separating Kant's Two Lines of Argument",
                ("Metageometry refutes Kant's regressive argument from Euclidean apodeicticity, while Kant's "
                "metaphysical deduction establishes only *some* homogeneous :term:`form of externality <form-of-externality>`, "
                "not specifically Euclidean parallels."),
            ),
            (
                "§§69–73: Physics Presupposes Geometry (Against Helmholtz)",
                ("Defining congruence via physical rigid bodies is viciously circular because mechanics and "
                "rigidity cannot even be stated without prior spatial measurement—an argument echoed by "
                ":person:`Hoenen <hoenen>` against :person:`Poincaré <poincare>` in Caput IV, §3."),
            ),
            (
                "§§90–95: Point-by-Point Refutation of Lotze (Figs. 3–5)",
                ("Lotze begs the parallel question in defining parallels $a\\alpha, b\\beta$ by equidistant chords "
                "(Fig. 3, p. 99), misconstrues intrinsic spherical geodesics $NBS$ (Fig. 4, p. 101), and "
                "ignores orders of infinity ($\\infty^2$) in his perpendicularity proof of 3-space (Fig. 5, p. 106)."),
            ),
        ),
        critical_notes=(
            (
                "Anticipation of PoM §390 and Convergence with Hoenen",
                ("Russell's §§70–73 distinction between 'abstract geometrical matter' and physical rigid bodies "
                "directly anticipates :ref:`PoM §390 <pom-390>` and closely parallels—before Russell's 1903 "
                "turn against motion—:person:`Hoenen <hoenen>`'s :term:`materia intelligibilis <materia-intelligibilis>`!"),
            ),
        ),
    ),
    "ch-03a-projective": ChapterApparatus(
        executive_summary=(
            "Chapter III, Section A (*The Axioms of Projective Geometry*, §§102–140, pp. 117–147) presents "
            ":person:`Russell <russell>`'s constructive philosophical deduction of :term:`projective geometry <projective-geometry>` "
            "as wholly *a priori*. Expounding qualitative projective equivalence, :term:`anharmonic ratio <anharmonic-ratio>` "
            "(Fig. 6, p. 123), :term:`harmonic ranges <harmonic-range>` (Fig. 7, p. 124), and "
            ":person:`von Staudt <staudt>`'s :term:`quadrilateral construction <quadrilateral-construction>` "
            "(Fig. 8, p. 125; §§111–114), Russell isolates three implicit projective axioms—homogeneity/relativity "
            "of position, unique determination of lines and planes (Fig. 9, p. 145), and finite multi-dimensionality—"
            "and deduces them from the general concept of a :term:`form of externality <form-of-externality>` (§§128–139)."
        ),
        mermaid_flow=(
            'flowchart LR\n'
            '    A["§§102–110 Qualitative Equivalence & Coordinates as Names"] --> B["§§111–118 Anharmonic Ratio & Von Staudt Quadrilateral (Figs. 6–8)"]\n'
            '    B --> C["§§119–127 Principle of Duality & Three Projective Axioms"]\n'
            '    C --> D["§§128–140 Transcendental Deduction from Form of Externality (Fig. 9)"]'
        ),
        key_arguments=(
            (
                "§§111–114: Von Staudt's Purely Qualitative Harmonic Fourth",
                ("Projective cross-ratio requires no measurement of segments: harmonic conjugation is defined "
                "purely by incidence via the complete quadrilateral $ABDOPQRS T$ (Fig. 8, p. 125), whose "
                "uniqueness follows from Desargues's theorem in three-space."),
            ),
            (
                "§§128–139: Deduction from the Form of Externality",
                ("Any medium enabling experience of simultaneous diverse interrelated things must be purely "
                "relational, homogeneous, infinitely divisible, and of at least two (and finite) dimensions, "
                "entailing two-point line determination and three-point plane closure (Footnote 144, Fig. 9)."),
            ),
        ),
        critical_notes=(
            (
                "Cross-Link to Pappus & PoM Ch. XLV",
                ("Figures 6–8 (pp. 123–125) illustrate the exact projective invariants of ``geometor/pappus`` "
                "and :ref:`PoM §365 <pom-365>`. In 1903, Russell retains the mathematical exposition of "
                "§§111–127 while discarding the neo-Kantian transcendental deduction of §§128–139."),
            ),
        ),
    ),
    "ch-03b-metrical": ChapterApparatus(
        executive_summary=(
            "Chapter III, Section B (*The Axioms of Metrical Geometry*, §§141–179, pp. 147–177) transitions "
            "from pure projective quality to spatial quantity and measurement, deriving three *a priori* "
            "metrical axioms presupposed in any measurable spatial manifold: **I. The Axiom of Free Mobility** "
            "(Congruence, §§146–161), **II. The Axiom of Dimensions** (finite integral dimensionality, with "
            "$n = 3$ empirical, §§162–166), and **III. The Axiom of Distance** (unique two-point magnitude "
            "along geodesics, with local Euclidean flatness as limiting calculus condition, §§167–176)."
        ),
        mermaid_flow=(
            'flowchart TD\n'
            '    A["§§141–145 Transition from Projective Quality to Spatial Quantity"] --> B["§§146–161 I. Axiom of Free Mobility (Congruence)"]\n'
            '    B --> C["§§162–166 II. Axiom of Finite Dimensions (n=3 Empirical)"]\n'
            '    C --> D["§§167–179 III. Axiom of Distance & Geodesic Line"]'
        ),
        key_arguments=(
            (
                "§§146–154: Philosophical Deduction of Free Mobility",
                ("Spatial comparison of separated magnitudes requires motion without distortion; to hypothesize "
                "that shapes vary systematically with position (§147) is logically meaningless unless some "
                "position-independent standard existed outside space. Notice how close 1897 Russell is here to "
                "defending congruence via mobility—six years before repudiating superposition in :ref:`PoM §390 <pom-390>`!"),
            ),
            (
                "§§149–153: Enantiomorphs (Chiral Solids), Time, and Visual Estimation",
                ("Russell resolves four objections to congruence: chiral solids (right/left hands), temporal "
                "measurement, optical estimation, and curved surfaces embedded in 3-space."),
            ),
            (
                "§§167–176: Unique Two-Point Distance and Spherical Exception",
                ("Pairwise point-relations require unique distance; antipodal ambiguity in spherical space "
                "(§170–172) motivates preferring Klein's polar elliptic space or treating spherical geometry "
                "via embedded intuition."),
            ),
        ),
        critical_notes=(
            (
                "Crucial Contrast Between 1897 (§§146–154) and 1903 (PoM §§390–391)",
                ("Comparing :ref:`EFG §147 <efg-147>` with :ref:`PoM §390 <pom-390>` illuminates the entire "
                "arc of Russell's thought and :person:`Hoenen <hoenen>`'s critique: in 1897 Russell treated "
                ":term:`Free Mobility <free-mobility>` as an *a priori* condition of spatial comparison; by "
                "1903, convinced by Cantor and Weierstrass that motion reduces to static occupation of "
                "different positions at different times, he declared superposition 'a tissue of nonsense' and "
                "replaced mobility with static congruence relations."),
            ),
        ),
    ),
    "ch-04-consequences": ChapterApparatus(
        executive_summary=(
            "Chapter IV (*Philosophical Consequences*, §§180–209, pp. 178–201) completes the 1897 *Essay* "
            "in two movements: first (§§181–192), proving against monism and pure temporalism that experience "
            "of diverse interrelated things requires a multi-dimensional :term:`form of externality <form-of-externality>` "
            "given in sense-perception; and second (§§193–209), diagnosing three Hegelian **antinomies of "
            "pure space**—the **Antinomy of the Point**, the **Circle in Relational Figures**, and **Relativity "
            "vs. Homogeneity**—concluding that geometry can escape contradiction only by referring spatial "
            "relations to unextended material atoms, pointing onward to kinematics and dynamics."
        ),
        mermaid_flow=(
            'flowchart LR\n'
            '    A["§§181–192 Necessity of Multi-Dimensional Form of Externality"] --> B["§§193–199 First Antinomy: The Point & Empty Space"]\n'
            '    B --> C["§§200–205 Relational Circle & Materia Prima"]\n'
            '    C --> D["§§206–209 Unextended Atoms & Transition to Dynamics"]'
        ),
        key_arguments=(
            (
                "§§186–191: Why Time Alone Cannot Ground Diverse Things",
                ("A one-dimensional temporal series yields only successive adjectives of a single subject; "
                "simultaneous substantival diversity requires a multi-dimensional form of externality."),
            ),
            (
                "§§194–205: The Three Antinomies of Empty Relational Space",
                ("Taken in abstraction from matter, points are neither extended figures nor unextended zeroes, "
                "and spatial relations appear to be 'relations without terms'—a dialectical impasse Russell "
                "solves provisionally in 1897 by positing unextended material atoms as terms."),
            ),
        ),
        critical_notes=(
            (
                "How Cantor and Moore Dissolved Chapter IV by 1903",
                ("Chapter IV represents the high-water mark of Russell's neo-Hegelian dialectical phase (explicitly "
                "comparing empty space to Aristotle's *materia prima* in §203 and citing Hegel's *Naturphilosophie*). "
                "Within three years, Cantor's set-theoretic continuum (:ref:`PoM Ch. L <pom-422>`) and Moore's "
                "realism about absolute points (:ref:`PoM Ch. LI <pom-428>`) led Russell to repudiate all three "
                "antinomies as artifacts of faulty pre-relational logic."),
            ),
        ),
    ),
}
