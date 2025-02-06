import tkinter as tk
from tkinter import messagebox, simpledialog
import utils
import json

class BuzonFrame(tk.Frame):
    def __init__(self, parent, participant):
        super().__init__(parent, width=995, height=525, background='white')
        self.parent = parent
        self.participant = participant
        self.create_widgets()

    def create_widgets(self):
        titulo = tk.Label(self, text="Buzón de Actividades", font=("Arial", 20, "bold"))
        titulo.pack(pady=20)

        self.lista_actividades = tk.Listbox(self, font=("Arial", 14), width=80, height=15)
        self.lista_actividades.pack(pady=10)

        boton_ver_detalles = tk.Button(self, text="Ver Detalles", command=self.ver_detalles)
        boton_ver_detalles.pack(pady=10)

        self.cargar_actividades()

    def cargar_actividades(self):
        self.lista_actividades.delete(0, tk.END)
        for idx, propuesta in enumerate(self.participant.inbox):
            self.lista_actividades.insert(tk.END, f"{idx + 1}. {propuesta.idea}")

    def ver_detalles(self):
        seleccion = self.lista_actividades.curselection()
        if seleccion:
            index = seleccion[0]
            propuesta = self.participant.inbox[index]
            DetallesActividadVentana(self, propuesta, self.participant, self.cargar_actividades)
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

        detalles = (
            f"Idea: {propuesta.idea}\n"
            f"Fecha: {propuesta.date}\n"
            f"Capacidad: {propuesta.capacity}\n"
            f"Objetivos: {propuesta.objective}\n"
            f"Duración: {propuesta.duration} horas\n"
            f"Material Requerido: {propuesta.required_materials}\n"
        )

        tk.Label(self, text=detalles, justify="left", font=("Arial", 12)).pack(pady=10)

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
                user["inbox"] = [prop for prop in user["inbox"] if not (prop["data"]["idea"] == self.propuesta.idea and prop["data"]["Fecha"] == self.propuesta.date)]
                break

        # Guardar los cambios en el archivo JSON
        with open("users.json", "w", encoding="utf-8") as archivo:
            json.dump(users, archivo, indent=4, ensure_ascii=False)

    def aprobar(self):
        with open("proposals.json", "r", encoding="utf-8") as archivo:
            proposals = json.load(archivo)
        
        for prop in proposals:
            if prop["idea"] == self.propuesta.idea and prop["Fecha"] == self.propuesta.date:
                prop["Aprobados"] += 1

        with open("proposals.json", "w", encoding="utf-8") as archivo:
            json.dump(proposals, archivo, indent=4, ensure_ascii=False)

        # Eliminar la propuesta del inbox del usuario
        self.participant.inbox.remove(self.propuesta)
        self.actualizar_inbox_usuario()

        messagebox.showinfo("Éxito", "¡Actividad aprobada!")
        self.refresh_callback()
        self.destroy()

    def rechazar(self):
        with open("proposals.json", "r", encoding="utf-8") as archivo:
            proposals = json.load(archivo)

        for prop in proposals:
            if prop["idea"] == self.propuesta.idea and prop["Fecha"] == self.propuesta.date:
                prop["Rechazados"] += 1

        with open("proposals.json", "w", encoding="utf-8") as archivo:
            json.dump(proposals, archivo, indent=4, ensure_ascii=False)

        # Eliminar la propuesta del inbox del usuario
        self.participant.inbox.remove(self.propuesta)
        self.actualizar_inbox_usuario()

        messagebox.showinfo("Éxito", "Actividad rechazada.")
        self.refresh_callback()
        self.destroy()

    def solicitar_cambios(self):
        cambios = simpledialog.askstring("Solicitar Cambios", "Especifica los cambios necesarios:")
        if cambios:
            with open("proposals.json", "r", encoding="utf-8") as archivo:
                proposals = json.load(archivo)

            for prop in proposals:
                if prop["idea"] == self.propuesta.idea and prop["Fecha"] == self.propuesta.date:
                    prop["Feedback"].append(cambios)

            with open("proposals.json", "w", encoding="utf-8") as archivo:
                json.dump(proposals, archivo, indent=4, ensure_ascii=False)

            # Eliminar la propuesta del inbox del usuario
            self.participant.inbox.remove(self.propuesta)
            self.actualizar_inbox_usuario()

        messagebox.showinfo("Éxito", "Cambios solicitados.")
        self.refresh_callback()
        self.destroy()
