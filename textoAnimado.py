#Importa módulos para Interfaz Gráfica de usuario (tkinter)
import multiprocessing as mp
import tkinter as tk
from tkinter import ttk
import time

#Crea la ventana principal
main_window = tk.Tk()
main_window.title("Ejemplo")
main_window.configure(width=350, height=200)

#Función que crea y posiciona el botón "Salir"
def opcionFinalizar():
    boton = ttk.Button(main_window, text="Salir", command=main_window.destroy)
    boton.place(x=170, y=170)

#Función que crea una etiqueta (label) de texto en la posición (x,y) de la pantalla.
def createLabel(a,b):
    label = ttk.Label(text="")
    label.place(x=a,y=b)
    return label

def animarLinea(char,q):
    texto = ""
    retardo: float=0.25
    for i in range(0,35):
        time.sleep(retardo)
        texto += char
        q.put([char, texto])

#Función que crea una etiqueta (llamando a createLabel()) y luego anima texto dentro de la misma.
def animar(txt, lbl):
    lbl.config(text = txt)
    main_window.update_idletasks()
    main_window.update()

#Ejecuta tres animaciones
if __name__ == "__main__":
    q = mp.Queue()
    lblX = createLabel(10,10)
    lblY = createLabel(10,30)
    lblZ = createLabel(10,50)
    animX = mp.Process(target=animarLinea, args=('X',q,))
    animY = mp.Process(target=animarLinea, args=('Y',q,))
    animZ = mp.Process(target=animarLinea, args=('Z',q,))
    animX.start()
    animY.start()
    animZ.start()
    # Coloca la opcion "Salir"
    opcionFinalizar()
    while(animX.is_alive() or animY.is_alive() or animZ.is_alive()):
        ret = q.get()
        if ret[0] == 'X':
            animar(ret[1], lblX)
        if ret[0] == 'Y':
            animar(ret[1], lblY)
        if ret[0] == 'Z':
            animar(ret[1], lblZ)
    # Bucle principal de la ventana
    main_window.mainloop()
