import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random  
import os  
import sys 
from PIL import Image, ImageTk


#----------------------------------------------------------------------------------------------------------------------------
def obtener_ruta_recurso(rel_path):
    try:
        base_path = sys._MEIPASS 
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__)) 
    return os.path.join(base_path, rel_path)

def agregar():
    nueva_opcion = impt_opcion.get().strip()
    if nueva_opcion:
        if nueva_opcion in opciones:
            messagebox.showwarning("Repetido", "ya ingresaste esa opción")
            return
        opciones.append(nueva_opcion)
        impt_opcion.delete(0, tk.END)
        lista_opciones.insert(tk.END, f" • {nueva_opcion}")
    else: 
        messagebox.showwarning("fijate", "No escribiste nada")


def resultado():
    if opciones:  
        elegido = random.choice(opciones)
        messagebox.showinfo("Resultado", f"{elegido}")
    else:
        messagebox.showwarning("Lista vacía", "No hay elementos para elegir")


def limpiar_lista():
    respuesta = messagebox.askyesno("Cuidado", "¿Querés borrar toda la lista?")
    if respuesta:
        opciones.clear()
        lista_opciones.delete(0, tk.END) 

#----------------------------------------------------------------------------------------------------------------------------


ventana = tk.Tk()               
ventana.title("aleatorizador")   
ventana.geometry("410x600")      


ruta_imagen = obtener_ruta_recurso(os.path.join("image.jpg"))
fondo_img = Image.open(ruta_imagen)  
fondo_tk = ImageTk.PhotoImage(fondo_img)
fondo_label = tk.Label(ventana, image=fondo_tk)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1) 


encabezado_font = ("verdana", 25, "bold")
texto_font = ("verdana", 12)
boton_font = ("verdana", 10, "bold")
#----------------------------------------------------------------------------------------------------------------------------


encabezado = tk.Label(ventana, text = "Aleatorizador", font=encabezado_font, bg="#8898E6", fg="#CE4C66", )  
encabezado.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew") 

descripcion = tk.Label(ventana, text = "Carga de a una en el cuadro de texto las opciones entre las que quieras decidir", font=texto_font, bg="#ecd8f0", borderwidth=1, fg="#CE4C66", wraplength=400, justify="center")
descripcion.grid(row=1, column=0, columnspan=3, pady=20, padx=10, sticky="ew")


impt_opcion = tk.Entry(ventana, bg="#ecd8f0", fg="#865370", font=texto_font, bd=2, relief="groove", highlightthickness=0, borderwidth=1, highlightcolor="#c47bb4")
impt_opcion.grid(row=2, column=0, pady=10)
impt_opcion.bind("<Return>", lambda event: agregar()) 

boton_borrar = tk.Button(ventana, text="   🗑️",  bd=1, activebackground="#8898E6", activeforeground="#c47bb4", command=limpiar_lista,  bg="#c47bb4", fg="#ecd8f0", font=("verdana", 10))
boton_borrar.grid(row=2, column=2, padx=10 )
boton_borrar.config(cursor="hand2")


ayuda = tk.Label(ventana, text = "(presiona enter para cargar los elementos)", font=("verdana", 10), bg="#c47bb4", fg="#865370", justify="center")
ayuda.grid(row=3, column=0, columnspan=3, padx=10, sticky="ew")


lista_opciones = tk.Listbox(ventana, height=10, font=("verdana", 14), fg="#865370", bg="#8898E6", borderwidth=1, highlightthickness=0 )
lista_opciones.grid(row=4, column=0, columnspan=3, pady=20, padx=20, sticky="ew") 


boton_aleatorizar = tk.Button(ventana, text="Elegir", command=resultado, fg="#ecd8f0", bg="#c47bb4", activebackground="#8898E6", activeforeground="#c47bb4", font=("verdana", 14, "bold"))
boton_aleatorizar.grid(row=5, column=0, columnspan=3, pady=10, padx=20, sticky="ew")
boton_aleatorizar.config(cursor="hand2", width=20)


#----------------------------------------------------------------------------------------------------------------------------


opciones = []  

ventana.grid_columnconfigure(0, weight=1) 
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)


ventana.mainloop() 
