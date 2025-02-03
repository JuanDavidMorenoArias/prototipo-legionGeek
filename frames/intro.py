import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  

class IntroFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=500, height=600, background='white')
        self.create_widgets()

    def create_widgets(self): # Agrega el logo, titulo y el texto de creador a la intro


        # Legion
        icon_image = Image.open("images/Legion.png").resize((450,160))
        icon_image_tk = ImageTk.PhotoImage(icon_image)
        logo = ttk.Label(self, image=icon_image_tk, background='white')
        logo.image = icon_image_tk
        logo.place(relx=0.5, rely=0.25, anchor='center')

        # Geek
        title_image = Image.open("images/Geek.png").resize((450, 140))
        title_image_tk = ImageTk.PhotoImage(title_image)
        titulito = ttk.Label(self, image=title_image_tk, background='white')
        titulito.image = title_image_tk
        titulito.place(relx=0.5, rely=0.50, anchor='center')

        # Eslogan
        eslogan_image = Image.open("images/Eslogan.png").resize((450, 100))
        eslogan_image_tk = ImageTk.PhotoImage(eslogan_image)
        eslogan = ttk.Label(self, image=eslogan_image_tk, background='white')
        eslogan.image = eslogan_image_tk
        eslogan.place(relx=0.5, rely=0.80, anchor='center')