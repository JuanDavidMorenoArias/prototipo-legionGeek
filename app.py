#Librerias para creacion de la app
import tkinter as tk
from tkinter import ttk
# Importo la clase de inicio de sesion, registro y funciones
from frames.login import LogInFrame
from frames.intro import IntroFrame
from frames.toggle_menu import ToggleMenuFrame

import utils

class App():
    # Init va a correr cada que llamemos la clase como en la linea App()
    def __init__(self):

        self.root = tk.Tk() # crea instancia de la app
        utils.legionGeek_window_style(self.root)
        self.entry_show() # Genera la ventana de la app
        self.root.mainloop() # mandatorio la visualización de la app
        return

    def entry_show(self):

        # FRAME DE TITULO Y LOGO
        self.intro_frame = IntroFrame(self.root)
        self.intro_frame.place(relx=0.27,rely=0.5,anchor='center')

        # FRAME DE INICIO DE SESION 
        self.login_frame = LogInFrame(self.root,self.on_login)
        self.login_frame.place(relx=0.75,rely=0.5, anchor='center')
        self.login_frame.connect_focus_events()
    
    def on_login(self, login_successful):
        if login_successful:
            self.intro_frame.destroy()
            self.login_frame.destroy()
            self.main_show()

            pass # aqui ira supongo la llamada del after login
    
    def main_show(self):
        toggle_menu = ToggleMenuFrame(self.root,self.entry_show)
        toggle_menu.pack(side=tk.TOP,fill=tk.X)
        toggle_menu.pack_propagate(False)
        toggle_menu.configure(height=70)

        
                    
