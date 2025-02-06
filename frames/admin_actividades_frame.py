import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from idea import Idea
import utils
from proposal import Proposal

class AdminActividadesFrame(tk.Frame):
    # En esta clase
    def __init__(self,parent):
        super().__init__(parent,width=995, height=525, background='white',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        titulo = tk.Label(self, text="Plantear Actividad", font=("Trebuchet MS", 20, "bold"))
        titulo.grid(row=0, column=1, pady=20, padx=20)

        borde_config = {"highlightbackground": "black", "highlightcolor": "black", "highlightthickness": 1}
        # Campos de entrada
        # Etiqueta y campo de entrada para la idea
        label_idea = tk.Label(self, text="Idea:", font=("Trebuchet MS", 14))
        label_idea.grid(row=1, column=0, sticky='w', padx=20)
        self.entrada_idea = tk.Entry(self, font=("Trebuchet MS", 16), width=40, **borde_config)
        self.entrada_idea.grid(row=1, column=1, pady=10, padx=20)

        # Etiqueta y campo de entrada para la fecha
        label_fecha = tk.Label(self, text="Fecha (DD/MM/AAAA):", font=("Trebuchet MS", 14))
        label_fecha.grid(row=2, column=0, sticky='w', padx=20)
        self.entrada_fecha = tk.Entry(self, font=("Trebuchet MS", 16), width=40, **borde_config)
        self.entrada_fecha.grid(row=2, column=1, pady=10, padx=20)

        # Etiqueta y campo de entrada para la capacidad
        label_capacidad = tk.Label(self, text="Capacidad:", font=("Trebuchet MS", 14))
        label_capacidad.grid(row=3, column=0, sticky='w', padx=20)
        self.entrada_capacidad = tk.Entry(self, font=("Trebuchet MS", 16), width=40, **borde_config)
        self.entrada_capacidad.grid(row=3, column=1, pady=10, padx=20)

        # Etiqueta y campo de entrada para los objetivos
        label_objetivos = tk.Label(self, text="Objetivos:", font=("Trebuchet MS", 14))
        label_objetivos.grid(row=4, column=0, sticky='w', padx=20)
        self.entrada_objetivos = tk.Entry(self, font=("Trebuchet MS", 16), width=40, **borde_config)
        self.entrada_objetivos.grid(row=4, column=1, pady=10, padx=20)

        # Etiqueta y campo de entrada para la duración
        label_duracion = tk.Label(self, text="Duración (horas):", font=("Trebuchet MS", 14))
        label_duracion.grid(row=5, column=0, sticky='w', padx=20)
        self.entrada_duracion = tk.Entry(self, font=("Trebuchet MS", 16), width=40, **borde_config)
        self.entrada_duracion.grid(row=5, column=1, pady=10, padx=20)

        # Etiqueta y campo de entrada para el material requerido
        label_material = tk.Label(self, text="Material Requerido:", font=("Trebuchet MS", 14))
        label_material.grid(row=6, column=0, sticky='w', padx=20)
        self.entrada_material = tk.Entry(self, font=("Trebuchet MS", 16), width=40, **borde_config)
        self.entrada_material.grid(row=6, column=1, pady=10, padx=20)

        # Botón para enviar
        boton_enviar = tk.Button(self, text="Enviar", font=("Trebuchet MS", 14), command=self.enviar_propuesta)
        boton_enviar.grid(row=7, column=1, pady=20)

    def enviar_propuesta(self):
        idea = self.entrada_idea.get()
        fecha = self.entrada_fecha.get()
        capacidad = self.entrada_capacidad.get()
        objetivos = self.entrada_objetivos.get()
        duracion = self.entrada_duracion.get()
        material = self.entrada_material.get()

        if all([idea.strip(), fecha.strip(), capacidad.strip(), objetivos.strip(), duracion.strip(), material.strip()]):
            nueva_propuesta = Proposal(
                idea=idea,
                date=fecha,
                capacity=capacidad,
                objective=objetivos,
                duration=duracion,
                MR=material
            )

            # Cargar ususarios existentes
            users = utils.load_existing_users()
            
            # Verificar si algún participante tiene 2 o más propuestas
            limite_superado = any(len(user.inbox) >= 2 for user in users if user.role == 'participante')
            
            if limite_superado:
                messagebox.showwarning("Límite de propuestas alcanzado", "No se puede enviar más propuestas, los participantes ya cuentan con 2 propuestas.")
                return  # Salir sin guardar la propuesta
            
            # Guardar la propuesta y enviarla a los participantes
            utils.save_proposal(nueva_propuesta)
            
            users = utils.load_existing_users()
            for user in users:
                if user.role == 'participante':
                    user.add_activity_to_inbox(nueva_propuesta)
            utils.save_users(users)

            # Limpiar campos
            self.clear_fields()
            messagebox.showinfo("Éxito", "¡Propuesta enviada correctamente!")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar completos.")

    def clear_fields(self):
        self.entrada_idea.delete(0, tk.END)
        self.entrada_fecha.delete(0, tk.END)
        self.entrada_capacidad.delete(0, tk.END)
        self.entrada_objetivos.delete(0, tk.END)
        self.entrada_duracion.delete(0, tk.END)
        self.entrada_material.delete(0, tk.END)