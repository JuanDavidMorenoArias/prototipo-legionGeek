import tkinter as tk
from tkinter import messagebox, simpledialog
import utils
import json
from proposal import Proposal
from activityIns import ActivityIns
from final_activity import FinalActivity

class BuzonFrame(tk.Frame):
    def __init__(self, parent, participant):
        super().__init__(parent, width=995, height=525, background='white')
        self.parent = parent
        self.participant = participant
        self.create_widgets()

    def create_widgets(self):
        titulo = tk.Label(self, text="Buzón de Actividades", background='white', foreground='#1872d9',font=("Trebuchet MS", 20, "bold"))
        titulo.pack(pady=20)

        self.lista_propuestas = tk.Listbox(self, font=("Trebuchet MS", 14), width=25, height=15)
        self.lista_actividadesI = tk.Listbox(self, font=("Trebuchet MS", 14), width=25, height=15)
        self.lista_actividadesfinalizadas = tk.Listbox(self, font=("Trebuchet MS", 14), width=25, height=15)
        self.lista_propuestas.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.lista_actividadesI.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.lista_actividadesfinalizadas.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        boton_ver_detalles = tk.Button(self, text="Ver Detalles", command=self.ver_detalles)
        boton_ver_detalles.pack(pady=10)
        boton_ver_inscribir=tk.Button(self, text="inscribir", command=self.ver_detallesIns)
        boton_ver_inscribir.pack(pady=10)
        self.cargar_actividades()

    def cargar_actividades(self):
        #self.lista_actividades.delete(0, tk.END)
        for idx, actividad in enumerate(self.participant.inbox):
            if isinstance(actividad, Proposal):
                self.lista_propuestas.insert(tk.END, f"{actividad.getIdea()}")

            if isinstance(actividad, ActivityIns):
                self.lista_actividadesI.insert(tk.END, f"{actividad.getIdea()}")

            if isinstance(actividad, FinalActivity):
                self.lista_actividadesfinalizadas.insert(tk.END, f"{actividad.getIdea()}")

    def ver_detalles(self):
        seleccion = self.lista_propuestas.curselection()
        if seleccion:
            index = seleccion[0]
            data=self.lista_propuestas.get(index)
            for actividad in self.participant.inbox:
                if actividad.idea==data:
                    propuesta = actividad
            DetallesActividadVentana(self, propuesta, self.participant, self.cargar_actividades)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una actividad para ver los detalles.")
    def ver_detallesIns(self):
        seleccion = self.lista_actividadesI.curselection()
        if seleccion:
            index = seleccion[0]
            data=self.lista_actividadesI.get(index)
            for actividad in self.participant.inbox:
                if actividad.idea==data:
                    propuesta = actividad
            DetallesActividadVentanaIns(self, propuesta, self.participant, self.cargar_actividades)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una actividad para ver los detalles.")        


class DetallesActividadVentana(tk.Toplevel):
    def __init__(self, parent, propuesta, participant, refresh_callback):
        super().__init__(parent)
        self.propuesta = propuesta
        self.participant = participant
        self.refresh_callback = refresh_callback
        self.title("Detalles de la Actividad")
        self.geometry("400x400")
        self.parent=parent

        detalles = (
            f"Idea: {propuesta.idea}\n"
            f"Fecha: {propuesta.date}\n"
            f"Capacidad: {propuesta.capacity}\n"
            f"Objetivos: {propuesta.objective}\n"
            f"Duración: {propuesta.duration} horas\n"
            f"Material Requerido: {propuesta.required_materials}\n"
        )
        tk.Label(self, text=detalles, justify="left", font=("Trebuchet MS", 12)).pack(pady=10)

        btn_aprobar = tk.Button(self, text="Aprobar", command=self.aprobar)
        btn_aprobar.pack(pady=5)

        btn_rechazar = tk.Button(self, text="Rechazar", command=self.rechazar)
        btn_rechazar.pack(pady=5)

        btn_solicitar_cambios = tk.Button(self, text="Solicitar Cambios", command=self.solicitar_cambios)
        btn_solicitar_cambios.pack(pady=5)

    def actualizar_inbox_usuario(self):
        """ Elimina la propuesta del inbox del usuario en el archivo JSON de usuarios """
        with open("users.json", "r", encoding="utf-8") as archivo:
            users = json.load(archivo)

        # Buscar al participante en el JSON
        for user in users:
            if user["userID"] == self.participant.userID: 
                user["inbox"] = [prop for prop in user["inbox"] if not (prop["idea"] == self.propuesta.idea)]
                break

        # Guardar los cambios en el archivo JSON
        with open("users.json", "w", encoding="utf-8") as archivo:
            json.dump(users, archivo, indent=4, ensure_ascii=False)

    def aprobar(self):
        with open("activities.json", "r", encoding="utf-8") as archivo:
            activities = json.load(archivo)
        
        for prop in activities:
            if prop["idea"] == self.propuesta.idea:
                prop['Propuesta']['Aprobados'] += 1

        with open("activities.json", "w", encoding="utf-8") as archivo:
            json.dump(activities, archivo, indent=4, ensure_ascii=False)
        # Eliminar la propuesta del inbox del usuario
        self.actualizar_inbox_usuario()
        messagebox.showinfo("Éxito", "¡Actividad aprobada!")
        self.refresh_callback()
        self.destroy()

    def rechazar(self):
        with open("activities.json", "r", encoding="utf-8") as archivo:
            activities = json.load(archivo)

        for prop in activities:
            if prop["idea"] == self.propuesta.idea:
                prop['Propuesta']["Rechazados"] += 1

        with open("activities.json", "w", encoding="utf-8") as archivo:
            json.dump(activities, archivo, indent=4, ensure_ascii=False)

        # Eliminar la propuesta del inbox del usuario

        self.actualizar_inbox_usuario()

        messagebox.showinfo("Éxito", "Actividad rechazada.")
        self.destroy()

    def solicitar_cambios(self):
        cambios = simpledialog.askstring("Solicitar Cambios", "Especifica los cambios necesarios:")
        if cambios:
            with open("activities.json", "r", encoding="utf-8") as archivo:
                activities = json.load(archivo)

            for prop in activities:
                if prop["idea"] == self.propuesta.idea:
                    prop["Feedback"].append(cambios)

            with open("activities.json", "w", encoding="utf-8") as archivo:
                json.dump(activities, archivo, indent=4, ensure_ascii=False)

            # Eliminar la propuesta del inbox del usuario
            self.participant.inbox.remove(self.propuesta)
            self.actualizar_inbox_usuario()

        messagebox.showinfo("Éxito", "Cambios solicitados.")
        self.refresh_callback()
        self.destroy()
class DetallesActividadVentanaIns(tk.Toplevel):
    def __init__(self, parent, actividadins, participant, refresh_callback):
        super().__init__(parent)
        self.actividadins = actividadins
        self.participant = participant
        self.refresh_callback = refresh_callback
        self.title("Detalles de la Actividad")
        self.geometry("400x400")
        self.parent=parent

        detalles = (
            f"Idea: {actividadins.idea}\n"
            f"Fecha: {actividadins.date}\n"
            f"Capacidad: {actividadins.capacity}\n"
            f"Objetivos: {actividadins.objective}\n"
            f"Duración: {actividadins.duration} horas\n"
            f"Material Requerido: {actividadins.required_materials}\n"
        )
        tk.Label(self, text=detalles, justify="left", font=("Trebuchet MS", 12)).pack(pady=10)
        with open("activities.json", "r", encoding="utf-8") as archivo:
            activities = json.load(archivo)
            for prop in activities:
                if prop["idea"] == self.actividadins.idea and not self.participant.userID in  prop['Actividad']["inscritos"]:
                    detalles = (
                        f"Idea: {actividadins.idea}\n"
                        f"Fecha: {actividadins.date}\n"
                        f"Capacidad: {actividadins.capacity}\n"
                        f"Objetivos: {actividadins.objective}\n"
                        f"Duración: {actividadins.duration} horas\n"
                        f"Material Requerido: {actividadins.required_materials}\n")
                    btn_aprobar = tk.Button(self, text="inscribirse", command=self.inscribir)
                    btn_aprobar.pack(pady=5)

                    btn_rechazar = tk.Button(self, text="Rechazar", command=self.declinar)
                    btn_rechazar.pack(pady=5)
                if prop["idea"] == self.actividadins.idea and self.participant.userID in  prop['Actividad']["inscritos"]:
                    detalles = (
                        f"Idea: {actividadins.idea}\n"
                        f"Fecha: {actividadins.date}\n"
                        f"Capacidad: {actividadins.capacity}\n"
                        f"Objetivos: {actividadins.objective}\n"
                        f"Duración: {actividadins.duration} horas\n"
                        f"Material Requerido: {actividadins.required_materials}\n"
                        )
                    tk.Label(self, text="YA TE ENCUENTRAS INSCRITO", font=("Arial", 12)).pack(pady=10)
                    btn_cancelar = tk.Button(self, text="cancelar", command=self.declinar)
                    btn_cancelar.pack(pady=5)
    def inscribir(self):
        with open("activities.json", "r", encoding="utf-8") as archivo:
            activities = json.load(archivo)
        for prop in activities:
            if prop["idea"] == self.actividadins.idea:
                prop['Actividad']["Inscripciones"] += 1
                prop['Actividad']["inscritos"].append(self.participant.userID)
        with open("activities.json", "w", encoding="utf-8") as archivo:
                json.dump(activities, archivo, indent=4, ensure_ascii=False)
        self.destroy()
    def declinar(self):
        self.destroy()