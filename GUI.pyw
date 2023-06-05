from tkinter import *
import os

def crearDegradeBG(raiz, color1, color2):
    canvas = Canvas(raiz, width=800, height=600)
    canvas.place(x=0, y=0)

    for y in range(600):
        r = int(color1[0] + (color2[0] - color1[0]) * y / 600)
        g = int(color1[1] + (color2[1] - color1[1]) * y / 600)
        b = int(color1[2] + (color2[2] - color1[2]) * y / 600)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, y, 800, y, fill=color, width=1)

def abrirNuevaVentana():
    raiz.destroy()
    
    # Obtener la ruta absoluta del archivo de la nueva ventana
    ruta_ventana = os.path.join(os.path.dirname(__file__), "src/nueva_v entana.pyw")
    
    # Abrir la nueva ventana
    os.system("pythonw " + ruta_ventana)

raiz = Tk()
raiz.title("Test de Salud Mental")
raiz.geometry("800x600")

# Color de inicio y final del degradado
colorInicio = (255, 255, 255)  # Blanco
colorFinal = (0, 0, 255)    # Azul

crearDegradeBG(raiz, colorInicio, colorFinal)

botonAbrir = Button(raiz, text="Abrir nueva ventana", command=abrirNuevaVentana)
botonAbrir.grid(row=1, pady=10)

raiz.mainloop()


