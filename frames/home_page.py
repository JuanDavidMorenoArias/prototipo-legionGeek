import tkinter as tk
from tkinter import ttk

# LEGIONGEEK_:
class HomeFrame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent,width=995, height=525, background='red',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent