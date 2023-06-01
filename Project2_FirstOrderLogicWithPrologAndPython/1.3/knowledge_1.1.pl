/* Male members */
male(prince_philip).
male(prince_charles).
male(captain_mark_philips).
male(timothy_laurence).
male(prince_andrew).
male(prince_edward).
male(prince_william).
male(prince_harry).
male(peter_phillips).
male(mike_tindall).
male(james_viscount_severn).
male(prince_george).

/* Female members */
female(queen_elizabeth).
female(princess_diana).
female(camilla_parker_bowles).
female(sarah_ferguson).
female(sophie_rhys_jones).
female(kate_middleton).
female(princess_anne).
female(zara_phillips).
female(princess_beatrice).
female(princess_eugenie).
female(lady_louise_mountbatten_windsor).
female(princess_charlotte).
female(savannah_phillips).
female(isla_phillips).
female(mia_grace_tindall).
female(autumn_kelly).

/* Married couples */
married(queen_elizabeth, prince_philip).
married(prince_philip, queen_elizabeth).
married(prince_charles, camilla_parker_bowles).
married(camilla_parker_bowles, prince_charles).
married(princess_anne, timothy_laurence).
married(timothy_laurence, princess_anne).
married(peter_phillips, autumn_kelly).
married(autumn_kelly, peter_phillips).
married(zara_phillips, mike_tindall).
married(mike_tindall, zara_phillips).
married(prince_william, kate_middleton).
married(kate_middleton, prince_william).
married(sophie_rhys_jones, prince_edward).
married(prince_edward, sophie_rhys_jones).

/* Divorced couples */
divorced(princess_diana, prince_charles).
divorced(prince_charles, princess_diana).
divorced(sarah_ferguson, prince_andrew).
divorced(prince_andrew, sarah_ferguson).
divorced(captain_mark_philips, princess_anne).
divorced(princess_anne, captain_mark_philips).

/* Parent-child relationships */
parent(prince_philip, prince_charles).
parent(prince_philip, princess_anne).
parent(prince_philip, prince_andrew).
parent(prince_philip, prince_edward).
parent(queen_elizabeth, prince_charles).
parent(queen_elizabeth, princess_anne).
parent(queen_elizabeth, prince_andrew).
parent(queen_elizabeth, prince_edward).
parent(prince_charles, prince_william).
parent(prince_charles, prince_harry).
parent(princess_diana, prince_william).
parent(princess_diana, prince_harry).
parent(prince_andrew, princess_beatrice).
parent(prince_andrew, princess_eugenie).
parent(sarah_ferguson, princess_beatrice).
parent(sarah_ferguson, princess_eugenie).
parent(peter_phillips, savannah_phillips).
parent(peter_phillips, isla_phillips).
parent(autumn_kelly, savannah_phillips).
parent(autumn_kelly, isla_phillips).
parent(zara_phillips, mia_grace_tindall).
parent(mike_tindall, mia_grace_tindall).
parent(prince_william, prince_george).
parent(prince_william, princess_charlotte).
parent(kate_middleton, prince_george).
parent(kate_middleton, princess_charlotte).
parent(sophie_rhys_jones, lady_louise_mountbatten_windsor).
parent(sophie_rhys_jones, james_viscount_severn).
parent(prince_edward, lady_louise_mountbatten_windsor).
parent(prince_edward, james_viscount_severn).
parent(captain_mark_philips, peter_phillips).
parent(captain_mark_philips, zara_phillips).
parent(princess_anne, peter_phillips).
parent(princess_anne, zara_phillips).

/* Relationship definitions */
father(Parent,Child) :- parent(Parent,Child), male(Parent).
mother(Parent,Child) :- parent(Parent,Child), female(Parent).

husband(Person, Wife) :- male(Person), married(Person, Wife). 
wife(Person, Husband) :- female(Person), married(Husband, Person). 

child(Child, Parent) :- parent(Parent, Child). 
son(Child, Parent) :- parent(Parent, Child), male(Child). 
daughter(Child, Parent) :- parent(Parent, Child), female(Child). 

grandparent(GP, GC) :- parent(GP, P), parent(P, GC). 
grandfather(GF, GC) :- grandparent(GF, GC), male(GF). 
grandmother(GM, GC) :- grandparent(GM, GC), female(GM). 

grandchild(GC, GP) :- grandparent(GP, GC).
grandson(GS, GP) :- grandchild(GS, GP), male(GS). 
granddaughter(GD, GP) :- grandchild(GD, GP), female(GD). 

sibling(Person1,Person2) :- father(Father, Person1), father(Father, Person2), mother(Mother, Person1), mother(Mother, Person2).
sibling(Person1,Person2) :- sibling(Person2, Person1).
brother(Person,Sibling) :- sibling(Person, Sibling), male(Person).
sister(Person,Sibling) :- sibling(Person, Sibling), female(Person).

/* Aunt is mother's sister or father's sister or uncle's wife
- Uncle in this case can be interpreted as brother of parent
*/
aunt(Person, NieceNephew) :- female(Person), parent(Parent, NieceNephew), sister(Person, Parent).
aunt(Person, NieceNephew) :- female(Person), parent(Parent, NieceNephew), brother(Uncle, Parent), wife(Person, Uncle).

uncle(Person, NieceNephew) :- male(Person), parent(Parent, NieceNephew), brother(Person, Parent).
uncle(Person, NieceNephew) :- male(Person), parent(Parent, NieceNephew), sister(Aunt, Parent), husband(Person, Aunt).

niece(Person, AuntUncle) :- female(Person), aunt(AuntUncle, Person).
niece(Person, AuntUncle) :- female(Person), uncle(AuntUncle, Person).

nephew(Person, AuntUncle) :- male(Person), aunt(AuntUncle, Person).
nephew(Person, AuntUncle) :- male(Person), uncle(AuntUncle, Person).







