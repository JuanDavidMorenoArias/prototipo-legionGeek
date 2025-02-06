import tkinter as tk
from tkinter import ttk

# LEGIONGEEK_:
class AdminHomeFrame(tk.Frame):
    def __init__(self,parent, user):
        super().__init__(parent,width=995, height=525, background='orange',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Bienvenid@", font=('Trebuchet MS', 23, 'bold'), foreground='black', background='white')
        self.label.place(relx=0.5, rely=0.2, anchor='w')

        self.user_info = tk.Label(self, foreground='black', text=f"Nombre: {self.user.full_name}\nID: {self.user.userID}\nEmail: {self.user.email}\nTeléfono: {self.user.phone}\n\nPermisos: {self.user.role}", 
                                  font=('Trebuchet MS', 14), background='white')
        self.user_info.place(relx=0.5, rely=0.5, anchor='w')
