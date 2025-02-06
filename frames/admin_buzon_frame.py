import tkinter as tk
from tkinter import ttk, messagebox
import json
from frames.admin_modificar_frame import ModificarPropuestaVentana

class AdminPropuestasFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=995, height=525, background='white')
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        titulo = tk.Label(self, text="Buzón de Actividades Propuestas", font=("Arial", 20, "bold"))
        titulo.pack(pady=20)

        self.lista_actividades = tk.Listbox(self, font=("Arial", 14), width=80, height=15)
        self.lista_actividades.pack(pady=10)

        self.btn_verificar = tk.Button(self, text="Verificar Estado", command=self.verificar_estado)
        self.btn_verificar.pack(pady=10)

        self.cargar_propuestas()

    def cargar_propuestas(self):
        self.lista_actividades.delete(0, tk.END)
        with open("proposals.json", "r", encoding="utf-8") as archivo:
            propuestas = json.load(archivo)
        
        for propuesta in propuestas:
            self.lista_actividades.insert(tk.END, f"{propuesta['idea']}")

    def verificar_estado(self):
        selected_index = self.lista_actividades.curselection()
        
        if not selected_index:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una propuesta de la lista.")
            return

        propuesta_seleccionada = self.lista_actividades.get(selected_index[0])

        with open("users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        total_participantes = sum(1 for user in usuarios if user['role'] == 'participante')
        umbral = total_participantes / 2
        
        with open("proposals.json", "r", encoding="utf-8") as archivo:
            propuestas = json.load(archivo)
            
        for prop in propuestas:
            if prop['idea'] == propuesta_seleccionada:
                votos = prop['Aprobados'] + prop['Rechazados'] + len(prop['Feedback'])

                if votos < umbral:
                    estado_final = "Aún no tiene suficientes votos."
                else:
                    if prop['Aprobados'] >= max(prop['Rechazados'], len(prop['Feedback'])):
                        estado_final = "Aprobada"
                    elif len(prop['Feedback']) >= max(prop['Aprobados'], prop['Rechazados']):
                        estado_final = "Requiere Modificaciones"
                    else:
                        estado_final = "Rechazada"

                    # Si se alcanzó el umbral de votos, eliminar la propuesta del inbox de participantes
                    self.eliminar_propuesta_de_usuarios(prop['idea'])

                self.mostrar_ventana_estado(prop, estado_final)
                return  # Terminamos la iteración después de encontrar la propuesta seleccionada

    def eliminar_propuesta_de_usuarios(self, idea):
        with open("users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        for usuario in usuarios:
            if usuario['role'] == 'participante' and 'inbox' in usuario:
                usuario['inbox'] = [p for p in usuario['inbox'] if p['data']['idea'] != idea]

        with open("users.json", "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

    def mostrar_ventana_estado(self, propuesta, estado):
        ventana = tk.Toplevel(self)
        ventana.title("Estado de la Propuesta")
        ventana.geometry("400x300")
        ventana.configure(background="white")

        tk.Label(ventana, text="Detalles de la Propuesta", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
        tk.Label(ventana, text=f"Idea: {propuesta['idea']}", font=("Arial", 12), bg="white").pack(pady=5)
        tk.Label(ventana, text=f"Estado: {estado}", font=("Arial", 12, "bold"), bg="white").pack(pady=5)
        tk.Label(ventana, text=f"Aprobados: {propuesta['Aprobados']}", font=("Arial", 12), bg="white").pack(pady=5)
        tk.Label(ventana, text=f"Rechazados: {propuesta['Rechazados']}", font=("Arial", 12), bg="white").pack(pady=5)
        tk.Label(ventana, text=f"Feedback recibido: {len(propuesta['Feedback'])}", font=("Arial", 12), bg="white").pack(pady=5)
        
        
        if estado == "Rechazada":
            tk.Label(ventana, text="Sugerencia: Busque una nueva actividad.", font=("Arial", 12, "bold"), bg="white").pack(pady=5)

        if estado == "Requiere Modificaciones":
            tk.Button(ventana, text="Modificar Propuesta", command=lambda: self.abrir_modificar_propuesta(ventana, propuesta), bg="blue", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
        else:
            btn_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="red", fg="white", font=("Arial", 12, "bold"))
            btn_cerrar.pack(pady=10)

    def abrir_modificar_propuesta(self, ventana, propuesta):
        ventana.destroy()
        ModificarPropuestaVentana(self.parent, propuesta)
