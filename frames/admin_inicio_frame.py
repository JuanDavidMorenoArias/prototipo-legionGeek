import tkinter as tk
from tkinter import ttk

# LEGIONGEEK_:
class AdminHomeFrame(tk.Frame):
    def __init__(self,parent, user):
        super().__init__(parent,width=995, height=525, background='orange',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent
        self.user = user