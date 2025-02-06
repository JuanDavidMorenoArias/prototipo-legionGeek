import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from idea import Idea
import utils

class ProponerFrame(tk.Frame):
    def __init__(self,parent, user):
        super().__init__(parent,width=995, height=525, background='#fafdfb',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent
        self.user = user
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()


    def create_widgets(self):
        # Crear el título y colocarlo arriba
        titulo = tk.Label(self, text="Proponer Idea", font=("Trebuchet MS", 20, "bold"))
        titulo.grid(row=0, column=0, pady=20)  # Espaciado arriba y abajo

        # Crear el cuadro de texto más grande
        self.entrada = tk.Entry(self, font=("Trebuchet MS", 16), width=40)  # Fuente más grande y más ancho
        self.entrada.grid(row=1, column=0, pady=10)  # Espacio abajo

        # Crear botón de enviar
        boton_enviar = tk.Button(self, text="Enviar", font=("Trebuchet MS", 14), command=self.enviar_idea)
        boton_enviar.grid(row=2, column=0, pady=20)  # Espaciado abajo


        # Función para manejar el botón
    def enviar_idea(self):

        idea_text = self.entrada.get()
        if idea_text.strip():

            # Agregar la idea al archivo json con las ideas
            new_idea = Idea(description=idea_text, sender=self.user.full_name)
            utils.save_idea(new_idea)  

            # Enviar la idea al Buzon del moderador(es)  
            users = utils.load_existing_users()
            for user in users:
                if user.role == 'moderador':
                    user.add_activity_to_inbox(new_idea)
            utils.save_users(users)
              
            self.entrada.delete(0, tk.END)
            messagebox.showinfo("Éxito", "¡Tu idea ha sido enviada correctamente")
        else:
            messagebox.showwarning("Advertencia", "El campo no puede estar vacío.")