weight(sword, 5).

weight(potion, 2).

weight(shield, 4).

weight(gold, 6).

weight(chest, 15).

inventory([sword, potion]).

can_carry(Item) :-
    weight(Item,W),
    W =< 8.
