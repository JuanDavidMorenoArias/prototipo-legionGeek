import tkinter as tk
from tkinter import ttk, messagebox
import json
from frames.admin_modificar_frame import ModificarPropuestaVentana
import utils

class AdminPropuestasFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=995, height=525, background='white')
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        titulo = tk.Label(self, text="Buzón de Actividades Propuestas\n Izquierda propuestas,Mitad Actividades\n y Derecha Finalizadas",background='white', foreground='#9d2fcc', font=("Trebuchet MS", 20, "bold"))
        titulo.pack(pady=20)
        self.lista_propuestas = tk.Listbox(self, font=("Trebuchet MS", 14), width=25, height=15)
        self.lista_actividadesI = tk.Listbox(self, font=("Trebuchet MS", 14), width=25, height=15)
        self.lista_actividadesfinalizadas = tk.Listbox(self, font=("Trebuchet MS", 14), width=25, height=15)
        self.lista_propuestas.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.lista_actividadesI.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.lista_actividadesfinalizadas.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.btn_verificar = tk.Button(self, text="Verificar Estado de la propuesta", command=self.verificar_estado)
        self.btn_verificar.pack(pady=10)
        self.btn_verificaract = tk.Button(self, text="Verificar Estado de actividad", command=self.verificar_estadoact)
        self.btn_verificaract.pack(pady=10)
        self.btn_verificarfin = tk.Button(self, text="Verificar Estado de Finalizada", command=self.verificar_estadofin)
        self.btn_verificarfin.pack(pady=10)

        self.cargar_actividades()

    def cargar_actividades(self):
        self.lista_propuestas.delete(0, tk.END)
        self.lista_actividadesI.delete(0, tk.END)
        self.lista_actividadesfinalizadas.delete(0, tk.END)
        with open("activities.json", "r", encoding="utf-8") as archivo:
            actividades = json.load(archivo)
        
        for actividad in actividades:
            if actividad.get("Propuesta"):
                self.lista_propuestas.insert(tk.END, f"{actividad['idea']}")

            if actividad.get("Actividad"):
                self.lista_actividadesI.insert(tk.END, f"{actividad['idea']}")

            if actividad.get("Finalizada"):
                self.lista_actividadesfinalizadas.insert(tk.END, f"{actividad['idea']}")

            

    def verificar_estado(self):
        selected_index = self.lista_propuestas.curselection()
        
        if not selected_index:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una propuesta de la lista.")
            return

        propuesta_seleccionada = self.lista_propuestas.get(selected_index[0])

        with open("users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        total_participantes = sum(1 for user in usuarios if user['role'] == 'participante')
        umbral = total_participantes / 2
        
        with open("activities.json", "r", encoding="utf-8") as archivo:
            actividades = json.load(archivo)
            
        for act in actividades:
            if act['idea'] == propuesta_seleccionada:
                if act.get("Propuesta"):
                    
                    votos = act['Propuesta']["Aprobados"] + act['Propuesta']["Rechazados"]  + len(act['Propuesta']["Feedback"])

                    if votos < umbral:
                        estado_final = "Aún no tiene suficientes votos."
                    else:
                        if act['Propuesta']["Aprobados"] >= max(act['Propuesta']["Rechazados"], len(act['Propuesta']["Feedback"])):
                            estado_final = "Aprobada"
                        elif len(act['Propuesta']["Feedback"]) >= max(act['Propuesta']["Aprobados"], act['Propuesta']["Rechazados"]):
                            estado_final = "Requiere Modificaciones"
                        else:
                            estado_final = "Rechazada"

                        # Si se alcanzó el umbral de votos, eliminar la propuesta del inbox de participantes
                        self.eliminar_propuesta_de_usuarios(act)

                self.mostrar_ventana_estado(act, estado_final)
                return  # Terminamos la iteración después de encontrar la propuesta seleccionada
    def verificar_estadoact(self):
        selected_index = self.lista_actividadesI.curselection()
        
        if not selected_index:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una actividad para inscribir de la lista.")
            return

        propuesta_seleccionada = self.lista_actividadesI.get(selected_index[0])
        with open("activities.json", "r", encoding="utf-8") as archivo:
            actividades = json.load(archivo)
            
        for act in actividades:
            if act['idea'] == propuesta_seleccionada:
                if act.get("Actividad"):
                    umbral = int(act["Capacidad"]) / 2
                    votos = act['Actividad']["Inscripciones"]
                    if 1 < 15:
                        estado_final = "norealizar"
                    if act["Actividad"]["momento"]=="encurso":
                        estado_final="encurso"
                    if act["Actividad"]["momento"]=="cancelada":
                        estado_final="cancelada"
                    else:
                        estado_final="encurso"

                        # Si se alcanzó el umbral de votos, eliminar la propuesta del inbox de participantes
                        self.eliminar_propuesta_de_usuarios(act)

                self.mostrar_ventana_estadoact(act, estado_final)
                return
    def verificar_estadofin(self):
        selected_index = self.lista_actividadesfinalizadas.curselection()
        
        if not selected_index:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una actividad finalizada de la lista.")
            return

        propuesta_seleccionada = self.lista_actividadesfinalizadas.get(selected_index[0])
        with open("activities.json", "r", encoding="utf-8") as archivo:
            actividades = json.load(archivo)
            
        for act in actividades:
            if act['idea'] == propuesta_seleccionada:
                if act.get("Finalizada"):
                        self.eliminar_propuesta_de_usuarios(act)

                self.mostrar_ventana_estadofin(act)
                return
    def enviar_inscripciones(self, act):
        utils.update_activity(act, "Actividad")
        self.cargar_actividades()
        self.eliminar_propuesta_de_usuarios(act)
            
        with open("users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        for usuario in usuarios:
            if usuario['role'] == 'participante' and 'inbox' in usuario:
                usuario['inbox'].append(act)

        with open("users.json", "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
        
        

    def eliminar_propuesta_de_usuarios(self, act):
        with open("users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        for usuario in usuarios:
            if usuario['role'] == 'participante' and 'inbox' in usuario:
                usuario['inbox'] = [p for p in usuario['inbox'] if p['idea'] != act['idea']]

        with open("users.json", "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

    def mostrar_ventana_estado(self, actividad, estado):
        ventana = tk.Toplevel(self)
        ventana.title("Estado de la Propuesta")
        ventana.geometry("400x300")
        ventana.configure(background="white")

        tk.Label(ventana, text="Detalles de la Propuesta", font=("Trebuchet MS", 16, "bold"), bg="white", foreground='black').pack(pady=10)
        tk.Label(ventana, text=f"Idea: {actividad['idea']}", font=("Trebuchet MS", 12), bg="white", foreground='black').pack(pady=5)
        tk.Label(ventana, text=f"Estado: {estado}", font=("Trebuchet MS", 12, "bold"), bg="white").pack(pady=5)
        tk.Label(ventana, text=f"Aprobados: {actividad['Propuesta']['Aprobados']}", font=("Trebuchet MS", 12), bg="white", foreground='black').pack(pady=5)
        tk.Label(ventana, text=f"Rechazados: {actividad['Propuesta']['Rechazados']}", font=("Trebuchet MS", 12), bg="white", foreground='black').pack(pady=5)
        #tk.Label(ventana, tk.Label(ventana, text=f"Feedback recibidos: {len(actividad['Propuesta']['Feedback'])}",font=("Trebuchet MS", 12), bg="white", foreground='black').pack(pady=5))

        if estado == "Aprobada":
            tk.Label(ventana, text="Sugerencia: Cree la actividad.", font=("Trebuchet MS", 12, "bold"), bg="white").pack(pady=5)
            btn_crear = tk.Button(ventana, text="Crear Actividad", command=lambda: self.enviar_inscripciones(actividad,ventana), bg="green", fg="white", font=("Trebuchet MS", 12, "bold"))
            btn_crear.pack(pady=10)
            
            
        if estado == "Rechazada":
            tk.Label(ventana, text="Sugerencia: Busque una nueva actividad.", font=("Trebuchet MS", 12, "bold"), bg="white").pack(pady=5)

        if estado == "Requiere Modificaciones":
            tk.Button(ventana, text="Modificar Propuesta", command=lambda: self.abrir_modificar_propuesta(ventana, actividad), bg="blue", fg="white", font=("Trebuchet MS", 12, "bold")).pack(pady=10)
        else:
            btn_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="red", fg="white", font=("Trebuchet MS", 12, "bold"))
            btn_cerrar.pack(pady=10)
    def enviar_inscripciones(self, act,ventana):
        utils.update_activity(act, "Actividad")
        self.cargar_actividades()
        self.eliminar_propuesta_de_usuarios(act)
            
        with open("users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        for usuario in usuarios:
            if usuario['role'] == 'participante' and 'inbox' in usuario:
                usuario['inbox'].append(act)

        with open("users.json", "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
        ventana.destroy()
    def mostrar_ventana_estadoact(self, actividad, estado):
        ventana = tk.Toplevel(self)
        ventana.title("Estado de la Propuesta")
        ventana.geometry("400x300")
        ventana.configure(background="white")

        tk.Label(ventana, text="Detalles de la Propuesta", font=("Trebuchet MS", 16, "bold"), bg="white", foreground='black').pack(pady=10)
        tk.Label(ventana, text=f"Idea: {actividad['idea']}", font=("Trebuchet MS", 12), bg="white", foreground='black').pack(pady=5)
        tk.Label(ventana, text=f"Estado: {estado}", font=("Trebuchet MS", 12, "bold"), bg="white").pack(pady=5)
        tk.Label(ventana, text=f"#inscritos: {actividad['Actividad']['Inscripciones']}", font=("Trebuchet MS", 12), bg="white", foreground='black').pack(pady=5)
        tk.Label(ventana, text=f"inscritos: {actividad['Actividad']['inscritos']}", font=("Trebuchet MS", 12), bg="white", foreground='black').pack(pady=5)
        #tk.Label(ventana, tk.Label(ventana, text=f"Feedback recibidos: {len(actividad['Propuesta']['Feedback'])}",font=("Trebuchet MS", 12), bg="white", foreground='black').pack(pady=5))

        if estado == "norealizar":
            tk.Label(ventana, text="Sugerencia: Cree la actividad.", font=("Trebuchet MS", 12, "bold"), bg="white").pack(pady=5)
            btn_crear = tk.Button(ventana, text="cancelar", command=lambda:self.cancelar(actividad,ventana), bg="green", fg="white", font=("Trebuchet MS", 12, "bold"))
            btn_crear.pack(pady=10)
            btn_cerrar = tk.Button(ventana, text="cerrar", command=ventana.destroy(), bg="red", fg="white", font=("Trebuchet MS", 12, "bold"))
            btn_cerrar.pack(pady=10)
        if estado=="realizar":
            btn_cerrar = tk.Button(ventana, text="realizar", command=lambda:self.realize(actividad,ventana), bg="red", fg="white", font=("Trebuchet MS", 12, "bold"))
            btn_cerrar.pack(pady=10)
        if estado=="encurso":
            btn_cerrar = tk.Button(ventana, text="finalizar", command=lambda:self.finalize(actividad,ventana), bg="red", fg="white", font=("Trebuchet MS", 12, "bold"))
            btn_cerrar.pack(pady=10)
        if estado=="cancelada":
            btn_cerrar = tk.Button(ventana, text="cerrar", command=ventana.destroy(), bg="red", fg="white", font=("Trebuchet MS", 12, "bold"))
            btn_cerrar.pack(pady=10)
    def realize(self,act,ventana):
        utils.update_activity2(act, "realizar")
        self.cargar_actividades()
        self.eliminar_propuesta_de_usuarios(act)
            
        with open("users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        for usuario in usuarios:
            if usuario['role'] == 'participante' and 'inbox' in usuario:
                usuario['inbox'].append(act)

        with open("users.json", "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
        ventana.destroy()
    def finalize(self,act,ventana):
        utils.update_activity(act, "Finalizada")
        self.cargar_actividades()
        self.eliminar_propuesta_de_usuarios(act)
            
        with open("users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        for usuario in usuarios:
            if usuario['role'] == 'participante' and 'inbox' in usuario:
                usuario['inbox'].append(act)

        with open("users.json", "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
        ventana.destroy()
    def cancelar(self,act,ventana):
        utils.update_activity2(act, "norealizar")
        self.cargar_actividades()
        self.eliminar_propuesta_de_usuarios(act)
            
        with open("users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        for usuario in usuarios:
            if usuario['role'] == 'participante' and 'inbox' in usuario:
                usuario['inbox'].append(act)

        with open("users.json", "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
        ventana.destroy()
    def mostrar_ventana_estadofin(self, actividad):
        ventana = tk.Toplevel(self)
        ventana.title("Estado de la Propuesta")
        ventana.geometry("400x300")
        ventana.configure(background="white")

        tk.Label(ventana, text="Detalles de la Propuesta", font=("Trebuchet MS", 16, "bold"), bg="white", foreground='black').pack(pady=10)
        tk.Label(ventana, text=f"Idea: {actividad['idea']}", font=("Trebuchet MS", 12), bg="white", foreground='black').pack(pady=5)
        tk.Label(ventana, text=f"Estado:finalizada ", font=("Trebuchet MS", 12, "bold"), bg="white").pack(pady=5)
        tk.Label(ventana, text=f"Feedback: {actividad['Finalizada']['Feedback']}", font=("Trebuchet MS", 12), bg="white", foreground='black').pack(pady=5)
        btn_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="red", fg="white", font=("Trebuchet MS", 12, "bold"))
        btn_cerrar.pack(pady=10)
        btn_eliminar = tk.Button(ventana, text="eliminar", command=self.eliminar_propuesta_de_usuarios(actividad), bg="red", fg="white", font=("Trebuchet MS", 12, "bold"))
        btn_eliminar.pack(pady=10)
    def abrir_modificar_propuesta(self, ventana, propuesta):
        ventana.destroy()
        ModificarPropuestaVentana(self.parent, propuesta)
