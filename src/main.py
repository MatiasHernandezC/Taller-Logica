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
    # Crear instancia de Prolog
    prolog = Prolog()

    # Cargar archivo Prolog
    prolog.consult("src/consultas.pl")

    # Realizar consultas
    entrada = input("Inserte sus horas: ")
    entrada2 = input()
    print("Su estado de salud es: ", bool(list(prolog.query("menor_max_"+str(entrada2)+"("+str(entrada)+")"))))
if __name__ == "__main__":
    main()