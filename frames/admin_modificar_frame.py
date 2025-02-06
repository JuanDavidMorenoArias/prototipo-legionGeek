import tkinter as tk
from tkinter import messagebox
import json

class ModificarPropuestaVentana(tk.Toplevel):
    def __init__(self, parent, propuesta):
        super().__init__(parent)
        self.title("Modificar Propuesta")
        self.geometry("720x400")
        self.configure(background="white")
        
        self.propuesta = propuesta
        
        tk.Label(self, text="Modificar Propuesta", font=("Trebuchet MS", 18, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=10)
        
        self.crear_campos()
        self.mostrar_feedback()
        
        btn_guardar = tk.Button(self, text="Guardar Cambios", font=("Trebuchet MS", 12, "bold"), command=self.guardar_cambios)
        btn_guardar.grid(row=7, column=0, columnspan=2, pady=10)
    
    def crear_campos(self):
        labels = ["Idea:", "Fecha:", "Capacidad:", "Objetivos:", "Duración:", "Material:"]
        atributos = ["idea", "Fecha", "Capacidad", "Objetivos", "Duracion", "Material Requerido"]
        
        self.entradas = {}
        for i, (label, attr) in enumerate(zip(labels, atributos)):
            tk.Label(self, text=label, font=("Trebuchet MS", 12), bg="white").grid(row=i+1, column=0, sticky='w', padx=10, pady=5)
            entry = tk.Entry(self, font=("Trebuchet MS", 12), width=40)
            entry.insert(0, str(self.propuesta[attr]))
            entry.grid(row=i+1, column=1, pady=5, padx=10)
            self.entradas[attr] = entry
    
    def mostrar_feedback(self):
        tk.Label(self, text="Feedback recibido:", font=("Trebuchet MS", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5)
        self.lista_feedback = tk.Listbox(self, font=("Trebuchet MS", 12), width=30, height=10)
        self.lista_feedback.grid(row=2, column=2, rowspan=5, padx=10, pady=5)
        
        for comentario in self.propuesta.get("Feedback", []):
            self.lista_feedback.insert(tk.END, comentario)
    
    def guardar_cambios(self):
        for key, entry in self.entradas.items():
            self.propuesta[key] = entry.get()
        
        with open("proposals.json", "r", encoding="utf-8") as file:
            propuestas = json.load(file)
        
        for i, prop in enumerate(propuestas):
            if prop["idea"] == self.propuesta["idea"]:
                propuestas[i] = self.propuesta
                break
        
        with open("proposals.json", "w", encoding="utf-8") as file:
            json.dump(propuestas, file, indent=4, ensure_ascii=False)
        
        
        messagebox.showinfo("Éxito", "Propuesta actualizada correctamente.")
        self.destroy()
