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
% -------------------------------------------------------------------------
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
    (Y = Max;Y = Max+1),
    Z = 2.
% No saludable
estado_screen_time(X, Y, Z) :-
    max_screen_time(X, Max),
    Y > Max,
    Z = 3.
% -------------------------------------------------------------------------
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
% Calculo de saludabilidad ((1: saludable, 2: poco saludable, 3 o mas: no saludable))
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
% -------------------------------------------------------------------------
% Drogas y alcohol
consume(nada, alcohol, 0).
consume(poco, alcohol, 0).
consume(mucho, alcohol, 1).
consume(demasiado, alcohol, 3).

consume(nada, tabaco, 0).
consume(poco, tabaco, 1).
consume(mucho, tabaco, 2).
consume(demasiado, tabaco, 2).

consume(nada, drogas, 0).
consume(poco, drogas, 1).
consume(mucho, drogas, 2).
consume(demasiado, drogas, 3).

% Calculo de saludabilidad ((1: saludable, 2: poco saludable, 3 o mas: no saludable))
consumo_estupefacientes([], [], 0).
consumo_estupefacientes([H1|T1], [H2|T2], Z) :-
    consume(H1, H2, Cont),
    consumo_estupefacientes(T1, T2, Z1),
    Z = Z1 + Cont.
% -------------------------------------------------------------------------
% Actividad fisica
% https://www.who.int/es/news/item/25-11-2020-every-move-counts-towards-better-health-says-who
% Las nuevas directrices recomiendan por lo menos de 150 a 300 minutos de 
% actividad física aeróbica de intensidad moderada o vigorosa por semana 
% para todos los adultos, incluidas las personas que viven con afecciones 
% crónicas o discapacidad, y un promedio de 60 minutos al día para los niños 
% y adolescentes.
%
% https://www.unicef.org/uruguay/media/2276/file/La%20actividad%20f%C3%ADsica%20en%20ni%C3%B1os,%20ni%C3%B1as%20y%20adolescentes.pdf
% 0 a 2 año: 0 de actividad física de intensidad moderada a vigorosa
% 2 a 4 años: 60 minutos son de actividad física de intensidad moderada a vigorosa repartidas en el dia
% 5 y 17 años: 60 minutos de actividad física de intensidad moderada a vigorosa diariamente.

actividad_fisica(bebe, poco, 2).
actividad_fisica(bebe, normal, 1).
actividad_fisica(bebe, mucho, 2).

actividad_fisica(niño, poco, 2).
actividad_fisica(niño, normal, 1).
actividad_fisica(niño, mucho, 1).

actividad_fisica(adolecente, poco, 3).
actividad_fisica(adolecente, normal, 2).
actividad_fisica(adolecente, mucho, 1).

actividad_fisica(adulto_joven, poco, 3).
actividad_fisica(adulto_joven, normal, 2).
actividad_fisica(adulto_joven, mucho, 1).

actividad_fisica(adulto, poco, 3).
actividad_fisica(adulto, normal, 2).
actividad_fisica(adulto, mucho, 1).
