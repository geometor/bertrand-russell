:layout: book

.. _pom-ch-45-projective:
.. _pom-ch-45-projective-en:

CHAPTER XLV
===========

.. rubric:: Part VI — Space — Projective Geometry (§§ 361–373, pp. 381–392)

.. contents:: Analytical Section Outline
   :local:
   :depth: 2
   :backlinks: none

.. _pom-361:

§ 361. Recent threefold scrutiny of geometrical principles
----------------------------------------------------------

.. folio:: §361
   :page: p. 381

.. _pom-p381:

**361.** The foundations of Geometry have been subjected, in recent times, to a threefold scrutiny. First came the work of the non-Euclideans, which showed that various axioms, long known to be sufficient for certain results, were also necessary, *i.e.* that results inconsistent with the usual results but consistent with each other followed from the denial of those axioms. Next came the work of Dedekind and Cantor on the nature of continuity, which showed the necessity of investigating carefully the prerequisites of analytical Geometry. Lastly, a great change has been introduced by the Italian work on closed series, mentioned in Part IV, in virtue of which we are able, given a certain type of relation between *four* points of a line, to introduce an order of all the points of a line. The work of the non-Euclideans has, by this time, produced probably almost all the modifications that it is likely to produce in the foundations, while the work of Dedekind and Cantor only becomes relevant at a fairly advanced stage of Geometry. The work on closed series, on the contrary, being very recent, has not yet been universally recognized, although, as we shall see in the present chapter, it has enormously increased the range of pure projective Geometry.

.. _pom-362:

§ 362. Projective, descriptive and metrical geometry
----------------------------------------------------

.. folio:: §362
   :page: p. 381

.. _pom-p382:

**362.** In the discussions of the present Part, I shall not divide Geometries, as a rule, into Euclidean, hyperbolic, elliptic, and so on, though I shall of course recognize this division and mention it whenever it is relevant. But this is not so fundamental a division as another, which applies, generally speaking, within each of the above kinds of Geometry, and corresponds to a greater logical difference. The above kinds differ, not in respect of the indefinables with which we start, nor yet in respect of the majority of the axioms, but only in respect of comparatively few and late axioms. The three kinds which I wish to discuss differ both in respect of the indefinables and in respect of the axioms, but unlike the three previous kinds, they are, roughly speaking, mutually compatible. That is to say, given a certain body of geometrical propositions concerning a certain number of entities, it is more or less arbitrary which of the entities we take as indefinable and which of the propositions as indemonstrable. But the logical differences which result from different selections are very great, and the systems of deductions to which different selections lead must be separately discussed.

All Geometries, as commonly developed, agree in starting with points as indefinables. That is, there is a certain class-concept *point* (which need not be the same in different Geometries), of which we assume that there are at least two, or three, or four instances, according to circumstances. Further instances, *i.e.* further points, result from special assumptions in the various cases. Where the three great types of Geometry begin to diverge is as regards the straight line. *Projective* Geometry begins with the whole straight line, *i.e.* it asserts that any two points determine a certain class of points which is also determined by any two other members of the class. If this class be regarded as determined in virtue of a relation between the two points, then this relation is symmetrical. What I shall call *Descriptive* Geometry, on the contrary, begins with an asymmetrical relation, or a line with sense, which may be called a ray; or again it may begin by regarding two points as determining the stretch of points between them. *Metrical* Geometry, finally, takes the straight line in either of the above senses, and adds either a second relation between any two points, namely distance, which is a magnitude, or else the consideration of stretches as magnitudes. Thus in regard to the relations of two points, the three kinds of Geometry take different indefinables, and have corresponding differences of axioms. Any one of the three, by a suitable choice of axioms, will lead to any required Euclidean or non-Euclidean space; but the first, as we shall see, is not capable of yielding as many propositions as result from the second or the third. In the present chapter, I am going to assume that set of axioms which gives the simplest form of projective Geometry; and I shall call any collection of entities satisfying these axioms a *projective space*. We shall see in the :ref:`next chapter <pom-ch-46-descriptive-en>` how to obtain a set of entities forming a projective space from a set forming a Euclidean or hyperbolic space; projective space itself is, so far as it goes, indistinguishable from the polar form of elliptic space. It is defined, like all mathematical entities, solely by the formal nature of the relations between its constituents, not by what those constituents are in themselves. Thus we shall see in the following chapter that the “points” of a projective space may each be an infinite class of straight lines in a non-projective space. So long as the “points” have the requisite type of mutual relations, the definition is satisfied.

.. _pom-363:

§ 363. Projective points and straight lines
-------------------------------------------

.. folio:: §363
   :page: p. 382

.. _pom-p383:

**363.** Projective Geometry assumes a class of entities, called *points*, to which it assigns certain properties [#pom_fn382_1]_; In the first place, there are to be at least two different points, *a* and *b* say. These two points are to determine a certain class of points, their straight line, which we will call *ab*. This class is determined by *b* and *a*, as well as by *a* and *b*, *i.e.* there is no order of *a* and *b* involved; moreover *a* (and therefore *b*) is itself a member of the class. Further, the class contains at least one point other than *a* and *b*; if *c* be any such point, then *b* belongs to the class *ac*, and every point of *ac* belongs to *ab*. With these assumptions it follows [#pom_fn383_1]_ that, if *c*, *d* be any points of *ab*, then *cd* and *ab* coincide—*i.e.* any two points of a line determine that line, or two lines coincide if they have two points in common.

.. _pom-p384:

Before proceeding further, let us consider for a moment what is meant by saying that two points *determine* a class of points. This expression is often thought to require no explanation, but as a matter of fact it is not a perfectly precise statement. The precise statement of what is meant is this: There is a certain definite relation (*K* say) which holds between any couple of points and one and only one corresponding class of points. Without some such definite relation, there could be no question of two points determining a class. The relation *K* may be ultimate and indefinable, in which case we need the above properties of the class *ab*. We may obtain, however, a derivative relation between two points, *b* and *c* say, namely that of being both collinear with a given point *a*. This relation will be transitive and symmetrical, but will always involve reference to a term other than those (*b* and *c*) which are its terms. This suggests, as a simplification, that instead of a relation *K* between a couple of points and a class of points, we might have a relation *R* between the two points *a* and *b*. If *R* be a symmetrical aliorelative, transitive so far as its being an aliorelative will permit (*i.e.* if *aRb* and *bRc* imply *aRc*, unless *a* and *c* are identical), the above properties of the straight line will belong to the class of terms having to *a* the relation *R* together with *a* itself. This view seems simpler than the former, and leads to the same results. Since the view that the straight line is derived from a relation of two points is the simpler, I shall in general adopt it. Any two points *a*, *b* have, then, a relation $R_{ab}$; *a*, *c* have a relation $R_{ac}$. If $R_{ab}$ and $R_{ac}$ are identical, while *b* and *c* differ, $R_{bc}$ is identical with both $R_{ab}$ and $R_{ac}$; if not, not. It is to be observed that the formal properties of any such relation *R* are those belonging to the disjunction of an asymmetrical transitive relation and its converse—*e.g.* greater or less, before or after, *etc*. These are all symmetrical aliorelatives, and are transitive so far as their being aliorelatives will permit. But not all relations of the type in question are analyzable into a transitive asymmetrical relation or its converse; for diversity, which is of the above type, is not so analyzable. Hence to assume that the straight line can be generated by an asymmetrical relation and its converse is a new assumption, characteristic of what I shall call Descriptive Geometry. For the present, such an assumption would be out of place. We have, then, two indefinables, namely *point*, and the relation *R* or *K* [#pom_fn384_1]_. No others are required in projective space.

.. _pom-364:

§ 364. Definition of the plane
------------------------------

.. folio:: §364
   :page: p. 384

**364.** The next point is the definition of the plane. It is one of the merits of projective space that, unlike other spaces, it allows a very simple and easy definition of the plane. For this purpose, we need a new axiom, namely: If *a*, *b* be two distinct points, there is at least one point not belonging to *ab*. Let this be *c*. Then the plane is the class of points lying on any line determined by *c* and any point *x* of *ab*. That is, if *x* be any point of *ab*, and *y* any point of *cx*, then *y* is a point of the plane *cab*; and if *y* be a point of the plane *cab*, then there is some point *x* in *ab* such that *y* is a point of *cx*. It is to be observed that this definition will not apply to the Euclidean or hyperbolic plane, since in these two lines may fail to intersect. The exclusion of Euclidean and hyperbolic space results from the following axiom [#pom_fn384_2]_: “If *a*, *b*, *c* be three non-collinear points, and $a'$ be a point of *bc* other than *b* and *c*, $b'$ a point of *ac* other than *a* and *c*, then there is a point common to $aa'$ and $bb'$.” By means of this axiom we can prove that the plane *cab* is the same as the plane *abc* or *bac*, and generally that, if *d*, *e*, *f* be any three non-collinear points of *abc*, the plane *def* coincides with the plane *abc*; we can also show that any two lines in a plane intersect.

.. _pom-365:

§ 365. Harmonic ranges
----------------------

.. folio:: §365
   :page: p. 384

.. _pom-p385:

**365.** We can now proceed to the harmonic range and von Staudt’s quadrilateral construction. Given three collinear points *a*, *b*, *c* take any two points *u*, *v* collinear with *c* but not on *ab*. Construct the points of intersection *au* . *bv* and *av* . *bu*; join these points, and let the line joining them meet *ab* in *d*. This construction is called the quadrilateral construction. If we now assume that outside the plane *abu* there is at least one point, we can prove that the point *d* is independent of *u* and *v*, and is uniquely determined by *a*, *b*, *c*. The point *d* is called the harmonic of *c* with respect to *a* and *b*, and the four points are said to form a harmonic range. The uniqueness [#pom_fn384_3]_ of the above construction—the proof of which, it should be observed, requires a point not in the plane of the construction [#pom_fn384_4]_—is the fundamental proposition of projective Geometry. It gives a relation which may hold between four points of a line, and which, when two are given, is one-one as regards the other two. Denoting “*c* and *d* are harmonic with respect to *a* and *b*” by *cH*\ \ $_{ab}$\ \ *d*, the following properties of the relation are important: (1) *cH*\ \ $_{ab}$\ \ *d* implies *dH*\ \ $_{ab}$\ \ *c*, *i.e.* $H_{ab}$ is symmetrical; (2) *cH*\ \ $_{ab}$\ \ *d* implies *aH*\ \ $_{cd}$\ \ *b*, *i.e.* the relation of the pairs *ab*, *cd* is symmetrical; (3) *cH*\ \ $_{ab}$\ \ *d* implies that *c* and *d* are different points, *i.e.* $H_{ab}$ is an aliorelative. This last property is independent of the others, and has to be introduced by an axiom [#pom_fn385_1]_.

Having obtained the harmonic range, we may proceed in two different directions. We may regard the harmonic relation as a relation of two pairs of points: hence, by keeping one of the pairs fixed, we obtain what is called an involution. Or we may regard the harmonic relation, as in the symbol *cH*\ \ $_{ab}$\ \ *d*, as a relation between two points, which involves a reference to two others. In this way, regarding *a*, *b*, *c*, as fixed, we obtain three new points *d*, *e*, *f* on the line *ab* by the relations *cH*\ \ $_{ab}$\ \ *d*, *aH*\ \ $_{bc}$\ \ *e*, *bH*\ \ $_{ac}$\ \ *f*. Each of these may be used, with two of the previous points, to determine a fourth point, and so on. This leads to what Möbius [#pom_fn385_2]_ calls a *net*, and forms the method by which Klein [#pom_fn385_3]_ introduces projective coordinates. This construction gives also the method of defining an harmonic ratio. These two directions in which projective Geometry may be developed must be separately pursued to begin with. I shall take the former first.

.. _pom-366:

§ 366. Involutions
------------------

.. folio:: §366
   :page: p. 385

.. _pom-p386:

**366.** By means of the harmonic relation, we define an *involution*. This consists of all pairs of points which are harmonic conjugates with respect to two fixed points [#pom_fn385_4]_. That is to say, if *a*, *b* be the two fixed points, an involution is composed of all pairs of points *x*, *y* such that *xH*\ \ $_{ab}$\ \ *y*. If four points *x*, *y*, $x'$, $y'$ be given, it may or may not happen that there exist two points *a*, *b* such that *xH*\ \ $_{ab}$\ \ *y* and $x'H_{ab}y'$. The possibility of finding such points *a*, *b* constitutes a certain relation of *x*, *y* to $x'$, $y'$. It is plain that this relation sometimes holds, for it holds when *x*, *y* are respectively identical with $x'$, $y'$. It is plain also that it sometimes does not hold; for if *x* and *y* be identical, but not $x'$ and $y'$ then the relation is impossible. Pieri [#pom_fn385_5]_ has shown how, by means of certain axioms, this relation of four terms may be used to divide the straight line into two segments with respect to any two of its points, and to generate an order of all the points on a line. (It must be borne in mind that, in projective Geometry, the points of a line do not have an order to begin with.) This projective order is obtained as follows.

.. _pom-367:

§ 367. Projective generation of order
-------------------------------------

.. folio:: §367
   :page: p. 386

**367.** Given any three different points *a*, *b*, *c* on a line, consider the class of points *x* such that *a* and *c*, *b* and *x* are each harmonic conjugates with respect to some pair of points *y*, $y'$—in other words, *a* and *c*, *b* and *x* are pairs in an involution whose double points are *y*, $y'$. Here *y*, $y'$ are supposed variable: that is, if any such points can be found, *x* is to belong to the class considered. This class contains the point *b*, but not *a* or *c*. Let us call it the segment (*abc*). Let us denote the relation of *b* to *x* (*a* and *c* being fixed) by *bQ*\ \ $_{ac}$\ \ *x*. Then $Q_{ac}$ is symmetrical, and also *bQ*\ \ $_{ac}$\ \ *x* implies *aQ*\ \ $_{bx}$\ \ *c*. We have here a relation of four points, from which, as we saw in Part IV, Chapter xxiv, an order will result if certain further axioms are fulfilled. Three such axioms are required, and are given by Pieri as follows.

**(1)** If *d* is on the line *ab*, but does not belong to the segment (*abc*), and does not coincide with *a* or with *c*, then *d* must belong to the segment (*bca*). (If *d* coincides with *c*, we know already that *d* belongs to the segment (*bca*). This case is therefore excluded from the axiom to avoid a superfluity of assumptions.) In virtue of this axiom, if *a*, *b*, *c*, *d* be distinct points on a line, we must have either *bQ*\ \ $_{ac}$\ \ *d* or *cQ*\ \ $_{ab}$\ \ *d*. It follows that we must have either *bQ*\ \ $_{ac}$\ \ *d* or *aQ*\ \ $_{bc}$\ \ *d*. Thus at least two *Q*-relations hold between any four distinct collinear points. (2) If *a*, *b*, *c* be distinct collinear points, and *d* be a point belonging to both the segments (*bca*) and (*cab*), then *d* cannot belong to the segment (*abc*). That is, of the three segments to which *d* may belong, it never belongs to more than two. From this and the previous axiom it results that, if *d* be distinct from *a*, *b* and *c*, then *d* belongs to two and only two of the three segments defined by *a*, *b* and *c*. (3) If *a*, *b*, *c* be distinct collinear points, and *d* a point, other than *b*, of the segment (*abc*), and *e* a point of the segment (*adc*), then *e* is a point of the segment (*abc*). (Here again, the condition that *d* is to be other than *b* is required only to avoid superfluity, not for the truth of the axiom.) In terms of *Q*, this axiom states that *bQ*\ \ $_{ac}$\ \ *d* and *dQ*\ \ $_{ac}$\ \ *e* imply *bQ*\ \ $_{ac}$\ \ *e*; that is, $Q_{ac}$ is transitive. We saw already that $Q_{ac}$ is symmetrical. We can now prove that, by means of this relation, all points of the line except *a* and *c* are divided into two classes, which we may call (*ac*)\ $_{1}$ and (*ac*)\ $_{2}$. Any two points in the same class have the relation $Q_{ac}$, any two in different classes have not. The division into *two* classes results from the fact that, if we do not have *bQ*\ \ $_{ac}$\ \ *d*, nor yet *dQ*\ \ $_{ac}$\ \ *e* (*b*, *d*, *e* being points other than *a* and *c*), then we do have *bQ*\ \ $_{ac}$\ \ *e*. That is to say, $Q_{ac}$ has the formal properties of sameness of sign, and divides the line into two classes, just as sameness of sign divides numbers into positive and negative.

.. _pom-p387:

The opposite of $Q_{ac}$, which I shall denote by $T_{ac}$, corresponds in like manner to difference of sign. $T_{ac}$ is not to denote the mere negation of $Q_{ac}$, but the fact of belonging to different segments. That is, *bT*\ \ $_{ac}$\ \ *d* means that *d* does not coincide with *a* or *c*, that *d* lies in the line *ac*, but not in the segment (*abc*). Then *bT*\ \ $_{ac}$\ \ *d* may be taken as meaning that *b* and *d* are separated by *a* and *c*. It is a relation which has the formal properties of separation of couples, as enumerated in Part IV, Chapter xxiv. If *a*, *b*, *c*, *d*, *e* be five distinct points in one straight line, we have the following properties of the *T*-relation. (1) *bT*\ \ $_{ac}$\ \ *d* is equivalent to *dT*\ \ $_{ac}$\ \ *b*, *aT*\ \ $_{bd}$\ \ *c*, *cT*\ \ $_{bd}$\ \ *a*, *cT*\ \ $_{db}$\ \ *a*, etc. (2) We have one and only one of the three relations *aT*\ \ $_{bc}$\ \ *d*, *aT*\ \ $_{bd}$\ \ *C*, *aT*\ \ $_{cd}$\ \ *b*. (3) *dT*\ \ $_{ac}$\ \ *b* implies *dT*\ \ $_{ac}$\ \ *e* or *eT*\ \ $_{ac}$\ \ *b* [#pom_fn387_1]_.

By comparing the above properties of *T* with those of separation of couples, it will be seen that *T* leads to a closed series (in the sense of Part IV), *i.e.* to a series in which there is a first term, but this first term is arbitrary. The definition of the generating relation of the series (which involves, as in the general case, three fixed points) is given by Pieri as follows. With regard to the natural order *abc*, *a* precedes every other point of the line; *c* precedes every point *d* not belonging to (*abc*) and not coinciding with *a* or *c*, *i.e.* every point *d* such that *dT*\ \ $_{ac}$\ \ *b*; a general point *d* precedes a general point *e* if *dQ*\ \ $_{ac}$\ \ *b* and *eQ*\ \ $_{ad}$\ \ *c*, or if *dT*\ \ $_{ac}$\ \ *b* and *eT*\ \ $_{ad}$\ \ *c*, *i.e.* if *d* belongs to the segment (*abc*) and *e* to the segment (*acd*), or if *b* and *d* are separated by *a* and *c*, and likewise *c* and *e* by *a* and *d*. It is then shown, that of any two points of the line, one precedes the other, and that the relation is transitive and asymmetrical; hence all the points of the line acquire an order.

Having now obtained an order among our points, we can introduce an axiom of continuity, to which Pieri [#pom_fn387_2]_ gives a form analogous to that of Dedekind’s axiom, namely: If any segment (*abc*) be divided into two parts *h* and *k*, such that, with regard to the order *abc*, every point of *h* precedes every point of *k*, while *h* and *k* each contain at least one point, then there must be in (*abc*) at least one point *x* such that every point of (*abc*) which precedes *x* belongs to *h*, and every point of (*abc*) which follows *x* belongs to *k*. It follows from this axiom that every infinite class contained in (*abc*) and having no last (or first) term has a limit, which is either a point of (*abc*) or *c* (or *a*); and it is easy to prove that, when *h* and *k* are given, there can be only one such point as *x* in the axiom.

.. _pom-p388:

By means of the projective segment, it is easy to define triangles and tetrahedra. Three points determine four triangles, which between them contain all the points of the plane, and have no common points except the angles. Also we can define harmonic transformations, and prove their properties without any further axiom [#pom_fn388_1]_. Only one other axiom is required to complete our Geometry, namely: A plane and a line not in the plane always have a common point. This amounts to the axiom of three dimensions. Nothing is altered, in what precedes, by denying it, and proceeding to a space of *n* dimensions or of an infinite number of dimensions. This last, in fact, requires fewer axioms than a space of three dimensions [#pom_fn388_2]_.

.. _pom-368:

§ 368. Möbius nets
------------------

.. folio:: §368
   :page: p. 388

**368.** Let us now resume the other direction in which projective Geometry may be developed, in which we start from three fixed points on a line, and examine all the points obtainable from these three by successive quadrilateral constructions. We do not here, as in the development we have been examining, require any new axiom; but there is a corresponding restriction in the results obtainable. In order to give projective Geometry its fullest possible development we must combine the results of both directions.

.. _pom-p389:

Confining ourselves, to begin with, to one straight line, let us see how to construct a net and introduce projective coordinates. Denoting by *aH*\ \ $_{bc}$\ \ *d*, as before, the proposition “*a* and *d* are harmonic conjugates with respect to *b* and *c*,” we can, by the quadrilateral construction, when *a*, *b*, *c* are given, determine the only point *d* satisfying this proposition. We next construct the point *e* for which *bH*\ \ $_{cd}$\ \ *e*, then *f* for which *dH*\ \ $_{ce}$\ \ *f*, *g* for which *eH*\ \ $_{cf}$\ \ *g*, and so on. In this way we obtain a progression of points on our line, such that any three consecutive points, together with *c*, form a harmonic range. With our former definition of a segment, all these points will belong to the segments (*abc*) and (*bca*). We may number these points, beginning with *a*, 0, 1, 2, …, *n*, …. Since *c* does not belong to the progression, we may assign to it the number ∞ [#pom_fn388_3]_. Consider next the points obtained as follows. Let $d'$ be such that $d'H_{ab}$\ \ *c*, let $e'H_{ad}$\ \ *b*, $f'H_{ac}d'$, and so on. We have thus a new progression of points, such that any three consecutive points together with *a* form a harmonic range, and all belonging to the segments (*abc*), (*cab*). To these points let us assign the numbers 1/*n* in order. Similarly we can construct a progression belonging to the two segments (*cab*), (*bca*), and assign to them the negative integers. By proceeding in a similar manner with any triad of points so obtained, we can obtain more and more points. The principle adopted in assigning numbers to points (a principle which, from our present standpoint, has no motive save convenience) is the following: if *p*, *q*, *r* be the numbers assigned to three points already constructed, and *s* be the number to be assigned to the harmonic conjugate (supposed not previously constructed) of the *q*-point with respect to the *p*-point and the *r*-point, then we are to have $\frac{p - q}{r - q} / \frac{p - s}{r - s}$ = −1. In this manner, we can find one and only one point of our line for each rational number, positive or negative [#pom_fn389_1]_. Thus we obtain a denumerable endless compact series of points on our line. Whether these are all the points of our line or not, we cannot decide without a further axiom. If our line is to be a continuous series, or a collection of the power of the continuum, we must of course assume points not obtainable by quadrilateral constructions, however often repeated, which start with three given elements. But as the definition of our space is optional, we may, if we like, content ourselves with a rational space, and introduce an axiom to the effect that all points of our line can be obtained from three given points.

.. _pom-369:

§ 369. Projective order presupposed in assigning irrational coordinates
-----------------------------------------------------------------------

.. folio:: §369
   :page: p. 389

.. _pom-p390:

**369.** Before proceeding further, it may be well to point out a logical error, which is very apt to be committed, and has been committed, I think, even by Klein [#pom_fn389_2]_. So long as Pieri’s three axioms above enumerated are not assumed, our points have no order but that which results from the net, whose construction has just been explained. Hence only rational points (*i.e.* such as, starting from three given points, have rational coordinates) can have an order at all. If there be any other points, there can be no sense in which these can be limits of series of rational points, nor any reason for assigning irrational coordinates to them. For a limit and the series which it limits must both belong to some one series; but in this case, the rational points form the whole of the series. Hence other points (if there be any) cannot be assigned as limits of series of rational points. The notion that this can be done springs merely from the habit of assuming that all the points of a line form a series, without explicitly stating this or its equivalent as an axiom. Indeed, just as we found that series of rationals properly have no limit except when they happen to have a rational limit, so series of points obtainable by the quadrilateral construction will not have limits, *quâ* terms of the series obtained from the quadrilateral construction, except where they happen to have a limit within this series, *i.e.* when their coordinates have a rational limit. At this point, therefore, it is highly desirable to introduce Pieri’s three axioms, in virtue of which *all* the points of a line have an order. We shall find that, in the natural order *cab*, the order of the rational points, resulting from Pieri’s axioms, is the same as that of their coordinates assigned on the above principle [#pom_fn390_1]_. Thus we have only to assume that all infinite series of rational points have limits, as parts of Pieri’s series, and that all points are either rational or limits of rational series, in order to show that our straight line has continuity in Cantor’s sense. In this case we shall assign to non-rational points the irrational numbers corresponding to the series which such points limit.

.. _pom-370:

§ 370. Anharmonic ratio
-----------------------

.. folio:: §370
   :page: p. 390

**370.** Returning now to the quadrilateral construction, we define as the *anharmonic ratio* of four points whose coordinates are *p*, *q*, *r*, *s* the number $\frac{p - q}{r - q} / \frac{p - s}{r - s}$. It can be shown that this number is independent of the choice of our three original points *a*, *b*, *c*. It expresses the series of quadrilateral constructions required to obtain *s* when *p*, *q*, *r* are given, and thus expresses a purely projective relation of the four points. By the introduction of irrational points, in the manner just explained, it follows that *any* four points on a line have an anharmonic ratio. (This cannot possibly be proved without Pieri’s three axioms or some equivalent to them.) The anharmonic ratio is unaltered by any linear transformation, *i.e.* by substituting for every point *x* the point whose coordinate is (*αx* + *β*)/(*γx* + *δ*), where *α*, *β*, *γ*, *δ* are any fixed numbers such that *αδ* − *βγ* is not zero. From this point we can at last advance to what was formerly the beginning of projective Geometry, namely the operation of projection, to which it owes its name.

It can be shown that, if *p*, *r* be harmonic conjugates with respect to *q*, *s*, and *p*, *q*, *r*, *s* be joined to some point *o*, and if *op*, *oq*, *or*, *os* meet any line in $p'$, $q'$, $r'$, $s'$, then $p'$, $r'$ are harmonic conjugates with respect to $q'$, $s'$. Hence we can show that all anharmonic ratios are unaltered by the above operation. Similarly if *l* be any straight line not coplanar with *pqrs*, and the planes *lp*, *lq*, *lr*, *ls* meet any line not coplanar with *l* in $p'$, $q'$, $r'$, $s'$, these four points will have the same anharmonic ratio as *p*, *q*, *r*, *s*. These facts are expressed by saying that anharmonic ratio is unaltered by projection. From this point we can proceed to the assignment of coordinates to any point in space [#pom_fn390_2]_.

.. _pom-371:

§ 371. Assignment of coordinates to any point in space
------------------------------------------------------

.. folio:: §371
   :page: p. 390

.. _pom-p391:

**371.** To begin with a plane, take three points *a*, *b*, *c* not in one straight line, and assign coordinates in the above manner to the points of *ab*, *ac*. Let *p* be any point of the plane *abc*, but not on the line *bc*. Then if *cp* meets *ab* in $p_{1}$, and *bp* meets *ac* in $p_{2}$, and *x*, *y* are the coordinates of $p_{1}$, $p_{2}$ respectively, let (*x*, *y*) be the two coordinates of *p*. In this way all points of the plane not on *bc* acquire coordinates. To avoid this restriction, let us introduce three homogeneous coordinates, as follows. Take any four points *a*, *b*, *c*, *e* in a plane, no three of which are collinear; let *ae* meet *bc* in $e_{1}$, *b*\ e meet *ca* in $e_{2}$, *ce* meet *ab* in $e_{3}$. Assign coordinates to the points of *bc*, *ca*, *ab* as before, giving the coordinate 1 to $e_{1}$, $e_{2}$, $e_{3}$, and in *ab* giving 0 to *a*, and ∞ to *b*, and similarly for the other sides. In place of the single coordinate *x* of any point of *bc*, let us introduce the homogeneous coordinates $x_{2}$, $x_{3}$, where *x* = $x_{2}$/$x_{3}$. If now *p* be any point of the plane *abc*, let *ap* meet *bc* in $p_{1}$, *bp* meet *ca* in $p_{2}$, and *cp* meet *ab* in $p_{3}$. Let $x_{2}$, $x_{3}$ be the homogeneous coordinates of $p_{1}$, $x_{3}$, $x_{1}$ those of $p_{2}$; then $x_{1}$, $x_{2}$ will be those of $p_{3}$ [#pom_fn391_1]_. Hence we may assign $x_{1}$, $x_{2}$, $x_{3}$ as homogeneous coordinates of *p*. In like manner we can assign four homogeneous coordinates to any point of space. We can also assign coordinates to the lines through a point, or the planes through a line, or all the planes of space, by means of the anharmonic ratios of lines and planes [#pom_fn391_2]_. It is easy to show that, in point-coordinates, a plane has a linear equation, and a linear equation represents a plane; and that, in plane-coordinates, a point has a linear equation, and a linear equation represents a point. Thus we secure all the advantages of analytical Geometry. From this point onwards, the subject is purely technical, and ceases to have philosophic interest.

.. _pom-372:

§ 372. Comparison of projective and Euclidean geometry
------------------------------------------------------

.. folio:: §372
   :page: p. 391

**372.** It is now time to ask ourselves what portions of the Geometry to which we are accustomed are not included in projective Geometry. In the first place, the series of points on a line, being obtained from a four-term relation, is closed in the sense of Part IV. That is, the order of points requires three fixed points to be given before it can be defined. The practical effect of this is, that given only three points on a line, no one of them is between the other two. This is a definite difference between projective space and Euclidean or hyperbolic space. But it is easy to exaggerate this difference. We saw in Part IV that, wherever a series is generated by a two-term relation, there is also the four-term relation of separation of couples, by which we can generate a closed series consisting of the same terms. Hence in this respect the difference does not amount to an inconsistency. Euclidean and hyperbolic spaces contain what projective space contains, and something more besides. We saw that the relation by which the projective straight line is defined has the formal properties of “*P* or $\breve{P}$,” where *P* is transitive and asymmetrical. If the said relation be actually of this form, we shall have an open series with respect to *P*, and of three collinear points one will be between the other two. It is to be observed that, where the straight line is taken to be essentially closed, as in elliptic space, *between* must be excluded where three points only are given. Hence elliptic space, in this respect, is not only consistent with the projective axioms, but contains nothing more than they do.

.. _pom-p392:

It is when we come to the plane that actual inconsistencies arise between projective Geometry and Euclidean or hyperbolic Geometry. In projective space, any two lines in a plane intersect; in the Euclidean and hyperbolic Geometries, this does not occur. In elliptic Geometry, any two lines in a plane intersect; but in the antipodal form they intersect twice. Thus only the polar form wholly satisfies the projective axioms. Analogous considerations apply to the intersection of two planes, or of a line and a plane. These differences render the projective definition of a plane inapplicable to Euclidean and hyperbolic spaces, and render the theory of these spaces far more complicated than that of projective space.

Finally, in metrical Geometry it is assumed either that two points have a quantitative relation called distance, which is determined when the points are given, or that stretches satisfy axioms in virtue of which their divisibilities become numerically measurable. In this point, even elliptic space differs from projective space, though the difference is of the nature of an addition, not an inconsistency. But this matter cannot be discussed until we have examined metrical Geometry, when we shall be in a position to examine also the projective theory of distance to more advantage than is at present possible.

.. _pom-373:

§ 373. The principle of duality
-------------------------------

.. folio:: §373
   :page: p. 392

**373.** A few words may be added concerning the principle of duality. This principle states, in three dimensions, that the class of planes is also a projective space, the intersection of two planes being, as before, the straight line, and the intersection of three non-collinear planes taking the place of the point. In *n* dimensions, similarly, a projective space results from all sub-classes of (*n* − 1) dimensions. Such a duality, as we saw in :ref:`Chapter xliv <pom-ch-44-dimensions-en>`, belongs always to *n*-dimensional series as such. It would seem (though this is only a conjecture) that projective Geometry employs the smallest number of axioms from which it is possible to generate a series of more than two dimensions, and that projective duality therefore flows from that of dimensions in general. Other spaces have properties additional to those required to make them *n*-dimensional series, and in other spaces, accordingly, duality is liable to various limitations.

----

.. rubric:: Author's Footnotes (1903 Edition)

.. [#pom_fn382_1] In what follows, I am mainly indebted to Pieri, *I Principii della Geometria di Posizione.* Turin, 1898. This is, in my opinion, the best work on the present subject.

.. [#pom_fn383_1] Pieri, *op. cit.* §1, prop. 25.

.. [#pom_fn384_1] We shall see in :ref:`Chap. xlix <pom-ch-49-spaces-en>` that these notions, which are here provisionally undefined, are themselves variable members of definable classes.

.. [#pom_fn384_2] Pieri, *op. cit*, §3, p. 9.

.. [#pom_fn384_3] The proof of the uniqueness of the quadrilateral construction will be found in any text-book of Projective Geometry, *e.g.* in Cremona’s (Oxford 1893), Chap. viii.

.. [#pom_fn384_4] A proof that this proposition requires three dimensions is easily derivable from a theorem given by Hilbert, *Grundlagen der Geometrie*, p. 51 (Gauss-Weber Festschrift, Leipzig, 1899).

.. [#pom_fn385_1] See Fano, *Giornale di Matimatiche*, Vol. 30; Pieri, *op. cit.* §4, p. 17 and Appendix. Fano has proved the necessity of the above axiom in the only conclusive manner, by constructing a system satisfying all the previous axioms, but not this one. The discovery of its necessity is due to him. A simpler but equivalent axiom is that our space contains at least one line on which there are more than three points.

.. [#pom_fn385_2] *Barycentrischer Calcul*, Section ii, Chap. vi.

.. [#pom_fn385_3] *Math. Annalen*, 4, 6, 7, 37; *Vorlesungen über nicht-Euklidische Geometrie*, Göttingen, 1893, Vol. i, p. 308ff.

.. [#pom_fn385_4] In what follows, only involutions with real double points are in question.

.. [#pom_fn385_5] *Op. cit.* §§5, 6, 7. Pieri’s method was presumably suggested by von Staudt. Cf. *Geometrie der Lage*, §16: especially No. 216.

.. [#pom_fn387_1] This last property affords an instance (almost the only one known to me) where Peirce’s relative addition occurs outside the Algebra of Relatives. “*dT*\ \ $_{ac}$\ \ *e* or *eT*\ \ $_{ac}$\ \ *b*” is the relative sum of $T_{ac}$ and $T_{ac}$, if *d*, *e*, and *b* be variable. This property results formally from regarding $T_{ac}$ as the negation of the transitive relation $Q_{ac}$.

.. [#pom_fn387_2] *Op. cit.* §9, p. 7.

.. [#pom_fn388_1] These developments will be found in Pieri, *loc. cit.* §§8, 10.

.. [#pom_fn388_2] Pieri, §12

.. [#pom_fn388_3] We must not assign to *c* the definite number *ω*, since we cannot assume, without further axioms, that *c* is the limit of our progression. Indeed, so long as we exclude Pieri’s three axioms above mentioned, we do not know, to begin with, that *c* has any ordinal relation to the terms of our progression.

.. [#pom_fn389_1] On this subject, see Klein, *Vorlesungen über nicht-Euklidische Geometrie*, p. 338ff., where proofs will be found.

.. [#pom_fn389_2] *e.g. Op. cit.* p. 344.

.. [#pom_fn390_1] This has the one exception that *c* came last in the order of the quadrilateral constructions, and comes first in Pieri’s order. This may be remedied by the simple device of giving *c* the coordinate −∞ instead of ∞.

.. [#pom_fn390_2] See Pasch, *Neuere Geometrie*, §22; Klein, *Math. Annalen*, 37.

.. [#pom_fn391_1] See Pasch, *loc. cit*.

.. [#pom_fn391_2] The anharmonic ratio of four lines through a point or of four planes through a line is that of the four points in which they meet any line.
