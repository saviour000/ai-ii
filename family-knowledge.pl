% Facts about family relationships
parent(john, mary).
parent(john, steve).
parent(mary, alice).
parent(mary, bob).
parent(alice, carol).
parent(alice, david).
parent(bob, emily).
parent(bob, frank).

% Rules to derive additional relationships
grandparent(GP, GC) :-
    parent(GP, Parent),
    parent(Parent, GC).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y), 
    X \= Y.

brother(X, Y) :-
    male(X),
    sibling(X, Y).

sister(X, Y) :-
    female(X),
    sibling(X, Y).

uncle(Uncle, NieceNephew) :-
    brother(Uncle, Parent),
    parent(Parent, NieceNephew).

aunt(Aunt, NieceNephew) :-
    sister(Aunt, Parent),
    parent(Parent, NieceNephew).

% Define genders
male(john).
male(steve).
male(bob).
male(carol).
male(david).
male(frank).

female(mary).
female(alice).
female(emily).

% Example queries:
% ?- grandparent(GP, emily).
% ?- uncle(Uncle, carol).
% ?- aunt(Aunt, david).


% Extended family tree
parent(a,b).
parent(a,c).
parent(b,d).
parent(b,e).
parent(d,f).
parent(d,g).
parent(c,h).
parent(c,i).
parent(i,j).
parent(i,k).

male(a).
male(b).
male(e).
male(f).
male(g).
male(h).
male(i).
male(k).

female(c).
female(d).
female(j).
