import funciones as f
from tkinter import *
import os

### HANDLERS ###

def abrirVentanaEdad():
    raiz.destroy()
    
    # Obtener la ruta absoluta del archivo de la nueva ventana
    ruta_ventana = os.path.join(os.path.dirname(__file__), "ventanaEdad.pyw")
    
    # Abrir la nueva ventana
    os.system("pythonw " + ruta_ventana)

def salirAplicacion():
    raiz.destroy()

### INTERFACE ###

raiz = Tk()
raiz.resizable(0,0)
raiz.title("Test de Salud Mental")
raiz.geometry("600x400")

## Frame interno
frame = Frame(raiz)
frame.pack(fill="both", expand="True")
frame.config(bg="deep sky blue")
frame.config(width="600", height="400")
frame.config(bd=35)
frame.config(relief="groove")

## Título
miTitulo = Label(frame, text="Test de Salud Mental", bg="deep sky blue", font=("Comic Sans MS", 20))
miTitulo.grid(row=0, column=1, pady=30, padx=50)

## Botón Empezar test
botonAbrir = Button(frame, text="Comenzar test", font=("Comic Sans MS", 14), bg="SpringGreen2", relief=GROOVE, command=abrirVentanaEdad)
botonAbrir.grid(row=1, column=0, pady=10, padx=25)

## Botón Salir
botonAbrir = Button(frame, text="Salir", font=("Comic Sans MS", 14), bg="OrangeRed2", relief=GROOVE, command=salirAplicacion)
botonAbrir.grid(row=1, column=2, pady=10, padx=25)

raiz.mainloop()



