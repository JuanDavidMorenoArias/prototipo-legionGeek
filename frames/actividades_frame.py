import tkinter as tk
from tkinter import ttk

class ActividadesFrame(tk.Frame):
    # En esta clase
    def __init__(self,parent, user):
        super().__init__(parent,width=995, height=525, background='black',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        titulo = tk.Label(self, text="Coming\nSoon", font=("Trebuchet MS", 35, "bold"), background='black', foreground='white')
        titulo.place(relx=0.5, rely=0.4, anchor='center')
