from tkinter import *
import os
import pickle

def settearST():
    try:
        numeroPassing = int(numeroST.get())
        if numeroPassing < 0 or numeroPassing > 24:
            mensaje = Message(raiz, text = "Por favor, ingrese una edad válida entre 0 y 24")
            mensaje.pack()
        else:
            entero = numeroPassing
            with open("st.pickle", "wb") as archivoST:
                pickle.dump(entero, archivoST)
            abrirVentanaAlcohol()
    except ValueError:
        # Manejar la excepción
        mensaje_e = Message(raiz, text = "Por favor, ingrese una edad válida entre 0 y 24")
        mensaje_e.pack()
    

def abrirVentanaAlcohol():
    raiz.destroy()
    
    # Obtener la ruta absoluta del archivo de la nueva ventana
    ruta_ventana = os.path.join(os.path.dirname(__file__), "ventanaAlcohol.pyw")
    
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

numeroST = StringVar()

## Pregunta horas de sueño
miTitulo = Label(frame, text="¿Cuántas horas pasas frente a una pantalla?:", bg="deep sky blue", font=("Comic Sans MS", 15))
miTitulo.grid(row=0, column=0, pady=10, padx=25)

## Indica horas de sueño
textBoxHS = Entry(frame, textvariable=numeroST)
textBoxHS.grid(row=0, column=1, pady=10)

## Botón Siguiente
botonAbrir = Button(frame, text="Siguiente", font=("Comic Sans MS", 14), bg="SpringGreen2", relief=GROOVE, command=settearST)
botonAbrir.grid(row=1, column=0, pady=10, padx=25)

raiz.mainloop()