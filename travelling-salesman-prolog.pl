% tsp.pl
% Simple exhaustive TSP for a small set of cities (symmetric distances)

% ----------- Distances (facts) -------------
distance(delhi, mumbai, 1400).
distance(delhi, kolkata, 1500).
distance(delhi, chennai, 2200).
distance(mumbai, kolkata, 2000).
distance(mumbai, chennai, 1300).
distance(kolkata, chennai, 1650).

% Make distances bidirectional (symmetric)
path(X, Y, D) :- distance(X, Y, D).
path(X, Y, D) :- distance(Y, X, D).

% ----------- Utility: total distance of a route -------------
% total_distance(ListOfCitiesIncludingReturn, TotalDistance)
total_distance([_], 0).  % single node -> 0 distance
total_distance([A,B|Rest], Total) :-
    path(A, B, D1),
    total_distance([B|Rest], D2),
    Total is D1 + D2.

% ----------- List of cities in problem -------------
cities([delhi, mumbai, kolkata, chennai]).

% ----------- TSP Main: find shortest cycle starting and ending at Start -------------
% tsp(Start, BestFullPath, MinDistance).
tsp(Start, BestFullPath, MinDistance) :-
    cities(Cities),
    % ensure Start is one of the cities
    member(Start, Cities),
    % remove Start from city list to permute the remaining cities
    select(Start, Cities, Others),
    % collect all complete cycles (Start + permutation + Start) with their distances
    findall(Dist-FullPath,
            ( permutation(Others, Perm),               % all permutations of the other cities
              append([Start|Perm], [Start], FullPath),% make cycle: Start...Start
              total_distance(FullPath, Dist)
            ),
            Pairs),
    % sort by distance (key) and pick minimum
    keysort(Pairs, Sorted),
    Sorted = [MinDistance-BestFullPath | _].
