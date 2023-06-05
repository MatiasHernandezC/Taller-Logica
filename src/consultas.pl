
% 
% 
% 
% Screen time:
%  - https://www.osfhealthcare.org/blog/kids-screen-time-how-much-is-too-much/
%  - https://www.verywellfamily.com/the-negative-effects-of-too-much-screen-time-1094877
%  - https://www.reidhealth.org/blog/screen-time-for-adults

max_screen_time(bebe, 0).
max_screen_time(niño, 1).
max_screen_time(pre_adolecente, 2).
max_screen_time(adolecente, 2).
max_screen_time(adulto, 6).

menor_max_bebe(Number) :-
    max_screen_time(bebe, Max),
    Number =< Max.
menor_max_niño(Number) :-
    max_screen_time(niño, Max),
    Number =< Max.
menor_max_pre_adolecente(Number) :-
    max_screen_time(pre_adolecente, Max),
    Number =< Max.
menor_max_adolecente(Number) :-
    max_screen_time(adolecente, Max),
    Number =< Max.
menor_max_adulto(Number) :-
    max_screen_time(adulto, Max),
    Number =< Max.

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
saludable(X) :-
    X =< 33.

poco_saludable(X) :-
    X > 34,
    X =< 67.

no_saludable(X) :-
    X > 67,
    X =< 100.

