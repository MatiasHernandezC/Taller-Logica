% Calculo de rango de edad
edad(X, bebe):-
    X < 5.
edad(X, niño):-
    X >= 5,
    X < 11.
edad(X, adolecente):-
    X >= 11,
    X < 18.
edad(X, adulto_joven):-
    X >= 18,
    X < 26.
edad(X, adulto):-
    X >= 26.
% Calculo de maximo screen time
% Screen time:
%  - https://www.osfhealthcare.org/blog/kids-screen-time-how-much-is-too-much/
%  - https://www.verywellfamily.com/the-negative-effects-of-too-much-screen-time-1094877
%  - https://www.reidhealth.org/blog/screen-time-for-adults

max_screen_time(bebe, 0).
max_screen_time(niño, 1).
max_screen_time(adolecente, 2).
max_screen_time(adulto_joven, 5).
max_screen_time(adulto, 6).
% Saludable
estado_screen_time(X, Y, Z) :-
    max_screen_time(X, Max),
    Y < Max,
    Z = 1.
% Poco Saludable
estado_screen_time(X, Y, Z) :-
    max_screen_time(X, Max),
    Y = Max,
    Z = 2.
% No saludable
estado_screen_time(X, Y, Z) :-
    max_screen_time(X, Max),
    Y > Max,
    Z = 3.

% Calculo de min de horas de sueño
% Bebés de 4 a 12 meses 	De 12 a 16 horas por cada 24 horas, incluidas las siestas
% De 1 a 2 años 	        De 11 a 14 horas por cada 24 horas, incluidas las siestas
% De 3 a 5 años 	        De 10 a 13 horas por cada 24 horas, incluidas las siestas
% De 6 a 12 años 	        De 9 a 12 horas por cada 24 horas
% De 13 a 18 años 	        De 8 a 10 horas por cada 24 horas
% Adultos 	                7 horas por noche o más
% https://www.mayoclinic.org/es-es/healthy-lifestyle/adult-health/expert-answers/how-many-hours-of-sleep-are-enough/faq-20057898

horas_sueño_min(bebe, 12).
horas_sueño_min(niño, 10).
horas_sueño_min(adolecente, 9).
horas_sueño_min(adulto_joven, 7).
horas_sueño_min(adulto, 7).
% Saludable
estado_horas_sueño(X, Y, Z) :-
    horas_sueño_min(X, Max),
    Y > Max,
    Z = 1.
% Poco Saludable
estado_horas_sueño(X, Y, Z) :-
    (horas_sueño_min(X, Max),
    Y = Max;
    horas_sueño_min(X, Max),
    Y = Max+1),
    Z = 2.
% No saludable
estado_horas_sueño(X, Y, Z) :-
    horas_sueño_min(X, Max),
    Y < Max+1,
    Z = 3.

% Drogas y alcohol
consume(nada, alcohol, -1).
consume(poco, alcohol, 0).
consume(mucho, alcohol, 1).
consume(demaciado, alcohol, 2).

consume(nada, tabaco, -1).
consume(poco, tabaco, 0).
consume(mucho, tabaco, 1).
consume(demaciado, tabaco, 2).

consume(nada, drogas, 1).
consume(poco, drogas, 2).
consume(mucho, drogas, 2).
consume(demaciado, drogas, 3).
% Asumir que:
%   - 0 - 33: Saludable
%   - 34 - 66: Poco saludable
%   - 67 - 100: No saludable

