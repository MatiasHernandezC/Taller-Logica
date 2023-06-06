import funciones as f
from tkinter import *
import os

#def obtenerResultado():
    
    

def volverMenu():
    raiz.destroy()
    
    # Obtener la ruta absoluta del archivo de la nueva ventana
    ruta_ventana = os.path.join(os.path.dirname(__file__), "main.pyw")
    
    # Abrir la nueva ventana
    os.system("pythonw " + ruta_ventana)

def salirAplicacion():
    raiz.destroy()

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

valorResultado = 2

## Pregunta horas de sueño
miTitulo = Label(frame, text="¿Cuánta actividad fisica realizas?", bg="deep sky blue", font=("Comic Sans MS", 18))
miTitulo.grid(row=0, column=0, pady=10, padx=25)

## Botón Siguiente
botonAbrir = Button(frame, text="Volver al menú", font=("Comic Sans MS", 14), bg="LightGoldenrod1", relief=GROOVE, command=volverMenu)
botonAbrir.grid(row=5, column=0, pady=20, padx=25)

## Botón Siguiente
botonAbrir = Button(frame, text="Salir", font=("Comic Sans MS", 14), bg="SpringGreen2", relief=GROOVE, command=salirAplicacion)
botonAbrir.grid(row=5, column=0, pady=20, padx=25)

raiz.mainloop()