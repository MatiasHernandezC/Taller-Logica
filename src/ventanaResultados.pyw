import funciones as f
from tkinter import *
import os

def obtenerResultado():
    if valorResultado <= 1:
        mensaje = "Saludable"
    elif valorResultado > 1 and valorResultado <= 2:
        mensaje = "Poco saludable"
    elif valorResultado > 2:
        mensaje = "Nada saludable"
    return mensaje

def obtenerComentario():
    if valorResultado <= 1:
        mensajeComentario = "Tu estilo de vida es significado de una gran salud mental :)"
    elif valorResultado > 1 and valorResultado <= 2:
        mensajeComentario = "Tu estilo de vida requiere de un ligero cambio :/"
    elif valorResultado > 2:
        mensajeComentario = "Ten cuidado!! Debes cambiar tus malas prácticas con urgencia :("
    return mensajeComentario
        
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

valorResultado = f.calcularEstandarVida()
mensajeFinal = obtenerResultado()
mensajeComentario = obtenerComentario()

## Resultado Final
miTitulo = Label(frame, text="El resultado final es:", bg="deep sky blue", font=("Comic Sans MS", 18))
miTitulo.grid(row=0, column=0, pady=10, padx=25)

## Resultado Final a
miTitulo = Label(frame, text=mensajeFinal, bg="deep sky blue", font=("Comic Sans MS", 18))
miTitulo.grid(row=0, column=1, pady=10, padx=25)

## Comentario
miTitulo = Label(frame, text=mensajeComentario, bg="deep sky blue", font=("Comic Sans MS", 15))
miTitulo.grid(row=1, column=0, pady=10, padx=25)

## Botón Siguiente
botonAbrir = Button(frame, text="Volver al menú", font=("Comic Sans MS", 14), bg="LightGoldenrod1", relief=GROOVE, command=volverMenu)
botonAbrir.grid(row=2, column=0, pady=20, padx=25)

## Botón Siguiente
botonAbrir = Button(frame, text="Salir", font=("Comic Sans MS", 14), bg="SpringGreen2", relief=GROOVE, command=salirAplicacion)
botonAbrir.grid(row=2, column=1, pady=20, padx=25)

raiz.mainloop()