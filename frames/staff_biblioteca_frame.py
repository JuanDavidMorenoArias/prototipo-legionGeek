import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import utils
from activityIns import ActivityIns
from activity import Activity
import json


class StaffLibraryFrame(tk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent, width=995, height=525, background='white',
                         highlightbackground='white', highlightthickness=0)
        self.parent = parent
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        # Crear el título y colocarlo arriba
        titulo = tk.Label(self, text="Actividades en curso", foreground='#B79C27', background='white', font=("Trebuchet MS", 20, "bold"))
        titulo.place(relx=0.75, rely=0.07, anchor='center')  # Espaciado arriba y abajo

        titulo_detalle = tk.Label(self, text="Detalle de Actividad", foreground='#B79C27', background='white', font=("Trebuchet MS", 20, "bold"))
        titulo_detalle.place(relx=0.25, rely=0.07, anchor='center')  # Espaciado arriba y abajo

        # Crear el cuadro de texto más grande
        self.inbox_listbox = tk.Listbox(self, background='white',foreground='black', font=("Trebuchet MS", 14), width=40, height=15, highlightbackground='#B79C27', highlightthickness=1)
        self.inbox_listbox.place(relx=0.75, rely=0.5, anchor='center')  # Espacio abajo

        self.detalle = tk.Label(self, font=("Trebuchet MS", 12, "bold"),foreground='black',background='white', width=48, height=17, justify=tk.LEFT, highlightbackground='#B79C27', highlightthickness=1)
        self.detalle.place(relx=0.27, rely=0.5, anchor='center')  # Espaciado arriba y abajo

        # Crear botón de detalle
        boton_detalle = tk.Button(self, text="Detalle", background='green', font=("Trebuchet MS", 14), command=self.detallar_actividad)
        boton_detalle.place(relx=0.75, rely=0.91, anchor='w')  # Espaciado abajo


        self.load_activities("activities.json")

    def load_activities(self, file_path):
        with open(file_path, 'r') as file:
            activities = json.load(file)
    
        self.activity_ins_list = []
        for activity in activities:
            if "Actividad" in activity:
                act = ActivityIns.from_dict(activity)
                self.activity_ins_list.append(act)
                display_text = f"{act.idea}"
                self.inbox_listbox.insert(tk.END, display_text)
        

    def detallar_actividad(self):
        selected_index = self.inbox_listbox.curselection()
        if selected_index:
            # Obtener la actividad seleccionada
            selected_activity = self.inbox_listbox.get(selected_index[0])
            
            # Buscar la actividad en la lista de actividades cargadas
            for activity in self.activity_ins_list:
                if activity.idea == selected_activity:
                    detalle = (
                        f"Idea: {activity.idea}\n"
                        f"Fecha: {activity.date}\n"
                        f"Capacidad: {activity.capacity}\n"
                        f"Objetivos: {activity.objective}\n"
                        f"Duración: {activity.duration}\n"
                        f"Material Requerido: {activity.required_materials}\n"
                        f"Inscripciones: {activity.inscritos}"
                    )
                    self.detalle.config(text=detalle, foreground='black', wraplength=400)
                    break
