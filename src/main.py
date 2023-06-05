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

def estado_salud(num, prolog):
    if(bool(list(prolog.query("saludable("+str(num)+")")))):
        # 0 = saludable
        return 0
    elif(bool(list(prolog.query("poco_saludable("+str(num)+")")))):
        # 1 = poco saludable
        return 1
    elif(bool(list(prolog.query("no_saludable("+str(num)+")")))):
        # 2 = no saludable
        return 2
    else:
        # fuera de rango
        return -1

def main():
    # Crea una instancia de Prolog
    prolog = Prolog()

    # Carga el archivo consultas.pl
    prolog.consult("src/consultas.pl")

    # Realizar consultas
    entrada = input("Inserte sus horas: ")
    entrada2 = input("Inserte su edad: ")
    consulta2 = "edad("+str(entrada2)+",Edad)"
    soluciones = list(prolog.query(consulta2))
    edad = soluciones[0]['Edad']
    consulta = "estado_screen_time(" + str(edad) + "," + str(entrada) + ", Z)"
    # Consultar y obtener el valor de retorno
    soluciones = list(prolog.query(consulta))
    if soluciones:
        Z = soluciones[0]['Z']
        print("El valor de Z es:", Z)
    else:
        print("No se encontró una solución para la consulta.")
    
if __name__ == "__main__":
    main()