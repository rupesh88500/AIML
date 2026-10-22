% FACTS
parent(john, bob).
parent(john, lisa).
male(john).
male(bob).
female(lisa).

% RULES
father(F, C) :- parent(F, C), male(F).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
