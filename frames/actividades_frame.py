import tkinter as tk
from tkinter import ttk

class ActividadesFrame(tk.Frame):
    # En esta clase
    def __init__(self,parent, user):
        super().__init__(parent,width=995, height=525, background='pink',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent