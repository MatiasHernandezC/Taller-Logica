# Taller 1 Logica:
# "Aplicación LPO para sugerir el grado de Salud del Cerebro"
# 
# Integrantes:
# - Wladimir Duran
# - Ariel Nuñez
# - Matías Hernández
#
# Autores recomendados:
#- Bueno D. (2019) Neurociencia Aplicada a la Educación. Síntesis.
#- Céspedes A. (2014) Tu Cerebro. Penguin Random House Grupo Editorial Chile.
#- Céspedes A. (2007) Deficit Atencional. EDIC. B.
#- Carr N. (2010) ¿Qué está haciendo Internet con nuestras mentes? Superficiales. Taurus.
#- Mora F. (2021) NEUROEDUCACIÓN. ALIANZA EDITORIAL

from pyswip import Prolog

### VARIABLES GLOBALES ###
""" horasSueno = -1
screenTime = -1
edad = -1
listaEstupefacientes = []
actividadFisica = "" """

### FIN VARIABLES GLOBALES ###

# Entradas: entrada = hrs que esta frente a una pantalla, entrada2 = edad, consultas prolog
# Salida:   Int Nivel de saludable (1: saludable, 2: poco saludable, 3 o mas: no saludable)
# Objetivo: Obtener que tan saludable esta tu cerebro por tus horas de sueño y tu edad
def saludable_edad_screentime(entrada, entrada2, prolog):
    # Realizar consultas
    consulta2 = "edad("+str(entrada2)+",Edad)"
    soluciones = list(prolog.query(consulta2))
    edad = soluciones[0]['Edad']
    consulta = "estado_screen_time(" + str(edad) + "," + str(entrada) + ", Z)"
    # Consultar y obtener el valor de retorno
    soluciones = list(prolog.query(consulta))
    if soluciones:
        Z = soluciones[0]['Z']
        return Z
    else:
        return 0

# Entradas: entrada = hrs que duerme, entrada2 = edad, consultas prolog
# Salida:   Int Nivel de saludable (1: saludable, 2: poco saludable, 3 o mas: no saludable)
# Objetivo: Obtener que tan saludable esta tu cerebro por tus horas de sueño y tu edad
def saludable_edad_hrs_sueno(entrada, entrada2, prolog):
    # Realizar consultas
    consulta2 = "edad("+str(entrada2)+",Edad)"
    soluciones = list(prolog.query(consulta2))
    edad = soluciones[0]['Edad']
    consulta = "estado_horas_sueño(" + str(edad) + "," + str(entrada) + ", Z)"
    # Consultar y obtener el valor de retorno
    soluciones = list(prolog.query(consulta))
    if soluciones:
        Z = soluciones[0]['Z']
        return Z
    else:
        return 0

# Entradas: Lista cant consumo con orden [alcohol,tabaco,drogas], consultas prolog
# Salida:   Int Nivel de saludable (1: saludable, 2: poco saludable, 3 o mas: no saludable)
# Objetivo: Obtener que tan saludable esta tu cerebro por tu consumo de drogas
def saludable_consumo_estupefacientes(entrada, prolog):
    # Realizar consultas
    consultaLista = "consume(_, X, _)"
    listaDrogas = list(prolog.query(consultaLista))
    listaAux = []
    for x in listaDrogas:
        listaAux.append(x['X'])
    unique_aux= []
    for x in listaAux:
        if x not in unique_aux:
            unique_aux.append(x)
    consulta = "consumo_estupefacientes(["
    i=0
    for x in entrada:
        if(i != 2):
            consulta = consulta + str(x) + ","
        else:
            consulta = consulta + str(x)
        i=i+1
    consulta = consulta + "],["
    i=0
    for x in unique_aux:
        if(i != 2):
            consulta = consulta + str(x) + ","
        else:
            consulta = consulta + str(x)
        i=i+1
    consulta = consulta + "],Z)"
    soluciones = list(prolog.query(consulta))
    if soluciones:
        Z = soluciones[0]['Z']
        cont = 1
        for x in Z:
            if(x == '0' or x == '1' or x == '2' or x == '3'):
                cont = cont + int(x)
        return cont
    else:
        return 0

# Entradas: entrada = cant actividad fisica (poco, normal, mucho), entrada2 = edad, consultas prolog
# Salida:   Int Nivel de saludable (1: saludable, 2: poco saludable, 3 o mas: no saludable)
# Objetivo: Obtener que tan saludable esta tu cerebro por cant de actividad fisica
def saludable_actividad_fisica(entrada, entrada2, prolog):
    # Realizar consultas
    consulta2 = "edad("+str(entrada2)+",Edad)"
    soluciones = list(prolog.query(consulta2))
    edad = soluciones[0]['Edad']
    consulta = "actividad_fisica(" + str(edad) + "," + str(entrada) + ", Z)"
    # Consultar y obtener el valor de retorno
    soluciones = list(prolog.query(consulta))
    if soluciones:
        Z = soluciones[0]['Z']
        return Z
    else:
        return 0

def calcularEstandarVida(edad, horasSueno, screenTime, listaEstupefacientes, actividadFisica):
    # Crea una instancia de Prolog
    prolog = Prolog()

    # Carga el archivo consultas.pl
    prolog.consult("src/consultas.pl")

    # Consultamos
    z1 = saludable_edad_screentime(screenTime, edad, prolog)
    z2 = saludable_edad_hrs_sueno(horasSueno, edad, prolog)
    z3 = saludable_consumo_estupefacientes(listaEstupefacientes, prolog)
    z4 = saludable_actividad_fisica(actividadFisica, edad, prolog)
    prom = (z1 + z2 + z3 + z4)/4

    return prom