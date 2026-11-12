:layout: book

.. _pom-ch-46-descriptive:
.. _pom-ch-46-descriptive-en:

CHAPTER XLVI
============

.. rubric:: Part VI — Space — Descriptive Geometry (§§ 374–387, pp. 393–403)

.. contents:: Analytical Section Outline
   :local:
   :depth: 2
   :backlinks: none

.. _pom-374:

§ 374. Distinction between projective and descriptive geometry
--------------------------------------------------------------

.. folio:: §374
   :page: p. 393

.. _pom-p393:

**374.** The subject which I have called descriptive Geometry is not, as a rule, sharply distinguished from projective Geometry. These two terms, and the term “Geometry of Position,” are commonly used as synonyms. But it seems improper to include in projective Geometry any property which is not unaltered by projection, and it is by the introduction of one such property that I wish to define the subject of the present chapter. We have seen that, in projective space, three points on a line are not such that a definite one of them is *between* the other two. The simplest possible proposition involving *between*, in projective Geometry, requires four points, and is as follows: “If *a*, *b*, *c* be distinct collinear points, and *d* is on *ac*, but does not belong to the segment (*abc*), nor yet coincide with *a* or *c*, then, with regard to the order *abc*, *c* is between *b* and *d*.” When we reflect that the definition of the segment (*abc*) involves the quadrilateral construction—which demands, for its proof, a point outside its own plane, and four pairs of triangles in perspective—we shall admit that the projective method of generating order is somewhat complicated. But at any rate the ordinal propositions which result are unaltered by projection. The elementary sense of *between*, on the contrary, which is to be introduced in the present chapter, is in general not unaltered by projection [#pom_fn393_1]_.

.. _pom-p394:

In descriptive Geometry, we start, as before, with points, and as before, any two points determine a class of points. But this class now consists only of the points *between* the two given points. What is to be understood by *between* is not explained by any writer on this subject except Vailati, in terms of a transitive asymmetrical relation of two points; and Vailati’s explanation is condemned by Peano [#pom_fn394_1]_, on the ground that *between* is a relation of *three* points, not of two only. This ground, as we know from Part IV, is inadequate and even irrelevant. But on the subject of relations, even the best mathematicians go astray, for want, I think, of familiarity with the Logic of Relations. In the present case, as in that of projective Geometry, we may start either with a relation of two points, or with a relation between a pair and a class of points: either method is equally legitimate, and leads to the same results, but the former is far simpler. Let us examine first the method of Pasch and Peano, then that of Vailati.

.. _pom-375:

§ 375. Method of Pasch and Peano
--------------------------------

.. folio:: §375
   :page: p. 394

**375.** We start, in the former method, with two indefinables, *point*, and *between*. If *a*, *b*, *c* be three points, and *c* is between *a* and *b*, we say that *c* is an *ab*, or belongs to the class of points *ab*. Professor Peano has enumerated, with his usual care, the postulates required as regards the class *ab* [#pom_fn394_2]_. In the first place, the points *a* and *b* must be distinct, and when they are so, there always is a point between them. If *c* is between *a* and *b*, it is also between *b* and *a*: *a* itself (and therefore *b*) is not between *a* and *b*. We now introduce a new definition. If *a*, *b* be any two distinct points, then $a'$\ \ *b* is the class of all points *c* such that *b* is between *a* and *c*. Similarly $b'$\ \ *a* will be the class of points *d* such that *a* is between *b* and *d*. We then proceed to new postulates. If *a* and *b* be distinct points, $a'$\ \ *b* must contain at least one point. If *a*, *b*, *c*, *d* be points, and *c* is between *a* and *d*, *b* between *a* and *c*, then *b* is between *a* and *d*. If *b* and *c* be between *a* and *d*, *b* is between *a* and *c*, or identical with *c*, or between *c* and *d*. If *c*, *d* belong to $a'$\ \ *b*, then either *c* and *d* are identical, or *c* is between *b* and *d*, or *d* is between *b* and *c*. If *b* is between *a* and *c*, and *c* is between *b* and *d*, then *c* is between *a* and *d*. This makes in all nine postulates with regard to *between*. Peano confesses [#pom_fn394_3]_ that he is unable to prove that all of them are independent: hence they are only shown to be sufficient, not necessary. The complete straight line (*ab*) is defined as $b'$\ \ *a* and *a* and *ab* and *b* and $a'$\ \ *b*; that is, (1) points between which and *b* the point *a* lies; (2) the point *a*; (3) points between *a* and *b*; (4) the point *b*; (5) points between which and *a* the point *b* lies.

.. _pom-p395:

Concerning this method, we may observe to begin with that it is very complicated. In the second place, we must remark, as before, that the phrase “two points *determine* a class of points” must be expanded as follows: “There is a certain specific relation *K*, to whose domain belongs every couple of distinct points. *K* is a many-one relation, and the relatum, corresponding to a couple of points as referent, is a class of points.” In the third place, we may observe that the points of the line only acquire order by relation to the segments which they terminate, and that these acquire order by the relation of whole and part, or logical inclusion. Let *a*, *b* be any two points, and consider the class of points *ab* or *b* or $a'$\ \ *b*. Let *c*, *d* be any two distinct points of this class. Then either *ac* is a proper part of *ad*, or *ad* is a proper part of *ac*. Here *ac* and *ad* may be called segments, and we see that segments whose origin is *a* and whose limits belong to *ab* or *b* or $a'$\ \ *b* form a series in virtue of the transitive asymmetrical relation of whole and part. By correlation with these segments, their extremities also acquire an order; and it is easy to prove that this order is unchanged when we substitute for *a* any point of $ab'$. But the order still results, as it always must, from a transitive asymmetrical relation of two terms, and nothing is gained by not admitting such a relation immediately between points.

.. _pom-376:

§ 376. Method employing serial relations
----------------------------------------

.. folio:: §376
   :page: p. 395

**376.** Passing now to what I have called Vailati’s theory, we find a very great simplification. We may state the present theory (which is not in every detail identical with that of Vailati) as follows. There is a certain class, which we will call *K*, of transitive asymmetrical relations. Between any two points there is one and only one relation of the class *K*. If *R* be a relation of the class *K*, $\breve{R}$ is also a relation of this class. Every such relation *R* defines a straight line; that is, if *a*, *b* be two points such that *aRb*, then *a* belongs to the straight line *ρ*. (I use the corresponding Greek letter to denote the domain of a relation; thus if *S* be a relation, *σ* is the class of terms having the relation *S* to some term or other.) If *aRb*, then there is some point *c* such that *aRc* and *cRb*; also there is a point *d* such that *bRd*. Further, if *a*, *b* be any two distinct points belonging to *ρ*, then either *aRb* or *bRa*. With this apparatus we have all that we require.

We may do well to enumerate formally the above definition of the class *K*, or rather the postulates concerning its members—for *K* itself is not defined. I may remark to begin with that I define the field of a class of relations as the logical sum of the fields of the constituent relations; and that, if *K* be the class, I denote its field by *k*. Then the axioms we require are as follows.

**(1)** There is a class of relations *K*, whose field is defined to be the class *point*.

**(2)** There is at least one point.

If *R* be any term of *K* we have,

**(3)** *R* is an aliorelative.

**(4)** $\breve{R}$ is a term of *K*.

**(5)** $R^{2}$ = *R*.

**(6)** $\breve{\rho}$ (the domain of $\breve{R}$) is contained in *ρ*.

**(7)** Between any two points there is one and only one relation of the class *K*.

**(8)** If *a*, *b* be points of *ρ*, then either *aRb* or *bRa*.

.. _pom-p396:

The mutual independence of these axioms is easy to see. But let us first briefly sketch the proof that they give all the required results. Since there is, by (2), at least one point, and since by (1) this point has some relation of the class *K*, and since by (3) all relations of the class *K* are aliorelatives, it follows that there is some term, other than the one point, to which this one point has a relation *R* of the class *K*. But since $\breve{R}$, by (4), is a relation of the class *K*, it follows that the term to which the one point is so related is also a point. Hence there are at least two distinct points. Let *a*, *b* be two distinct points, and let *R* be the one relation of the class *K* between *a* and *b*. Thus we have *aRb*. But we do not have *bRa*, for if we did, since $R^{2}$ = *R*, by (5), we should have *aRa*, which contradicts (3). Thus *R* and $\breve{R}$ are always different, *i.e.* each is asymmetrical. Since $R^{2}$ = *R*, *aRb* *and* *bRc* imply *aRc*, *i.e.* *R* is transitive. Hence the points which have to *a* the relation *R* or $\breve{R}$, together with *a* itself, form a series. Since *R* = $R^{2}$, *aRb* implies that there is some point *c* such that *aRc*, *cRb*; *i.e.* the series generated by *R* is compact. Since, by (6), $\breve{\rho}$ is contained in *ρ*, *aRb* implies that there is some point *c* such that *bRc*. Applying the same argument to $\breve{R}$, there is a point *d* such that *dRa*. Thus we have *ρ* = $\breve{\rho}$, and the field of *R* has no beginning or end. By (8), the field of *R* is what, in Part IV, we called a connected series, that is, it does not fall apart into two or more detached portions, but of any two of its terms one is before and the other after. By (7), if there be more than one relation of the class *K*, the fields of two such relations cannot, unless one is the converse of the other, have more than one point in common. The field of one relation of the class *K* is called a *straight line*; and thus (7) assures us that two straight lines have at most one common point, while (8) assures us that, if *ab*, *cd* be the same line, so are *ac* and *bd*. Thus it is proved that our axioms are sufficient for the geometry of a line, while (7) goes beyond a single line, but is inserted here because it does not imply the *existence* of points outside a single line, or of more than one relation of the class *K*. It is most important to observe that, in the above enumeration of fundamentals, there is only one indefinable, namely *K*, not two as in Peano’s system.

.. _pom-377:

§ 377. Mutual independence of axioms
------------------------------------

.. folio:: §377
   :page: p. 396

.. _pom-p397:

**377.** With regard to the mutual independence of the axioms, it is to be observed that (1) is not properly an axiom, but the assumption of our indefinable *K*. (2) may obviously be denied while all the others are maintained. If (3) be denied, and *R* be taken to be the symmetrical relation of projective Geometry, together with identity with some term of *ρ*, we obtain projective Geometry, which is different from the present system, but self-consistent. If (4) be denied, all the rest can be maintained; the only difficulty is as regards (7), for if *aRb*, and $\breve{R}$ is not a term of *K*, *b* will not have to *a* any relation of the class *K*, unless indeed it has one which is not $\breve{R}$, which seems to be not contradictory. As regards (5), we may deny either that *R* is contained in $R^{2}$, or that $R^{2}$ is contained in *R*. To deny the former makes our series not compact, to which there is no logical objection. The latter, but not the former, is false as regards angles [#pom_fn397_1]_, which can be made to satisfy all the other axioms here laid down. (6) will become false if our lines have last terms: thus the space on the left of a plane, together with this plane, will satisfy all the axioms except (6). As regards (7), it is plainly independent of all the rest; it consists of two parts, (*a*) the assertion that between any two points there is at least one relation of the class *K*, (*b*) the assertion that there is not more than one such relation between two given points. If we consider a Euclidean and a hyperbolic space together, all the axioms will be true except (*a*). If we combine two different classes $K_{1}$, $K_{2}$ of relations of the above kind, such that $k_{1}$ = $k_{2}$, (*b*) alone will be false. Nevertheless it seems plain that (*b*) cannot be deduced from the other axioms. As regards (8), it alone is false if we take for *K* the class of directions in Euclidean space, in which a set of parallel lines all have the same direction. Thus the necessity of all except one of our axioms is strictly proved, and that of this one is highly probable.

.. _pom-378:

§ 378. Logical definition of the class of descriptive spaces
------------------------------------------------------------

.. folio:: §378
   :page: p. 397

**378.** We saw that the above method enabled us to content ourselves with one indefinable, namely the class of relations *K*. But we may go further, and dispense altogether with indefinables. The axioms concerning the class *K* were all capable of statement in terms of the logic of relations. Hence we can define a class *C* of classes of relations, such that every member of *C* is a class of relations satisfying our axioms. The axioms then become parts of a definition, and we have neither indefinables nor axioms. If *K* be any member of the class *C*, and *k* be the field of *K*, then *k* is a descriptive space, and every term of *k* is a descriptive point. Here every concept is defined in terms of general logical concepts. The same method can be applied to projective space, or to any other mathematical entity except the indefinables of logic. This is, indeed, though grammatically inconvenient, the true way, philosophically speaking, to define mathematical notions. Outside logic, indefinables and primitive propositions are not required by pure mathematics, and should therefore, strictly speaking, not be introduced. This subject will be resumed in :ref:`Chapter xlix <pom-ch-49-spaces-en>`.

.. _pom-379:

§ 379. Parts of straight lines
------------------------------

.. folio:: §379
   :page: p. 397

.. _pom-p398:

**379.** The two ways of defining the straight line—that of Pasch and Peano, and that which I have just explained—seem equally legitimate, and lead to the same consequences. The choice between them is therefore of no mathematical importance. The two methods agree in enabling us, in terms of two points only, to define three parts of a straight line, namely the part before *a* ($b'$\ \ *a*), the part between *a* and *b* (*ab*), and the part after *b* ($a'$\ \ *b*). This is a point in which descriptive Geometry differs from projective Geometry: there we had, with respect to *a* and *b*, only two segments of the straight line *ab*, and these could not be defined without reference to another point *c* of the line, and to the quadrilateral construction.

The straight line may be regarded either as the class of points forming the field of a relation *R*, or as this relation itself. For the sake of distinction, it will be well to call the relation *R* a *ray*, since this word suggests a sense; $\breve{R}$ will then be the opposite ray. In considering a number of lines all passing through one point *O*, it will be well to give the name of *ray* also to the class of points to which *O* has some relation *R*, *i.e.* to those points of a line through *O* which lie on one side of *O*. Those on the other side of *O* will then be the opposite ray. The context will show in which sense the word is used.

.. _pom-380:

§ 380. Definition of the plane
------------------------------

.. folio:: §380
   :page: p. 398

**380.** I come now to the *plane*. Easy as it is to define the plane in projective space, its definition when the line is not a closed series, or rather, when we wish to call coplanar some pairs of lines which do not intersect, is a matter of some difficulty. Pasch [#pom_fn398_1]_ takes the plane, or rather a finite portion of the plane, as a new indefinable. It is, however, capable of definition, as, following Peano, I shall now show.

.. _pom-p399:

We need, to begin with, some new axioms. First, if *ρ* be any straight line, there is at least one point not belonging to *ρ*. Next, if *a*, *b*, *c* be three points not in one straight line, and *d* be a point of *bc* between *b* and *c*, *e* a point of *ad* between *a* and *d*, then *be* will meet *ac* in a point *f* and *e* will be between *b* and *f*, *f* between *a* and *c*. Again, *a*, *b*, *c*, *d* being as before, if *y* be a point between *a* and *c*, then *ad* and *bf* will intersect in a point *e* between *a* and *d* and between *b* and *f* [#pom_fn398_2]_. We now define what may be regarded as the product (in a geometrical sense) of a point and a figure. If *a* be any point, and *k* any figure, *ak* is to denote the points which lie on the various segments between *a* and the points of *k*. That is, if *p* be any point of *k*, and *x* any point of the segment *ap*, then *x* belongs to the class *ak*. This definition may be applied even when *a* is a point of *k*, and *x* is a straight line or part of one. The figure *ak* will then be the whole line or some continuous portion of it. Peano now proves, by purely logical transformations, that, if *a*, *b*, *c* be distinct non-collinear points, *a*\ (*bc*) = *b*\ (*ac*). This figure is called the triangle *abc*, and is thus wholly determined by its three defining points. It is also shown that, if *p*, *q* be points of the segments *ab*, *ac* respectively, the segment *pq* is wholly contained in the triangle *abc*. After some more theorems, we come to a new definition. If *a* be a point, and *k* any figure (*i.e.* class of points), $a'$\ \ *k* is to denote all the points between which and *a* lies some point of *k*, that is, as Peano remarks, the whole shadow of *k* if *a* be an illuminated point. Thus if *a*, *b*, *c* be non-collinear points, $a'$\ (*bc*) will represent the class of points beyond *bc* and bounded by *ab*, *ac* produced. This enables us to define the plane (*abc*) as consisting of the straight lines *bc*, *ca*, *ab*, the triangle *abc*, and the figures $a'$\ \ *bc*, $b'$\ \ *ca*, $c'$\ \ *ab*, $b'c'$\ \ *a*, $c'a'$\ \ *b*, $a'b'$\ \ *c* [#pom_fn399_1]_. It is then easy to show that any other three points of the plane define the same plane, and that the line joining two points of a plane lies wholly in the plane. But in place of the proposition that any two lines in a plane intersect, we have a more complicated proposition, namely: If *a*, *b*, *c*, *d* be coplanar points, no three of which are collinear, then either the lines *ab*, *cd* intersect, or *ac*, *bd* do so, or *ad*, *bc* do so.

.. _pom-381:

§ 381. Solid geometry
---------------------

.. folio:: §381
   :page: p. 399

**381.** Having successfully defined the plane, we can now advance to solid Geometry. For this we need, to begin with, the axiom: Given any plane, there is at least one point outside the plane. We can then define a tetrahedron exactly as we defined a triangle. But in order to know that two planes, which have a point in common, have a line in common, we need a new axiom, which shows that the space we are dealing with has three dimensions. In projective space, this axiom was simply that a line and a plane always have at least one point in common. But here, no such simple axiom holds. The following is given by Peano (*loc. cit.* p. 74): If *p* be a plane, and *a* a point not on *p*, and *b* a point of $a'$\ \ *p* (*i.e.* a point such that the segment *ab* contains a point of *p*, or, in common language, a point on the other side of the plane from *a*), then if *x* be any point, either *x* lies on the plane, or the segment *ax* contains a point of the plane, or else the segment *bx* contains a point of the plane. By adding to this, finally, an axiom of continuity, we have all the apparatus of three-dimensional descriptive Geometry [#pom_fn399_2]_.

.. _pom-382:

§ 382. Descriptive geometry applies to Euclidean and hyperbolic, but not elliptic space
---------------------------------------------------------------------------------------

.. folio:: §382
   :page: p. 399

.. _pom-p400:

**382.** Descriptive Geometry, as above defined, applies equally to Euclidean and to hyperbolic space: none of the axioms mentioned discriminate between these two. Elliptic space, on the contrary, which was included in projective Geometry, is here excluded. It is impossible, or rather, it has hitherto proved so, to set up a general set of axioms which will lead to a general Geometry applying to all three spaces, for at some point our axioms must lead to either an open or a closed series of points on a line. Such a general Geometry can be constructed symbolically, but this results from giving different interpretations to our symbols, the indefinables in one interpretation being definable in another, and *vice versâ*. This will become plain by examining the method in which projective Geometry is made applicable to the space above defined, which, for want of a better name, I shall call descriptive space.

.. _pom-383:

§ 383. Ideal elements
---------------------

.. folio:: §383
   :page: p. 400

**383.** When we try to apply projective Geometry to descriptive space, we are met by the difficulty that some of the points required in a construction may not exist. Thus in the quadrilateral construction, given three points *a*, *b*, *c*, the fourth point *d* may not exist at all. We can prove as before that, if it exists, it is unique, and so with other projective propositions: they become hypothetical, since the construction indicated is not always possible. This has led to the introduction of what are called *ideal* elements (points, lines and planes), by means of which it becomes possible to state our projective theorems generally. These ideal elements have a certain analogy to complex numbers in Algebra—an analogy which in analytical Geometry becomes very close. Before explaining in detail how these elements are introduced, it may be well to state the logical nature of the process. By means of the points, lines and planes of descriptive Geometry, we define a new set of entities, some of which correspond (*i.e.* have a one-one relation) to our points, lines and planes respectively, while others do not. These new entities we call ideal points, lines and planes; and we find that they have all the properties of projective points, lines and planes. Hence they constitute a projective space, and all projective propositions apply to them. Since our ideal elements are defined by means of the elements of descriptive space, projective propositions concerning these ideal elements are theorems concerning descriptive space, though not concerning its actual points, lines and planes. Pasch, who has given the best account of the way in which ideal elements are to be defined [#pom_fn400_1]_, has not perceived (or, at any rate, does not state) that no ideal point is an actual point, even where it has a one-one relation to an actual point, and that the same holds of lines and planes. This is exactly the same remark as we have had to make concerning rationals, positive numbers, real numbers, and complex numbers, all of which are supposed, by the mathematician, to contain the cardinals or the ordinals, whereas no one of them can ever be one of the cardinals or ordinals. So here, an ideal element is never identical with an actual point, line or plane. If this be borne in mind, the air of magic which surrounds the usual expositions disappears.

.. _pom-384:

§ 384. Ideal points
-------------------

.. folio:: §384
   :page: p. 400

.. _pom-p401:

**384.** An ideal point is defined as follows. Consider first the class of all the lines passing through some point, called the vertex. This class of lines is called a *sheaf* of lines (*Strahlenbündel*). A sheaf so defined has certain properties which can be stated without reference to the vertex [#pom_fn400_2]_. Such are, for example, the following: Through any point (other than the vertex) there is one and only one line of the sheaf; and any two lines of the sheaf are coplanar. All the properties of a sheaf, which can be stated without reference to the vertex, are found to belong to certain classes of lines having no vertex, and such that no two of the class intersect. For these a simple construction can be given, as follows [#pom_fn401_1]_. Let *l*, *m* be any two lines in one plane, *A* any point not in this plane. Then the planes *Al*, *Am* have a line in common. The class of such lines, for all possible points *A* outside the plane *lm*, has the properties above alluded to, and the word *sheaf* is extended to all classes of lines so defined. It is plain that if *l*, *m* intersect, the sheaf has a vertex; if not, it has none. Thus, in Euclidean space, all the lines parallel to a given line form a sheaf which has no vertex. When our sheaf has no vertex, we define an *ideal point* by means of the sheaf. But this must not be supposed to be really a point: it is merely another name for the sheaf itself, and so, when our sheaf has a vertex, if we are to make propositions in which ideal points occur, we must substitute the sheaf for its vertex. That is, an ideal point is simply a sheaf, and no sheaf *is* an actual point.

Concerning sheaves of lines we may observe the following points. Any two straight lines in one plane uniquely determine a sheaf. Two sheaves both having a vertex always determine a line, namely that joining the vertices, which is common to both sheaves. Three sheaves, of which one at least has a vertex, determine a plane, unless they are collinear. A line and a plane always have a common sheaf, and so have three planes of which two at least have a common point.

.. _pom-385:

§ 385. Ideal lines
------------------

.. folio:: §385
   :page: p. 401

.. _pom-p402:

**385.** Thus sheaves of lines have some projective properties, in relation to lines and planes, which are lacking to points. In order to obtain entities with further projective properties, we must, to begin with, replace our lines by ideal lines. For this purpose we must first define pencils of planes (axial pencils, *Ebenenbüschel*). An axial pencil consists, in the first instance, of all the planes through a given straight line, called the axis. But as in the case of sheaves, it is found that such a figure has many properties independent of the axis, and that these properties all belong to certain other classes of planes, to which the name of pencil is therefore extended. These figures are defined as follows [#pom_fn401_2]_. Let *A*, *B* be two sheaves of lines. Let *D* be a point not on the line (if there be one) common to the two sheaves *A*, *B*. Then *A*, *B*, *D* determine uniquely a plane, which we may call *ABD*, or *P* (say). This will be the plane containing those lines of *A* and *B* that pass through *D*. Any other point *E*, not in the plane *P*, will determine a different plane *ABE*, or *Q*. The class of planes so obtained, by varying *D* or *E*, is a pencil of planes, and has all the properties of a pencil having a real axis, except those in which the axis is explicitly mentioned. Any two planes *P* and *Q* belonging to the pencil completely determine it. Moreover, in place of *A* and *B* above, we may substitute any other sheaves of lines $A'$, $B'$, belonging to both *P* and *Q*. (A sheaf belongs to a plane when one of its lines lies in the plane.) Any two sheaves belonging to both *P* and *Q* will serve to define the pencil of planes, and will belong to every plane of the pencil. Hence if, in place of actual points, we substitute ideal points, *i.e.* sheaves of lines, every pencil of planes has an axis, consisting of a certain collection of sheaves of lines, any two of which define the pencil. This collection of sheaves is called an *ideal line* [#pom_fn402_1]_.

.. _pom-386:

§ 386. Ideal planes
-------------------

.. folio:: §386
   :page: p. 402

**386.** Substituting ideal points and lines for actual ones, we find that we have now made a further advance towards projective space. Two ideal points determine one and only one ideal line; a given plane is determined by any three of its ideal points which do not belong to one ideal line, but three ideal points do not always determine a plane. Two ideal lines in a plane always have a common ideal point, and so have a plane and an ideal line. Also two planes always have a common ideal line, and three planes always have either a common ideal point or a common ideal line. The only point where our space is not strictly projective is in regard to planes. There is a plane through any two ideal points and one actual point, or through an ideal point and an actual line. If there is a plane at all through three non-collinear ideal points, or through an ideal line and an ideal point not on the line, then there is only one such plane; but in some cases there is no such plane. To remedy this, we must introduce one more new class of entities, namely ideal planes.

The definition of ideal planes [#pom_fn402_2]_ is comparatively simple. If *A*, *B*, *C* be any three ideal points, *D* an ideal point on the ideal line *AB*, and *E* on *AC*, then the ideal line *DE* has an ideal point in common with *BC*, whether there be an actual plane determined by *A*, *B*, *C* or not. Thus if *B*, *C*, *D* be any three ideal points, and *E* any other ideal point such that *BD*, *CE* intersect, then *BC*, *DE* intersect, and so do *BE*, *CD*. Hence, if *B*, *C*, *D* be not collinear, we define the ideal plane *BCD* as that class of ideal points *E* which are such that the ideal lines *BD*, *CE* intersect.

For the sake of clearness, let us repeat this definition in terms of our original points, lines and planes, without the use of the word *ideal*. Given three sheaves of lines *B*, *C*, *D*, which are not all contained in a common pencil of planes, let *E* be another sheaf of lines such that there is a sheaf of lines common to the two pencils of planes *BD*, *CE*. Then the class of all sheaves *E* satisfying this condition is called the ideal plane *BCD*.

.. _pom-p403:

The usual properties of planes are easily proved concerning our new ideal planes, as that any three of their points determine them, that the ideal line joining two of their ideal points is wholly contained in them, and so forth. In fact, we find now that the new points, lines and planes constitute a projective space, with all the properties described in the :ref:`preceding chapter <pom-ch-45-projective-en>`. The elementary order of points on a line, with which we began, has disappeared, and a new order has to be generated by means of the separation of couples [#pom_fn403_1]_. Thus all projective Geometry becomes available; and wherever our ideal points, lines and planes correspond to actual ones, we have a corresponding projective proposition concerning the latter.

.. _pom-387:

§ 387. The removal of a suitable selection of points renders a projective space descriptive
-------------------------------------------------------------------------------------------

.. folio:: §387
   :page: p. 403

**387.** I have explained this development at length, partly because it shows the very wide applicability of projective Geometry, partly because it affords a good instance of the emphasis which mathematics lays upon relations. To the mathematician, it is wholly irrelevant what his entities are, so long as they have relations of a specified type. It is plain, for example, that an instant is a very different thing from a point; but to the mathematician as such there is no relevant distinction between the instants of time and the points on a line. So in our present instance, the highly complex notion of a sheaf of lines—an infinite class of infinite classes—is philosophically very widely dissimilar to the simple notion of a point. But since classes of sheaves can be formed, having the same relations to their constituent sheaves that projective lines and planes have to projective points, a sheaf of lines in descriptive space *is*, for mathematical purposes, a projective point. It is not, however, even for mathematical purposes, a point of descriptive space, and the above transformation clearly shows that descriptive space is not a species of projective space, but a radically distinct entity. And this is, for philosophy, the principal result of the present chapter.

It is a remarkable fact, which the above generation of a projective space demonstrates, that if we remove from a projective space all the points of a plane, or all the points on one side of a closed quadric [#pom_fn403_2]_, the remaining points form a descriptive space, Euclidean in the first case, hyperbolic in the second. Yet, in ordinary metrical language, the projective space is finite, while the part of it which is descriptive is infinite. This illustrates the comparatively superficial nature of metrical notions.

----

.. rubric:: Author's Footnotes (1903 Edition)

.. [#pom_fn393_1] The present subject is admirably set forth by Pasch, *Neuere Geometrie*, Leipzig, 1882, with whose empirical pseudo-philosophical reasons for preferring it to projective Geometry, however, I by no means agree (see *Einleitung* and §1). It is carried further, especially as regards the definition of the plane, by Peano, *I Principii di Geometria logicamente esposti*, Turin, 1889. For the definition of the whole line by means of its various segments, see Peano’s note in *Rivista di Matematica*, ii, pp. 58–62. See also his article “Sui fondamenti della Geometria,” *ib.* iv, p. 51ff., and Vailati, “Sui Principi fondamentali della Geometria della retta,” *Riv. d. Mat.* ii, pp. 71–75. Whatever, in the following pages, is not controversial, will be found in the above sources.

.. [#pom_fn394_1] *Riv. di Mat.* iv, p. 62.

.. [#pom_fn394_2] *Ib.* iv, p. 55ff.

.. [#pom_fn394_3] *Ib.* p. 62.

.. [#pom_fn397_1] See Part IV, chap. xxiv.

.. [#pom_fn398_1] *Op. cit.* §2.

.. [#pom_fn398_2] *Riv. di Mat.* iv, p. 64.

.. [#pom_fn399_1] The figure $b'$\ ($c'$\ \ *a*), or $b'c'$\ \ *a*, represents the angle between *ba* and *ca* both produced, as may be seen from the definition.

.. [#pom_fn399_2] I confine myself as a rule to three dimensions, since a further extension has little theoretic interest. Three dimensions are far more interesting than two, because, as we have seen, the greater part of projective Geometry—*i.e.* everything dependent upon the quadrilateral construction—is impossible with less than three dimensions, unless the uniqueness of the quadrilateral construction be taken as an axiom.

.. [#pom_fn400_1] *Op. cit.* §§6–8.

.. [#pom_fn400_2] These are enumerated by Killing, *Grundlagen der Geometrie*, Vol. ii (Paderborn, 1898), p. 82.

.. [#pom_fn401_1] Pasch, *op. cit.* §5

.. [#pom_fn401_2] Pasch, *op. cit.* §7

.. [#pom_fn402_1] For logical purposes, it is better to define the ideal line as the class of ideal points associated with a sheaf of planes, than as the sheaf itself, for we wish a line to be, as in projective Geometry, a class of points.

.. [#pom_fn402_2] Pasch, *op. cit.* §8.

.. [#pom_fn403_1] See Pasch, *op. cit.* §9.

.. [#pom_fn403_2] For the projective definition of a surface of the second order (quadric) in a projective space cf. Reye, *Geometrie der Lage* (Hanover, 1868), Part ii, Lecture v. A quadric is closed if there are points not on it such that all straight lines through them cut the quadric. Such points are *within* the quadric.
