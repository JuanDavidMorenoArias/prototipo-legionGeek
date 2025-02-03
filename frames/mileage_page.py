import tkinter as tk
from tkinter import ttk

class MileageFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=995, height=525)    
        self.parent = parent

        self.style = ttk.Style()
        self.style.configure("Green.TFrame", background="black")
        self.configure(style="Green.TFrame")