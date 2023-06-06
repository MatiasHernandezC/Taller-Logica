from tkinter import *
import os
import pickle

def settearEdad():
    try:
        numeroPassing = int(numeroEdad.get())
        if numeroPassing < 1 or numeroPassing > 99:
            mensaje = Message(raiz, text = "Por favor, ingrese una edad válida entre 1 y 99")
            mensaje.pack()
        else:
            entero = numeroPassing
            with open("edad.pickle", "wb") as archivoEdad:
                pickle.dump(entero, archivoEdad)
            abrirVentanaHS()
    except ValueError:
        # Manejar la excepción
        mensaje_e = Message(raiz, text = "Por favor, ingrese una edad válida entre 1 y 99")
        mensaje_e.pack()
    

def abrirVentanaHS():
    raiz.destroy()
    
    # Obtener la ruta absoluta del archivo de la nueva ventana
    ruta_ventana = os.path.join(os.path.dirname(__file__), "ventanaHS.pyw")
    
    # Abrir la nueva ventana
    os.system("pythonw " + ruta_ventana)

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

numeroEdad = StringVar()

## Pregunta edad
miTitulo = Label(frame, text="Indique su edad:", bg="deep sky blue", font=("Comic Sans MS", 15))
miTitulo.grid(row=0, column=0, pady=10, padx=25)

## Indica edadS
textBoxEdad = Entry(frame, textvariable=numeroEdad)
textBoxEdad.grid(row=0, column=1, pady=10, padx=25)

## Botón Siguiente
botonAbrir = Button(frame, text="Siguiente", font=("Comic Sans MS", 14), bg="SpringGreen2", relief=GROOVE, command=settearEdad)
botonAbrir.grid(row=1, column=0, pady=10, padx=25)

raiz.mainloop()