import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import utils
from idea import Idea

class AdminBuzonFrame(tk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent, width=995, height=525, background='white',
                         highlightbackground='white', highlightthickness=0)
        self.parent = parent
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        # Crear el título y colocarlo arriba
        titulo = tk.Label(self, text="Buzón de Ideas", foreground='#9d2fcc', background='white', font=("Trebuchet MS", 20, "bold"))
        titulo.place(relx=0.75, rely=0.07, anchor='center')  # Espaciado arriba y abajo

        titulo_detalle = tk.Label(self, text="Detalle de Idea", foreground='#9d2fcc', background='white', font=("Trebuchet MS", 20, "bold"))
        titulo_detalle.place(relx=0.25, rely=0.07, anchor='center')  # Espaciado arriba y abajo

        # Crear el cuadro de texto más grande
        self.inbox_listbox = tk.Listbox(self, background='black',foreground='white', font=("Trebuchet MS", 14), width=40, height=15)
        self.inbox_listbox.place(relx=0.75, rely=0.5, anchor='center')  # Espacio abajo

        self.detalle = tk.Label(self, font=("Trebuchet MS", 12, "bold"),foreground='white',background='black', width=48, height=17, justify=tk.LEFT)
        self.detalle.place(relx=0.27, rely=0.5, anchor='center')  # Espaciado arriba y abajo
        # Crear botón de eliminar
        boton_eliminar = tk.Button(self, text="Eliminar", background='red', font=("Trebuchet MS", 14), command=self.eliminar_idea)
        boton_eliminar.place(relx=0.75, rely=0.91, anchor='w')  # Espaciado abajo

        # Crear botón de detalle
        boton_eliminar = tk.Button(self, text="Detalle", background='green', font=("Trebuchet MS", 14), command=self.detallar_idea)
        boton_eliminar.place(relx=0.65, rely=0.91, anchor='w')  # Espaciado abajo


        self.load_inbox()

    def load_inbox(self):
        # Cargar las ideas del buzón del usuario
        for item in self.user.inbox:
            if isinstance(item, Idea):
                display_text = f"{item.sender} a las {item.timestamp}"
                self.inbox_listbox.insert(tk.END, display_text)

    def detallar_idea(self):
        selected_index = self.inbox_listbox.curselection()
        if selected_index:
            idea = self.user.inbox[selected_index[0]]
            detalle = f"Descripción: {idea.description}\n\nEnviado por: {idea.sender}\n\nFecha y hora de envío: {idea.timestamp}"
            self.detalle.config(text=detalle, foreground='white', wraplength=400)

    def eliminar_idea(self):
        # Eliminar la idea seleccionada
        selected_index = self.inbox_listbox.curselection()
        if selected_index:
            self.user.inbox.pop(selected_index[0])
            self.inbox_listbox.delete(selected_index)

            # Cargar todos los usuarios
            users = utils.load_existing_users()

            # Actualizar el usuario actual en la lista de usuarios
            for i, u in enumerate(users):
                if u.userID == self.user.userID:
                    users[i] = self.user
                    break

            # Guardar todos los usuarios actualizados
            utils.save_users(users)
            messagebox.showinfo("Éxito", "¡La idea ha sido eliminada correctamente!")
        else:
            messagebox.showwarning("Advertencia", "Selecciona una idea para eliminar.")