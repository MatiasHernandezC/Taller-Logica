from tkinter import *
import os
import pickle

def settearA():
    opcion = frecuenciaAlcohol.get()
    if opcion == 0:
        varString = "nada"
    elif opcion == 1:
        varString = "poco"
    elif opcion == 2:
        varString = "mucho"
    elif opcion == 3:
        varString = "demasiado"
    lista = [varString]
    with open("lista.pickle", "wb") as archivoLista:
        pickle.dump(lista, archivoLista)
    abrirVentanaTabaco()
    

def abrirVentanaTabaco():
    raiz.destroy()
    
    # Obtener la ruta absoluta del archivo de la nueva ventana
    ruta_ventana = os.path.join(os.path.dirname(__file__), "ventanaTabaco.pyw")
    
    # Abrir la nueva ventana
    os.system("python3 " + ruta_ventana)

### INTERFACE ###

raiz = Tk()
raiz.resizable(0,0)
raiz.title("Test de Salud Mental")
raiz.geometry("800x600")

## Frame interno
frame = Frame(raiz)
frame.pack(fill="both", expand="True")
frame.config(bg="deep sky blue")
frame.config(width="800", height="600")
frame.config(bd=35)
frame.config(relief="groove")

frecuenciaAlcohol = IntVar()
frecuenciaAlcohol.set(-1)

## Pregunta horas de sueño
miTitulo = Label(frame, text="¿Cuánto alcohol consumes?", bg="deep sky blue", font=("Comic Sans MS", 18))
miTitulo.grid(row=0, column=0, pady=10, padx=25)

Radiobutton(frame, text="Nada", bg="deep sky blue", font=("Comic Sans MS", 15), variable=frecuenciaAlcohol, value=0).grid(row=1, column=0, pady = 10, padx = 25)
Radiobutton(frame, text="Poco", bg="deep sky blue", font=("Comic Sans MS", 15), variable=frecuenciaAlcohol, value=1).grid(row=2, column=0, pady = 10, padx = 25)
Radiobutton(frame, text="Mucho", bg="deep sky blue", font=("Comic Sans MS", 15), variable=frecuenciaAlcohol, value=2).grid(row=3, column=0, pady = 10, padx = 25)
Radiobutton(frame, text="Demasiado", bg="deep sky blue", font=("Comic Sans MS", 15), variable=frecuenciaAlcohol, value=3).grid(row=4, column=0, pady = 10, padx = 25)

## Botón Siguiente
botonAbrir = Button(frame, text="Siguiente", font=("Comic Sans MS", 14), bg="SpringGreen2", relief=GROOVE, command=settearA)
botonAbrir.grid(row=5, column=0, pady=20, padx=25)

raiz.mainloop()