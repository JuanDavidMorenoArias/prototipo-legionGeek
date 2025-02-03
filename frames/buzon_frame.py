import tkinter as tk
from tkinter import ttk

# Frame que...
class BuzonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=995, height=525, background='green',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent