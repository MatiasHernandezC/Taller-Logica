% 
% 
% 
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

%
%
% 
% https://www.mayoclinic.org/es-es/healthy-lifestyle/adult-health/expert-answers/how-many-hours-of-sleep-are-enough/faq-20057898
horas_sueño(pocas).
horas_sueño(decentes).
horas_sueño(buenas).
horas_sueño(excelentes).

horas_sueño(X, pocas) :-
    X >= 0,
    X < 5.
horas_sueño(X, decentes) :-
    X >= 5,
    X < 6.
horas_sueño(X, buenas) :-
    X >= 6,
    X < 9.
horas_sueño(X, excelentes) :-
    X >= 9,
    X =< 12.
% Asumir que:
%   - 0 - 33: Saludable
%   - 34 - 66: Poco saludable
%   - 67 - 100: No saludable

