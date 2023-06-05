%
consult('hechos.pl').

% Asumir que:
%   - 0 - 33: Saludable
%   - 34 - 66: Poco saludable
%   - 67 - 100: No saludable
saludable(X) :-
    X =< 33.

poco_saludable(X) :-
    X > 34,
    X =< 67.

no_saludable(X) :-
    X > 67,
    X =< 100.

