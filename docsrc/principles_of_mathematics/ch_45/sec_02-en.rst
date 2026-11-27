:layout: book
:type: section
:order: 2
:canonical_id: XLV.2
:folio: §367
:page: 386
:title: Möbius Nets, Projective Order, and Duality
:tracks: English: sec_02-en | Summary: sec_02-summary | Notes: sec_02-notes

.. _pom-ch_45-sec_02-en:

.. folio:: §367
   :page: 386

Möbius Nets, Projective Order, and Duality
==========================================

.. rubric:: Projective Geometry (§§ 367–373, pp. 386–392)

.. _pom-367:

§ 367. Projective generation of order
-------------------------------------

.. folio:: §367
   :page: p. 386

**367.** Given any three different points *a*, *b*, *c* on a line, consider the class of points *x* such that *a* and *c*, *b* and *x* are each harmonic conjugates with respect to some pair of points *y*, :math:`y'`—in other words, *a* and *c*, *b* and *x* are pairs in an involution whose double points are *y*, :math:`y'`. Here *y*, :math:`y'` are supposed variable: that is, if any such points can be found, *x* is to belong to the class considered. This class contains the point *b*, but not *a* or *c*. Let us call it the segment (*abc*). Let us denote the relation of *b* to *x* (*a* and *c* being fixed) by *bQ*\ \ :math:`_{ac}`\ \ \ *x*. Then :math:`Q_{ac}` is symmetrical, and also *bQ*\ \ :math:`_{ac}`\ \ \ *x* implies *aQ*\ \ :math:`_{bx}`\ \ \ *c*. We have here a relation of four points, from which, as we saw in Part IV, Chapter xxiv, an order will result if certain further axioms are fulfilled. Three such axioms are required, and are given by Pieri as follows.

**(1)** If *d* is on the line *ab*, but does not belong to the segment (*abc*), and does not coincide with *a* or with *c*, then *d* must belong to the segment (*bca*). (If *d* coincides with *c*, we know already that *d* belongs to the segment (*bca*). This case is therefore excluded from the axiom to avoid a superfluity of assumptions.) In virtue of this axiom, if *a*, *b*, *c*, *d* be distinct points on a line, we must have either *bQ*\ \ :math:`_{ac}`\ \ \ *d* or *cQ*\ \ :math:`_{ab}`\ \ \ *d*. It follows that we must have either *bQ*\ \ :math:`_{ac}`\ \ \ *d* or *aQ*\ \ :math:`_{bc}`\ \ \ *d*. Thus at least two *Q*-relations hold between any four distinct collinear points. (2) If *a*, *b*, *c* be distinct collinear points, and *d* be a point belonging to both the segments (*bca*) and (*cab*), then *d* cannot belong to the segment (*abc*). That is, of the three segments to which *d* may belong, it never belongs to more than two. From this and the previous axiom it results that, if *d* be distinct from *a*, *b* and *c*, then *d* belongs to two and only two of the three segments defined by *a*, *b* and *c*. (3) If *a*, *b*, *c* be distinct collinear points, and *d* a point, other than *b*, of the segment (*abc*), and *e* a point of the segment (*adc*), then *e* is a point of the segment (*abc*). (Here again, the condition that *d* is to be other than *b* is required only to avoid superfluity, not for the truth of the axiom.) In terms of *Q*, this axiom states that *bQ*\ \ :math:`_{ac}`\ \ \ *d* and *dQ*\ \ :math:`_{ac}`\ \ \ *e* imply *bQ*\ \ :math:`_{ac}`\ \ \ *e*; that is, :math:`Q_{ac}` is transitive. We saw already that :math:`Q_{ac}` is symmetrical. We can now prove that, by means of this relation, all points of the line except *a* and *c* are divided into two classes, which we may call (*ac*)\ :math:`_{1}` and (*ac*)\ :math:`_{2}`. Any two points in the same class have the relation :math:`Q_{ac}`, any two in different classes have not. The division into *two* classes results from the fact that, if we do not have *bQ*\ \ :math:`_{ac}`\ \ \ *d*, nor yet *dQ*\ \ :math:`_{ac}`\ \ \ *e* (*b*, *d*, *e* being points other than *a* and *c*), then we do have *bQ*\ \ :math:`_{ac}`\ \ \ *e*. That is to say, :math:`Q_{ac}` has the formal properties of sameness of sign, and divides the line into two classes, just as sameness of sign divides numbers into positive and negative.

.. _pom-p387:

The opposite of :math:`Q_{ac}`, which I shall denote by :math:`T_{ac}`, corresponds in like manner to difference of sign. :math:`T_{ac}` is not to denote the mere negation of :math:`Q_{ac}`, but the fact of belonging to different segments. That is, *bT*\ \ :math:`_{ac}`\ \ \ *d* means that *d* does not coincide with *a* or *c*, that *d* lies in the line *ac*, but not in the segment (*abc*). Then *bT*\ \ :math:`_{ac}`\ \ \ *d* may be taken as meaning that *b* and *d* are separated by *a* and *c*. It is a relation which has the formal properties of separation of couples, as enumerated in Part IV, Chapter xxiv. If *a*, *b*, *c*, *d*, *e* be five distinct points in one straight line, we have the following properties of the *T*-relation. (1) *bT*\ \ :math:`_{ac}`\ \ \ *d* is equivalent to *dT*\ \ :math:`_{ac}`\ \ \ *b*, *aT*\ \ :math:`_{bd}`\ \ \ *c*, *cT*\ \ :math:`_{bd}`\ \ \ *a*, *cT*\ \ :math:`_{db}`\ \ \ *a*, etc. (2) We have one and only one of the three relations *aT*\ \ :math:`_{bc}`\ \ \ *d*, *aT*\ \ :math:`_{bd}`\ \ \ *C*, *aT*\ \ :math:`_{cd}`\ \ \ *b*. (3) *dT*\ \ :math:`_{ac}`\ \ \ *b* implies *dT*\ \ :math:`_{ac}`\ \ \ *e* or *eT*\ \ :math:`_{ac}`\ \ \ *b* [#pom_fn387_1]_.

By comparing the above properties of *T* with those of separation of couples, it will be seen that *T* leads to a closed series (in the sense of Part IV), *i.e.* to a series in which there is a first term, but this first term is arbitrary. The definition of the generating relation of the series (which involves, as in the general case, three fixed points) is given by Pieri as follows. With regard to the natural order *abc*, *a* precedes every other point of the line; *c* precedes every point *d* not belonging to (*abc*) and not coinciding with *a* or *c*, *i.e.* every point *d* such that *dT*\ \ :math:`_{ac}`\ \ \ *b*; a general point *d* precedes a general point *e* if *dQ*\ \ :math:`_{ac}`\ \ \ *b* and *eQ*\ \ :math:`_{ad}`\ \ \ *c*, or if *dT*\ \ :math:`_{ac}`\ \ \ *b* and *eT*\ \ :math:`_{ad}`\ \ \ *c*, *i.e.* if *d* belongs to the segment (*abc*) and *e* to the segment (*acd*), or if *b* and *d* are separated by *a* and *c*, and likewise *c* and *e* by *a* and *d*. It is then shown, that of any two points of the line, one precedes the other, and that the relation is transitive and asymmetrical; hence all the points of the line acquire an order.

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

Confining ourselves, to begin with, to one straight line, let us see how to construct a net and introduce projective coordinates. Denoting by *aH*\ \ :math:`_{bc}`\ \ \ *d*, as before, the proposition “*a* and *d* are harmonic conjugates with respect to *b* and *c*,” we can, by the quadrilateral construction, when *a*, *b*, *c* are given, determine the only point *d* satisfying this proposition. We next construct the point *e* for which *bH*\ \ :math:`_{cd}`\ \ \ *e*, then *f* for which *dH*\ \ :math:`_{ce}`\ \ \ *f*, *g* for which *eH*\ \ :math:`_{cf}`\ \ \ *g*, and so on. In this way we obtain a progression of points on our line, such that any three consecutive points, together with *c*, form a harmonic range. With our former definition of a segment, all these points will belong to the segments (*abc*) and (*bca*). We may number these points, beginning with *a*, 0, 1, 2, …, *n*, …. Since *c* does not belong to the progression, we may assign to it the number ∞ [#pom_fn388_3]_. Consider next the points obtained as follows. Let :math:`d'` be such that :math:`d'H_{ab}`\ \ \ *c*, let :math:`e'H_{ad}`\ \ \ *b*, :math:`f'H_{ac}d'`, and so on. We have thus a new progression of points, such that any three consecutive points together with *a* form a harmonic range, and all belonging to the segments (*abc*), (*cab*). To these points let us assign the numbers 1/*n* in order. Similarly we can construct a progression belonging to the two segments (*cab*), (*bca*), and assign to them the negative integers. By proceeding in a similar manner with any triad of points so obtained, we can obtain more and more points. The principle adopted in assigning numbers to points (a principle which, from our present standpoint, has no motive save convenience) is the following: if *p*, *q*, *r* be the numbers assigned to three points already constructed, and *s* be the number to be assigned to the harmonic conjugate (supposed not previously constructed) of the *q*-point with respect to the *p*-point and the *r*-point, then we are to have :math:`\frac{p - q}{r - q} / \frac{p - s}{r - s}` = −1. In this manner, we can find one and only one point of our line for each rational number, positive or negative [#pom_fn389_1]_. Thus we obtain a denumerable endless compact series of points on our line. Whether these are all the points of our line or not, we cannot decide without a further axiom. If our line is to be a continuous series, or a collection of the power of the continuum, we must of course assume points not obtainable by quadrilateral constructions, however often repeated, which start with three given elements. But as the definition of our space is optional, we may, if we like, content ourselves with a rational space, and introduce an axiom to the effect that all points of our line can be obtained from three given points.

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

**370.** Returning now to the quadrilateral construction, we define as the *anharmonic ratio* of four points whose coordinates are *p*, *q*, *r*, *s* the number :math:`\frac{p - q}{r - q} / \frac{p - s}{r - s}`. It can be shown that this number is independent of the choice of our three original points *a*, *b*, *c*. It expresses the series of quadrilateral constructions required to obtain *s* when *p*, *q*, *r* are given, and thus expresses a purely projective relation of the four points. By the introduction of irrational points, in the manner just explained, it follows that *any* four points on a line have an anharmonic ratio. (This cannot possibly be proved without Pieri’s three axioms or some equivalent to them.) The anharmonic ratio is unaltered by any linear transformation, *i.e.* by substituting for every point *x* the point whose coordinate is (*αx* + *β*)/(*γx* + *δ*), where *α*, *β*, *γ*, *δ* are any fixed numbers such that *αδ* − *βγ* is not zero. From this point we can at last advance to what was formerly the beginning of projective Geometry, namely the operation of projection, to which it owes its name.

It can be shown that, if *p*, *r* be harmonic conjugates with respect to *q*, *s*, and *p*, *q*, *r*, *s* be joined to some point *o*, and if *op*, *oq*, *or*, *os* meet any line in :math:`p'`, :math:`q'`, :math:`r'`, :math:`s'`, then :math:`p'`, :math:`r'` are harmonic conjugates with respect to :math:`q'`, :math:`s'`. Hence we can show that all anharmonic ratios are unaltered by the above operation. Similarly if *l* be any straight line not coplanar with *pqrs*, and the planes *lp*, *lq*, *lr*, *ls* meet any line not coplanar with *l* in :math:`p'`, :math:`q'`, :math:`r'`, :math:`s'`, these four points will have the same anharmonic ratio as *p*, *q*, *r*, *s*. These facts are expressed by saying that anharmonic ratio is unaltered by projection. From this point we can proceed to the assignment of coordinates to any point in space [#pom_fn390_2]_.

.. _pom-371:

§ 371. Assignment of coordinates to any point in space
------------------------------------------------------

.. folio:: §371
   :page: p. 390

.. _pom-p391:

**371.** To begin with a plane, take three points *a*, *b*, *c* not in one straight line, and assign coordinates in the above manner to the points of *ab*, *ac*. Let *p* be any point of the plane *abc*, but not on the line *bc*. Then if *cp* meets *ab* in :math:`p_{1}`, and *bp* meets *ac* in :math:`p_{2}`, and *x*, *y* are the coordinates of :math:`p_{1}`, :math:`p_{2}` respectively, let (*x*, *y*) be the two coordinates of *p*. In this way all points of the plane not on *bc* acquire coordinates. To avoid this restriction, let us introduce three homogeneous coordinates, as follows. Take any four points *a*, *b*, *c*, *e* in a plane, no three of which are collinear; let *ae* meet *bc* in :math:`e_{1}`, *b*\ e meet *ca* in :math:`e_{2}`, *ce* meet *ab* in :math:`e_{3}`. Assign coordinates to the points of *bc*, *ca*, *ab* as before, giving the coordinate 1 to :math:`e_{1}`, :math:`e_{2}`, :math:`e_{3}`, and in *ab* giving 0 to *a*, and ∞ to *b*, and similarly for the other sides. In place of the single coordinate *x* of any point of *bc*, let us introduce the homogeneous coordinates :math:`x_{2}`, :math:`x_{3}`, where *x* = :math:`x_{2}`/:math:`x_{3}`. If now *p* be any point of the plane *abc*, let *ap* meet *bc* in :math:`p_{1}`, *bp* meet *ca* in :math:`p_{2}`, and *cp* meet *ab* in :math:`p_{3}`. Let :math:`x_{2}`, :math:`x_{3}` be the homogeneous coordinates of :math:`p_{1}`, :math:`x_{3}`, :math:`x_{1}` those of :math:`p_{2}`; then :math:`x_{1}`, :math:`x_{2}` will be those of :math:`p_{3}` [#pom_fn391_1]_. Hence we may assign :math:`x_{1}`, :math:`x_{2}`, :math:`x_{3}` as homogeneous coordinates of *p*. In like manner we can assign four homogeneous coordinates to any point of space. We can also assign coordinates to the lines through a point, or the planes through a line, or all the planes of space, by means of the anharmonic ratios of lines and planes [#pom_fn391_2]_. It is easy to show that, in point-coordinates, a plane has a linear equation, and a linear equation represents a plane; and that, in plane-coordinates, a point has a linear equation, and a linear equation represents a point. Thus we secure all the advantages of analytical Geometry. From this point onwards, the subject is purely technical, and ceases to have philosophic interest.

.. _pom-372:

§ 372. Comparison of projective and Euclidean geometry
------------------------------------------------------

.. folio:: §372
   :page: p. 391

**372.** It is now time to ask ourselves what portions of the Geometry to which we are accustomed are not included in projective Geometry. In the first place, the series of points on a line, being obtained from a four-term relation, is closed in the sense of Part IV. That is, the order of points requires three fixed points to be given before it can be defined. The practical effect of this is, that given only three points on a line, no one of them is between the other two. This is a definite difference between projective space and Euclidean or hyperbolic space. But it is easy to exaggerate this difference. We saw in Part IV that, wherever a series is generated by a two-term relation, there is also the four-term relation of separation of couples, by which we can generate a closed series consisting of the same terms. Hence in this respect the difference does not amount to an inconsistency. Euclidean and hyperbolic spaces contain what projective space contains, and something more besides. We saw that the relation by which the projective straight line is defined has the formal properties of “*P* or :math:`\breve{P}`,” where *P* is transitive and asymmetrical. If the said relation be actually of this form, we shall have an open series with respect to *P*, and of three collinear points one will be between the other two. It is to be observed that, where the straight line is taken to be essentially closed, as in elliptic space, *between* must be excluded where three points only are given. Hence elliptic space, in this respect, is not only consistent with the projective axioms, but contains nothing more than they do.

.. _pom-p392:

It is when we come to the plane that actual inconsistencies arise between projective Geometry and Euclidean or hyperbolic Geometry. In projective space, any two lines in a plane intersect; in the Euclidean and hyperbolic Geometries, this does not occur. In elliptic Geometry, any two lines in a plane intersect; but in the antipodal form they intersect twice. Thus only the polar form wholly satisfies the projective axioms. Analogous considerations apply to the intersection of two planes, or of a line and a plane. These differences render the projective definition of a plane inapplicable to Euclidean and hyperbolic spaces, and render the theory of these spaces far more complicated than that of projective space.

Finally, in metrical Geometry it is assumed either that two points have a quantitative relation called distance, which is determined when the points are given, or that stretches satisfy axioms in virtue of which their divisibilities become numerically measurable. In this point, even elliptic space differs from projective space, though the difference is of the nature of an addition, not an inconsistency. But this matter cannot be discussed until we have examined metrical Geometry, when we shall be in a position to examine also the projective theory of distance to more advantage than is at present possible.

.. _pom-373:

§ 373. The principle of duality
-------------------------------

.. folio:: §373
   :page: p. 392

**373.** A few words may be added concerning the principle of duality. This principle states, in three dimensions, that the class of planes is also a projective space, the intersection of two planes being, as before, the straight line, and the intersection of three non-collinear planes taking the place of the point. In *n* dimensions, similarly, a projective space results from all sub-classes of (*n* − 1) dimensions. Such a duality, as we saw in :ref:`Chapter xliv <pom-ch-44-dimensions-en>`, belongs always to *n*-dimensional series as such. It would seem (though this is only a conjecture) that projective Geometry employs the smallest number of axioms from which it is possible to generate a series of more than two dimensions, and that projective duality therefore flows from that of dimensions in general. Other spaces have properties additional to those required to make them *n*-dimensional series, and in other spaces, accordingly, duality is liable to various limitations.

.. rubric:: Footnotes

.. [#pom_fn387_1] This last property affords an instance (almost the only one known to me) where Peirce’s relative addition occurs outside the Algebra of Relatives. “*dT*\ \ :math:`_{ac}`\ \ \ *e* or *eT*\ \ :math:`_{ac}`\ \ \ *b*” is the relative sum of :math:`T_{ac}` and :math:`T_{ac}`, if *d*, *e*, and *b* be variable. This property results formally from regarding :math:`T_{ac}` as the negation of the transitive relation :math:`Q_{ac}`.

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
