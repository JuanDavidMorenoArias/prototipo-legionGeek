import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import utils
from idea import Idea

class AdminBuzonFrame(tk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent, width=995, height=525, background='red',
                         highlightbackground='white', highlightthickness=0)
        self.parent = parent
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        # Crear el título y colocarlo arriba
        titulo = tk.Label(self, text="Buzón de Ideas", font=("Arial", 20, "bold"))
        titulo.place(relx=0.5, rely=0.2, anchor='center')  # Espaciado arriba y abajo

        # Crear el cuadro de texto más grande
        self.inbox_listbox = tk.Listbox(self, background='orange', font=("Arial", 16), width=50, height=10)
        self.inbox_listbox.place(relx=0.5, rely=0.5, anchor='center')  # Espacio abajo

        # Crear botón de eliminar
        boton_eliminar = tk.Button(self, text="Eliminar", background='red', font=("Arial", 14), command=self.eliminar_idea)
        boton_eliminar.place(relx=0.5, rely=0.8, anchor='center')  # Espaciado abajo

        self.load_inbox()

    def load_inbox(self):
        # Cargar las ideas del buzón del usuario
        for item in self.user.inbox:
            if isinstance(item, Idea):
                display_text = f"{item.description} - Enviado por: {item.sender} a las {item.timestamp}"
                self.inbox_listbox.insert(tk.END, display_text)

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