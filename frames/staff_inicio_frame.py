import tkinter as tk
from tkinter import ttk

# LEGIONGEEK_:
class StaffHomeFrame(tk.Frame):
    def __init__(self,parent, user):
        super().__init__(parent,width=995, height=525, background='black',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Bienvenid@", justify=tk.LEFT, font=('Trebuchet MS', 23, 'bold'), foreground='orange', background='black')
        self.label.place(relx=0.58, rely=0.2, anchor='center')

        self.user_info = tk.Label(self, foreground='white', text=f"Nombre: {self.user.full_name}\nID: {self.user.userID}\nEmail: {self.user.email}\nTeléfono: {self.user.phone}\n\nPermisos: {self.user.role}", justify=tk.LEFT, 
                                  font=('Trebuchet MS', 16), background='black')
        self.user_info.place(relx=0.6, rely=0.5, anchor='center')
