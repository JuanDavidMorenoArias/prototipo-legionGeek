import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
class ProponerFrame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent,width=995, height=525, background='#fafdfb',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Crear el título y colocarlo arriba
        titulo = tk.Label(self, text="Proponer Idea", font=("Arial", 20, "bold"))
        titulo.grid(row=0, column=0, pady=20)  # Espaciado arriba y abajo

        # Crear el cuadro de texto más grande
        entrada = tk.Entry(self, font=("Arial", 16), width=40)  # Fuente más grande y más ancho
        entrada.grid(row=1, column=0, pady=10)  # Espacio abajo
        ideas=[]
        # Función para manejar el botón
        def enviar_idea():
            idea = entrada.get()
            if idea.strip():
                with open("ideas.txt", "a") as f:
                    f.write(idea + "\n")  # Guardar en el archivo
                entrada.delete(0, tk.END)
                messagebox.showinfo("Éxito", "¡Tu idea ha sido enviada correctamente")
            else:
                messagebox.showwarning("Advertencia", "El campo no puede estar vacío.")
        # Crear botón de enviar
        boton_enviar = tk.Button(self, text="Enviar", font=("Arial", 14), command=enviar_idea)
        boton_enviar.grid(row=2, column=0, pady=20)  # Espaciado abajo