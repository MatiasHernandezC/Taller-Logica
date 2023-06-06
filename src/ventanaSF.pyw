from tkinter import *
import os
import pickle

def settearSF():
    opcion = cantidadSF.get()
    if opcion == 0:
        varString = "poco"
    elif opcion == 1:
        varString = "normal"
    elif opcion == 2:
        varString = "mucho"
    cadena = varString
    with open("cadena.pickle", "wb") as archivoSF:
        pickle.dump(cadena, archivoSF)
    abrirVentanaResultados()
    

def abrirVentanaResultados():
    raiz.destroy()
    
    # Obtener la ruta absoluta del archivo de la nueva ventana
    ruta_ventana = os.path.join(os.path.dirname(__file__), "ventanaResultados.pyw")
    
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

cantidadSF = IntVar()
cantidadSF.set(-1)

## Pregunta horas de sueño
miTitulo = Label(frame, text="¿Cuánta actividad fisica realizas?", bg="deep sky blue", font=("Comic Sans MS", 18))
miTitulo.grid(row=0, column=0, pady=10, padx=25)

Radiobutton(frame, text="Poca", bg="deep sky blue", font=("Comic Sans MS", 15), variable=cantidadSF, value=0).grid(row=1, column=0, pady = 10, padx = 25)
Radiobutton(frame, text="Normal", bg="deep sky blue", font=("Comic Sans MS", 15), variable=cantidadSF, value=1).grid(row=2, column=0, pady = 10, padx = 25)
Radiobutton(frame, text="Mucha", bg="deep sky blue", font=("Comic Sans MS", 15), variable=cantidadSF, value=2).grid(row=3, column=0, pady = 10, padx = 25)

## Botón Siguiente
botonAbrir = Button(frame, text="Ver resultados", font=("Comic Sans MS", 14), bg="SpringGreen2", relief=GROOVE, command=settearSF)
botonAbrir.grid(row=4, column=0, pady=20, padx=25)

raiz.mainloop()