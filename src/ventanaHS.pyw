from tkinter import *
import os
import pickle

def settearHS():
    try:
        numeroPassing = int(numeroHorasSueno.get())
        if numeroPassing < 0 or numeroPassing > 24:
            mensaje = Message(raiz, text = "Por favor, ingrese un valor válido entre 0 y 24")
            mensaje.pack()
        else:
            entero = numeroPassing
            with open("hs.pickle", "wb") as archivoHS:
                pickle.dump(entero, archivoHS)
            abrirVentanaST()
    except ValueError:
        # Manejar la excepción
        mensaje_e = Message(raiz, text = "Por favor, ingrese una edad válida entre 0 y 24")
        mensaje_e.pack()
    

def abrirVentanaST():
    raiz.destroy()
    
    # Obtener la ruta absoluta del archivo de la nueva ventana
    ruta_ventana = os.path.join(os.path.dirname(__file__), "ventanaST.pyw")
    
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

numeroHorasSueno = StringVar()

## Pregunta horas de sueño
miTitulo = Label(frame, text="Indique horas de sueño promedio:", bg="deep sky blue", font=("Comic Sans MS", 15))
miTitulo.grid(row=0, column=0, pady=10, padx=25)

## Indica horas de sueño
textBoxHS = Entry(frame, textvariable=numeroHorasSueno)
textBoxHS.grid(row=0, column=1, pady=10)

## Botón Siguiente
botonAbrir = Button(frame, text="Siguiente", font=("Comic Sans MS", 14), bg="SpringGreen2", relief=GROOVE, command=settearHS)
botonAbrir.grid(row=1, column=0, pady=10, padx=25)

raiz.mainloop()