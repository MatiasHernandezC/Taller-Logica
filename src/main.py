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

def estado_salud(Num, prolog):
    print(Num)
    if(bool(list(prolog.query("saludable("+str(Num)+")")))):
        # 0 = saludable
        return 0
    elif(bool(list(prolog.query("poco_saludable("+str(Num)+")")))):
        # 1 = poco saludable
        return 1
    elif(bool(list(prolog.query("no_saludable("+str(Num)+")")))):
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
    entrada = input("Inserte su estado de salud (0-100): ")
    print("Su estado de salud es: ", estado_salud(entrada, prolog))

if __name__ == "__main__":
    main()